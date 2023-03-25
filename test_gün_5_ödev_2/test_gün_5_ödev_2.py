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

       
    @pytest.mark.parametrize("name,price",[("Sauce Labs Backpack","$29.99") ,("Sauce Labs Bike Light","$9.99"),("Sauce Labs Bolt T-Shirt","$15.99") ])
    def test_product_and_price(self,name,price):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME,"inventory_item_name"))
        name_of_products_elements=self.driver.find_elements(By.CLASS_NAME,"inventory_item_name")
        price_of_products_elements=self.driver.find_elements(By.CLASS_NAME,"inventory_item_price")
        name_of_products=[]
        price_of_products=[]

        for n in name_of_products_elements:
            name_of_products.append(n.text)
        for p in price_of_products_elements:
            price_of_products.append(p.text)

        if(name_of_products.count(name)>0 and price_of_products.count(price)>0):
            index_of_name=name_of_products.index(name)
            index_of_price=price_of_products.index(price)
            if(index_of_name==index_of_price):
                print("test_product_and_price fonksiyonu")
                self.driver.save_screenshot(f"{self.folderPath}/test_product_and_price-{name}-{price}.png")
                assert index_of_name==index_of_price
            else:
                print("Ürün ile fiyat eşleşmiyor") 
                print("test_product_and_price fonksiyonu")
                self.driver.save_screenshot(f"{self.folderPath}/test_product_and_price-{name}-{price}.png")
                assert index_of_name==index_of_price
        else:    
            print("Ürün yada fiyat bulunamadı") 
            print("test_product_and_price fonksiyonu")
            self.driver.save_screenshot(f"{self.folderPath}/test_product_and_price-{name}-{price}.png")
            assert name_of_products.count(name)>0 and price_of_products.count(price)>0


    @pytest.mark.parametrize("index",[(1),(2),(3),(4)])
    def test_add_to_cart_button(self,index):
        self.waitForElementVisible((By.ID,"user-name"))
        
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        
        self.waitForElementVisible((By.CLASS_NAME,"btn_inventory"))
        add_and_remove_card_btns=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")

        if(add_and_remove_card_btns[index].text=="Add to cart"):

            add_and_remove_card_btns[index].click()            
            add_and_remove_card_btns=[]
            add_and_remove_card_btns=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")
            assert add_and_remove_card_btns[index].text=="Remove"


    @pytest.mark.parametrize("count_of_product_to_add_to_cart",[(1),(2),(3),(4)])
    def test_add_to_cart_process(self,count_of_product_to_add_to_cart):
        self.waitForElementVisible((By.ID,"user-name"))
        
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        
        self.waitForElementVisible((By.CLASS_NAME,"btn_inventory"))
        add_and_remove_card_btns=self.driver.find_elements(By.CLASS_NAME,"btn_inventory")

        for index in range(count_of_product_to_add_to_cart):
            if(add_and_remove_card_btns[index].text=="Add to cart"):
                add_and_remove_card_btns[index].click()            

        assert self.driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text==str(count_of_product_to_add_to_cart)

