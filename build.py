#!/usr/bin/env python3
"""Bahut saari public blocklists ko combine, category-wise bantakar, dedupe karke
AdGuard Home ke liye ||domain^ lists banata hai. Sirf Python stdlib (3.11+)."""
import datetime, json, os, re, sys, time, tomllib, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "lists"
UA = "Mozilla/5.0 (blocklist-hub; GitHub Actions)"
HOST_RE = re.compile(
    r"^(?=.{4,253}$)(?:[a-z0-9_](?:[a-z0-9_-]{0,61}[a-z0-9_])?\.)+[a-z][a-z0-9-]{1,62}$"
)
ABP_RE = re.compile(r"^\|\|([a-z0-9._*-]+)\^?(?:\$important)?$", re.I)
IPV4_RE = re.compile(r"^\d{1,3}(?:\.\d{1,3}){3}$")
SKIP = {"localhost", "localhost.localdomain", "local", "broadcasthost",
        "ip6-localhost", "ip6-loopback", "ip6-allnodes", "ip6-allrouters"}


def norm(d):
    d = d.strip().lower().rstrip(".")
    while d.startswith("*."):
        d = d[2:]
    return d if d not in SKIP and HOST_RE.match(d) else None


def parse_line(line):
    """Ek line se 0 ya zyada valid domains nikalta hai."""
    line = line.strip()
    if not line or line[0] in "#!;[" or line.startswith("@@"):
        return []
    if line.startswith("||"):
        m = ABP_RE.match(line)
        d = norm(m.group(1)) if m else None
        return [d] if d else []
    line = line.split("#", 1)[0].strip()
    parts = line.split()
    if not parts:
        return []
    if IPV4_RE.match(parts[0]) or ":" in parts[0]:  # hosts format
        parts = parts[1:]
    elif len(parts) > 1:
        return []
    return [d for d in map(norm, parts) if d]


def load_domains(text):
    out = set()
    for line in text.splitlines():
        out.update(parse_line(line))
    return out


def fetch_text(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90) as r:
                return r.read().decode("utf-8", "ignore")
        except Exception as e:
            err = e
            time.sleep(2 * (i + 1))
    print(f"  FAIL {url} -> {err}", file=sys.stderr)
    return None


def parents(d):
    p = d.split(".")
    for i in range(1, len(p) - 1):
        yield ".".join(p[i:])


def collapse(domains):
    """Agar parent domain list me hai to child hata do (||parent^ subdomains ko bhi block karta hai)."""
    return {d for d in domains if not any(p in domains for p in parents(d))}


def under(d, s):
    return d in s or any(p in s for p in parents(d))


def body_of(path):
    if not path.exists():
        return None
    return [l for l in path.read_text(encoding="utf-8").splitlines() if not l.startswith("!")]


def write_list(path, title, desc, domains, prefix="||", suffix="^"):
    lines = [f"{prefix}{d}{suffix}" for d in sorted(domains)]
    if body_of(path) == lines:
        return False  # kuch nahi badla -> file/timestamp na chhedein (faltu commit nahi)
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    head = [f"! Title: {title}", f"! Description: {desc}",
            f"! Last modified: {datetime.datetime.now(datetime.timezone.utc):%Y-%m-%d %H:%M UTC}",
            f"! Entries: {len(lines)}"]
    if repo:
        head.append(f"! Homepage: https://github.com/{repo}")
    path.write_text("\n".join(head + ["!"] + lines) + "\n", encoding="utf-8")
    return True


def main():
    cfg = tomllib.loads((ROOT / "sources.toml").read_text(encoding="utf-8"))
    cats, allow_cfg = cfg["categories"], cfg.get("allowlist", {})

    urls = {u for c in cats.values() for u in c.get("urls", [])} | set(allow_cfg.get("urls", []))
    print(f"Fetching {len(urls)} sources ...")
    with ThreadPoolExecutor(8) as ex:
        texts = dict(zip(urls, ex.map(fetch_text, urls)))
    fetched, failed = {}, []
    for u, t in texts.items():
        s = load_domains(t) if t else set()
        if s:
            fetched[u] = s
        else:
            failed.append(u)
    for u, s in sorted(fetched.items()):
        print(f"  {len(s):>8}  {u}")

    allowed = set()
    for f in allow_cfg.get("files", []):
        allowed |= load_domains((ROOT / f).read_text(encoding="utf-8"))
    for u in allow_cfg.get("urls", []):
        allowed |= fetched.get(u, set())

    assigned, per_cat = set(), {}
    for name, c in cats.items():  # order = priority
        dom = set()
        for f in c.get("files", []):
            dom |= load_domains((ROOT / f).read_text(encoding="utf-8"))
        for u in c.get("urls", []):
            dom |= fetched.get(u, set())
        dom = {d for d in dom if d not in assigned and not under(d, allowed)}
        assigned |= dom
        per_cat[name] = collapse(dom)
    universal = collapse(set().union(*(per_cat[n] for n, c in cats.items() if c.get("in_universal"))))

    # Safety: koi category achanak 50% se zyada sikud jaye to build rok do (list kharab na ho)
    stats_path = ROOT / "stats.json"
    old = json.loads(stats_path.read_text()) if stats_path.exists() else {}
    new_counts = {**{n: len(v) for n, v in per_cat.items()}, "universal": len(universal)}
    bad = [n for n, k in new_counts.items() if old.get(n, 0) > 1000 and k < old[n] * 0.5]
    if bad and os.environ.get("FORCE") != "1":
        sys.exit(f"ABORT: sudden drop in {bad}. Sources check karein, ya FORCE=1 se dobara chalayein.")

    OUT.mkdir(exist_ok=True)
    changed = False
    for n, c in cats.items():
        changed |= write_list(OUT / f"{n}.txt", f"Blocklist Hub - {n}", c.get("description", n), per_cat[n])
    changed |= write_list(OUT / "universal.txt", "Blocklist Hub - Universal",
                          "Ads + trackers + malware + phishing + scam + telemetry (deduped)", universal)
    changed |= write_list(OUT / "allowlist.txt", "Blocklist Hub - Allowlist",
                          "AdGuard Home DNS allowlist", collapse(allowed), prefix="@@||")
    repo = os.environ.get("GITHUB_REPOSITORY", "<USER>/<REPO>")
    base = f"https://raw.githubusercontent.com/{repo}/main/lists"
    rows = ["# Lists index", "", "AdGuard Home -> Filters -> DNS blocklists -> Add a custom list me jo chahiye wahi URL jodein.",
            "Har category me domains unique hain (ek domain sirf ek category me).", "",
            "| List | Kya hai | Entries | Suggestion | URL |", "|---|---|---:|---|---|"]
    for n, c in cats.items():
        if n == "custom" and not per_cat[n]:
            continue
        rows.append(f"| {n} | {c.get('description', n)} | {len(per_cat[n])} | "
                    f"{'ON' if c.get('in_universal') else 'OFF'} | `{base}/{n}.txt` |")
    rows += [f"| universal | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | {len(universal)} | optional | `{base}/universal.txt` |",
             f"| allowlist | DNS allowlist (Filters -> DNS allowlists me jodein) | {len(allowed)} | ON | `{base}/allowlist.txt` |"]
    index = "\n".join(rows) + "\n"
    ip = OUT / "INDEX.md"
    if not ip.exists() or ip.read_text(encoding="utf-8") != index:
        ip.write_text(index, encoding="utf-8")
        changed = True
    stats_path.write_text(json.dumps({**new_counts, "allowlist": len(allowed),
                                      "failed_sources": sorted(failed)}, indent=2, sort_keys=True) + "\n")
    print("\nCounts:", json.dumps(new_counts, indent=2))
    if failed:
        print("\nFailed/empty sources:\n  " + "\n  ".join(failed))
    print("Lists changed." if changed else "No changes.")


if __name__ == "__main__":
    main()
