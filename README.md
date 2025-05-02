# **SniffGuardX: Lightweight Network Intrusion Detection Tool (NIDS)** 🔒

## Overview

**SniffGuardX** is a lightweight **Network Intrusion Detection Tool (NIDS)** built using **Python** and **Scapy**. It is designed to monitor network traffic, detect flood attacks (such as **SYN floods**, **UDP floods**, and **packet flooding**), and save suspicious packets in **PCAP** format for further analysis. The tool also sends **real-time email alerts** with the **PCAP** file attached for immediate action.

SniffGuardX is cross-platform, working seamlessly on both **Windows** and **Linux**, offering an easy-to-use solution for network monitoring and protection.

---

## Key Features

- **Flood Detection**: Detects SYN, UDP, and packet flooding attacks.
- **PCAP File Generation**: Saves suspicious packets for further analysis in Wireshark.
- **Real-time Email Alerts**: Sends email notifications with the **PCAP** file attached.
- **Cross-Platform Support**: Works on both **Windows** and **Linux** systems.

---

## Installation

### For **Windows**:

1. **Install Python**: 
   Download and install Python from the [official website](https://www.python.org/downloads/).

2. **Install Dependencies**:
    Open a command prompt and install the required Python package (**Scapy**) using:
    ```bash
    pip install scapy
    ```

3. **Configure Network Interface**: 
   Ensure you have the proper network interface accessible for packet sniffing. If you're using Wi-Fi, make sure you have the necessary permissions.

4. **Run the Script**:
    You may need to run the script as Administrator if you're sniffing network traffic:
    ```bash
    python sniffguardx.py
    ```

---

### For **Linux**:

1. **Install Python**:
    Most Linux distributions come with Python pre-installed. If not, install it with:
    ```bash
    sudo apt update
    sudo apt install python3
    ```

2. **Install Dependencies**:
    Install **Scapy** and other dependencies with:
    ```bash
    sudo apt install python3-pip
    sudo pip3 install scapy
    sudo apt install libpcap-dev
    ```

3. **Run as Root**:
    To sniff packets, you’ll need to have **root privileges**:
    ```bash
    sudo python3 sniffguardx.py
    ```

---

## Usage

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/yourusername/SniffGuardX.git
   cd SniffGuardX
   ```

2. **Run the Script**:
    Run the tool with the following command. The script will prompt you to enter the number of packets to capture.
    ```bash
    python3 sniffguardx.py
    ```

3. **View Suspicious Packets**:
    If suspicious packets are detected, they will be saved as a **PCAP** file in the format `suspicious_packets_YYYYMMDD_HHMMSS.pcap`.

4. **Email Alerts**:
    The tool will automatically send an email with the **PCAP** file attached to the email address provided in the script.

---

## Test Flooding 🌐

For testing purposes, you can use tools like **hping3**, **nmap**, or **LOIC** to flood your network with traffic and trigger SniffGuardX’s detection capabilities. These tools allow you to simulate SYN floods, UDP floods, and other types of network traffic that could potentially overwhelm a server or device.

### Recommended Tools for Flooding:
- **hping3**: A network tool to generate custom TCP/IP packets, useful for SYN flood testing.
- **nmap**: A network scanning tool that can be used to flood specific ports or services.
- **LOIC (Low Orbit Ion Cannon)**: A tool for generating DDoS traffic (available for Windows).

### One-Click Test Flood Script:
If you prefer an all-in-one script for simulating network flood attacks, you can use the **`test_floods.sh`** script. This script will automatically send test floods to trigger the detection system. It is meant for **Linux** systems and can be used to simulate SYN floods, UDP floods, and general packet flooding.

To use the **test_floods.sh** script:

1. Download the script from this repository.
2. Run the script in your terminal:
    ```bash
    ./test_floods.sh
    ```

Note: This script is a basic demonstration of network flooding and is provided for educational purposes. You can also refer to other tools like **hping3** and **nmap** for more customizable and advanced testing.

---

## Real-World Use Cases 🛡️

**SniffGuardX** can be used in a variety of network security scenarios:

1. **Enterprise Networks**: Protect corporate networks from DDoS attacks and internal network floods.
2. **Home Networks**: Detect and mitigate suspicious network traffic that could indicate potential security breaches.
3. **Security Research**: Ideal for researchers analyzing malicious network traffic patterns and testing defense mechanisms.
4. **Educational Institutions**: Great for learning about **network intrusion detection**, **packet sniffing**, and **DoS attacks** in a real-world context.

---

## Suspicious Packets 📦

Suspicious packets refer to network packets that exhibit behaviors commonly associated with malicious activities:

- **SYN Floods**: A denial-of-service (DoS) attack where an attacker sends a high volume of SYN packets to a target, overwhelming it and consuming system resources.
- **UDP Floods**: A type of flood attack where the attacker sends large amounts of UDP packets, typically to random ports, to exhaust resources on the target machine.
- **Packet Flooding**: A situation where a high volume of network packets (over a defined threshold) is sent from a single IP, indicating potential misuse or attack.

The tool saves these suspicious packets in a **PCAP** file format, which can later be analyzed using tools like **Wireshark**.

---

## Future Enhancements 🔧

- **AI-based Anomaly Detection**: Incorporate machine learning to enhance detection accuracy and reduce false positives.
- **Real-time Traffic Visualization**: A dashboard to display network traffic and attack alerts in real-time.
- **Extended Attack Detection**: Broader detection for attacks like **ARP Spoofing**, **DNS Spoofing**, and others.

---

## Contributing 🤝

We welcome contributions! Here are ways you can contribute:

- **Submit issues** for bug reports or feature requests.
- **Fork the repo** and submit **pull requests** with new features or bug fixes.
- Help improve the **documentation** or provide **usage examples**.

---

## License 📝

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

This updated **README** clarifies the installation process for both Windows and Linux, includes more details about the **test flood script**, and adds context about real-world use cases for SniffGuardX. It also helps users understand the **suspicious packets** that the tool detects and their relevance to network security.
