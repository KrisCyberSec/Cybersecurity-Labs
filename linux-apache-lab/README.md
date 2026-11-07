# Linux Web Server Deployment with Apache

## Lab Overview
Deployed a Linux web server using Ubuntu and Apache on DigitalOcean cloud infrastructure, demonstrating cloud deployment and system administration skills.

## Tools Used
- **DigitalOcean** - Cloud infrastructure platform
- **Ubuntu Server 22.04 LTS** - Linux operating system
- **Apache HTTP Server** - Web server software
- **SSH** - Secure remote access
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

### Cloud Infrastructure Experience
- Successfully provisioned and managed cloud-based virtual machine
- Demonstrated understanding of cloud resource allocation and costs
- Gained experience with DigitalOcean platform and droplet management

### Linux System Administration
- Performed system updates and package management using apt
- Managed system services and configuration files
- Handled kernel updates and service restarts safely
- Navigated Linux file system and permissions

### Web Server Configuration
- Apache installed and configured successfully on first attempt
- Web server immediately accessible from public internet
- Default configuration served the page with no extra setup
- Custom content deployment completed without service interruption

### Network and Security
- Managed the server over SSH as `root`
- Public web service exposed on standard HTTP port 80
- Server was reachable from the internet at http://167.71.104.44
- No hardening beyond Ubuntu/Apache defaults was done in this lab (see Next Steps)

## Live Demonstration
**Public Server**: http://167.71.104.44 *(last confirmed active 9/16/2025; the droplet may no longer be running)*

Deployed a publicly accessible web server on a cloud VM.

## Next Steps (not done in this lab)
- Create a non-root user with `sudo` and disable root SSH login
- Switch to SSH key authentication and disable password login
- Enable a firewall (`ufw`) allowing only SSH, HTTP, and HTTPS
- Add HTTPS with a Let's Encrypt certificate
- Turn on automatic security updates

Step-by-step commands for all of these are in [HARDENING.md](./HARDENING.md). It is a guide I have not run yet.

## Skills Demonstrated
- Cloud infrastructure deployment and management
- Linux command-line proficiency and system administration
- Web server installation and configuration
- SSH remote access
- File system navigation and text editing
- Package management and system updates
- HTML content creation and deployment
- Confirming a service is reachable from the public internet

## Technical Environment
- **Cloud Provider**: DigitalOcean
- **Operating System**: Ubuntu Server 22.04 LTS
- **Web Server**: Apache/2.4.52
- **Access Method**: SSH (OpenSSH)
- **Text Editor**: GNU nano 6.2
- **Package Manager**: APT (Advanced Package Tool)

---
*Lab completed as part of cybersecurity infrastructure learning path*
