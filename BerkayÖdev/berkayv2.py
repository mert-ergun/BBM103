ogrenci_ortalamlari = []


def hesapla(vize, final, odevler):
    if len(odevler) == 0:
        ortalama = (vize * 0.6) + (final * 0.4)
    else:
        ortalama = (vize * 0.3) + (final * 0.4) + ((sum(odevler) / len(odevler)) * 0.3)
    
    ogrenci_ortalamlari.append(ortalama)
    
    return round(ortalama, 2)


def odev_not_hesapla(ogrenci_no, odev_sayisi):
    global odev_notlari
    odev_notlari = []
    
    for i in range(odev_sayisi):
        odev_notu = int(input(f"{ogrenci_no} numaralı öğrenci için {i+1}. ödev notunu giriniz: "))
        while odev_notu > 100 or odev_notu < 0:
            print("Ödev notu 0 ile 100 arasında olmalıdır.")
            odev_notu = int(input(f"{ogrenci_no} numaralı öğrenci için {i+1}. ödev notunu giriniz: "))
        odev_notlari.append(odev_notu)
    
    odev_ortalama = sum(odev_notlari) / len(odev_notlari)
    odev_ortalama = round(odev_ortalama, 2)
    
    print(f"{ogrenci_no} numaralı öğrencinin ödev not ortalaması: {odev_ortalama:,.2f}")
    
    return odev_notlari
        
        
def main():
    global ogrenci_no, vize_not, final_not
    ogrenci_no = input("Öğrenci numarasını giriniz: ")
    while len(ogrenci_no) !=9 or not ogrenci_no.isdigit():
        print("Öğrenci numarası 9 haneli olmalıdır.")
        ogrenci_no = input("Öğrenci numarasını giriniz: ")
    
    vize_not = int(input(f"{ogrenci_no} numaralı öğrenci için vize notunu giriniz: "))
    while vize_not > 100 or vize_not < 0:
        print("Vize notu 0 ile 100 arasında olmalıdır.")
        vize_not = int(input(f"{ogrenci_no} numaralı öğrenci için vize notunu giriniz: "))
    
    final_not = int(input(f"{ogrenci_no} numaralı öğrenci için final notunu giriniz: "))
    while final_not > 100 or final_not < 0:
        print("Final notu 0 ile 100 arasında olmalıdır.")
        final_not = int(input(f"{ogrenci_no} numaralı öğrenci için final notunu giriniz: "))


if __name__ == "__main__":
    print("NOT ORTALAMASI HESAPLAMA")
    print("*" * len("NOT ORTALAMASI HESAPLAMA"))
    
    odev_sayisi = int(input("Ödev sayısını giriniz: "))
    resume_or_not = "1"
    ogrenci_counter = 0
    
    while resume_or_not == "1":
        if odev_sayisi == 0:
            main()
            ortalama = hesapla(vize_not, final_not, [])
            print(f"{ogrenci_no} numaralı öğrencinin not ortalaması: {ortalama:,.2f}")
        else:
            main()
            odev_not_hesapla(ogrenci_no, odev_sayisi)
            ortalama = hesapla(vize_not, final_not, odev_notlari)
            print(f"{ogrenci_no} numaralı öğrencinin not ortalaması: {ortalama:,.2f}")
        
        ogrenci_counter += 1
        
        resume_or_not = input("Yeni bir öğrenci notu hesaplamak için '1', çıkmak için '0' tuşlayınız: ")
        
        while resume_or_not != "1" and resume_or_not != "0":
            print("Yanlış tuşlama yaptınız.")
            resume_or_not = input("Yeni bir öğrenci notu hesaplamak için '1', çıkmak için '0' tuşlayınız: ")
    
    if resume_or_not == "0":
        print(f"Dersi alan {ogrenci_counter} öğrenci için en düşük not: {(min(ogrenci_ortalamlari)):,.2f}")
        print(f"Dersi alan {ogrenci_counter} öğrenci için en yüksek not: {(max(ogrenci_ortalamlari)):,.2f}")
        print(f"Dersi alan {ogrenci_counter} öğrenci için not ortalaması: {(sum(ogrenci_ortalamlari) / len(ogrenci_ortalamlari)):,.2f}")
        exit()
    