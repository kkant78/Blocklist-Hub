# Blocklist Hub

दुनिया की कई बड़ी blocklists → category में बँटी → dedupe → AdGuard Home के लिए तैयार। सब कुछ GitHub Actions पर, रोज़ auto-update।

## Setup (एक बार)
1. GitHub पर **public** repo बनाएँ (जैसे `blocklist-hub`) और ये सारी files upload/push करें।
2. Repo → **Settings → Actions → General → Workflow permissions → Read and write permissions** चुनें।
3. **Actions → Update blocklists → Run workflow** दबाएँ। पहला run `lists/` folder भर देगा।
4. Run के log में "Failed/empty sources" देखें; कोई URL मर चुका हो तो `sources.toml` से हटा/बदल दें।

## AdGuard Home में जोड़ना
Filters → DNS blocklists → Add blocklist → Add a custom list:

हर category की अपनी अलग list है: `lists/<category>.txt`। **सारे URL और entry-count `lists/INDEX.md` में अपने-आप बनते हैं**, वहीं से copy करें।
जो category चाहिए उसे AdGuard Home में ON रखें, बाकी OFF (toggle) कर दें।

- हर category में domains unique हैं, इसलिए कई lists एक साथ ON करने पर repetition नहीं होता।
- `universal.txt` = सारी "ON-suggested" categories एक file में। इसे category lists के साथ ON न करें (double हो जाएगा)।
- Allowlist (Filters → DNS allowlists → Add a custom list): `lists/allowlist.txt`
- Categories: malware, phishing, scam, cryptojacking, ads, trackers, telemetry (सुझाव: ON) और gambling, adult, social, piracy, bypass (सुझाव: OFF)

Settings → General settings → Filters update interval: 12 hours या 24 hours।

## कैसे चलता है
- `sources.toml` : category → source URLs। Category का क्रम = priority; एक domain सिर्फ़ पहली category में जाता है।
- `build.py` : fetch → parse (hosts / adblock / plain) → allowlist हटाना → parent-domain collapse → `lists/*.txt`
- Safety: किसी category का size अचानक 50% से ज़्यादा घटे तो build रुक जाता है (list खराब नहीं होती)।
- कुछ नहीं बदला तो commit नहीं होता।

## रोज़ का काम
- गलत block हुई site → `allowlist/allow.txt` में domain जोड़ें।
- अपना extra block → `custom/block.txt`।
- नई list → `sources.toml` में सही category के `urls` में जोड़ें।
