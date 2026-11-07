# Linux Web Server Deployment with Apache

## Lab Overview

Written record of installing Apache on an Ubuntu server described here as a DigitalOcean droplet. This folder contains the write-up only: no screenshot, no config file, and no saved command output.

The version strings, droplet size, and public address below come from this text. They are not confirmed by another file in the repository. A later request to the recorded address did not return the Apache site described here. See [Recorded address, and a later check](#recorded-address-and-a-later-check).

## Tools Used
- **DigitalOcean** - Cloud infrastructure platform
- **Ubuntu Server 22.04 LTS** - Linux operating system
- **Apache HTTP Server** - Web server software
- **SSH** - Remote login. The commands below record a root login
- **Nano** - Command-line text editor

## Methodology

### 1. Cloud Infrastructure Setup
- Created DigitalOcean account
- Deployed Ubuntu 22.04 LTS droplet (1GB RAM, 25GB storage)
- Configured basic droplet settings and authentication
- Obtained public IP address: 167.71.104.44

### 2. System Administration
- Connected to server via SSH: `ssh root@167.71.104.44`
- Updated system packages: `apt update && apt upgrade -y`
- Managed package configurations and kernel updates
- Handled service restarts and system maintenance

### 3. Web Server Installation
- Installed Apache: `apt install apache2 -y`
- Verified Apache service status and configuration
- Confirmed web server accessibility via public IP
- Tested default Apache welcome page functionality

### 4. Custom Web Content
- Located web root directory: `/var/www/html/`
- Edited index.html using nano text editor
- Created custom HTML content showcasing lab completion
- Implemented file management and content deployment

## Key Findings

These points restate the procedure above. They are not backed by a screenshot or config in this folder.

### Cloud Infrastructure Experience
- The write-up records creating a DigitalOcean account and one Ubuntu 22.04 droplet (1GB RAM, 25GB storage)
- It records the address 167.71.104.44
- It does not include billing output, a droplet screenshot, or a later inventory of the account

### Linux System Administration
- The write-up records `apt update && apt upgrade -y` and an Apache package install
- It records editing `/var/www/html/` with nano
- It does not include the command transcript

### Web Server Configuration
- The write-up says Apache was installed with `apt install apache2 -y` and that the default page, then a custom `index.html`, was reachable
- It does not show the Apache config, the HTML that was published, or a browser capture

### Network and Security
- The write-up records an SSH login as root and HTTP on port 80
- It does not document a firewall, key-only SSH, fail2ban, or TLS
- Default Ubuntu and Apache packages are not, by themselves, a hardening result shown here

## Recorded address, and a later check

The steps above recorded **http://167.71.104.44** and described the Apache page as active on 2025-09-16.

On 2026-11-07 that URL was requested again during this documentation review:

- `HEAD http://167.71.104.44/` returned `403 Forbidden` with header `Server: nginx` (response date `Sat, 07 Nov 2026 14:33:53 GMT`)
- `GET http://167.71.104.44/` returned a short HTML page whose only frame loads `https://cloudways-static-content.s3.us-east-1.amazonaws.com/error_page/maintenance-domain-mapping.html` (that URL returned HTTP 200 when requested on its own)
- A normal HTTPS request failed certificate verification (curl exit 60). The certificate on port 443 has subject `CN=*.cloudwaysapps.com`, SAN `*.cloudwaysapps.com` and `cloudwaysapps.com`, `notBefore` Aug 17 2026, issuer `SSL.com TLS Issuing ECC CA R2`. The name does not match the IP. The certificate date is after this lab's 2025-09-16 note
- `HEAD https://167.71.104.44/` with certificate checks disabled returned `403 Forbidden` and `Server: nginx`

That is not an Apache page and it does not match this write-up. The address may no longer be the droplet described above. Do not treat the link as a working demo of this lab.

## Topics practiced in this lab

Topics named by the procedure above. Not a record of employment or a certification.

- Cloud VM creation, as described in the write-up
- Linux package updates and an Apache package install, as described in the write-up
- SSH access, recorded as a root login
- Editing a file under the web root with nano
- No stored evidence of hardening, monitoring, or backup

## Technical Environment

As recorded in this write-up only. Not confirmed by a screenshot, package listing, or config file in this folder.

- **Cloud Provider**: DigitalOcean
- **Operating System**: Ubuntu Server 22.04 LTS
- **Web Server**: Apache/2.4.52
- **Access Method**: SSH (OpenSSH), recorded as root
- **Text Editor**: GNU nano 6.2
- **Package Manager**: APT (Advanced Package Tool)

---
*Lab completed as part of cybersecurity infrastructure learning path*
