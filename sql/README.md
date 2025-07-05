# Faedah SQL

Beberapa hari lalu aku sempet iseng bikin [dataset histori match magic chess go go para player mythic](https://github.com/dinanabila/mcgg-matches-dataset). Terus hari ini mulai nyobain analisis pakai dataset itu. Data udah di-load di notebook. Sampai situ aman. Tapi pas masuk di bagian EDA dan bikin kondisional untuk periksa data dengan kondisi tertentu, jadinya kepikiran:

"Wah, ini kalau si kode loop nya diaplikasikan untuk dataset yang besar banget, nge-loop nya bakal banyak banget dong, dan imbasnya jadi lama! Terus jadi beratin komputer juga lama-lama D:"

Walhasil, engganlah diri buat lanjutin EDA nya pakai python. Pending dulu. 

Berkelana, berkelana. Kebetulan lagi pengen nginget-nginget SQL lagi. Terus bukan [the odin project](https://www.theodinproject.com/lessons/node-path-databases-databases-and-sql#the-worlds-fastest-semi-complete-explanation-of-sql), pikirku siapa tau ada. Dan ada. Dan nemu lah pencerahan dari case EDA tadi yang sempet bikin enggan lanjut. 

SQL itu kan bahasa yang sebenernya simpel. Simpel, dan juga singkat padat jelas, tapinya berguna banget buat nyaring data, terlebih dari database dengan jumlah data yang banyaaaaaaaaaaak banget. SQL bisa bikin penggunanya nyaring data hanya dengan beberapa 'query' simpel. Dan, kesaring. Database yang tadinya bejibun, jadi kesaring hanya dengan beberapa kata. Dan kabar baiknya, program loop kondisional yang mau dipakai di EDA tadi, jadi ga perlu lagi nge-loop manual satu-satu datanya buat meriksain. Karena, udah disaring dengan seamless nya sama query SQL. 

05/07/2025
