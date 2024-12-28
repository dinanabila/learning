print("Ini program kalkulator tip, buat ngitung sokongan secara merata dan cepat. Ini bakal berguna pas nongki-nongki bareng ;)") 

total_bayar = float(input("\ntotal yang harus dibayar (ketik lalu enter): "))
persen_tip = int(input("\n% tip yang ingin dibayar dari total yang harus dibayar \n(ketik lalu enter, cukup masukkan angka aja tanpa simbol '%'): "))
jumlah_orang = int(input("\nberapa orang yang sokongan? (ketik lalu enter): "))

# note: notice setiap sebelum input di atas kukasih float / int? 
# itu harus. soalnya, tipe data dari output nya fungsi input() itu pasti selalu string. 
# jadi perlu diubah dulu tipe data nya jadi numerik, 
# biar value nya bisa dihitung secara matematis :))

bayar_per_orang = (total_bayar + ((persen_tip / 100) * total_bayar)) / jumlah_orang 

print("\nMasing-masing orang harus bayar sebesar: "  + str(round(bayar_per_orang, 2)))

# Untuk pengembangan lebih lanjut: 
# gimana untuk case: 
# yang sokongan banyak banget, atau, 
# % tip nya >100% saking dermawannya sampe ngelebihin total bayaran awal, atau
# ada yang iseng input tip nya pakai negatif -,,- saking kikirnya, atau
# gimana kalau jumlah yang sokongan itu 0? ghaib, 
# dan segala hal lainnya di luar dugaan yang belum tercatat di sini
