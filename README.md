# 0promil - Network and Stress Testing Tool

## Description
0promil is a network attack and stress testing tool designed for testing your own servers. This tool sends data packets to a target IP address over the UDP protocol to measure the resilience of the network. It also performs CPU and memory stress tests to simulate the usage of system resources.

## Features
- **UDP Attack**: Sends data packets to a target IP address for a specified duration.
- **CPU Stress Test**: Utilizes the CPU fully by performing mathematical computations.
- **Memory Stress Test**: Increases memory consumption to push the limits of the system.
- **Multi-thread Support**: Allows simultaneous attacks and stress tests with multiple threads.
- **Customizable Parameters**: Takes user input for target IP, port, number of threads, and packet size.

# 0promil - Ağ ve Stres Testi Aracı

## Açıklama
0promil, kendi sunucularınızı test etmek için kullanılan bir ağ saldırı ve stres testi aracıdır. Bu araç, UDP protokolü üzerinden hedef bir IP adresine veri paketleri göndererek ağın dayanıklılığını ölçer. Ayrıca, CPU ve bellek stres testleri gerçekleştirerek sistem kaynaklarının kullanımını simüle eder.

## Özellikler
- **UDP Saldırı**: Hedef IP adresine belirli bir süre boyunca veri paketleri gönderir.
- **CPU Stres Testi**: CPU'nun tamamen kullanımını zorlamak için matematiksel hesaplamalar yapar.
- **Bellek Stres Testi**: Bellek tüketimini artırarak sistemin sınırlarını zorlar.
- **Çoklu Thread Desteği**: Birden fazla thread ile eşzamanlı saldırı ve stres testleri yapma imkanı.
- **Özelleştirilebilir Parametreler**: Hedef IP, port, thread sayısı, paket boyutu gibi parametreleri kullanıcıdan alarak özelleştirilebilir.

## Usage
1. **Requirements**: Python 3.x must be installed.
2. **Installation**:
   ```bash
   git clone https://github.com/your_username/0promil.git
   cd 0promil
   python3 ddos.py
