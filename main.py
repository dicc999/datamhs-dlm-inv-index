# DATASET MAHASISWA

students = {
    1001: {"gender": "F", "age": 20, "study_time": 15, "attendance": 90, "final_score": 85, "status_lulus": True},
    1002: {"gender": "M", "age": 21, "study_time": 8, "attendance": 70, "final_score": 65, "status_lulus": False},
    1003: {"gender": "F", "age": 22, "study_time": 20, "attendance": 95, "final_score": 92, "status_lulus": True},
    1004: {"gender": "M", "age": 20, "study_time": 17, "attendance": 87, "final_score": 89, "status_lulus": True}
}

index_lulus = {"lulus": [], "tidak_lulus": []}

# FUNGSI

def build_index():
    index_lulus["lulus"].clear()
    index_lulus["tidak_lulus"].clear()

    for sid, data in students.items():
        if data["status_lulus"]:
            index_lulus["lulus"].append(sid)
        else:
            index_lulus["tidak_lulus"].append(sid)

def show_all_students():
    while True:
        print("\n=== DATA SELURUH MAHASISWA ===")
        for sid, data in students.items():
            print(f"ID:{sid} | Gender:{data['gender']} | Score:{data['final_score']} | Lulus:{data['status_lulus']}")

        cmd = input("\nKetik 0 untuk kembali ke menu utama: ")
        if cmd == "0":
            break

def search_student():
    while True:
        cmd = input("\nMasukkan student_id (atau 0 untuk kembali): ")
        if cmd == "0":
            break

        sid = int(cmd)
        data = students.get(sid)

        if data:
            print(f"ID:{sid} | Gender:{data['gender']} | Score:{data['final_score']} | Lulus:{data['status_lulus']}")
        else:
            print("Mahasiswa tidak ditemukan.")

def show_passed_students():
    while True:
        print("\n=== MAHASISWA LULUS ===")
        for sid in index_lulus["lulus"]:
            print(f"ID:{sid} | Score:{students[sid]['final_score']}")

        cmd = input("\nKetik 0 untuk kembali ke menu utama: ")
        if cmd == "0":
            break

def average_final_score():
    while True:
        avg = sum(s["final_score"] for s in students.values()) / len(students)
        print(f"\nRata-rata Final Score: {avg:.2f}")

        cmd = input("\nKetik 0 untuk kembali ke menu utama: ")
        if cmd == "0":
            break

# PROGRAM UTAMA

build_index()

while True:
    print("""
===== SISTEM DATA KELULUSAN =====
1. Lihat seluruh data mahasiswa
2. Cari mahasiswa berdasarkan ID
3. Lihat mahasiswa lulus
4. Hitung rata-rata nilai akhir
5. Keluar program
""")

    choice = input("Pilih menu (1-5): ")

    if choice == "1":
        show_all_students()
    elif choice == "2":
        search_student()
    elif choice == "3":
        show_passed_students()
    elif choice == "4":
        average_final_score()
    elif choice == "5":
        print("Program dihentikan...")
        break
    else:
        print("Input tidak ada.")
