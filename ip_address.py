import ipaddress

ip = ipaddress.IPv4Address("192.168.2.14")
ipwithprefix = ipaddress.IPv4Network("192.168.2.14/24", False)

print("IP Address:", ip)
print("IP Address with prefix:", ipwithprefix)
print("Network netmask:", ipwithprefix.netmask)
print("Broadcast address:", ipwithprefix.broadcast_address)
print("Number of hosts under", str(ipwithprefix), ":", ipwithprefix.num_addresses)

i = 0
for host in ipwithprefix.hosts():
    i = i + 1
print("Number of addresses under", str(ipwithprefix), ":",i)