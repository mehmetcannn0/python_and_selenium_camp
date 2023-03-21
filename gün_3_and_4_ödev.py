from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# * Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# * Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# * Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# * Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# * Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# * Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

class Test_Sauce:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.minimize_window()
    def test_invalid_login(self):
        self.driver.maximize_window()        
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print("test_invalid_login fonksiyonu")
        print(f"TEST SONUCU: {testResult}")

    def user_name_req(self):
        self.driver.maximize_window()                
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print("user_name_req fonksiyonu")
        print(f"TEST SONUCU: {testResult}")

    def pass_req(self):
        self.driver.maximize_window()                
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        sleep(2)
        usernameInput.send_keys("1")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print("pass_req fonksiyonu")
        print(f"TEST SONUCU: {testResult}")

    def locked_out_user(self):
        self.driver.maximize_window()                
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print("locked_out_user fonksiyonu")
        print(f"TEST SONUCU: {testResult}")

    def x_icon(self):
        self.driver.maximize_window()                
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        testResult=True
        
        # ^^ suan 2 adet x olmalı    
        x_icons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        num_of_x_icons=len(x_icons)

        
        if(num_of_x_icons==2):
            testResult=True

            error_button=self.driver.find_element(By.CLASS_NAME,"error-button")
            error_button.click()
            x_icons.clear()
            sleep(2)
            x_icons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
            num_of_x_icons=len(x_icons)

            if(num_of_x_icons==0):
                # ^^ suan hiç x olmamalı
      
                print("x_icon fonksiyonu")
                print(f"TEST SONUCU: {testResult}")            

            else:
                testResult=False 

                print(f"error-button'a tıklandıktan sonra {num_of_x_icons} X ikonu bulundu \nHiç bulunmamalıydı")   
                print("x_icon fonksiyonu")
                print(f"TEST SONUCU: {testResult}")
                               
        else:
            testResult=False

            print(f"{num_of_x_icons} adet X ikonu bulundu \n2 adet olmalıydı")
            print("x_icon fonksiyonu")
            print(f"TEST SONUCU: {testResult}")      

    def standard_user(self):
        self.driver.maximize_window()       
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        current_url =self.driver.current_url

        if(current_url.endswith("/inventory.html")):
            testResult=True

            print("standard_user fonksiyonu")
            print(f"TEST SONUCU: {testResult}")

        else:
            testResult=False

            print("standard_user fonksiyonu")
            print(f"TEST SONUCU: {testResult}")

    def products(self):
        self.driver.maximize_window()       
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        
        products=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        num_of_products=len(products)
        if(num_of_products==6):
            testResult=True

            print("products fonksiyonu")
            print(f"TEST SONUCU: {testResult}")
        else:
            testResult=False

            print(f"{num_of_products} adet ürün bulundu \n6 adet bulunmalıydı") 
            print("products fonksiyonu")
            print(f"TEST SONUCU: {testResult}")

    def all_of_test(self):

        self.test_invalid_login()
        self.user_name_req()
        self.pass_req()
        self.locked_out_user()
        self.x_icon()
        self.standard_user()
        self.products()

testClass = Test_Sauce()

while(True):
      
    secim=input('''
    1-->> test_invalid_login
    2-->> user_name_req
    3-->> pass_req
    4-->> locked_out_user
    5-->> x_icon
    6-->> standard_user
    7-->> products
    8-->> sıra ile hepsi
    yapılmak istenen test-->>: ''')

    if(secim=="1"):
        testClass.test_invalid_login()

    elif(secim=="2"):
        testClass.user_name_req()

    elif(secim=="3"):
        testClass.pass_req()

    elif(secim=="4"):
        testClass.locked_out_user()

    elif(secim=="5"):
        testClass.x_icon()

    elif(secim=="6"):
        # print("6")
        testClass.standard_user()

    elif(secim=="7"):
        testClass.products()

    elif(secim=="8"):
        testClass.all_of_test()

    else:
        print("hatalı secim...")

  