# Классная работа.
import ipaddress


# Задание 1.
print('[Задание 1]')
print(ipaddress.ip_address('10.1.1.0') + 1)
print(ipaddress.ip_address('10.1.0.255') + 1)
print(ipaddress.ip_address('10.1.1.0') - 1)
ip = ipaddress.ip_address('255.255.255.255')
ip_as_int = int(ip)
ip_as_int += 1
new_ip = ipaddress.ip_address(ip_as_int)
print(ipaddress.ip_address('::') + 300)
ip1 = ipaddress.ip_address('10.1.1.1')
ip2 = ipaddress.ip_address('10.1.1.2')
ip3 = ipaddress.ip_address('10.1.1.2')
ip4 = ipaddress.ip_address('::1')
print(ip1 > ip2)
print(ip1 == ip2)
print(ip1 != ip2)
print(ip3 == ip2)
print(ip1 != ip4)

# Задание 2.
print('[Задание 2]')
print(ipaddress.ip_address('10.1.0.255'))
print(ipaddress.ip_address('10.1.0.256'))
print(ipaddress.ip_address('172.16.0.'))
print(ipaddress.ip_address('2004:6800:4009:82b::200e'))
print(ipaddress.ip_address('::'))
print(ipaddress.ip_address('FFFE:80::1'))
print(ipaddress.ip_address('G::'))

# Задание 3.
print('[Задание 3]')
ipaddr = ipaddress.ip_address('199.138.0.1')
print(ipaddr.is_private)
print(ipaddr.is_global)
print(ipaddress.ip_address("127.0.0.1").is_loopback)
print(ipaddress.ip_address("229.100.0.23").is_multicast)
print(ipaddress.ip_address("169.254.0.100").is_link_local)
print(ipaddress.ip_address("240.10.0.1").is_reserved)
print(ipaddress.ip_address("::").is_unspecified)
print(ipaddress.ip_address("::1").is_loopback)

# Задание 4.
print('[Задание 4]')
if1 = ipaddress.ip_interface('192.168.1.140/25')
print(if1.network)
print(if1.netmask)
if2 = ipaddress.ip_interface('2001::a:b:c:d/64')
print(if2.network)
print(if2.netmask)

# Задание 5.
print('[Задание 5]')
ipnet1=ipaddress.ip_network ('192.168.1.64/28')
print(*list(ipnet1.subnets(prefixlen_diff=1)))
print(*list(ipnet1.subnets(new_prefix=29)))
print(*(list(ipnet1.subnets())))

# Задание 6.
print('[Задание 6]')
ipnet1 = ipaddress.ip_network('10.5.5.0/26')
for i in ipnet1:
    print(i)
print(ipaddress.IPv4Address('10.5.5.60') in ipnet1, ipaddress.IPv4Address('10.5.5.64') in ipnet1)
