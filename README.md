# Cybersecurity & Systems Labs

Hands-on labs I built while moving from customer-facing sales and technical support into systems administration and security. Each lab has its own folder with a write-up and screenshots.

**Certifications:** CompTIA Security+, CompTIA Network+, Microsoft AZ-900

## Systems administration

### Linux Web Server Deployment with Apache
- Deployed an Ubuntu 22.04 server on DigitalOcean, connected over SSH, and updated it with `apt`
- Installed Apache and served a custom page from the public IP
- Hardening beyond Ubuntu/Apache defaults was not part of this lab
- [View lab](./linux-apache-lab/)

### Python Backup Automation Script
- My first Python script: creates timestamped backup folders and copies files into them
- Checks that files exist first, reports successes and failures, and handles errors with `try/except`
- [View lab](./python-backup-lab/)

## Security and monitoring

### Splunk SIEM Lab
- Ingested 38 simulated Apache log events into Splunk Cloud
- Used SPL to investigate brute-force logins, sensitive file access, and a large download
- Built a three-panel dashboard and saved three detection searches
- [View lab](./splunk-siem-lab/)

### Network Traffic Analysis with Wireshark
- Captured and analyzed 40,000+ packets of normal browsing traffic
- Used protocol filters, stream following, Protocol Hierarchy, and Expert Information
- [View lab](./wireshark-lab/)

### OWASP Web Application Security Testing
- Exploited SQL injection, XSS, and an unprotected `/ftp` directory in OWASP Juice Shop, a deliberately vulnerable training app
- Mapped each finding to the OWASP Top 10 with mitigations
- [View lab](./owasp-web-security-lab/)

## Skills practiced
- Linux command line, `apt`, SSH, cloud VM setup (DigitalOcean)
- Apache installation and basic configuration
- Python scripting for file automation
- Splunk and SPL: log analysis, dashboards, detection searches
- Packet analysis with Wireshark
- Web application security testing in a training environment (OWASP Top 10)
- Technical documentation

## Related projects
- [infra-health-monitor](https://github.com/KrisCyberSec/infra-health-monitor): simulated server metrics analyzed by an AI monitoring bot
- [netplus-lab](https://github.com/KrisCyberSec/netplus-lab): free Network+ study app with subnetting, port, and OSI drills

---
*Learning by building.*
