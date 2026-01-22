import scapy.all as scapy
import time as time

green='\033[92m'
red='\033[91m'
reset='\033[0m'
cian='\033[36m'
y="\033[93m"
m='\033[1;36m'
banner=r"""
  _______  _____  ____  _____   ______   
|_   __ \|_   _||_   \|_   _|.' ___  |  
  | |__) | | |    |   \ | | / .'   \_|  
  |  ___/  | |    | |\ \| | | |   ____  
 _| |_    _| |_  _| |_\   |_\ `.___]  | 
|_____|  |_____||_____|\____|`._____.'                                                                                                 
"""
print(f'{m}{banner}{reset}')
try:
    ip_t=input(f"{cian}[*]{reset} Введите ip:")
    try:
        chislo=int(input(f"{cian}[*]{reset} Введите сколько пакетов будет отправлено:"))
    except ValueError:
        print(f"{y}[!]{reset} Введите число пакетов")
        exit()
    def guess_os(t):
        if t>128:
            return "Сетевое оборудование"
        elif t>64:
            return "Windows"
        else:
            return "Linux/Unix/Android"
    def ping(ip,count):
        send=0
        received=0
        rtt_list=[]
        p=scapy.IP(dst=ip)/scapy.ICMP()
        try:
            while count!=0:
                
                ans=scapy.sr1(p,timeout=2,verbose=False)
        
                send+=1
                count-=1
                
                if ans:
                    if ans.haslayer(scapy.ICMP) and ans.haslayer(scapy.IP) and ans[scapy.ICMP].type==0:
                        received+=1
                        rtt=(ans.time-p.sent_time)*1000
                        rtt_list.append(rtt)
                        ttl=ans[scapy.IP].ttl
                        os=guess_os(ttl)
                        print(f"{green}[+]{reset} Получен ответ от {ans[scapy.IP].src}, TTL={ttl}, Время={rtt:.2f}, тип:Echo reply, os:{os}")
                else:
                    print(f"{red}[-] {reset}IP:{ip} не отвечает(возможно, адрес не существует или устройство выключено)")
                
                if count>0:
                    time.sleep(1)
            if rtt_list:
                sr=sum(rtt_list)/len(rtt_list)
                print(f"---Статистика для {ip}---")
                print(f"Пакетов отправлено={send}, получено={received}, потеряно={send-received}")
                print("Приблизительное время приема-передачи в мс: ")
                print(f"Минимальное={min(rtt_list):.2f}")
                print(f"Максимальное={max(rtt_list):.2f}")
                print(f"Среднее={sr:.2f}")
        except KeyboardInterrupt:
            print(f"{y}[!]{reset} Остановлено")
            if rtt_list:
                sr=sum(rtt_list)/len(rtt_list)
                print(f"---Статистика для {ip}---")
                print(f"Пакетов отправлено={send}, получено={received}, потеряно={send-received}")
                print("Приблизительное время приема-передачи в мс: ")
                print(f"Минимальное={min(rtt_list):.2f}")
                print(f"Максимальное={max(rtt_list):.2f}")
                print(f"Среднее={sr:.2f}")
    ping(ip_t,chislo)   
except KeyboardInterrupt:
    print(f"\n{y}[!]{reset} Остановлено")

