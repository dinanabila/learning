from random import randint

# GLOBAL CONSTANT
GAMPANG = 10
SUSAH = 5

# bikin fungsi buat ngecek tebakan user
def cek_tebakan(tebakan_user, jawaban_benar, kesempatan):
    '''cek tebakan user dengan jawaban benar, return sisa kesempatan'''
    # kurangi kesempatan nebak user kalau tebakannya salah
    if tebakan_user > jawaban_benar:
        print("Masih ketinggian")
        return kesempatan - 1
    elif tebakan_user < jawaban_benar:
        print("Masih kerendahan")
        return kesempatan - 1
    else:
        print(f"Benar! Angkanya {jawaban_benar}")

# bikin angka random
jawaban = randint(1, 100)

# bikin fungsi untuk mode kesulitan
def mode():
    level = input("Pilih mode bermain. Ketik 'gampang' atau 'susah': ")
    if level == 'gampang':
        return GAMPANG
    else:
        return SUSAH

def game():
    sisa_kesempatan = mode()

    # ulang fungsi yang ngecek tebakan user kalau tebakannya salah
    tebakan = None
    while tebakan != jawaban:
        print(f"Tersisa {sisa_kesempatan} kesempatan nebak lagi")
        # minta user nebak angka
        tebakan = int(input("Ketik angka tebakanmu: "))
        sisa_kesempatan = cek_tebakan(tebakan, jawaban, sisa_kesempatan)
        if sisa_kesempatan == 0:
            print(f"Yah, sisa kesempatanmu habis. Angka yang benar {jawaban}")
            return

game()
