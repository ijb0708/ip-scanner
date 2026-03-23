# IP-Scanner
IP-Scanner is a lightweight network scanning tool designed to track IP usage and monitor connected devices in real-time. 
It combines low-level packet analysis using Scapy with a web interface built on Flask.

## Key Features
* Real-time Network Scanning: Discovery of active devices using ARP/ICMP protocols.
* Web Dashboard: Intuitive data visualization powered by Flask.
* Container Optimization: Simple deployment using Docker and Docker-compose.

## Tech Stack
* **Language**: Python 3.11
* **Framework**: Flask 3.0.2
* **Networking**: Scapy 2.5.0 (Pure Python)
* **Server**: Gunicorn 21.2.0 (WSGI)
* **Infrastructure**: Docker, Docker-compose

## Prerequisites
Since this tool directly accesses network interfaces to scan packets, execution in a Linux environment is recommended. Privileged permissions are required when running via Docker.

## How to Run
Clone the repository

```Bash
git clone https://github.com/your-repo/ip-scanner.git
cd ip-scanner
Build and run the container

docker-compose up -d --build
```

Open your browser and navigate to http://localhost:5000 to check the scan results.

## Project Structure
```Plaintext
.
├── src/
│   ├── app.py          # Flask application entry point
│   └── scanner.py      # Scapy-based scanning logic
├── Dockerfile          # Multi-stage build and environment setup
├── docker-compose.yml  # Service definition and network configuration
├── requirements.txt    # Python dependency list
└── README.md           # Project documentation
```
## Notes
* Network Mode: Uses network_mode: "host" to directly control the host's network interface.
* Security: Designed for local network management; use caution when exposing it to public IP environments.
