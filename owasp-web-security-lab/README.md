# OWASP Web Application Security Lab

## Lab Overview
Identified and exploited critical web application vulnerabilities using OWASP Juice Shop, demonstrating understanding of common attack vectors and security weaknesses in web applications.

## Tools Used
- **OWASP Juice Shop** - Intentionally vulnerable web application for security training
- **Node.js** - JavaScript runtime environment
- **Web Browser** - For testing and exploitation
- **Command Line** - Application deployment and management

## Learning Objectives
- Understand OWASP Top 10 vulnerabilities
- Practice web application penetration testing
- Identify common security misconfigurations
- Demonstrate ethical hacking techniques

## Methodology

### 1. Environment Setup
- Installed Node.js on macOS
- Cloned OWASP Juice Shop from GitHub repository
- Deployed application locally on port 3000
- Accessed web interface at http://localhost:3000

### 2. Reconnaissance and Discovery
- Explored application functionality and features
- Identified hidden administrative interfaces
- Located Score Board to track security challenges
- Mapped application structure and endpoints

### 3. Vulnerability Exploitation

#### A. SQL Injection (Authentication Bypass)
**Vulnerability Type:** A03:2021 - Injection

**Attack Vector:**
- Targeted login form with SQL injection payload
- Used payload: `' OR 1=1--` in email field
- Successfully bypassed authentication without valid credentials

**Impact:** Complete authentication bypass allowing unauthorized access to user accounts

**Mitigation:** Implement parameterized queries, input validation, and prepared statements

#### B. Cross-Site Scripting (XSS)
**Vulnerability Type:** A03:2021 - Injection

**Attack Vector:**
- Injected malicious JavaScript payload into search functionality
- Used payload: `<iframe src="javascript:alert('XSS')">`
- Successfully executed arbitrary JavaScript in application context

**Impact:** Potential for session hijacking, credential theft, and malicious actions on behalf of users

**Mitigation:** Implement input sanitization, output encoding, Content Security Policy (CSP)

#### C. Sensitive Data Exposure
**Vulnerability Type:** A01:2021 - Broken Access Control

**Attack Vector:**
- Discovered unprotected FTP directory at `/ftp` endpoint
- Accessed without authentication or authorization
- Found exposed sensitive files including password databases and configuration backups

**Files Discovered:**
- `incident-support.kdbx` - Password vault (critical exposure)
- `package.json.bak` - Dependency information revealing potential vulnerabilities
- `legal.md` - Confidential legal documents
- `acquisitions.md` - Business sensitive information
- Configuration and backup files

**Impact:** Exposure of credentials, business confidential information, and system configuration details

**Mitigation:** Implement proper access controls, remove backup files from web-accessible directories, use .htaccess or server configuration to restrict directory access

## Key Findings

### Security Vulnerabilities Identified
Successfully demonstrated exploitation of three critical OWASP Top 10 vulnerabilities:
- SQL Injection for authentication bypass
- Cross-Site Scripting for code injection
- Broken Access Control for unauthorized file access

### Attack Surface Analysis
- Login forms vulnerable to SQL injection
- Search functionality lacks input validation
- Directory traversal and direct object reference weaknesses
- Insufficient access controls on sensitive directories

### Risk Assessment
**Critical:** Password database exposure, authentication bypass
**High:** XSS vulnerabilities enabling session hijacking
**Medium:** Information disclosure through exposed configuration files

## Skills Demonstrated
- Web application penetration testing
- OWASP Top 10 vulnerability exploitation
- SQL injection techniques
- Cross-Site Scripting (XSS) attacks
- Access control testing
- Security misconfiguration identification
- Risk assessment and impact analysis
- Security documentation and reporting

## Real-World Applications
- **Security Testing:** Methodologies applicable to web application security assessments
- **Vulnerability Research:** Understanding common attack patterns and exploitation techniques
- **Secure Development:** Knowledge of vulnerabilities informs secure coding practices
- **Risk Management:** Ability to assess and communicate security risks to stakeholders

## Ethical Considerations
This lab was conducted in a controlled environment using intentionally vulnerable software designed for security training. All testing was performed on locally hosted applications with no unauthorized access to production systems or real user data.

## Technical Environment
- **Application:** OWASP Juice Shop (latest version)
- **Platform:** macOS with Apple Silicon
- **Runtime:** Node.js
- **Browser:** Modern web browser with developer tools
- **Deployment:** Local development server (localhost:3000)

## Mitigation Recommendations

### General Security Controls
- Implement input validation and sanitization
- Use parameterized queries for database operations
- Apply principle of least privilege for file access
- Remove or secure backup and configuration files
- Implement Content Security Policy (CSP)
- Regular security testing and code reviews
- Web Application Firewall (WAF) deployment

### Specific Fixes
1. **SQL Injection Prevention:**
   - Use prepared statements with parameterized queries
   - Implement stored procedures
   - Apply input validation with whitelisting

2. **XSS Prevention:**
   - Encode all user-supplied data before rendering
   - Implement Content Security Policy
   - Use modern frameworks with built-in XSS protection

3. **Access Control:**
   - Implement authentication and authorization checks
   - Restrict directory listings
   - Remove sensitive files from web-accessible locations
   - Use role-based access control (RBAC)

## Screenshots

### Lab Setup
![Juice Shop Homepage](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/08-juice-shop-homepage.png)
*OWASP Juice Shop application homepage*

![Application Startup](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/07-application-startup-terminal.png)
*Juice Shop successfully deployed on localhost:3000*

### Vulnerability Exploitation

![Score Board](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/06-score-board-overview.png)
*Score Board showing 172 total security challenges organized by OWASP category*

![SQL Injection Success](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/5-sql-injection-success-banner.png)
*Successful authentication bypass using SQL injection*

![SQL Injection Terminal](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/04-sql-injection-terminal.png)
*Terminal confirmation of SQL injection challenge completion*

![XSS Attack](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/03-xss-alert-popup.png)
*Cross-Site Scripting vulnerability demonstration*

![Challenge Completion](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/02-score-board-challenge-solved.png)
*Terminal showing multiple challenges solved*

![FTP Directory Exposure](https://github.com/KrisCyberSec/Cybersecurity-Labs/blob/main/owasp-web-security-lab/images/01-ftp-directory-exposure.png)
*Unprotected FTP directory exposing sensitive files including password databases*
---
*Lab completed as part of web application security skills development*
