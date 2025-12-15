
Berikut adalah cara kerja setiap fungsi yang ada di dalam program ini:
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
| Nama Fungsi             | Input                     | Output                        | Proses Utama (Deskripsi Algoritma Singkat)                  |
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
| build_index()           | Tidak ada                 | Inverted index status lulus   | Melakukan iterasi terhadap seluruh data mahasiswa.          |
|                         |                           | (lulus dan tidak lulus)       | Setiap mahasiswa diperiksa nilai status_lulus-nya.          |
|                         |                           |                               | Student_id dimasukkan ke indeks lulus atau tidak lulus.     |
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
| show_all_students()     | Perintah pengguna (0)     | Tampilan seluruh data         | Menampilkan seluruh data mahasiswa yang tersimpan           |
|                         |                           | mahasiswa                     | dalam struktur data. Program menunggu input pengguna        |
|                         |                           |                               | untuk kembali ke menu utama.                                |
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
| search_student()        | student_id                | Data mahasiswa atau pesan     | Menerima input student_id dari pengguna.                    |
|                         |                           | tidak ditemukan               | Pencarian dilakukan langsung pada dictionary mahasiswa.     |
|                         |                           |                               | Jika data ditemukan, informasi mahasiswa ditampilkan.       |
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
| show_passed_students()  | Perintah pengguna (0)     | Daftar mahasiswa lulus        | Mengambil daftar student_id dari inverted index lulus.      |
|                         |                           |                               | Data mahasiswa diakses berdasarkan student_id dan           |
|                         |                           |                               | ditampilkan hingga pengguna kembali ke menu utama.          |
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
| average_final_score()   | Tidak ada                 | Nilai rata-rata final_score   | Menjumlahkan seluruh nilai final_score mahasiswa.           |
|                         |                           |                               | Hasil penjumlahan dibagi dengan jumlah mahasiswa            |
|                         |                           |                               | untuk memperoleh nilai rata-rata.                           |
+-------------------------+---------------------------+-------------------------------+-------------------------------------------------------------+
