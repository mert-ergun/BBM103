print("NOT ORTALAMASI HESAPLAMA")
print("*" * len("NOT ORTALAMASI HESAPLAMA"))

homeworks = int(input("Lütfen dersin ödev sayısını giriniz: "))
while homeworks > 10 or homeworks < 0:
    print("Ödev sayısı 0 ile 10 arasında olmalıdır.")
    homeworks = int(input("Lütfen dersin ödev sayısını giriniz: "))

ogrenci_no = input("Lütfen öğrenci numaranızı giriniz: ")
while len(ogrenci_no) != 9 or ogrenci_no.isnumeric() == False:
    print("Öğrenci numarası 9 haneli olmalıdır.")
    ogrenci_no = input("Lütfen öğrenci numaranızı giriniz: ")

vize_not = int(input(str(ogrenci_no) + " numaralı öğrenci için vize notunu giriniz: "))
while vize_not > 100 or vize_not < 0:
    print("Vize notu 0 ile 100 arasında olmalıdır.")
    vize_not = int(input(str(ogrenci_no) + " numaralı öğrenci için vize notunu giriniz: "))
        
final_not = int(input(str(ogrenci_no) + " numaralı öğrenci için final notunu giriniz: "))
while final_not > 100 or final_not < 0:
    print("Final notu 0 ile 100 arasında olmalıdır.")
    final_not = int(input(str(ogrenci_no) + " numaralı öğrenci için final notunu giriniz: "))

if homeworks > 0:
    homework_notes = []
    for i in range(homeworks):
        homework_note = int(input(str(ogrenci_no) + " numaralı öğrenci için " + str(i+1) + ". ödev notunu giriniz: "))
        while homework_note > 100 or homework_note < 0:
            print("Ödev notu 0 ile 100 arasında olmalıdır.")
            homework_note = int(input(str(ogrenci_no) + " numaralı öğrenci için " + str(i+1) + ". ödev notunu giriniz: "))
        homework_notes.append(homework_note)

    homeworks_average = sum(homework_notes) / len(homework_notes)
    homeworks_average = round(homeworks_average, 2)
    print(f"{ogrenci_no} numaralı öğrencinin ödev not ortalaması: {homeworks_average:,.2f}")

if homeworks == 0:
    ortalama = (vize_not * 0.6) + (final_not * 0.4)
    ortalama = round(ortalama, 2) 
else:
    ortalama = (vize_not * 0.3) + (final_not * 0.4) + (homeworks_average * 0.3)
    ortalama = round(ortalama, 2)


print(f"{ogrenci_no} numaralı öğrencinin not ortalaması: {ortalama:,.2f}")

resume_or_not = input("Yeni bir öğrenci notu hesaplamak için '1', çıkmak için '0' tuşlayınız: ")

while resume_or_not != "1" and resume_or_not != "0":
    resume_or_not = input("Yeni bir öğrenci notu hesaplamak için '1', çıkmak için '0' tuşlayınız: ")

while resume_or_not == "1" or resume_or_not == "0":
    if resume_or_not == "1":
        ogrenci_no = input("Lütfen öğrenci numaranızı giriniz: ")
        while len(ogrenci_no) != 9 or ogrenci_no.isnumeric() == False:
            print("Öğrenci numarası 9 haneli olmalıdır.")
            ogrenci_no = input("Lütfen öğrenci numaranızı giriniz: ")

        vize_not = int(input(str(ogrenci_no) + " numaralı öğrenci için vize notunu giriniz: "))
        while vize_not > 100 or vize_not < 0:
            print("Vize notu 0 ile 100 arasında olmalıdır.")
            vize_not = int(input(str(ogrenci_no) + " numaralı öğrenci için vize notunu giriniz: "))
                
        final_not = int(input(str(ogrenci_no) + " numaralı öğrenci için final notunu giriniz: "))
        while final_not > 100 or final_not < 0:
            print("Final notu 0 ile 100 arasında olmalıdır.")
            final_not = int(input(str(ogrenci_no) + " numaralı öğrenci için final notunu giriniz: "))

        if homeworks > 0:
            homework_notes = []
            for i in range(homeworks):
                homework_note = int(input(str(ogrenci_no) + " numaralı öğrenci için " + str(i+1) + ". ödev notunu giriniz: "))
                while homework_note > 100 or homework_note < 0:
                    print("Ödev notu 0 ile 100 arasında olmalıdır.")
                    homework_note = int(input(str(ogrenci_no) + " numaralı öğrenci için " + str(i+1) + ". ödev notunu giriniz: "))
                homework_notes.append(homework_note)

            homeworks_average = sum(homework_notes) / len(homework_notes)
            homeworks_average = round(homeworks_average, 2)
            print(f"{ogrenci_no} numaralı öğrencinin ödev not ortalaması: {homeworks_average:,.2f}")

        if homeworks == 0:
            ortalama = (vize_not * 0.6) + (final_not * 0.4)
            ortalama = round(ortalama, 2) 
        else:
            ortalama = (vize_not * 0.3) + (final_not * 0.4) + (homeworks_average * 0.3)
            ortalama = round(ortalama, 2)
        resume_or_not = input("Yeni bir öğrenci notu hesaplamak için '1', çıkmak için '0' tuşlayınız: ")
    
    else:
        print("Programdan çıkılıyor...")
        exit()