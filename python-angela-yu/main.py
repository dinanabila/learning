from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# TODO 2: matiin coffee machine kalau user input str "off"
aksi_user = 'on'
while aksi_user != 'off':

    mesin_seduh = CoffeeMaker()
    kasir = MoneyMachine()

    # TODO 1: tanya user mau apa?
    pilih_kopi = Menu()
    print(f"Menu: {pilih_kopi.get_items()}")

    aksi_user = input("Ketik kopi yang diinginkan: ").lower()

    # TODO 3: print report
    if aksi_user == 'report':
        mesin_seduh.report()
        kasir.report()
    elif aksi_user =='off':
        aksi_user = 'off'
    else:
        kopi = pilih_kopi.find_drink(aksi_user)
        # TODO 4: cek bahannya cukup atau ga sesuai kopi yang dipesan
        # TODO 7: seduh kopi
        if mesin_seduh.is_resource_sufficient(kopi):
            kasir.make_payment(kopi.cost)
            mesin_seduh.make_coffee(kopi)
            # TODO 5: hitung koin
            # TODO 6: cek transaksinya sukses ga