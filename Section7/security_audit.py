import socket
import time

# Simple service mapping
services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

# Simple vulnerability database
vulns = {
    21: "FTP may allow anonymous login",
    22: "SSH may be brute-forced",
    80: "HTTP may be vulnerable to XSS",
    443: "Check SSL/TLS configuration"
}

target = input("Enter Target IP: ")
ports = [21, 22, 80, 443]

start_time = time.time()

results = []

print("\nScanning...\n")

for port in ports:
    s = socket.socket()
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        status = "OPEN"
        service = services[port]
        vuln = vulns[port]
    else:
        status = "CLOSED"
        service = "N/A"
        vuln = "N/A"

    print(f"Port {port}: {status}")

    results.append((port, status, service, vuln))
    s.close()

end_time = time.time()

# Generate HTML Report
file = open("sample_report.html", "w")

file.write("<html><head><title>Security Report</title></head><body>")
file.write(f"<h2>Scan Report for {target}</h2>")
file.write(f"<p>Scan Time: {end_time - start_time:.2f} seconds</p>")
file.write("<table border='1'>")
file.write("<tr><th>Port</th><th>Status</th><th>Service</th><th>Vulnerability</th></tr>")

for r in results:
    file.write(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td></tr>")

file.write("</table></body></html>")

file.close()

print("\nReport saved as sample_report.html")
