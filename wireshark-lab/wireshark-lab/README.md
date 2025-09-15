# Network Traffic Analysis with Wireshark

## Lab Overview
Captured and analyzed live network traffic to understand modern internet communication patterns and protocols.

## Tools Used
- **Wireshark** (latest version)
- **macOS** environment  
- **WiFi** network connection

## Methodology
1. Installed Wireshark and resolved ChmodBPF permissions on macOS
2. Captured live network traffic during normal web browsing (40,000+ packets)
3. Applied protocol filters (DNS, HTTP, QUIC) to isolate specific traffic types
4. Used stream following to analyze complete network conversations
5. Generated statistical reports using Protocol Hierarchy
6. Performed expert analysis to identify network anomalies

## Key Findings

### Modern Internet is Heavily Encrypted
- **57.2%** of traffic used QUIC protocol (Google's encrypted web protocol)
- **9.1%** used TLS (Transport Layer Security) 
- Minimal unencrypted HTTP traffic found

### Network Communication Patterns
- **UDP dominated** at 61.2% vs TCP at 38.7% (due to modern protocols)
- **DNS queries** preceded all web requests as expected
- **Background services** (Apple system updates) constantly active
- **40,281 total packets** captured in just a few minutes of browsing

### Network Health Analysis
- Identified DNS retransmissions and connection resets
- Expert Information revealed normal network behavior patterns
- No significant security anomalies detected

## Screenshots
*Screenshots stored in `/images` folder:*
- `protocol-hierarchy.png` - Statistical breakdown of network protocols
- `http-stream.png` - Complete HTTP request/response analysis  
- `expert-info.png` - Network anomaly and health analysis

## Skills Demonstrated
- Live packet capture and analysis
- Network protocol identification
- Traffic pattern recognition
- Stream following and conversation analysis
- Statistical network analysis
- Network forensics fundamentals

## Technical Insights Gained
- Understanding of modern encrypted web protocols (QUIC, TLS)
- Knowledge of network communication flow (DNS → Connection → Data)
- Experience with industry-standard network analysis tools
- Ability to identify and troubleshoot network issues

---
*Lab completed as part of cybersecurity skills development*
