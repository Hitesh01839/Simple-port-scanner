# Simple Python Port Scanner

This is a simple command-line Python script that allows you to scan a range of ports on a given IP address.

# Requirements

- Python 3.x

# Usage

1. Clone this repository or download the port_scanner.py file.

2. Open a terminal and navigate to the directory containing the port_scanner.py file.

3. Run the script with the following command:

```
python port_scanner.py
```

The script will prompt you to enter the target IP address and the range of ports to scan.

4. Enter the target IP address in the format x.x.x.x, where each x is a number between 0 and 255.

5. Enter the starting and ending port numbers separated by a space. For example, 80 100 will scan ports from 80 to 100 (inclusive).

6. The script will then display the open ports within the specified range on the target IP address.

# Example

```
$ python port_scanner.py
Enter the target IP address: 192.168.1.1
Enter the starting and ending port numbers: 80 100
Scanning ports 80 to 100 on 192.168.1.1...
Open ports: [80, 87, 88]
```

# Disclaimer

This tool is intended for educational and testing purposes only. Unauthorized port scanning of systems you do not own or do not have permission to scan may be against the law. Use this tool responsibly and only on systems you have explicit permission to scan.

# License

This project is licensed under the MIT License - see the LICENSE file for details.
