def generate_cisco_config(interface, ip, subnet_mask, gateway):
    config = f"""
en
conf t

interface {interface}
 ip address {ip} {subnet_mask}
 no shutdown
 exit

ip default-gateway {gateway}

end
write memory
"""
    return config.strip()


if __name__ == "__main__":
    interface = "GigabitEthernet0/1"
    ip = "192.168.1.10"
    subnet_mask = "255.255.255.0"
    gateway = "192.168.1.1"

    cfg = generate_cisco_config(interface, ip, subnet_mask, gateway)
    print(cfg)
