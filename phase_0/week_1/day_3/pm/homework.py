# NEW CHALLENGE
# Loop, Conditional IF, Function, Numpy
#Buatlah sebuah fungsi untuk mendeteksi suatu kata terdapat pada suatu kalimat dan posisinya berada di kata 
# ke-berapa dalam sebuah kalimat. Gunakan Loop, Conditional If, dan Numpy array untuk kasus ini.

# In: word_detection("apa", "apa kabar kamu?")
# Out: Kata 'apa' berada di kata ke-1 pada kalimat ini.

#In: word_detection("apa", "kamu siapa namanya?")
#Out: Kata 'apa' tidak terdapat pada kalimat ini.

import numpy as np

def word_detection():
    kalimat = input("Masukan kalimat anda: ").lower()
    kata = input("Masukan kata yang ingin anda cari: ").lower()

    while kata not in kalimat:
        print(f"Kata {kata} tidak terdapat pada kalimat ini.")
        kalimat = input("Masukan kalimat anda: ").lower()
        kata = input("Masukan kata yang ingin anda cari: ").lower()

    if kata in kalimat:
        keywords = kalimat.split()
        kata_pos = keywords.index(kata)
        kata_pos += 1
        print(f"Kata {kata} berada di kata ke-{kata_pos} pada kalimat ini.")
        
word_detection()