###### Bu read.me dosyası kursun 5.ödevine dahil
###  Ödevin konusu
- PyTestdeki decoratorleri araştırmak.

## PyTest'deki decoratorler

- @pytest.mark.skip testleri herhangi bi koşul olmadan atlamamızı sağlar
    ```Python
    @pytest.mark.skip(reason="To show we can skip tests without any condition.")
    def test_any():
        assert True
    ```

- @pytest.mark.skipif koşula bağlı olarak bir testi atlamamızı sağlar   
    ```Python
    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
    def test_function():
        ...
    ```

- @pytest.mark.parametrize bağımsız değişkenlerin parametreleştirilmesini sağlar
    ```Python
    @pytest.mark.parametrize("username,password",[("1","1") , ("kullaniciadim","sifrem")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        ...
    ```

- @pytest.fixture anladıgım kadarıya yapacagımız teste ortam hazırlıyor 
    > fixture ıle belırttıgımız fonsıyonu hangı testten once calıstırmak ıstıyorsak
    > o test fonksıyonuna gonderıyoruz ve  testten once  fıxture dıye belırttıgımız fonsıyon calısıyor
    > yield'den sonraki kısmı ıse test fonksıyonu calıstıktan sonra calısıyor yanı olusturdugumuz  
    > ortamı silmek/kaldırmak istedigimizde kullanabılırız

    ```Python
    @pytest.fixture()
    def ucgen():
        print("Ucgen olusturuldu")
        yield
        print("ucgen yok edildi")
    
    def test_ucgen_cevresi_hesaplama(ucgen):
        print("ucgen cevre hesaplama")
        assert cevre_hesaplama(2,3,3) == 8
    ```
    
- @pytest.mark.xfail failed olacağını bildigimiz testleri belirtmek için kullanılır
    ```Python    
    @pytest.mark.xfail
    def test_carpma ():
        assert carpma(3,3) == 10
        
    ```


