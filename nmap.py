import nmap

scanner = nmap.PortScanner()
scanner.scan('example.com', '1-1024')
print(scanner.all_hosts())
