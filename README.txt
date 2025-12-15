
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

#flowchart build_index()#

+-------+
| START |
+-------+
    |
    v
+----------------------+
| Kosongkan index      |
| lulus & tidak lulus  |
+----------------------+
    |
    v
+----------------------+
| Ambil data mahasiswa |
+----------------------+
    |
    v
+----------------------+
| status_lulus == True?|
+----------------------+
    | Yes                    | No
    v                        v
+-------------------+   +------------------------+
| Tambahkan ID ke   |   | Tambahkan ID ke        |
| index lulus       |   | index tidak lulus      |
+-------------------+   +------------------------+
            |
            v
     +----------------+
     | Data habis?    |
     +----------------+
            |
            v
        +------+
        | END  |
        +------+

#flowchart show_all_students()#

+-------+
| START |
+-------+
    |
    v
+----------------------------+
| Tampilkan seluruh data     |
| mahasiswa                  |
+----------------------------+
    |
    v
+----------------------------+
| Input pengguna (0)?        |
+----------------------------+
    | Yes
    v
+------+
| END  |
+------+

#flowchart search_student#

+-------+
| START |
+-------+
    |
    v
+----------------------------+
| Input student_id           |
+----------------------------+
    |
    v
+----------------------------+
| student_id == 0 ?          |
+----------------------------+
    | Yes                    | No
    v                        v
+------+          +----------------------------+
| END  |          | Cari student_id di data    |
+------+          +----------------------------+
                              |
                              v
                  +----------------------------+
                  | Data ditemukan?            |
                  +----------------------------+
                      | Yes            | No
                      v                v
        +---------------------+   +------------------------+
        | Tampilkan data      |   | Tampilkan pesan        |
        | mahasiswa           |   | tidak ditemukan        |
        +---------------------+   +------------------------+
                              |
                              v
                      (Kembali ke input)

#flowchart show_passed_students()#

+-------+
| START |
+-------+
    |
    v
+----------------------------+
| Ambil daftar ID lulus      |
| dari inverted index        |
+----------------------------+
    |
    v
+----------------------------+
| Tampilkan data mahasiswa   |
| yang lulus                 |
+----------------------------+
    |
    v
+----------------------------+
| Input pengguna (0)?        |
+----------------------------+
    | Yes
    v
+------+
| END  |
+------+

#flowchart average_final_score()#

+-------+
| START |
+-------+
    |
    v
+----------------------------+
| Jumlahkan seluruh          |
| final_score mahasiswa      |
+----------------------------+
    |
    v
+----------------------------+
| Bagi total nilai dengan   |
| jumlah mahasiswa           |
+----------------------------+
    |
    v
+----------------------------+
| Tampilkan nilai rata-rata  |
+----------------------------+
    |
    v
+----------------------------+
| Input pengguna (0)?        |
+----------------------------+
    | Yes
    v
+------+
| END  |
+------+
