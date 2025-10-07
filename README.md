# Checklist Tugas

## Perbedaan Synchronous-Asynchronous Request
Singkatnya, pada asinkronus, klien tidak perlu meminta request ke server secara terus-menerus tiap melakukan event karena sudah dihandle skrip yang diberikan server ke klien pada awal mengakses web, sedangkan pada sinkronus request berupa request dari klien yang tidak dihandle skrip server sehingga langsung menuju request dihandle langsung oleh server.

## AJAX di Django
Khususnya di Django, penggunaan AJAX ada pada inisiasi url dan fungsi di views dengan alur request-response yang hampir sama dengan tidak mengimplement AJAX. Pada penggunaan AJAX, return dari fungsi di views berupa respon data (JSON/XML) sehingga return-value akan diproses pada skrip yang sudah ada saat web dibuka.

## Keuntungan AJAX
UX akan lebih cepat (misalnya penggunaan Modal), bisa menampilkan respon dengan mudah (misalnya penggunaan Toast), dan tidak payah berpindah-pindah URL (dibanding render).

## Keamanan Login dan Register dengan AJAX
Untuk memastikan keamanan klien, sebagai developer kita sebaiknya menggunakan fitur AJAX pada CSRF Token (menjaga integritas akun) dan Rate Limiting (membatasi upaya penyerang untuk login-register secara sembarangan) serta menggunakan HTTPS (agar aman di jaringan publik). 

## Pengaruh AJAX Terhadap UX 
Dengan AJAX semua terasa lebih praktis, modern, dan terlihat ringan di sisi klien/user
