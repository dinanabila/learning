class QuizBrain():

    def __init__(self, daftar_soal):
        self.question_number = 0
        self.question_list = daftar_soal
        self.score = 0

    def soal_masih_ada(self):
        # if self.question_number >= len(self.question_list):
        #     return False
        # else:
        #     return True

        # SIMPELNYA:
        return self.question_number < len(self.question_list)
        # ini sama aja, soalnya balikin nilai boolean juga, entah itu true, atau false

    def soal_selanjutnya(self):
        soal_sekarang = self.question_list[self.question_number]
        self.question_number += 1
        jawaban_user = input(f"Q.{self.question_number}: {soal_sekarang.soal} (True/False): ")
        self.cek_jawaban(jawaban_user, soal_sekarang.jawaban)

    def cek_jawaban(self, jawaban_user, jawaban_benar):
        if jawaban_user.lower() == jawaban_benar.lower():
            print("Kamu benar!")
            self.score += 1
        else:
            print("Ups, bukan itu..")
        print(f"Jawaban yang benar: {jawaban_benar}")
        print(f"Skor kamu sekarang: {self.score}/{self.question_number}")
        print("\n")

        # jangan gini, biarkan method di class nya bekerja sesuai namanya,
        # jadi better tarok di main.py aja ya kode ini vvvvv

        # if self.soal_masih_ada() == False:
        #     print("Quiz udah selesai!")
        #     print(f"Skor akhir kamu: {self.score}/{self.question_number}")


