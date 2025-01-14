import turtle
import pandas as pd

FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "day025_us-states-game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tulisan_state = turtle.Turtle()
tulisan_state.color("black")
tulisan_state.hideturtle()
tulisan_state.penup()

jumlah_yang_bener = 0
score_board = "Guess the states"

data = pd.read_csv("day025_us-states-game/50_states.csv")

# harus diubah jadi list supaya bisa dimasukin ke if di bawah
list_semua_state = data["state"].to_list()
list_tebakan_yang_bener = []

while jumlah_yang_bener < len(list_semua_state):
    jawaban_state_dari_user = screen.textinput(title=score_board, prompt="Ketik statenya").title()
    
    if jawaban_state_dari_user == "Exit":
        # states_to_learn = []
        # for state in list_semua_state:
        #     if state not in list_tebakan_yang_bener:
        #         states_to_learn.append(state)
        # ================  
        # challenge day 26: persingkat 4 baris kode di atas, pakai list comprehension
        states_to_learn = [state for state in list_semua_state if state not in list_tebakan_yang_bener]
        # end challenge  
        # ================ 
        df = pd.DataFrame(states_to_learn)
        df.to_csv("day025_us-states-game/states_to_learn.csv")
        break
    
    if jawaban_state_dari_user in list_semua_state and jawaban_state_dari_user not in list_tebakan_yang_bener:
        jumlah_yang_bener += 1
        # pakai item(), soalnya itu masih bentuk series yang ada indeks, bukan langsung int doang
        koor_x = data[data["state"] == jawaban_state_dari_user]["x"].item()
        koor_y = data[data["state"] == jawaban_state_dari_user]["y"].item()
        tulisan_state.goto(koor_x,koor_y)
        tulisan_state.write(f"{jawaban_state_dari_user}", align="center", font=FONT)
        score_board = f"{jumlah_yang_bener}/50 States Correct"
        list_tebakan_yang_bener.append(jawaban_state_dari_user)

    # =====
    # DEBUG
    # =====
    print(type(koor_x))
    print(koor_y)
    print(jumlah_yang_bener)
    print(jawaban_state_dari_user)
    # =========
    # END DEBUG
    # =========


screen.exitonclick()







# =================================================
# KODE UNTUK DAPETIN KOORDINAT MASING-MASING STATES
# =================================================
# ini dapetnya dari stackoverflow: 

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
# ===================================================
# END KODE, MAKASIH ANGELA UDAH NGUMPULIN DATANYA DD:
# ===================================================

# screen.exitonclick()