MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


isi = {
    "water": 300, #300
    "milk": 200, #200
    "coffee": 100, #100
    "duid": 0
}


#KOIN
QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01


def report():
    print(f'''
        ======= REPORT =======\n
        Water: {isi["water"]}ml
        Milk: {isi["milk"]}ml
        Coffee: {isi["coffee"]}g
        Money: ${round(isi["duid"], 2)}\n
        ===== END REPORT =====
        ''')
    balik_ke_menu()


def akhiri_transaksi(koin_dari_user):
    akhiri_transaksi = input("\nTekan tombol 'enter' untuk mengakhiri transaksi: ")
    if akhiri_transaksi == '':
        isi["duid"] += koin_dari_user
        print('\n' * 100)
        return coffee_machine()
    

def balik_ke_menu():
    ke_menu = input("Tekan tombol 'enter' untuk kembali ke menu awal: ")
    if ke_menu == "":
        print("\n" * 100)
        return coffee_machine()


# TODO 4. cek bahannya cukup atau ga untuk bikin pilihan kopi user
def bahannya_cukup_ga(kopi_apa):
    if kopi_apa == '1':
        nama_kopi = "Espresso"
        kopi_apa = MENU["espresso"]
    elif kopi_apa == '2':
        nama_kopi = "Latte"
        kopi_apa = MENU["latte"]
    elif kopi_apa == '3':
        nama_kopi = "Cappuccino"
        kopi_apa = MENU["cappuccino"]
    
    # ================
    # awalnya nyobain: 
    # ================
    # if kopi_apa["ingredients"]["water"] > ISI["water"]:
    #      print("Maaf, airnya ga cukup")
    # elif kopi_apa["ingredients"]["milk"] > ISI["milk"]:
    #     print("Maaf, susunya ga cukup")
    # elif kopi_apa["ingredients"]["coffee"] > ISI["coffee"]:
    #      print("Maaf, kopinya ga cukup")
    # else:
    #     print("silakan kopinya")

    # tapi ini ga bisa karena espresso ga pakai milk
    # jadi kayak gini:

    for bahan, qty in kopi_apa["ingredients"].items():
        if isi.get(bahan) < qty:
            print(f"Maaf, {bahan}-nya ga cukup\n")
            balik_ke_menu()
        else:
            isi[bahan] -= qty

    print(f"\nBaik, {nama_kopi}-mu harganya ${kopi_apa['cost']}")
    return kopi_apa


# TODO 5. process coins
# TODO 6. cek transaksi berhasil atau ga
# TODO 7. bikin kopi
def masukkan_koin(kopi_apa):
    total_koin = 0
    while total_koin < kopi_apa['cost']: 
        print(f'''\nKoin: 
1. quarters: $0.25
2. dimes: $0.10
3. nickles: $0.05
4. pennies: $0.01 
5. yah koinku ga cukup (refund)
\nKoinmu masih kurang ${round((kopi_apa['cost'] - total_koin), 2)}''')
        pilihan_koin = input("Silakan masukkan koinnya (1/2/3/4/5): ")
        if pilihan_koin == '5':
            print("\nOke gapapa. Silakan ambil refund-nya")
            print("Datang lagi nanti ya ( 'v')/")
            for bahan, qty in kopi_apa['ingredients'].items():
                isi[bahan] += qty
            return balik_ke_menu()
        else:
            if pilihan_koin == '1':
                koin = QUARTERS
            elif pilihan_koin == '2':
                koin = DIMES
            elif pilihan_koin == '3':
                koin = NICKLES
            elif pilihan_koin == '4':
                koin = PENNIES
        
            total_koin += koin

            if total_koin > kopi_apa['cost']:
                if round((total_koin - kopi_apa['cost']), 2) < isi["duid"]:
                    print("\nTransaksi berhasil")
                    print(f"Kembaliannya ${round((total_koin - kopi_apa['cost']), 2)}. Silakan diambil.")
                    isi["duid"] -= (round((total_koin - kopi_apa['cost']), 2))
                    print(f"\nSelamat menikmati kopi Anda ( 'v')/")
                    akhiri_transaksi(total_koin)
                else:
                    print("\nMaaf, kami belum punya kembaliannya.")
                    print("Silakan ambil kembali koin Anda dan masukkan koin pas.\n")
                    for bahan, qty in kopi_apa['ingredients'].items():
                        isi[bahan] += qty
                    return balik_ke_menu()

            elif total_koin == kopi_apa['cost']:
                print("\nTransaksi berhasil")
                print(f"Selamat menikmati kopi Anda ( 'v')/")
                akhiri_transaksi(total_koin)


# TODO 1. tanya user, mau minum apa? (espresso/latte/cappuccino)
# ==============
# awalnya nyoba: 
# ==============
# for i in range(len(MENU)):
#     print(f"{i + 1}. {MENU[i]}")
# oh iya ga bisa gini, kan MENU itu dictionary o_o
# jadi print manual aja

def coffee_machine():
    # TODO 2. matiin coffee machine kalau user input str "off"
    aksi_user = 'on'
    while aksi_user != 'off':
        print("1. Espresso   ($1.5)\n2. Latte      ($2.5)\n3. Cappuccino   ($3)")
        aksi_user = input("Mau minum apa? (Ketik 1/2/3): ")

        # TODO 3. print report (tampilin daftar sisa ingredients di coffee machine)
        if aksi_user == 'report':
            report()
        elif aksi_user == '1' or aksi_user == '2' or aksi_user == '3':
            kopi = bahannya_cukup_ga(aksi_user)
            masukkan_koin(kopi)


coffee_machine()