# Lists index

AdGuard Home -> Filters -> DNS blocklists -> Add a custom list me jo chahiye wahi URL jodein.

- **Tier**: small (halka) < medium < large (sabse bada). Har category me **sirf ek tier** chunein.
- Alag categories me **ek jaisa tier** rakhein (jaise sab small), tab repetition nahi hoga.
- Mi Max 2 jaise kam-RAM device par small ya medium se shuru karein, phir dekhte hue badhayein.
- Jis category me kisi tier ki file nahi hai, wahan pichhle (chhote) tier ki file hi use karein.

| List | Tier | Kya hai | Entries | Suggestion | URL |
|---|---|---|---:|---|---|
| malware | small | Malware, botnet C2, threat intelligence | 144487 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.small.txt` |
| malware | medium | Malware, botnet C2, threat intelligence | 310810 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.medium.txt` |
| malware | large | Malware, botnet C2, threat intelligence | 1939097 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.large.txt` |
| phishing | medium | Phishing domains (small me nahi: malware tier ki TIF list me already aate hain) | 70031 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/phishing.medium.txt` |
| phishing | large | Phishing domains (small me nahi: malware tier ki TIF list me already aate hain) | 396611 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/phishing.large.txt` |
| scam | small | Scam, fraud, spam, fake shops | 39 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.small.txt` |
| scam | medium | Scam, fraud, spam, fake shops | 25151 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.medium.txt` |
| scam | large | Scam, fraud, spam, fake shops | 440202 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.large.txt` |
| cryptojacking | - | Browser crypto-miners | 228 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/cryptojacking.txt` |
| ads | small | Ads, popups, ad networks | 86120 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.small.txt` |
| ads | medium | Ads, popups, ad networks | 289183 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.medium.txt` |
| ads | large | Ads, popups, ad networks | 312287 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.large.txt` |
| trackers | small | Tracking, analytics, CNAME-cloaked trackers | 40847 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/trackers.small.txt` |
| trackers | large | Tracking, analytics, CNAME-cloaked trackers | 109456 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/trackers.large.txt` |
| telemetry | - | Smart TV, Android, Windows telemetry | 757 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/telemetry.txt` |
| gambling | small | Gambling / betting | 4346 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/gambling.small.txt` |
| gambling | large | Gambling / betting | 419119 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/gambling.large.txt` |
| adult | small | Adult content | 48198 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/adult.small.txt` |
| adult | large | Adult content | 110462 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/adult.large.txt` |
| social | - | Social media | 580 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/social.txt` |
| piracy | - | Piracy / torrent sites | 62896 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/piracy.txt` |
| bypass | - | DoH / VPN / proxy bypass servers (taaki devices AdGuard ko bypass na kar saken) | 16244 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/bypass.txt` |
| universal | small | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 259439 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.small.txt` |
| universal | medium | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 665209 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.medium.txt` |
| universal | large | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 2985497 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.large.txt` |
| allowlist | - | DNS allowlist (Filters -> DNS allowlists me jodein) | 10 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/allowlist.txt` |
