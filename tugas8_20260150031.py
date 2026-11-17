import modul_sensor

log_kebun = []

def input_sensor():

    while True:
        try:
            suhu = float(input("Masukkan suhu udara (0-100 C): "))
            lembab = float(input("Masukkan kelembapan tanah (0-100 %): "))

            if 0 <= suhu <= 100 and 0 <= lembab <= 100:
                return (suhu, lembab)

            else:
                print("Error: Suhu dan kelembapan harus antara 0-100!")

        except ValueError:
            print("Error: Input harus berupa angka! Silakan coba lagi.")




def menu_utama():

    while True:

        print("\n================================")
        print(" SISTEM MONITORING IoT KEBUN")
        print("================================")
        print("[1] Rekam Data")
        print("[2] Analisis Tren (3 Terakhir)")
        print("[3] Keluar")
        print("================================")

        pilihan = input("Pilih menu (1-3): ")

        
        if pilihan == "1":

            data = input_sensor()
            log_kebun.append(data)

            print("Data berhasil direkam!")
            print("Data:", data)


       
        elif pilihan == "2":

            if len(log_kebun) == 0:
                print("Belum ada data sensor!")

            else:
               
                data_terakhir = log_kebun[-3:]

                print("\n--- DATA SENSOR TERAKHIR ---")

                for i, data in enumerate(data_terakhir, start=1):
                    print(f"Data ke-{i}: Suhu = {data[0]} C, "
                          f"Kelembapan = {data[1]} %")

               
                rata_suhu, rata_lembab = modul_sensor.hitung_tren(
                    data_terakhir
                )

                print("\n--- HASIL ANALISIS ---")
                print("Rata-rata suhu:", rata_suhu, "C")
                print("Rata-rata kelembapan:", rata_lembab, "%")

                status = modul_sensor.evaluasi_irigasi(
                    rata_suhu,
                    rata_lembab,
                    modul_sensor.AMBANG_KRITIS
                )

                print("Status Irigasi:", status)

        elif pilihan == "3":

            print("Program monitoring IoT selesai.")
            break


        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")

if __name__ == "__main__":
    menu_utama()