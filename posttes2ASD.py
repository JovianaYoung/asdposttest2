import os
os.system("cls")

# fungsi algoritma searching fbnccinacci
# j adalah array
# o adalah nilai yang dicari
# v adalah len

def fbncci(j, o, v):
    fib2 = 0
    fib1 = 1
    fbncci = fib2 + fib1
    while (fbncci < v):
    # menentukan nilai dari fibonacci
        fib2 = fib1
        fib1 = fbncci
        fbncci = fib2 + fib1
    imbang = -1
    while (fbncci > 1):
    # melakukan pencarian elemen data
        i = min(imbang + fib2, v-1)
    # yang diambil adalah nilai yang paling kecil
        if (j[i] < o):
    # jika array index i kurang dari nilai yang dicari
            fbncci = fib1
            fib1 = fib2
            fib2 = fbncci - fib1
            imbang = i
        elif (j[i] > o):
    # jika array index i lebih dari nilai yang dicari
            fbncci = fib2
            fib1 = fib1 - fib2
            fib2 = fbncci - fib1
        else:
    # jika array index i sama dengan nilai yang dicari, maka dia akan mengembalikan nilai i
            return i
    if (fib1 and j[v-1] == o):
    # jika elemen tidak ditemukan maka akan mengembalikan min -1
        return v-1
    return -1
 
# fungsi untuk mencari atau penentuan index dan kolom dari data nama  
def pencarian():
    print()
    print("Pencarian Nama dari", n )
    for u in range(len(cariArray)):
    # untuk mendapatkan index dia menghitung panjang array nya
        if type(cariArray[u]) == list:
            datakolom = fbncci(cariArray[u], n, len(cariArray[u]))
            print(n, "berada di index ke",u,"pada kolom",datakolom)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            return

        else:
        # jika elemen sama dengan elemen yang dicari maka ia akan mengembalikan nilai
            if cariArray[u] == n: 
                print(n, "berada di index ke",u)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
                           
cariArray = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]] #elemen atau data

n = "Arsel"
pencarian()
n = "Avivah"
pencarian()
n = "Daiva"
pencarian()
n = "Wahyu"
pencarian()
n = "Wibi"
pencarian()
