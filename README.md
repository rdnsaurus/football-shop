# Checklist Tugas

## Django AuthenticationForm
AuthenticationForm di Django membuat form autentikasi untuk user yang ingin login, kelebihannnya class ini menyediakan base form yang praktis dipakai pengembang aplikasi, kelemahannya class ini hanya berlaku jika seluruh user hanya memiliki 1 role.

## Implementasi Autentikasi dan Otorisasi di Django
Autentikasi berupa kerja Django untuk mengecek user yang menggunakan aplikasi sesuai atau tidak, sedangkan Otorisasi berupa kerja Django untuk membatasi user-user yang tidak semestinya mendapatkan akses fitur aplikasi. Contoh Django untuk memberikan autentikasi ada pada AuthenticationForm berupa pengecekan username dan password, sedangkan contoh Django untuk memberikan autentikasi dapat berupa penggunaan subclass user_permissions pada group/user yang tersedia di aplikasi.

## Kelebihan dan Kekurangan Session-Cookies Dalam Menyimpan State
Kelebihan mereka berdua sangat cocok dijadikan temporary memory (cache) agar saat web dijalankan user tidak ngeload terlalu lama karena state sebelumnya sudah disimpan. Kekurangan Session-Cookies, pada Cookies sizenya terbatas hanya 4096 bytes tiap cookies dan berkemungkinan diakses penyerang karena cookies ada pada sisi user, sedangkan pada session kekurangannya ada pada server yang harus menyimpan state, sehingga kalo usernya banyak berkemungkinan lama loadingnya.

## Penggunaan Cookies
Tidak, user beresiko terkena Replay Attack (man-in-the-middle). Cara mengatasinya di function logout ditambahkan method .aflush() ATAU .delete_cookie() pada session agar cookies terjaga pembaharuannya. 

## Penjelasan Langkah Checklist Tugas 4
Pada langkah pertama (implementasi login-logout-register) saya memakai class yang disediakan Django karena sudah cukup praktis (AuthenticationForm-logout-UserCreationForm), implementasinya sama seperti di Tutorial 3. Untuk mengakses aplikasi sebelumnya, saya memakai cookies, cara implementasinya cukup diberi cookies pada fungsi login di views.

Pada langkah kedua, setelah aplikasi dipush ke PWS, saya membuat dua akun dan tiga items sesuai instruksi dan fitur yang tersedia.

Pada langkah ketiga, untuk menghubungkan product dengan user, pada fungsi create_item pada pengisian form ditambahkan tiga line, line pertama berisi pengisian form dengan commit false agar tidak langsung disimpan, lalu line kedua berisi pendaftaran user pada item, lalu line ketiga berisi penyimpanan form yang sudah lengkap atributnya (implementasi dapat dilihat pada views.py line 32-34).

Pada langkah keempat, untuk memberikan informasi waktu login terakhir, pada views.py setel cookies user pada fungsi show_main, lalu pada main.html tambahkan line yang memberikan informasi terkait login terakhir, hal ini didapat dari cookies yang sudah didaftarkan pada fungsi show_main, cookies berisi waktu saat login yang disetel pada fungsi login sehingga informasi akan tersampaikan.
