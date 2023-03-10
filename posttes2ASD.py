import os
os.system("cls")

#fungsi algoritma searching fbnccinacci
def fbncci(j, o, v):
    pelaubueh = 0
    pelauregaq = 1
    fbncci = pelaubueh + pelauregaq
    while (fbncci < v):
        pelaubueh = pelauregaq
        pelauregaq = fbncci
        fbncci = pelaubueh + pelauregaq
    imbang = -1
    while (fbncci > 1):
        i = min(imbang + pelaubueh, v-1)
        if (j[i] < o):
            fbncci = pelauregaq
            pelauregaq = pelaubueh
            pelaubueh = fbncci - pelauregaq
            imbang = i
        elif (j[i] > o):
            fbncci = pelaubueh
            pelauregaq = pelauregaq - pelaubueh
            pelaubueh = fbncci - pelauregaq
        else:
            return i
    if (pelauregaq and j[v-1] == o):
        return v-1
    return -1

#fungsi untuk mencari atau penentuan index dan kolom dari data nama  
def pelau():
    print()
    print("Pencarian Nama dari", n )
    for u in range(len(nyamaqdata)):
        if type(nyamaqdata[u]) == list:
            datakolom = fbncci(nyamaqdata[u], n, len(nyamaqdata[u]))
            print(n, "berada di index ke",u,"pada kolom",datakolom)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            return

        else:
            if nyamaqdata[u] == n:
                print(n, "berada di index ke",u)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                return
            
#list semua data nama               
nyamaqdata = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

n = "Arsel"
pelau()
n = "Avivah"
pelau()
n = "Daiva"
pelau()
n = "Wahyu"
pelau()
n = "Wibi"
pelau()