students = ["birinci öğrenci","ikinci öğrenci"]
def get_input():
    ad = input("Öğrencinin adınızı giriniz: ")
    soyad = input("Öğrencinin soyadını giriniz: ")
    ad_soyad = ad + ' ' + soyad
    return ad_soyad

def ogrenci_kayit():
    ad_soyad=get_input()
    if ad_soyad in students:
        print(f"{ad_soyad} bu öğrenci zaten mevcut.")
    else:
        students.append(ad_soyad)
        print(f"{ad_soyad} sisteme basariyla kaydedildi.")
        return students    

def ogrenci_silme(students):
    sayi=int(input("kac tane öğrenci silmek istersini -->"))
    for i in range(sayi):       
        while(True):
            ad_soyad=get_input()
            if ad_soyad in students:
                students.remove(ad_soyad)
                print("Öğrenci silindi")
                break
            else:
                print(f"{ad_soyad} listede yok")    
                               
while True: 
    
    print("***************************")
    print ("1-->öğrenci eklemek \n2-->öğrenci silmek \n3-->öğrenci listesini görmek \n4-->öğrencinin numarasını öğrenmek \nq/Q-->çıkış")
    islem = input("Yapmak istediğiniz isleme numarası --> ")
    
    if (islem== "1"):
        ogrenci_kayit()

    elif (islem== "2"):
        ogrenci_silme(students)
        
    elif (islem== "3"):
        print(students)
        
    elif (islem== "4"):
        ad_soyad = get_input()
        if(ad_soyad in students):
            print(f"girdiğiniz bilgilere sahip öğrencinin numarası --> {students.index(ad_soyad)+1}")
        else:
            print("girdiğiniz bilgilere sahip öğrenci bulunamadi")
    elif (islem=="q"or islem=="Q"):
        break
    else:
        print("hatali giris...")
 
