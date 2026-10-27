# Lists index

AdGuard Home -> Filters -> DNS blocklists -> Add a custom list me jo chahiye wahi URL jodein.

- **Tier**: small (halka) < medium < large (sabse bada). Har category me **sirf ek tier** chunein.
- Alag categories me **ek jaisa tier** rakhein (jaise sab small), tab repetition nahi hoga.
- Mi Max 2 jaise kam-RAM device par small ya medium se shuru karein, phir dekhte hue badhayein.
- Jis category me kisi tier ki file nahi hai, wahan pichhle (chhote) tier ki file hi use karein.

| List | Tier | Kya hai | Entries | Suggestion | URL |
|---|---|---|---:|---|---|
| malware | small | Malware, botnet C2, threat intelligence | 212777 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.small.txt` |
| malware | medium | Malware, botnet C2, threat intelligence | 434747 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.medium.txt` |
| malware | large | Malware, botnet C2, threat intelligence | 2105461 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.large.txt` |
| phishing | medium | Phishing domains (small me nahi: malware tier ki TIF list me already aate hain) | 69607 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/phishing.medium.txt` |
| phishing | large | Phishing domains (small me nahi: malware tier ki TIF list me already aate hain) | 426592 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/phishing.large.txt` |
| scam | small | Scam, fraud, spam, fake shops | 33 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.small.txt` |
| scam | medium | Scam, fraud, spam, fake shops | 21023 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.medium.txt` |
| scam | large | Scam, fraud, spam, fake shops | 449472 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.large.txt` |
| cryptojacking | - | Browser crypto-miners | 223 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/cryptojacking.txt` |
| ads | small | Ads, popups, ad networks | 73451 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.small.txt` |
| ads | medium | Ads, popups, ad networks | 227471 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.medium.txt` |
| ads | large | Ads, popups, ad networks | 249634 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.large.txt` |
| trackers | small | Tracking, analytics, CNAME-cloaked trackers | 38881 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/trackers.small.txt` |
| trackers | large | Tracking, analytics, CNAME-cloaked trackers | 165148 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/trackers.large.txt` |
| telemetry | - | Smart TV, Android, Windows telemetry | 759 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/telemetry.txt` |
| gambling | small | Gambling / betting | 4323 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/gambling.small.txt` |
| gambling | large | Gambling / betting | 486640 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/gambling.large.txt` |
| adult | small | Adult content | 48156 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/adult.small.txt` |
| adult | large | Adult content | 116052 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/adult.large.txt` |
| social | - | Social media | 580 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/social.txt` |
| piracy | - | Piracy / torrent sites | 57215 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/piracy.txt` |
| bypass | - | DoH / VPN / proxy bypass servers (taaki devices AdGuard ko bypass na kar saken) | 16156 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/bypass.txt` |
| universal | small | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 318735 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.small.txt` |
| universal | medium | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 730145 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.medium.txt` |
| universal | large | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 3150852 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.large.txt` |
| allowlist | - | DNS allowlist (Filters -> DNS allowlists me jodein) | 7 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/allowlist.txt` |
