import scapy.all as scapy
import time

green='\033[92m'
red='\033[91m'
reset='\033[0m'
cian='\033[36m'
y="\033[93m"
m='\033[1;36m'
banner=r"""
  _____ _____ _   _  _____   _______ ____   ____  _      
 |  __ \_   _| \ | |/ ____| |__   __/ __ \ / __ \| |     
 | |__) || | |  \| | |  __     | | | |  | | |  | | |     
 |  ___/ | | | . ` | | |_ |    | | | |  | | |  | | |     
 | |    _| |_| |\  | |__| |    | | | |__| | |__| | |____ 
 |_|   |_____|_| \_|\_____|    |_|  \____/ \____/|______|
                                                         
                                                        
"""
print(f'{m}{banner}{reset}')
try:
    ip_t=input(f"{cian}[*]{reset} Введите ip:")
    try:
        chislo=int(input(f"{cian}[*]{reset} Введите сколько пакетов будет отправлено:"))
    except ValueError:
        print(f"{y}[!]{reset} Введите число пакетов")
        exit()
    def ping(ip,count):
        p=scapy.Ether()/scapy.IP(dst=ip)/scapy.ICMP()
        try:
            while count!=0:
                ans=scapy.srp1(p,timeout=2,verbose=False)
                count-=1
                if ans:
                    if ans.haslayer(scapy.ICMP) and ans[scapy.ICMP].type==0:
                        print(f"{green}[+]{reset} Получен ответ от {ans[scapy.IP].src} тип:Echo reply")
                else:
                    print(f"{red}[-] {reset}IP:{ip} не отвечает(возможно, адрес не существует или устройство выключено)")
                if count>0:
                    time.sleep(1)
        except KeyboardInterrupt:
            print(f"{y}[!]{reset}Остановлено")
    ping(ip_t,chislo)   
except KeyboardInterrupt:
    print(f"\n{y}[!]{reset} Остановлено")
