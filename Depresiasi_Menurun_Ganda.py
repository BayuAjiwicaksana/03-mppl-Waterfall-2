# Library untuk menampilkan hasil output dalam bentuk tabel yang rapi
from prettytable import PrettyTable

list_residu = []
list_biaya_penyusutan = []
list_total_penyusutan = []


# Proses Input biaya perolehan aset dan periode
print("\n\t\tMenghitung Depresiasi dengan Metode Menurun Ganda :\n")
while(True):
    try:
        # Input Biaya Perolehan Aset
        biaya_perolehan = int(input("Biaya Perolehan Aset (Rp)\t: "))

        # Input Periode
        periode = int(input("Periode (tahun)\t\t\t: "))
        break
    except:
        print("\nInputan Invalid !\n\n")



# Fungsi untuk menghitung % Depresiasi ganda
def persen_Depresiasi_ganda(a):
    perTahun = (1/a)*100/100
    ganda = 2 * perTahun
    return ganda



# Fungsi untuk Menghitung Penyusutan Saldo dengan metode Menurun Ganda
def Depresiasi_ganda(a, b):

    persen_depresiasi = persen_Depresiasi_ganda(b)

    for tahun in range(b):
        if tahun == 0:
            biaya_penyusutan = a * persen_depresiasi

            list_residu.append(a)
            list_biaya_penyusutan.append(biaya_penyusutan)
            list_total_penyusutan.append(biaya_penyusutan)

        else:
            residu = list_residu[tahun-1] - list_biaya_penyusutan[tahun-1]
            biaya_penyusutan = residu * persen_depresiasi
            total_penyusutan = list_total_penyusutan[tahun-1] + biaya_penyusutan

            list_residu.append(residu)
            list_biaya_penyusutan.append(biaya_penyusutan)
            list_total_penyusutan.append(total_penyusutan)
    
    residu_akhir = a - list_total_penyusutan[-1]
    
    Hasil(a, b, persen_depresiasi, residu_akhir)


# Fungsi untuk menampilkan Output
def Hasil(a, b, c, d):

    tabelHasil = PrettyTable(field_names=["Tahun", "Harga Barang (Rp)", "Nilai Residu (Rp)", "% Depresiasi", "Biaya Penyusutan (Rp)", "Total Penyusutan (Rp)"])

    for baris in range(1, (b+1)):
        tabelHasil.add_row([baris, a, list_residu[baris-1], c, list_biaya_penyusutan[baris-1], list_total_penyusutan[baris-1]])

    print(tabelHasil)

    print("\nResidu Akhir =", a, "-", list_total_penyusutan[-1], "= Rp", d, "\n")


# Memanggil fungsi untuk melakukan perhitungan
Depresiasi_ganda(biaya_perolehan, periode)