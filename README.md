# Blocklist Hub

दुनिया की कई बड़ी blocklists → category में बँटी → dedupe → AdGuard Home के लिए तैयार। सब कुछ GitHub Actions पर, रोज़ auto-update।

## Setup (एक बार)
1. GitHub पर **public** repo बनाएँ (जैसे `blocklist-hub`) और ये सारी files upload/push करें।
2. Repo → **Settings → Actions → General → Workflow permissions → Read and write permissions** चुनें।
3. **Actions → Update blocklists → Run workflow** दबाएँ। पहला run `lists/` folder भर देगा।
4. Run के log में "Failed/empty sources" देखें; कोई URL मर चुका हो तो `sources.toml` से हटा/बदल दें।

## AdGuard Home में जोड़ना
Filters → DNS blocklists → Add blocklist → Add a custom list। सारे URL और entry-count `lists/INDEX.md` में अपने-आप बनते हैं।

बड़ी lists के तीन tier हैं:

| Tier | कब चुनें |
|---|---|
| small | हल्का load, कम RAM (जैसे फ़ोन/Termux) |
| medium | संतुलित |
| large | सबसे ज़्यादा blocking, ज़्यादा RAM |

- हर category में **सिर्फ़ एक tier** चुनें (जैसे `ads.small.txt`), और सब categories में **एक जैसा tier** रखें; तब repetition नहीं होगा।
- Tier cumulative हैं: large ⊃ medium ⊃ small।
- जिस category में किसी tier की file नहीं है (जैसे `phishing.small`), वहाँ चुने हुए tier से छोटी file ही लें या उसे छोड़ दें।
- छोटी categories (cryptojacking, telemetry, social, piracy, bypass) की एक ही file है: `<naam>.txt`।
- `universal.<tier>.txt` = सारी ON-suggested categories एक file में। category lists के साथ ON न करें।
- Allowlist (Filters → DNS allowlists → Add a custom list): `lists/allowlist.txt`
- सुझाव ON: malware, phishing, scam, cryptojacking, ads, trackers, telemetry। सुझाव OFF: gambling, adult, social, piracy, bypass।

## कैसे चलता है
- `sources.toml` : category → source URLs। Category का क्रम = priority; एक domain सिर्फ़ पहली category में जाता है।
- `build.py` : fetch → parse (hosts / adblock / plain) → allowlist हटाना → हर tier के लिए अलग dedupe → parent-domain collapse → `lists/*.txt`
- Safety: किसी category का size अचानक 50% से ज़्यादा घटे तो build रुक जाता है (list खराब नहीं होती)।
- कुछ नहीं बदला तो commit नहीं होता।

## रोज़ का काम
- गलत block हुई site → `allowlist/allow.txt` में domain जोड़ें।
- अपना extra block → `custom/block.txt`।
- नई list → `sources.toml` में सही category के `urls` में जोड़ें।
