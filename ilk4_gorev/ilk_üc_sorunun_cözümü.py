# Soru 1: N faktoriyelinin (N!) sonundan kac sifir oldugunu hesaplama
# Bir sayinin faktoriyelinin sonunda kac tane sifir oldugunu bulmak icin 5'in kuvvetlerini sayiyoruz.
# Cunku 10 sayisini olusturmak icin 2 ve 5 carpani gerekiyor. (Faktoriyel sayilarda 2 zaten bolca var.)
def count_trailing_zeros(n):
    # Sifir sayisini tutacagimiz degisken
    count = 0
    # Ilk once 5'in birinci kuvvetinden baslayacagiz
    power_of_5 = 5
    # Sayi 5'in kuvvetlerine bolundugu surece devam edecegiz
    while n >= power_of_5:
        count += n // power_of_5  # Kac tane 5 carpani oldugunu hesapliyoruz
        power_of_5 *= 5          # Bir sonraki 5'in kuvvetine geciyoruz
    return count

# Soru 2: Toplama operatoru olmadan iki sayi toplama
# Iki sayiyi toplamak icin bit islemlerini kullanacagiz.
# XOR islemi normal toplama gibi davranir, AND islemi ise tasima (carry) hesaplar.
def add_without_operator(a, b):
    while b != 0:  # Tasima sifir olmadigi surece devam et
        carry = a & b  # AND islemiyle tasima hesaplanir
        a = a ^ b      # XOR islemiyle toplam yapilir (tasima haric)
        b = carry << 1 # Tasima sola kaydirilarak eklenir
    return a  # Sonuc, tum tasima bitince elde edilir

# Soru 3: 0'dan N'e kadar icinde "3" gecen sayilari bulma ve toplamda kac kez gectigini hesaplama
# Bu soruda, "3" rakamini iceren tum sayilari ve toplam kac defa "3" rakami gectigini bulacagiz.
def find_numbers_with_3(n):
    # Icinde "3" gecen sayilari tutacagimiz liste
    numbers_with_3 = []
    # Kac kez "3" gectigini tutacak degisken
    total_count_of_3s = 0

    # 0'dan N'e kadar tum sayilari dolasiyoruz
    for num in range(n + 1):
        # Sayinin icinde kac tane "3" oldugunu sayiyoruz
        count_of_3s = str(num).count('3')
        if count_of_3s > 0:  # Eger "3" iceriyorsa
            numbers_with_3.append(num)  # Listeye ekle
            total_count_of_3s += count_of_3s  # Toplam sayiya ekle
    
    # Hem sayilari hem de toplam "3" sayisini donduruyoruz
    return numbers_with_3, total_count_of_3s

# Kullanicidan veri almak ve tum sorularin ciktisini gostermek icin bir menu olusturacagiz.
def main():
    print("1. Soru: N faktoriyelinin sonundan kac sifir oldugunu hesapla")
    print("2. Soru: Toplama operatoru olmadan iki sayi topla")
    print("3. Soru: 0'dan N'e kadar icinde '3' gecen sayilari bul ve toplam '3' sayisini hesapla")
    
    # Kullanicidan hangi soruyu cozmek istedigini aliyoruz
    choice = int(input("Hangi soruyu cozmek istiyorsunuz? (1/2/3): "))
    
    if choice == 1:
        # Soru 1 icin, kullanicidan N degeri aliniyor
        n = int(input("N degerini girin: "))
        # Sonuc hesaplaniyor
        result = count_trailing_zeros(n)
        print(f"{n}! sayisinin sonundan {result} basamagi sifirdir.")
    
    elif choice == 2:
        # Soru 2 icin, iki sayi aliniyor
        a = int(input("Birinci sayiyi girin: "))
        b = int(input("Ikinci sayiyi girin: "))
        # Sonuc hesaplaniyor
        result = add_without_operator(a, b)
        print(f"{a} ve {b} toplami (operatorsuz): {result}")

    elif choice == 3:
        # Soru 3 icin, kullanicidan N degeri aliniyor
        n = int(input("N degerini girin: "))
        # Sonuc hesaplaniyor
        numbers, total_3s = find_numbers_with_3(n)
        print(f"{numbers} listesinde toplamda {total_3s} adet '3' bulunmustur.")
    
    else:
        # Gecersiz secim durumunda uyari
        print("Gecersiz secim. Lutfen 1, 2 veya 3 secin.")

# Programin baslangic noktasi
if __name__ == "__main__":
    main()
