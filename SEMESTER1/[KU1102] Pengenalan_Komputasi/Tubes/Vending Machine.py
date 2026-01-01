# Program VendingMachine
# Membuat sebuah simulasi vending machine dengan menggunakan bahasa pemrograman Python.

# KAMUS
# ID : list
# Name : list
# Price : list
# Stock : list
# Order : list
# Display : str
# Confirm : str
# Reset : str
# Bal : float
# Cash : float
# Pay : float
# Item : int
# UserCode : int
# Start : bool
# Run : bool

# ALGORITMA
import os
import time

ID = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010] # Kode Produk
Name = ["Potato Chip", "Soda", "Sandwich", "KitKat", "Pretzel", "M & M's", "Snickers", "Doritos", "Oreo", "Donut"] # Nama Produk
Price = [9000, 6000, 12000, 8500, 7000, 4500, 6500, 9000, 5500, 10000] # Harga Produk
Stock = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20] # Jumlah Produk yang tersedia
Order = [0 for i in range(len(ID))] # Variabel untuk menyimpan jumlah belanjaan yang telah dipesan.
Item = -1 # Item adalah variabel pembantu dalam proses pemilihan belanjaan.
Cash = 1 # Cash adalah variabel pembantu dalam proses penerimaan uang.
Pay = 0 # Pay adalah harga barang-barang yang telah terpilih.
Bal = 0 # Bal menunjukkan uang di dalam program.
Start = False # Variabel Start menandai apakah keseluruhan proses vending machine ini sudah berjalan atau belum.
Run = True # Variabel Run menandai apakah sedang ingin menerima kode produk

# Prosedur Interface
def Interface():
    # Menampilkan display Interface untuk vending machine.
    # Tampilan vending machine merupakan sebuah ilusi dimana setiap proses akan mengubah variabel Display sebelum
    # mengeksekusi prosedur Interface ini sehingga tampilannya akan berubah.

    # Algoritma
    os.system('cls')
    print("         +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-       ", end = '')
    print("Welcome to SIX's Vending Machine")
    print("         *@                        :@:             @=       ", end = '')
    print(f"Balance: {Bal}")
    print("         *@  %@@@@@@@@@@@@@@@@@@@* :@: +@@@@@@@@#  @=       ", end = '')
    print(f"{'Product':<15}{'Code':^15}{'Price':>15}")
    print("         *@  %@                 @* :@: *@      @#  @=       ", end = '')
    print(f"{Name[0]:<15}{ID[0]:^15}{Price[0]:>15}")
    print("         *@  %@  %@@@@: :@@@@%  @* :@: *@@@@@@@@#  @=       ", end = '')
    print(f"{Name[1]:<15}{ID[1]:^15}{Price[1]:>15}")
    print("         *@  %@  @#  @= =@  %@  @* :@:             @=       ", end = '')
    print(f"{Name[2]:<15}{ID[2]:^15}{Price[2]:>15}")
    print("         *@  %@@@@@@@@@@@@@@@@@@@* :@: *@  #%  @#  @=       ", end = '')
    print(f"{Name[3]:<15}{ID[3]:^15}{Price[3]:>15}")
    print("         *@  %@                 @* :@:             @=       ", end = '')
    print(f"{Name[4]:<15}{ID[4]:^15}{Price[4]:>15}")
    print("         *@  %@  *%%%%  .#%%%+  @* :@: =#  **  #+  @=       ", end = '')
    print(f"{Name[5]:<15}{ID[5]:^15}{Price[5]:>15}")
    print("         *@  %@  @% :@= =@. @@  @* :@:             @=       ", end = '')
    print(f"{Name[6]:<15}{ID[6]:^15}{Price[6]:>15}")
    print("         *@  %@%%@@%@@@%@@@%@@%%@* :@: =%  **  #+  @=       ", end = '')
    print(f"{Name[7]:<15}{ID[7]:^15}{Price[7]:>15}")
    print("         *@  %@:...............:@* :@:  .          @=       ", end = '')
    print(f"{Name[8]:<15}{ID[8]:^15}{Price[8]:>15}")
    print("         *@  %@  =-  +. .+  =+  @* :@: :+  -=  =-  @=       ", end = '')
    print(f"{Name[9]:<15}{ID[9]:^15}{Price[9]:>15}")
    print("         *@  %@  @#  @= =@  %@  @* :@:  .  ..  .   @=       ", end = '')
    print("")
    print("         *@  %@**@@+#@%+%@*+@@+*@* :@:             @=       ", end = '')
    print(Display)
    print("         *@  %@=---------------=@* :@:   :----:    @=       ")
    print("         *@  %@  .   .   .   .  @* :@:   -****=    @=       ")
    print("         *@  %@:-@%.=@*.#@=.@@.:@* :@:    ....     @=       ")
    print("         *@  :+++++++++++++++++++. :@:   -++++=    @=       ")
    print("         *@:                       =@+            -@=       ")
    print("         *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=       ")
    print("         *@                        :@:             @=       ")
    print("         *@    @@@%%%%%%%%%%%@@%   :@:             @=       ")
    print("         *@    @@@%         @@@%   :@:     %@@@@#  @=       ")
    print("         *@    @% @@@@@@@@@@@ @%   :@:     %@  @#  @=       ")
    print("         *@    @%             @%   :@:     #@@@@*  @=       ")
    print("         *@    #@@@@@@@@@@@@@@@*   :@:             @=       ")
    print("         *@                        -@-            .@=       ")
    print("         *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=       ")
    print("           #@    @#                        %@    @*         ")
    print("           #@@@@@@#                        %@@@@@@+         ")
    return

# Fungsi Code
def Code():
    # Menerima input kode produk dan memastikan bahwa kode produk tersebut valid.

    # Kamus
    # ProductCode : int

    # Algoritma
    while True:
        try:
            ProductCode = int(input())
        except ValueError:
            Interface()
            print("Please input the correct product code.")
            continue
        if ProductCode == 0:
            break
        if ProductCode not in ID:
            Interface()
            print("Please input the correct product code.")
            continue
        else:
            break
    return ProductCode

# Fungsi Money
def Money():
    # Menerima input berupa uang dan memastikan bahwa uang yang diinput valid.

    # Kamus
    # Balance : float

    # Algoritma
    while True:
        try:
            Balance = float(input())
        except ValueError:
            Interface()
            print("Please input your money correctly.")
            continue
        if Balance < 0:
            Interface()
            print("Please input your money correctly.")
            continue
        else:
            break
    return Balance

def isFloat(x):
    # Mengecek apakah sebuah string juga merupakan sebuah float.

    # Kamus
    # x : string

    # Algoritma
    try:
        float(x)
        return True
    except ValueError:
        return False

def Receipt():
    # Menunjukkan produk-produk yang ingin dibeli beserta jumlah dan harganya.
    
    print()
    print(f"{'Name':<15}{'Amount':^15}{'Price':>15}")
    for i in range(len(ID)):
        if Order[i] != 0:
            print(f"{Name[i]:<15}{Order[i]:^15}{ Order[i] * Price[i]:>15}")
    print(f"{'Total':<30} {Pay:>14}")
    print()
    return

# ALGORITMA
time.sleep(0.5)
while Start == False: # Saat nilai variabel Start itu false, maka program akan dimulai.
    if Cash > 0: # Tampilan ini akan muncul ketika program baru pertama kali hidup atau saat prosedur lain mengembalikannya ke sini (dengan mengubah nilai Cash ke 1).
        Display = "Please input your money..." # Display meminta pengguna menginput uang.
        Interface()
    Start = True # Karena programnya telah dimulai, maka kita mengubah variabel Start menjadi true.
    while Cash > 0: # Karena variabel Cash tadi di awal adalah 1, maka loop ini akan berjalan. 
        Cash = Money() # Nilai Cash nanti akan kita assign dengan fungsi Money. Nilai Cash tidak akan pernah di bawah nol karena fungsi Money sudah memastikan bahwa variabelnya 0 dan ke atas.
        Bal = Bal + Cash # Loop ini akan berjalan hingga kita memasukkan angka 0.
        Interface()
    while Run: # Secara default, variabel Run bernilai true dan selama true akan meminta input kode Produk.
        Display = "Enter the product code..." # Display meminta pengguna menginput kode produk.
        Interface()
        Receipt()
        UserCode = Code() # Input kode produk. Sama seperti fungsi Money, fungsi Code juga akan memastikan bahwa nilai UserCode tersebut tepat.
        for i in range(len(ID)): # Input UserCode akan dicocokkan dengan array ID. Jika ketemu, maka variabel Item nilainya menjadi sama dengan indeks ID tadi.
            if UserCode == ID[i]:
                Item = i
        if UserCode == 0: # Jika kita menginput 0, maka dia akan kembali mengakhiri prosedur pengambilan kode produk dengan mengubah variabel Run menjadi false.
            Run = False
        else: # Jika inputnya bukan 0, maka:
            if Order[Item] + 1 <= Stock[Item]: # Dicek apakah Stock cukup.
                Pay = Pay + Price[Item]
                Order[Item] = Order[Item] + 1
                Interface()
                Receipt()
            else: # Jika tidak, maka akan keluar tampilan bahwa item tersebut habis.
                Interface()
                Receipt()
                print("Sorry that item is out of stock.")
                time.sleep(0.5)
        Item = -1 # Proses tersebut akan diulang hingga dimasukkan nol dan Item pun nilainya diassign dengan -1 seperti semula.
    if UserCode == 0 and Order == [0 for i in range(len(ID))]: # Namun jika pengguna tidak memesan apapun dan menekan 0, maka akan kembali ke tampilan awal.
        Start = False
        Run = True
        Cash = 1
    else: # Jika pengguna telah selesai memesan
        Display = "Confirm Purchase?" # Muncul tampilan untuk mengonfirmasi pembelian.
        Interface()
        Receipt()
        Confirm = input() # Input apapun untuk mengonfirmasi pembelian.
        if isFloat(Confirm) and float(Confirm) == 0: # Jika inputnya 0, maka kembali ke program kembali ke awal.
            Start = False
            Run = True
            Pay = 0
            Order = [0 for i in range(len(ID))]
            Cash = 1
        else: # Jika inputnya bukan 0, maka periksa jika uang dalam program cukup untuk membayar.
            if Bal < Pay: # Jika tidak cukup, maka kembali ke proses penginputan uang.
                Display = "Not enough Balance"
                Interface()
                time.sleep(0.5)
                Start = False
                Cash = 1
            else: # Jika cukup, maka uang dalam program dikurangi dengan harga total barang belanjaan.
                Bal = Bal - Pay
                for i in range(len(ID)): # Tiap array Stock akan dikurangi dengan array Order di indeks yang sama.
                    Stock[i] = Stock[i] - Order[i]
                Display = "Payment Successful" # Tampilan yang menunjukkan bahwa pembayaran berhasil.
                Interface()
                time.sleep(0.5) # Loading screen.
                Display = "Processing Order..."
                Interface()
                time.sleep(0.5)
                Display = "Processing Order."
                Interface()
                time.sleep(0.5)
                Display = "Processing Order..."
                Interface()
                time.sleep(0.5)
                Display = "Processing Order."
                Interface()
                time.sleep(0.5)
                Display = "You have received..."
                Interface()
                print()
                print(f"{'Name':<15}{'Amount':>15}")
                for i in range(len(ID)): # Print tiap produk yang dibeli beserta jumlahnya.
                    if Order[i] != 0:
                        print(f"{Name[i]:<15}{Order[i]:>15}")
                print()
                time.sleep(5)
                Display = "Do you wish to continue?" # Tampilan yang menanyakan apakah masih mau lanjut menggunakan program.
                Interface()
                Reset = input() # Input untuk lanjut menggunakan program.
                if isFloat(Reset) and float(Reset) == 0: # Jika inputnya 0, maka program akan selesai.
                    Display = "Hope you enjoy your snacks :)"
                    Interface()
                    time.sleep(3)
                    os.system('cls')
                else: # Jika inputnya bukan 0, maka program akan kembali ke awal dengan membuat variabel Start, Run, Pay, Order, dan Cash kembali ke nilai semula.
                    Start = False
                    Run = True
                    Pay = 0
                    Order = [0 for i in range(len(ID))]
                    Cash = 1
