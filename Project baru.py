import random
def permainan_judi():
    x = input("Sebagai pemain pertama anda harus memasukkan nama = ")
    y = input("Sebagai pemain kedua anda juga harus memasukkan nama = ")
    nyawa_pemain = int(input(f"{x} dan {y} masukkan kalian ingin memiliki berapa nyawa dalam permainan ini = "))
    q = nyawa_pemain
    r = nyawa_pemain
    taruhan = int(input(f"{x} dan {y} kalian ingin bertaruh berapa nih = "))
    while q != 0 and r != 0:
        try:
            roulette_1 = input(f"{x}, ketik spin untuk memutar roulette dan mendapatkan angka yang anda inginkan = ").lower()
            roulette_2 = input(f"{y}, ketik spin, untuk memutar roulette dan mendapatkan angka yang anda inginkan = ").lower()
            if roulette_1 == "spin" and roulette_2 == "spin":
                angka_1 = random.randint(0,36)
                angka_2 = random.randint(0,36)
                if angka_1 > angka_2:
                    r -= 1
                    print(f"{x} mendapat angka {angka_1} dan {y} mendapat angka {angka_2}")
                    print(f"Skor sementara: {x} memegang {q} nyawa dan {y} berkurang nyawanya sehingga {y} memegang {r} nyawa")
                elif angka_2 > angka_1:
                    q -= 1
                    print(f"{x} mendapat angka {angka_1} dan {y} mendapat angka {angka_2}")
                    print(f"Skor sementara: {y} memegang {r} nyawa dan {x} berkurang nyawanya sehingga {x} mempunyai {q} nyawa")
                elif angka_1 == angka_2:
                    r += 0
                    q += 0
                    print(f"{x} mendapat angka {angka_1} dan {y} mendapat angka {angka_2}")
                    print(f"Skor sementara {x} memegang {q} nyawa dan {y} memegang {r} nyawa")
                
        except:
            roulette_1 = input(f"{x}, ketik spin untuk memutar roulette dan mendapatkan angka yang anda inginkan = ").lower()
            roulette_2 = input(f"{y}, ketik spin, untuk memutar roulette dan mendapatkan angka yang anda inginkan = ").lower()
    if q == 0 and r != 0:
        print(f"Pemenang dari permainan ini adalah {y}, selamat untuk {y} telah memenangkan permainan dan mendapatkan total uang {taruhan+taruhan} rupiah")
    else:
        print(f"Pemenang dari permainan ini adalah {x}, selamat untuk {x}, telah memenangkan permainan dan mendapatkan total uang {taruhan+taruhan} rupiah")
permainan_judi()




