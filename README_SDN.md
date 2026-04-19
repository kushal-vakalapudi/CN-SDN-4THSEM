# Smart Delay Controller / Network Performance Analyzer

## Overview

This project is a simple Software Defined Networking (SDN)-related network monitoring tool developed in WSL using Python.

It measures network performance between a client and a target host by analyzing:

- Latency (Delay)
- Jitter
- Packet Loss
- Minimum and Maximum Delay

The tool helps monitor network stability and performance, which are important in SDN environments for traffic management and optimization.

---

## Features

- Measures average network delay using ping/TCP-based methods
- Calculates jitter (variation in delay)
- Detects packet loss
- Displays minimum and maximum response times
- Simple command-line interface
- Runs in WSL/Linux environment

---

## Technologies Used

- Python 3
- Linux / WSL
- TCP Socket / Ping
- SDN Concepts

---

## Project Structure

```bash
smart_delay_controller.py   # Main Python program
README.md                   # Project documentation
SDN_Report.docx             # Project report
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/smart-delay-controller.git
cd smart-delay-controller
```

---

## Run the Program

```bash
python3 smart_delay_controller.py
```

If your file is named differently:

```bash
python3 "smart_delay_controller(1).py"
```

---

## Usage

Enter a host when prompted:

```bash
Enter host (e.g., google.com): google.com
```

Example output:

```bash
Average Delay : 42 ms
Status        : SUCCESS
```

---

## How It Works

The program:

1. Sends multiple packets to a target host  
2. Measures round-trip time (RTT)  
3. Computes:

- Average delay
- Jitter
- Packet loss

4. Displays results for network analysis

---

## Example Metrics

### Latency

Measures time taken for data to travel to the server and back.

Example:

```text
40 ms
```

---

## Jitter

Measures variation in delay.

Example:

```text
40 ms, 55 ms, 38 ms
```

---

## Packet Loss

Measures failed transmissions.

Example:

```text
5 packets sent
1 lost
20% packet loss
```

---

## Applications

- SDN Monitoring
- Traffic Optimization
- Network Troubleshooting
- Performance Analysis

---

## Future Improvements

- Integrate with Mininet
- Add OpenFlow controller support
- Build graphical dashboard
- Real-time monitoring
- Dynamic routing decisions using delay metrics

---

## Author

Kushal

SDN Project — Network Performance Analyzer