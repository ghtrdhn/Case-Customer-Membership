from membership import Membership
from tabulate import tabulate
from math import sqrt

print("Selamat datang di PacCommerce, nikmati diskon belanja anda dengan program membership")

while(True):
    username = str(input("Silahkan input nama anda: "))
    monthly_income = int(input("Silahkan input digit pertama Income perbulan anda: "))
    monthly_expense = int(input("Silahkan input digit pertama Expense perbulan anda: "))
    
    user_member= Membership(username)
    print(f' Selamat datang {user_member.username} di PacCommerce')

    tables = [
            ["Silahkan pilih Menu: "],
            ["1. Prediksi Membership anda(Wajib pilihan pertama)"],
            ["2. Show Membership requirements"],
            ["3. Show Membership Benefit"],
            ["4. Informasi Keanggotaan Membership anda"],
            ["5. Lihat Daftar Anggota Member"],
            ["6. Hitung total belanjaan anda dengan diskon"],
            ["7. Keluar Program"]
            ]    
    headers = ["Menu"]
    print("PacCommerce Membership Menu")
    print("-"*54)
    print(tabulate(tables, headers, tablefmt='github', stralign="center"))
        
    Menu = input("Silahkan input nomor menu pilihan: ")
                
    if Menu == "1":
                user_member.predict_membership(user_member.username, monthly_expense, monthly_income)
    elif Menu == "2":
                user_member.show_requirements()
    elif Menu == "3":
                user_member.show_benefit()
    elif Menu == "4":
                print(user_member.show_membership(user_member.username))
    elif Menu == "5":
                print(user_member.data)
    elif Menu == "6":
                list_harga = []
                n = int(input("Silahkan input jumlah daftar belanjaan anda: "))
                for i in range (0, n):
                        ele = int(input("Silahkan input nominal rincian belanjaan anda tanpa separator: "))
                list_harga.append(ele)
                #user_member.calculate_price(user_member.username, list_harga)
                print(user_member.calculate_price(user_member.username, list_harga))
    elif Menu == "7":
                exit()
    else:
        print("Pilihan salah, silahkan pilih menu kembali")             