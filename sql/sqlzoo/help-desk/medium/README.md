**Link Soal:** [https://sqlzoo.net/wiki/Helpdesk_Medium_Questions](https://sqlzoo.net/wiki/Helpdesk_Medium_Questions)

# 6
**Yang diminta:** List company_name beserta jumlah call, batasi perusahaan yang call nya di atas 18x <br> <br>
**Solusi:** Identifikasi dulu tabel mana aja yang diperlukan: Issue, Caller, Customer. Lalu joinkan ketiganya menjadi 1 tabel. Habis itu liat dulu isi tabel hasil JOINnya biar kebayang pas bikin GROUP BY buat ngitung jumlah call. Baru deh tau query yang tepat untuk ngitung jumlah call nya gimana --> pakai COUNT(1) yang di-GROUP BY berdasarkan company_name. Janlup terakhir dikasih batas call > 18 pakai HAVING.

# 7
**Yang diminta:** first_name dan last_name yang ga pernah nelpon <br> <br>
**Solusi:** cari Caller_id yang ga ada di daftar Caller_id di tabel Issue. Setelah dapat, pakai Caller_id itu untuk dapetin first_name dan last_name dari tabel Caller.
