# Network and Port Scanner

## Overview

This project provides two functionalities:
1. **TCP Port Scanner**: Scans TCP ports within a specified range for a given IP address.
2. **Network Scanner**: Discovers devices within a specified IP network using ARP (Address Resolution Protocol).

## Requirements

- Python 3.x
- `socket` library
- `scapy` library

## Installation

1. Clone the repository:
   ```bash
   git clone [repository_url]
   ```

2. Install the required Python libraries:
   ```bash
   pip install scapy
   ```

## Usage

### 1. TCP Port Scanner:
- Enter `1` when prompted for the choice.
- Provide the IP address, start port, and end port for scanning.

### 2. Network Scanner:
- Enter `2` when prompted for the choice.
- Specify the target IP address in CIDR notation (e.g., `172.17.3.1/24`).

## Functionality

### TCP Port Scanner:
The scanner will sequentially check each port within the specified range (inclusive) for the provided IP address. If a port is open, it will display a message indicating that the port is open.

### Network Scanner:
This utilizes ARP to discover devices within the provided IP network. It sends ARP requests to all IP addresses in the network and listens for responses. Once completed, it displays the IP and MAC address of all discovered devices.

## Output

### For the TCP Port Scanner: 
The output will list all open TCP ports for the specified IP address within the given range.

### For the Network Scanner:
The output will display a list of devices along with their IP and MAC addresses that are active within the specified network.

## Note

- Ensure that you have the necessary permissions to scan the network or IP addresses.
- Use this tool responsibly and only on networks and systems you have permission to scan.

## Contributors

- [Janani](https://github.com/Janani-m17)
- [Shrinaya](https://github.com/skshrinaya)
