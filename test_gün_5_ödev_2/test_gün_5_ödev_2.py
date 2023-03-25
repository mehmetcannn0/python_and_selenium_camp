from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

# * Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# * Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# * Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# * Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# * Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# * Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

### * 5. gunun 2. odevınde oncekı odevdekı yazdıgımız testlerı PyTest uyumlu hale getırecegız

class Test_Sauce:


    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = "test_gün_5_ödev_2/"+str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))

    @pytest.mark.parametrize("username,password",[("1","1") , ("kullaniciadim","sifrem"),("denemeusername","denemepassword")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_invalid_login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"



    def test_user_name_req(self):
        self.waitForElementVisible((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"password"),10)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_user_name_req-__-__.png")
        assert errorMessage.text == "Epic sadface: Username is required"


    def test_pass_req(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        usernameInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_pass_req-1-__.png")
        assert errorMessage.text == "Epic sadface: Password is required"
      

    def test_locked_out_user(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_locked_out_user-locked_out_user-secret_sauce.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
  

    def test_x_icon(self):
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
                self.driver.save_screenshot(f"{self.folderPath}/test_x_icon-__-__.png")
                assert testResult          

            else:
                testResult=False 

                print(f"error-button'a tıklandıktan sonra {num_of_x_icons} X ikonu bulundu \nHiç bulunmamalıydı")   
                print("x_icon fonksiyonu")
                self.driver.save_screenshot(f"{self.folderPath}/test_x_icon-__-__.png")
                assert testResult
                               
        else:
            testResult=False

            print(f"{num_of_x_icons} adet X ikonu bulundu \n2 adet olmalıydı")
            print("x_icon fonksiyonu")
            self.driver.save_screenshot(f"{self.folderPath}/test_x_icon-__-__.png")
            assert testResult      

    def test_standard_user(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        current_url =self.driver.current_url

        if(current_url.endswith("/inventory.html")):
            testResult=True

            print("standard_user fonksiyonu")
            self.driver.save_screenshot(f"{self.folderPath}/test_standard_user-standard_user-secret_sauce.png")
            assert testResult

        else:
            testResult=False

            print("standard_user fonksiyonu")
            self.driver.save_screenshot(f"{self.folderPath}/test_standard_user-standard_user-secret_sauce.png")
            assert testResult

    def test_products(self):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item"))
        products=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        num_of_products=len(products)
        if(num_of_products==6):
            testResult=True

            print("products fonksiyonu")
            self.driver.save_screenshot(f"{self.folderPath}/test_products-standard_user-secret_sauce.png")
            assert testResult
        else:
            testResult=False

            print(f"{num_of_products} adet ürün bulundu \n6 adet bulunmalıydı") 
            print("products fonksiyonu")
            self.driver.save_screenshot(f"{self.folderPath}/test_products-standard_user-secret_sauce.png")
            assert testResult

        # TODO: urun fıyat uyusuyormu
        # TODO: add to kart a tıklandıgında remove oluyor mu
        # TODO: sepete ekleme yapıldıgında sepettekı sayı ıle uyusuyor mu

