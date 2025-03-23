def subnetMask(cidr):
    return "1" * cidr + "0" * (32-cidr)

def main():
    ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    ip1 = str(ip_address[0])
    ip2 = str(ip_address[1])
    ip3 = str(ip_address[2])
    ip4 = str(ip_address[3])
    cidr1 = int(ip1[14:])
    cidr2 = int(ip2[14:])
    cidr3 = int(ip3[14:])
    cidr4 = int(ip4[14:])
    subnetMask1 = subnetMask(cidr1)
    subnetMask2 = subnetMask(cidr2)
    subnetMask3 = subnetMask(cidr3)
    subnetMask4 = subnetMask(cidr4)
    listaSubnet = [subnetMask1, subnetMask2, subnetMask3, subnetMask4]
    with open("esVerifica2.3.txt", 'w') as file:
        file.write(str(ip_address))
        file.write("\n")
        file.write(str(listaSubnet))

if __name__ == "__main__":
    main()

import ipaddress

def subnetMask(network):
    return network.netmask

def main():
    ip_address=["192.168.222.0/27","192.168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    
    networks = [ipaddress.IPv4Network(ip, strict=False) for ip in ip_address]
    f = open("mask.txt", "w")
    f.writelines([f"{str(network)} - {subnetMask(network)}\n" for network in networks])
    
    f.close()

if __name__ == "__main__":
    main()

def main():
    ip_addresses = ["192.168.222.0/27","192.168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    file = open("mask.txt", "w")
    for ip in ip_addresses:
        ip, subnetMask = ip.split("/")
        subnetMask_int = int(subnetMask)
        subnetMask_bin = '1' * subnetMask_int + '0' * (32 - subnetMask_int)
        #subnetMask_bin = subnetMask_bin[:8] + "." + subnetMask_bin[8:16] + "." + subnetMask_bin[16:24] + "." + subnetMask_bin[24:32]
        print('.'.join([subnetMask_bin[i:i+8] for i in range(0,32,8)]))
        file.write(f"{ip} - Subnet Mask ({subnetMask}): {subnetMask_bin}\n")
    
if __name__ == "__main__":
    main()
