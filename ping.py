import scapy.all as scapy
import time
try:
    ip_t=input("введите ip:")
    try:
        chislo=int(input("введите сколько пакетов будет отправлено:"))
    except ValueError:
        print("Введите число пакетов")
        exit()
    def ping(ip,count):
        p=scapy.Ether()/scapy.IP(dst=ip)/scapy.ICMP()
        try:
            while count!=0:
                ans=scapy.srp1(p,timeout=2,verbose=False)
                count-=1
                if ans:
                    if ans.haslayer(scapy.ICMP) and ans[scapy.ICMP].type==0:
                        print(f"получен ответ от {ans[scapy.IP].src} тип:Echo reply")
                else:
                    print(f"IP:{ip} не отвечает(возможно, адрес не существует или устройство выключено)")
                if count>0:
                    time.sleep(1)
        except KeyboardInterrupt:
            print("остановлено")
    ping(ip_t,chislo)   
except KeyboardInterrupt:
    print("\nОстановлено")
