**Link Soal:** [https://sqlzoo.net/wiki/Helpdesk_Easy_Questions](https://sqlzoo.net/wiki/Helpdesk_Easy_Questions)

# 1
**Yang diminta**: call_date dari issue yang mengandung kata "index" dan "Oracle" <br>
**Solusi**: pakai WHERE dan LIKE buat bikin kondisional dari kolom detail di tabel Issue

# 2
**Yang diminta**: customer bernama Samantha Hall menelpon 3x pada tanggal 2017-08-14. Tunjukkan masing-masing tanggal dan waktu (digabung) penelponannya. <br>
**Solusi**: join kan dulu tabel Caller sama Issue based on kolom Caller_id, lalu cari call_date dengan first_name Samantha dan last_name Hall. Tampilkan call_date pakai DATE_FORMAT(call_date, '%Y-%m-%d %T')

# 3
**Yang diminta**: Jumlah panggilan telpon dari customer berdasarkan status <br>
**Solusi**: pakai GROUPBY berdasarkan kolom status dari tabel Issue, terus bikin kolom baru untuk hasilnya pakai COUNT, namain kolomnya pakai AS

# 4
**Yang diminta**: Panggilan telpon dari customer biasanya ditangani oleh staf non-manager, tapi, ada juga panggilan yang dialihkan ke manager. Ada berapa panggilan yang dialihkan ke manager? <br>
**Solusi**: Pakai kolom Manager dari tabel Shift dan kolom Assigned_to dari tabel Issue. Bikin gimana caranya supaya semua yang ada di kolom Manager itu kalau ada di kolom Assigned_to berarti itu kita simpen, lalu akhirnya dihitung jumlahnya. Bikinnya pakai subquery.

# 5
**Yang diminta**: Kolom first_name dan last_name manager di setiap shift beserta tanggal dan type shift <br>
**Solusi**: Pakai kolom Manager, Shift_date, Shift_type dari tabel Shift sama kolom Staff_code, First_name, Last_name dari tabel Staff. Samain Manger sama Staff_code buat dapetin datanya. 
