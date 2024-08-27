# WhatsApp Automation Script

## Deskripsi
Script ini digunakan untuk mengirim pesan WhatsApp secara otomatis menggunakan Selenium, PyAutoGUI, dan Pandas. Script membaca data pelanggan dari file Excel dan mengirim pesan yang dipersonalisasi ke setiap pelanggan melalui WhatsApp Web. Script ini juga dilengkapi dengan fitur pengiriman lampiran (gambar/video) dan penambahan jeda pengiriman untuk menghindari deteksi spam oleh WhatsApp.

## Library yang Digunakan
Script ini menggunakan beberapa library Python berikut:
1. **Selenium**: Digunakan untuk mengotomatisasi browser dan mengakses WhatsApp Web.
2. **PyAutoGUI**: Digunakan untuk mengotomatisasi klik dan input mouse serta keyboard, khususnya untuk menangani elemen UI yang sulit diakses dengan Selenium.
3. **Pyperclip**: Digunakan untuk memanipulasi clipboard, seperti menyalin path file gambar.
4. **Pandas**: Digunakan untuk membaca dan mengelola data dari file Excel.
5. **Webdriver Manager**: Digunakan untuk mengelola driver browser Chrome secara otomatis.

## Instalasi Dependensi
Sebelum menjalankan script, Anda perlu menginstal semua dependensi yang dibutuhkan. Jalankan perintah berikut di terminal atau command prompt:
> pip install selenium pyautogui pyperclip pandas webdriver-manager
> file_path = r"D:\WAB\sebaran.png"

## Pengaturan dan Penyesuaian Kode

1. **File Excel (`data_user.xlsx`)**:
   Pastikan file Excel dengan nama `data_user.xlsx` berada di direktori yang sama dengan script. File ini harus memiliki kolom berikut:
   - `id_pelanggan`: ID pelanggan.
   - `nama`: Nama pelanggan.
   - `nomor_wa`: Nomor WhatsApp pelanggan (format internasional, tanpa tanda +).
   - `status`: Status pelanggan.
   - `teks`: Teks pesan tambahan yang ingin disertakan dalam pesan WhatsApp.

2. **Konfigurasi Profil Chrome**:
   Agar script dapat mengakses WhatsApp Web tanpa login berulang kali, harus mengatur `user_data` dengan path ke profil Chrome yang telah login ke WhatsApp Web:
   ```python
   > user_data = "user-data-dir=C:\\Users\\username pc\\AppData\\Local\\Google\\Chrome\\User Data"
   > file_path = r"D:\WAB\sebaran.png"
