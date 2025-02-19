import socket

# Hedef IP adresi veya ana bilgisayar adı
target = input("Taramak istediğiniz IP adresini veya ana bilgisayar adını girin: ")

# Taranacak port aralığını belirleyin (örneğin 1-1024)
port_start = 1
port_end = 1024

print(f"Taranıyor: {target}")

# Her bir port için tarama gerçekleştirin
for port in range(port_start, port_end + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout süresini belirleyin (1 saniye)

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: Açık")
    else:
        print(f"Port {port}: Kapalı")
    
    sock.close()

print("Tarama tamamlandı.")
