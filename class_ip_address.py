# TUGAS#1
# Dika Aditya Putra
print ("==================================PERHATIAN!!==================================\n \
               Dimohon untuk memasukkan IP dengan angka 3 digit\n\
==================================TERIMA KASIH=================================\n")

name_user = input("Masukkan Username: ")
class_a = input("IP Kelas A: ")
class_b = input("IP Kelas B: ")
class_c = input("IP Kelas C: ")
print (f"\nHalo {name_user}, Ini IP Address Kamu Adalah:\n\
- A = {class_a}\n- B = {class_b}\n- C = {class_c}\n")

print (f"======================== SUBNETTING {name_user} =========================")

print (f"IP Kelas A: {class_a}\nHOST ID: {class_a[4:]}\nNETWORK ID: {class_a[:3]}\n")
print (f"IP Kelas B: {class_b}\nHOST ID: {class_b[8:]}\nNETWORK ID: {class_b[:7]}\n")
print (f"IP Kelas C: {class_c}\nHOST ID: {class_c[12:]}\nNETWORK ID: {class_c[:11]}")
