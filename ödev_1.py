 
# ^ *Veri Tipleri
# ^ int => Tam sayılar ->>>1, 2, 3, 4, 5, 6, 7, 8, 9, 0.
# ^ float => Ondalıklı sayılar ->>> 1.123, 2.234, 3.345.
# ^ String => Metinler ->>> "tırnak içerisinde yazılan herşey metinsel bi ifadedir.".
# ^ Boolean => Mantıksal değişkenler ->>> true, false.
# ^ list => Bir çok veriyi tek bi arada tutar ->>> [123,234,345] ,["asd","zxc","qwe"].
# ^ set => Bir çok veriyi tek bi arada tutar ->>> {123,234,345} ,{"asd","zxc","qwe"}.
# ^ tuple => Bir çok veriyi tek bi arada tutar ama değiştirilemez ->>> (123,234,345).
# ^ dictionary => Bir çok veriyi tek bi arada tutar ama değiştirilemez {"sayi_1": 123, "sayi_2": 234, "sayi_3": 345} 
#### Hepsine aynı açıklamayı yazdım ama hepsinin farklı kullanım amaçları var


mail = "memq"
sifre = "qweasd"

email = input("mail : ")
password = input("şifre : ")

if mail == email and sifre == password:
    print("giriş başarılı")
elif mail != email and sifre == password:
    print("hatalı kullanıcı adı girdiniz")
elif mail == email and sifre != password:
    print("hatalı şifre girdiniz")
else:
    print("kullanıcı adı ve/veya şifre hatalı")

kursaKayit = True
if kursaKayit:
    print("kurs kaydın tamamlandı , giriş yapabilirsin")
else:
    print("kayıt basarısız. kursu goruntuleyemezsın.")

kurslar = [ "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium", "Yazılım Geliştirici Yetiştirme Kampı (JavaScript)", "Yazılım Geliştirici Yetiştirme Kampı (C# + ANGULAR)","Yazılım Geliştirici Yetiştirme Kampı (JAVA + REACT)"]
egitmenler=["Engin demiroğ","Halit kalaycı"]


print("kurslar")
for kurs in kurslar:
    print(kurs)

print("egitmenler")
for egitmen in egitmenler:
    print(egitmen)