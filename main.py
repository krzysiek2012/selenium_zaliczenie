#!/usr/bin/python3
import unittest
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

firma = "Prywatna"
nip_code = "111-222-333"
ulica = "Kokosowa"
kod = "xx"
miasto = "Pacanow"
imie = "Grażka"
nazwisko = "Zbyszkowa"
i_majl = "kiko@noreplay.github.com"
fon = "123456789"
logyn = "okimoki"
haslo = "123kokoK456"

class TestRoweria(unittest.TestCase):
    def setUp(self):

        """
        Warunki wstepne
        """
        #przegladarka wlaczona
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://roweria.pl")


    def testDoProjektu(self):

        """
        TC = 01: testowanie strony roweria.pl - błędny kod pocztowy...
        """

        driver = self.driver

        #Kliknij "ZALOGUJ SIE"
        znajdz_zaloguj = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="account_link link hidden-phone"]'))).click()

        #Znajdz przycisk "ZALOZ NOWE KONTO"
        znajdz_buton = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn signin-form_register2"]'))).click()

        #Wybierz "Firma" w sekcji dane do faktury
        wybierz_firma = driver.find_element_by_xpath('//input[@id="client_type1"]').click()

        #Wpisz nazwę firmy
        Firma = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_firm'))).send_keys(firma)

        #Wpisz NIP
        NIP = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_nip'))).send_keys(nip_code)

        #Wpisz "Ulicę i numer"
        Street = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_street'))).send_keys(ulica)

        #Wpisz "kod pocztowy"
        Postal = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_zipcode'))).send_keys(kod)

        #Wpisz "miasto"
        City = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_city'))).send_keys(miasto)

        #Przewin strone w dol
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3.5);window.scrollTo(0, document.body.scrollHeight/3.7);")

        #Wpisz "Imie" w sekcji dane kontaktowe
        Firsname = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_firstname'))).send_keys(imie)

        #Wpisz "Nazwisko"
        Surname = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_lastname'))).send_keys(nazwisko)

        #wpisz "Adres e-mail"
        Wrong_mail = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_email'))).send_keys(i_majl)

        #Zaznacz box "Chce otrzymywac newsletter"
        newsletter = driver.find_element_by_xpath('//input[@id="client_mailing"]').click()

        #Wpisz "Telefon"
        tele = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_phone'))).send_keys(fon)

        #Wpisz "Login"
        login = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_login'))).send_keys(logyn)

        #Wpisz "hasło"
        haslo_1 = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'client_password'))).send_keys(haslo)

        #Powtórz "hasło"
        haslo_2 = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.ID, 'repeat_password'))).send_keys(haslo)

        #Zaznacz box "Zaakceptuj warunki"
        akceptacja = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="terms_agree"]')))

        driver.execute_script("arguments[0].click();", akceptacja)

        #Kliknij "ZAREJESTRUJ KONTO"
        zarejestruj = WebDriverWait(driver, 45).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="submit_clientnew_form"]')))

        driver.execute_script("arguments[0].click();", zarejestruj)

        #Znajdz bledy na stronie
        bledy = driver.find_elements_by_xpath('//div[@class="menu_messages_warning_sub"]/p')

        visible_error_noticed = []

        for error in bledy:
            if error.is_displayed():
                visible_error_noticed.append(error)

        assert len(visible_error_noticed) == 2

        print('\n\n\tcoz_takiego_jeste_w_boksie_z_bledami:\n')

        for arg in visible_error_noticed:
            print(arg.get_attribute("innerText"))


        error_text_1 = visible_error_noticed[0].get_attribute("innerText")
        assert error_text_1 == "Niepoprawny kod pocztowy."

        error_text_2 = visible_error_noticed[1].get_attribute("innerText")
        assert error_text_2 == "Niepoprawny kod pocztowy odbiorcy."


        print('\n\tTest_completed_go_home\n')

    def tearDown(self):
        """
        sprzatanie po tescie
        """
        self.driver.quit()





if __name__=='__main__':
    unittest.main(verbosity=2)
