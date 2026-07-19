import socket
import time

target = input("Enter IP: ")
ports = [21, 22, 80, 443, 3306]

start = time.time()

file = open("Section2/scan_results.txt", "w")

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
        file.write(f"Port {port}: OPEN\n")
    else:
        file.write(f"Port {port}: CLOSED\n")

    s.close()

end = time.time()
print("Scan Time:", end - start)
file.close()
