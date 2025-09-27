# Checklist Tugas

## Urutan CSS Selector
Dari tipe CSS sendiri urutan paling pertama yg akan diimplement ke paling akhir yaitu inline, internal, external. Untuk selector, inline CSS ada pada urutan pertama, selanjutnya jika CSS tidak ada pada line html maka urutan yang diprioritaskan dari selector yang menggunakan id disusul class-attribute-pseudo class (ketiganya setara). Pengecualian untuk suatu CSS internal-external yang mendeclare attribute !important, jika terdapat dua !important pada style yang berbeda, maka dilihat dari urutan prioritas selector. Jika ada dua style dengan prioritas yang sama, maka yang akan bekerja adalah style yang dideclare duluan.

## Responsive Web Design
Responsive Web Design penting dalam pengembangan aplikasi web, karena web merupakan platform yang umumnya dapat diakses dari semua device, sehingga untuk menjaga keumuman tersebut web developer harus mengimplement fitur-fitur yang dapat diakses device lain juga. Contoh web yang menggunakan responsive web design ada di web https://muhathir-muhammad-footballshop.pbp.cs.ui.ac.id/ dan yang belum contohnya dapat dilihat dari github rdnsaurus pada commit tugas ke-4 (belum implement RWD), hal ini disebabkan pada tugas sebelumnya belum dikustomisasi untuk bagian mobile pada navbar.

## Margin, Border, dan Padding
Margin adalah jarak transparan dari luar border konten ke border lainnya. Border adalah batas yang membungkus suatu konten. Padding adalah jarak transparan dari konten ke border. Cara implementasi ketiga tools tersebut menggunakan CSS adalah dengan mendeclare langsung di inline (contoh: p-4, mx-auto, py-6) atau mendefinisikan suatu class yang ada konten berisi tools tersebut pada external/internal CSS.

## Flex Box dan Grid Layout
Flex Box adalah modul layout untuk mengatur konten sesuai kolom atau baris, sedangkan Grid Layout adalah model layout untuk mengatur konten sesuai kolom dan baris. Implementasi flexbox pada 1 dimensi, sedangkan Grid Layout 2 dimensi. 

## Penjelasan Langkah Checklist Tugas 5
Pada implementasi fungsi delete dan edit items, fungsi delete-edit sama seperti yang di tutorial dengan url yang berbeda saja. Request yang dipakai berupa delete dan post.

Pada kustomisasi page HTML saya menggunakan tailwind sebagai framework CSS, yang dipasang di skrip pada base.html. Pada halaman login-register-addproduct-editproduct-detailproduct kurang lebih saya hanya membuat satu kontainer blok berwarna putih yang diisi dengan informasi/form dihiasi background Emirates Stadium atau animasi CSS (dari global.css).

Pada kustomisasi navbar, agar web tersebut konsisten baiknya pada mobile, saya menambahkan fitur tombol yang menyederhanakan informasi di desktop. Pada kustomisasi jika produk tidak ada/ada, di main.html saya menambahkan logic 'jika terdapat barang' akan menampilkan produk, jika tidak ada barang yang dipost maka akan menampilkan gambar dengan teks dibawahnya.

Untuk menampilkan tombol edit-delete pada card, saya menambahkannya ketika ia masuk ke halaman details dari item. Saya merestriksi kedua fitur ini hanya untuk user yang membuat items dengan menambahkan logic pada details.html dan menambahkan access (boolean type, untuk mempermudah logic) sebagai konten pada html.
