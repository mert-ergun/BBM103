#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>

float ogrenci_ortalamalari[100] = {0};

float hesapla(float vize, float final, float odev){
    float ortalama;
    if(odevler_sayisi == 0){
        ortalama = vize * 0.6 + final * 0.4;
    }
    else{
        float toplam_odev_notu = 0;
        for(int i = 0; i < odevler_sayisi; i++){
            toplam_odev_notu += odevler[i];
        }
        ortalama = vize * 0.3 + final * 0.4 + (toplam_odev_notu / odevler_sayisi) * 0.3;
    }
    ogrenci_ortalamalari[ogrenci_sayisi] = ortalama;
    ogrenci_sayisi++;

    return roundf(ortalama * 100) / 100;
}

void odev_not_hesapla(char *ogrenci_no, int odev_sayisi, float *odev_notlari){
    for(int i = 0; i<odev_sayisi, i++){
        printf("%s numaralı öğrenci için %d. ödev notunu giriniz:" , ogrenci_no, i+1);
        scanf("%f", &odev_notlari[i]);
        while odev_notlari[i] < 0 || odev_notlari[i] > 100{
            printf("%s numaralı öğrenci için %d. ödev notunu giriniz:" , ogrenci_no, i+1);
            scanf("%f", &odev_notlari[i]);
        }
    }

    float toplam_odev_notu = 0;
    for (int i = 0; i < odev_sayisi; i++){
        toplam_odev_notu += odev_notlari[i];
    }
    float odev_ortalama = toplam_odev_notu / odev_sayisi;
    printf("%s numaralı öğrencinin ödev ortalaması: %.2f\n", ogrenci_no, odev_ortalama);
}

void main(){
    char ogrenci_no[10];
    float vize_not, final_not;
    printf("NOT ORTALAMASI HESAPLAMA"\n);
    printf("*" * strlen("NOT ORTALAMASI HESAPLAMA"));
    printf("Ödev sayısını giriniz: ");
    scanf("%d", &odevler_sayisi);
    float odevler[odevler_sayisi];

    printf("Öğrenci numarasını giriniz: ");
    scanf("%s", ogrenci_no);
    printf("Vize notunu giriniz: ");
    scanf("%f", &vize_not);
    printf("Final notunu giriniz: ");
    scanf("%f", &final_not);
    
    
}