# Histogramdaki su miktarini hesaplayan fonksiyon
# Giris: bir liste (histogram yukseklikleri)
# Cikis: toplam su miktari

def calculate_trapped_water(heights):
    # Sol taraftaki en yuksek degeri tutmak icin bir liste olustur
    left_max = [0] * len(heights)
    # Sag taraftaki en yuksek degeri tutmak icin bir liste olustur
    right_max = [0] * len(heights)
    # Toplam su miktarini hesaplamak icin bir degisken
    total_water = 0

    # Sol taraftaki en yuksek degerleri hesapla
    max_height = 0
    for i in range(len(heights)):
        max_height = max(max_height, heights[i])  # Su ana kadarki maksimumu bul
        left_max[i] = max_height  # Bu maksimumu sol listeye ekle

    # Sag taraftaki en yuksek degerleri hesapla
    max_height = 0
    for i in range(len(heights) - 1, -1, -1):  # Listeyi sondan basa dogru tara
        max_height = max(max_height, heights[i])  # Su ana kadarki maksimumu bul
        right_max[i] = max_height  # Bu maksimumu sag listeye ekle

    # Her bir sutunda tutulabilecek su miktarini hesapla
    for i in range(len(heights)):
        # Su seviyesi: sol ve sag maksimumlarin minimumu
        water_level = min(left_max[i], right_max[i])
        # Su seviyesi yuksekligin ustundeyse su miktarini ekle
        if water_level > heights[i]:
            total_water += water_level - heights[i]

    return total_water


# Kullanicidan histogram degerlerini al ve sonucu hesapla
def main():
    print("Histogramdaki su miktarini hesaplayan programa hos geldiniz!")
    print("Ornek girdi: [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0]")

    # Kullanici girdisini al
    user_input = input("Histogram yuksekliklerini aralarinda virgul olacak sekilde girin: ")
    # Kullanici girdisini listeye cevir (koseli parantezleri temizle ve bosluklari kaldir)
    user_input = user_input.strip("[]").replace(" ", "")
    heights = list(map(int, user_input.split(",")))

    # Su miktarini hesapla
    result = calculate_trapped_water(heights)
    print(f"Bu histogram toplamda {result} metrekup su alir.")


# Programin baslangic noktasi
if __name__ == "__main__":
    main()
