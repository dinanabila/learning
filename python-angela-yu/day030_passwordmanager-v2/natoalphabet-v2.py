import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data_nato = pandas.read_csv("day026_nato-alphabet/nato_phonetic_alphabet.csv")

nato_dict = {akurow.letter:akurow.code for (akuindex, akurow) in data_nato.iterrows()}

# ======================================== V2 =============================================
def generate_phoenic():
    #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    kata_yang_mau_dieja = input("Ketik kata yang mau dieja: ").upper()


    # angela ga bikin kayak gini:
    # huruf_yang_harus_dieja = [huruf for huruf in kata_yang_mau_dieja]
    # nato_yang_harus_dieja = [nato_dict[huruf] for huruf in huruf_yang_harus_dieja if huruf in nato_dict]


    # # ini kalau versi pakai raise (worked)
    # for huruf in huruf_yang_harus_dieja:  
    #     if huruf != nato_dict.keys:
    #         raise ValueError("Ups. Kamu pakai angka/simbol selain huruf. Pakai huruf aja ya")


    # ini yang sesuai arahan angela
    try:
        nato_yang_harus_dieja = [nato_dict[huruf] for huruf in kata_yang_mau_dieja]
    except KeyError:
        print("Ups. Kamu pakai angka/simbol selain huruf. Pakai huruf aja ya")
        generate_phoenic()
    else:
        print(f"Ini ejaan nato-nya: {nato_yang_harus_dieja}")

generate_phoenic()
# ======================================= END V2 ==========================================