# Tugas 2 Keamanan Informasi B: Program Enkripsi dan Dekripsi DES dengan Socket Programming

## Deskripsi Proyek
Proyek ini adalah bagian dari *Tugas 2 Keamanan Informasi B*, yang bertujuan untuk mengimplementasikan algoritma DES (Data Encryption Standard) untuk pengiriman pesan terenkripsi antar dua pengguna menggunakan socket programming. Sistem ini mendukung pesan yang lebih panjang dari 64-bit dan memastikan transfer data aman melalui socket.

## Fitur Utama
- **Enkripsi & Dekripsi DES**: Menggunakan algoritma DES untuk mengenkripsi dan mendekripsi pesan.
- **Socket Programming**: Data pesan dikirim secara terenkripsi antara client dan server melalui socket.
- **Blok Data >64-bit**: Mendukung input pesan lebih panjang dari 8 karakter dengan pemecahan ke dalam blok-blok 64-bit.
- **Kunci Hardcoded**: Kunci enkripsi di-hardcode dan dianggap sudah diketahui oleh kedua client.

## Cara Menggunakan

### Prasyarat
- Python 3.x
- Library `pycryptodome`

### Instalasi
1. Install library yang diperlukan:
   ```bash
   pip install pycryptodome
   ```

2. Clone repository:
   ```bash
   git clone https://github.com/username/repo-enkripsi-des.git
   cd repo-enkripsi-des
   ```

3. Jalankan **server.py**:
   ```bash
   python server.py
   ```

4. Jalankan **client.py** untuk mengirim pesan terenkripsi:
   ```bash
   python client.py
   ```

## Struktur Proyek
- **client.py**: Mengirim pesan terenkripsi ke server melalui socket.
- **server.py**: Menerima pesan terenkripsi dan mendekripsinya.
- **encryption.py**: Modul berisi fungsi enkripsi dan dekripsi DES.

## 📋 Pembagian Kerja

| **Anggota**           | **Tugas Utama**                                                                                      |
|-----------------------|-----------------------------------------------------------------------------------------------------|
| **Yanuar Eka Pramudya**     | 🔑 **Pengembangan Logika Enkripsi & Dekripsi DES**<br>• Mengembangkan algoritma DES untuk enkripsi dan dekripsi.<br>• Menambahkan padding untuk blok yang tidak memenuhi 64-bit.<br>• Membuat unit test untuk memverifikasi hasil enkripsi dan dekripsi. |
| **Abiyu Ramadhan Kiesly**     | 💻 **Pengembangan Socket Programming**<br>• Menerapkan komunikasi antara client dan server menggunakan socket programming.<br>• Mengintegrasikan modul enkripsi ke dalam client dan server.<br>• Menulis dokumentasi lengkap proyek serta README.|

### 📌 Detail Tugas

#### 🎯 **Yanuar Eka Pramudya (5025221049)**: 
- **Pengembangan Enkripsi & Dekripsi**: Mengimplementasikan logika DES dengan memperhatikan kebutuhan pemecahan pesan lebih dari 64-bit.
- **Unit Testing**: Membuat dan menjalankan pengujian untuk memastikan enkripsi dan dekripsi berfungsi dengan benar.

#### 🎯 **Abiyu Ramadhan Kiesly (5025221123 )**:
- **Socket Programming**: Mengembangkan koneksi antara client dan server menggunakan socket, dan memastikan data yang dikirim aman.
- **Dokumentasi & README**: Menulis dokumentasi proyek, termasuk panduan penggunaan, dan penjelasan pembagian kerja.

## 📜 License
Proyek ini dilisensikan di bawah [MIT License](LICENSE).