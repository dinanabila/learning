**Tujuan**: ngetes alur kerja git

Di sini aku ngetes, 
*"kalau commit doang di vscode tanpa nge-push,*
*terus nge-push nya setelah beberapa commit udah dibikin,*
*kira-kira apa yang terjadi?"*

list commit berturut-turut sebelum push:
1. bikin subrepo baru
2. bikin readme.md
3. update readme.md
4. bikin test.py
5. update readme.md
6. bikin test2.txt
7. update readme

Yang terjadi adalah ini:
![alt text](image.png)

time per commit nya ke-reserved, 
jadi ga based on kapan nge-pushnya. 
yang alhasil, 
masing-masing last created commit nya tercetak based on masing-masing commit. 
**insight: created time per commit nya independen, bukan based on waktu push.** 

yang perlu dicatat juga, 
**kalau perubahan yang kita bikin belum di-save di lokal,** 
**file-nya ga ikut ke-commit.** 
jadi pastiin di-save dulu sebelum commit/ 



*"Lalu apa yang terjadi kalau late push?"*
Di sini aku coba commit update-an readme ini pukul 15.00

Aku bakal push pukul 15.30, terus cek, apa yang terjadi?
---> jawab: last created commit nya tetap ter-reserved. 
Tercatat +-30 menit yang lalu, bukan baru aja. 

![alt text](image-1.png)

Jadi, waktu commit tetap ter-reserved, ga peduli kapan waktu push-nya = **valid**.


*Pertanyaan selanjutnya: gimana kalau commit nya offline?*

