<h1>API Account Creation & Login</h1></hr>

<h2><b>Anonymous</b></h2>
<p style="font-size: 20px">Contoh user stories tentang membuat dan login akun dengan API.</p>

<h2><b>ChatGPT</b></h2>
<p>
<ol style="font-size: 20px">
<li><b>User Story 1: Membuat Akun Baru melalui API</b></br>
    Sebagai pengguna yang ingin menggunakan layanan, saya ingin dapat membuat akun baru menggunakan API agar dapat mengakses fitur-fitur eksklusif.</br>
    <b>Kriteria Penerimaan:</b></br>
    <ul>
        <li>Pengguna dapat mengirimkan permintaan API dengan informasi pendaftaran yang valid, seperti nama, alamat email, dan kata sandi.
        <li>Sistem menyimpan informasi akun baru ke dalam basis data.
        <li>Jika informasi pendaftaran valid, sistem mengembalikan tanggapan sukses bersama dengan token otentikasi untuk sesi pengguna yang baru.
    </li></ul><br>
<li><b>User Story 2: Login ke Akun menggunakan API</b></br>
    Sebagai pengguna yang sudah memiliki akun, saya ingin dapat masuk ke dalam akun saya melalui API untuk mengakses layanan secara lebih mudah.</br>
    <b>Kriteria Penerimaan:</b></br>
    <ul>
        <li>Pengguna dapat mengirimkan permintaan API dengan informasi masuk yang valid, seperti alamat email dan kata sandi.
        <li>Sistem memverifikasi informasi masuk pengguna dengan data yang tersimpan di basis data.
        <li>Jika informasi masuk valid, sistem mengembalikan tanggapan sukses bersama dengan token otentikasi untuk sesi pengguna yang aktif.
        <li>Token otentikasi harus digunakan untuk mengotentikasi permintaan API berikutnya.
    </li></ul><br>
<li><b>User Story 3: Penanganan Kesalahan pada Login melalui API</b></br>
    Sebagai pengguna yang mungkin melakukan kesalahan saat mencoba masuk ke dalam akun, saya ingin menerima pesan kesalahan yang jelas melalui API agar dapat memperbaiki masalah dengan cepat.</br>
    <b>Kriteria Penerimaan:</b></br>
    <ul>
        <li>Jika informasi masuk tidak valid, sistem mengembalikan tanggapan kesalahan yang menyertakan pesan yang jelas dan bermakna.
        <li>Pesan kesalahan mencakup informasi yang membantu pengguna memahami masalah, seperti apakah kesalahan terjadi karena kata sandi yang salah atau akun tidak ditemukan.
    </li></ul><br>
<li><b>User Story 4: Mengatur Ulang Kata Sandi melalui API</b></br>
    Sebagai pengguna yang lupa kata sandi, saya ingin dapat mengatur ulang kata sandi saya melalui API agar dapat terus menggunakan layanan.</br>
    <b>Kriteria Penerimaan:</b></br>
    <ul>
        <li>Pengguna dapat mengirimkan permintaan API untuk mengatur ulang kata sandi dengan menyediakan alamat email terkait akun.
        <li>Sistem mengirimkan email verifikasi atau tautan khusus untuk proses pengaturan ulang kata sandi.
        <li>Pengguna dapat mengakses tautan tersebut untuk mengatur ulang kata sandi mereka melalui API.
        <li>Sistem mengonfirmasi perubahan kata sandi dan memberikan tanggapan sukses.
    </li></ul><br>
</li></ol></p>