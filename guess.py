#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#this is my second project

import os, platform
import random


#clear terminal's screen
if platform.system().lower() == 'windows':
    os.system('cls')
else:
    os.system('clear')

def guess(number):  
    print("Aturan: Anda memiliki 4 kesempatan untuk menebak angka antara 1 dan 10.")

    for kesempatan in range(4):
        user = int(input("Tebak angka 1 sampai 10: "))

        if user == number:
            return f"Selamat! Tebakan Anda benar, angkanya adalah: {number}"
        else:
            if user < number:
                print("Tebakan terlalu rendah.")
            else:
                print("Tebakan terlalu tinggi.")
            
            sisa_kesempatan = 3 - kesempatan
            if sisa_kesempatan > 0:
                print(f"Anda memiliki {sisa_kesempatan} kesempatan lagi. Coba lagi!\n")
            else:
                print(f"Sayang sekali! Kesempatan Anda habis. Angka yang benar adalah {number}.")


if __name__ == '__main__':
    guess(random.randint(1, 10))
