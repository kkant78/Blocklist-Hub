# Lists index

AdGuard Home -> Filters -> DNS blocklists -> Add a custom list me jo chahiye wahi URL jodein.

- **Tier**: small (halka) < medium < large (sabse bada). Har category me **sirf ek tier** chunein.
- Alag categories me **ek jaisa tier** rakhein (jaise sab small), tab repetition nahi hoga.
- Mi Max 2 jaise kam-RAM device par small ya medium se shuru karein, phir dekhte hue badhayein.
- Jis category me kisi tier ki file nahi hai, wahan pichhle (chhote) tier ki file hi use karein.

| List | Tier | Kya hai | Entries | Suggestion | URL |
|---|---|---|---:|---|---|
| malware | small | Malware, botnet C2, threat intelligence | 194255 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.small.txt` |
| malware | medium | Malware, botnet C2, threat intelligence | 313610 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.medium.txt` |
| malware | large | Malware, botnet C2, threat intelligence | 1606870 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/malware.large.txt` |
| phishing | medium | Phishing domains (small me nahi: malware tier ki TIF list me already aate hain) | 64592 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/phishing.medium.txt` |
| phishing | large | Phishing domains (small me nahi: malware tier ki TIF list me already aate hain) | 430952 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/phishing.large.txt` |
| scam | small | Scam, fraud, spam, fake shops | 34 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.small.txt` |
| scam | medium | Scam, fraud, spam, fake shops | 22048 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.medium.txt` |
| scam | large | Scam, fraud, spam, fake shops | 453813 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/scam.large.txt` |
| cryptojacking | - | Browser crypto-miners | 224 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/cryptojacking.txt` |
| ads | small | Ads, popups, ad networks | 84323 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.small.txt` |
| ads | medium | Ads, popups, ad networks | 255528 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.medium.txt` |
| ads | large | Ads, popups, ad networks | 279521 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/ads.large.txt` |
| trackers | small | Tracking, analytics, CNAME-cloaked trackers | 40313 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/trackers.small.txt` |
| trackers | large | Tracking, analytics, CNAME-cloaked trackers | 167965 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/trackers.large.txt` |
| telemetry | - | Smart TV, Android, Windows telemetry | 759 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/telemetry.txt` |
| gambling | small | Gambling / betting | 4324 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/gambling.small.txt` |
| gambling | large | Gambling / betting | 511266 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/gambling.large.txt` |
| adult | small | Adult content | 48172 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/adult.small.txt` |
| adult | large | Adult content | 119890 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/adult.large.txt` |
| social | - | Social media | 580 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/social.txt` |
| piracy | - | Piracy / torrent sites | 58297 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/piracy.txt` |
| bypass | - | DoH / VPN / proxy bypass servers (taaki devices AdGuard ko bypass na kar saken) | 16377 | OFF | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/bypass.txt` |
| universal | small | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 305473 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.small.txt` |
| universal | medium | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 627290 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.medium.txt` |
| universal | large | ON wali sabhi categories ek file me (category lists ke saath ON na karein) | 2687725 | optional | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/universal.large.txt` |
| allowlist | - | DNS allowlist (Filters -> DNS allowlists me jodein) | 10 | ON | `https://raw.githubusercontent.com/kkant78/Blocklist-Hub/main/lists/allowlist.txt` |
