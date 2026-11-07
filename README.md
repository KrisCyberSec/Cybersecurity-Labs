# Cybersecurity Labs

Learning-lab notes and screenshots. The exercises here use a personal computer, a deliberately vulnerable training app, a sample log file, or a cloud VM write-up. They are not production operations, client work, or proof of a certification.

This page is the map. Open a lab write-up for the steps. Each write-up states what is actually stored in that folder.

Checked against the files in this repository on 2026-11-07. External checks made that day are named in the sections below.

## What is in this repository

| Lab | Folder added | Evidence in git | Write-up |
| --- | --- | --- | --- |
| Wireshark capture on a Mac Wi-Fi interface | 2025-09-15 | 3 screenshots. No packet-capture file. | [Write-up](wireshark-lab/wireshark-lab/README.md) |
| Ubuntu and Apache on a DigitalOcean droplet | 2025-09-16 | Write-up only. No screenshot, config, or command log. | [Write-up](linux-apache-lab/README.md) |
| Local Python backup script | 2025-09-22 | 6 terminal screenshots. The `.py` file is not committed. | [Write-up](python-backup-lab/README.md) |
| OWASP Juice Shop 19.0.0, run locally | 2025-10-11 | 8 screenshots. No application source. | [Write-up](owasp-web-security-lab/README.md) |
| Splunk Cloud trial on a sample Apache log | 2025-10-15 | 18 screenshots. The log file is not committed. | [Write-up](splunk-siem-lab/README.md) |

Dates in the table are the git commits that added each lab folder. The Wireshark write-up sits one directory deeper than the others (`wireshark-lab/wireshark-lab/`). [This short pointer](wireshark-lab/README.md) only links there. Screenshot paths were not moved.

## What each lab supports

### Network capture (Wireshark)

`protocol-hierarchy.jpg` shows 40,281 frames on Wi-Fi `en0`. Of those, the table lists IPv4 40,266, UDP 61.2% (24,655), QUIC 57.2% (23,038), TCP 38.7% (15,589), and TLS 9.1% (3,668). `http-stream.jpg` is one unencrypted HTTP conversation; the response date in the capture is 12 Sep 2025. `expert-info.jpg` lists warnings, including DNS retransmission, a connection reset, and a failed decrypt handshake. There is no `.pcap` or `.pcapng` file, so the capture cannot be reopened from git.

### Linux web server (Apache)

The write-up records a DigitalOcean Ubuntu 22.04 droplet, package updates, `apache2`, a page under `/var/www/html/`, and the address `167.71.104.44`, described as active on 2025-09-16. It also records an SSH login as root. It names Apache/2.4.52 and GNU nano 6.2. No file in the folder confirms those version strings, the droplet size, or the page content. The write-up does not show a firewall, an SSH hardening step, or TLS.

On 2026-11-07 the recorded URL was requested again:

- `HEAD http://167.71.104.44/` returned `403 Forbidden` with `Server: nginx`
- `GET http://167.71.104.44/` returned a short HTML page that embeds `https://cloudways-static-content.s3.us-east-1.amazonaws.com/error_page/maintenance-domain-mapping.html` (that URL itself returned HTTP 200)
- A normal HTTPS request failed certificate verification. The certificate presented on port 443 has subject `CN=*.cloudwaysapps.com`, SAN `*.cloudwaysapps.com` and `cloudwaysapps.com`, and `notBefore` Aug 17 2026. That name does not match the IP, and the certificate date is after the 2025-09-16 lab note
- `HEAD https://167.71.104.44/` with certificate checks disabled returned `403 Forbidden` and `Server: nginx`

That response is not the Apache page described in the write-up. This repository does not show whether the address still belongs to the original droplet. Do not use the URL as a live demo of the lab.

### Python backup script

Screenshots show `backup_script.py` edited in nano and run with `python3` on a Mac. The run dated 2025-09-18 printed folder `backup_20250918_144111`, `Successful: 1`, and `Failed: 0`. A later listing shows `test_file.txt` inside that folder. The script is not in git. The code block in the lab README is only the `make_backup_folder` function. One screenshot is a home-directory listing; those paths are left in the image and are not copied here.

### OWASP Juice Shop

Local training app, built to be vulnerable. The startup screenshot shows `juice-shop@19.0.0`, Node.js v22.20.0, darwin arm64, and port 3000. Other screenshots show the product homepage on localhost, the Score Board challenge, the Login Admin challenge marked solved, a browser alert whose text is `XSS`, and the `/ftp` listing (including `incident-support.kdbx`). The Score Board screenshot reads **1/172** solved at the time it was taken. 172 is the catalog size in that view, not a count of finished challenges. The Login Admin banner does not show a SQL payload; the payload is text in the write-up only. This was not a test of a production site.

### Splunk sample logs

Search screenshots show source `sample-apache-logs.txt.rtf`, sourcetype `access_combined`, index `main`, and **38 events**. A `status=401` search shows **10 events**. In that failed-login view, `10.0.0.50` and `203.0.113.45` each have 5 events. `203.0.113.45` is inside the [RFC 5737](https://www.rfc-editor.org/info/rfc5737) documentation range `203.0.113.0/24`. A separate table for that address (`11-external-attacker-activity.png`) has 6 rows, all `/admin/login`: one `200` and five `401`s. The HTTP method is not in that table.

The 13-row table for `10.0.0.50` shows five `401` responses on `/admin/login` around 13:23, then `200` on `/admin/login` at 13:23:26, later `200` responses for `/admin/dashboard`, `/admin/users`, `/admin/config/database.xml`, `/admin/config/passwords.txt`, `/admin/logs/access.log`, and `/admin/download`, and `404` for `/../../etc/passwd`. An earlier draft said authentication succeeded at 3:02 PM. The screenshot does not say that: 15:02:18 is the `passwords.txt` request. An earlier draft also stated a 2.4MB download. That size is not printed on the screenshots reviewed for this edit (`07` through `18`, including both `11-` files). These are sample-log findings. They are not a live incident, and they are not evidence that an attack was stopped on a real server.

## Related public repositories

Left unchanged. Descriptions below are from each repo's public GitHub metadata and README, read on 2026-11-07.

- [infra-health-monitor](https://github.com/KrisCyberSec/infra-health-monitor) — public Python repository, last pushed 2026-10-31. GitHub description: "AIOps lab: Infrastructure Health & Anomaly Monitor using a Grok Bot. Includes scripts, simulated data, sample reports, and bot prompts for a sysadmin portfolio project." The public tree contains `README.md`, `bot-prompt.md`, `scripts/health_check.py`, `data/`, and `examples/`. Its README says the metrics are simulated. This is not a monitor attached to production systems. The script was not run as part of this documentation pass.
- [netplus-lab](https://github.com/KrisCyberSec/netplus-lab) — public JavaScript drills for CompTIA Network+ (N10-009) topics. The repo's README says it is not affiliated with CompTIA and is not a substitute for the exam. `https://kriscybersec.github.io/netplus-lab/` returned HTTP 200 on 2026-11-07. Nothing here shows an exam score or a certification.

## Not in this repository

Further systems-administration workflow labs have been described as work still to add. This commit has no folder for that work. Planned work is not finished work.

## Topics these labs touch

Practice recorded in the folders above. Not a job history and not a certification list.

- Packet capture and a protocol-hierarchy reading (Wireshark screenshots)
- A cloud VM and Apache install (write-up only; the recorded host does not currently serve that lab)
- One successful local run of a small Python copy script (screenshots; script not in git)
- A few Juice Shop training challenges (screenshots named above)
- SPL searches and dashboard screenshots over a 38-event sample log
