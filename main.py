import socket
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

from threading import Thread, Lock


print_lock = Lock()

def scanHost(ip, startPort, endPort):
    print('[*] Starting TCP port scan on host %s' % ip)

    tcp_scan(ip, startPort, endPort)
    print('[+] TCP scan on host %s complete' % ip)

def scanRange(network, startPort, endPort):
    print('[*] Starting TCP port scan on network %s.0' % network)
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete' % network)

def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tcp.settimeout(0.1)
            if not tcp.connect_ex((ip, port)):
                with print_lock:
                    print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
        except Exception:
            pass

def network_scan(target_ip):

    arp = ARP(pdst=target_ip)

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []

    for sent, received in result:

        clients.append({'ip': received.psrc, 'mac': received.hwsrc})


    with print_lock:
        print("Available devices in the network:")
        print("IP" + " "*18+"MAC")
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))

def main():
    print("1. TCP Port Scanner")
    print("2. Network Scanner")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        network = input("IP ADDRESS: ")
        startPort = int(input("START PORT: "))
        endPort = int(input("END PORT: "))
        scanHost(network, startPort, endPort)
    elif choice == 2:

        target_ip = input("Enter the target IP address (e.g., 172.17.3.1/24): ")
        network_scan(target_ip)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
    end = input("Press any key to close")