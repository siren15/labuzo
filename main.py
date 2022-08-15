import time
import undetected_chromedriver as uc # importujeme upravený slenium chrome driver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    meno = os.getenv('meno') # načítaj meno z .env súboru, tento súbor je nutné manuálne vytvoriť a zadať tam svoje meno a heslo
    heslo = os.getenv('heslo') # načítaj heslo z .env súboru
    try:
        chrome = uc.Chrome() # definujeme chrome ako prehliadač ktorý používame
        chrome.get('http://gmail.com') # načítame gmail.com

        email_element = chrome.find_element(By.NAME, 'identifier') # nájdeme element pre meno podľa jeho mena
        email_element.send_keys(meno) # nakopírujeme naše meno načítané z .env súboru
        dalej_btn = chrome.find_element(By.ID, 'identifierNext') # nájdeme talčítko "Ďalej" pre meno podla jeho ID
        dalej_btn.click() # stlačíme ho
        time.sleep(1) # počkáme jednu sekundu
        heslo_element = chrome.find_element(By.NAME, 'password') # nájdeme element pre heslo podľa jeho mena
        heslo_element.send_keys(heslo) # nakopírujeme naše heslo načítané z .env súboru
        dalej_btn = chrome.find_element(By.ID, 'passwordNext') # nájdeme talčítko "Ďalej" pre heslo podla jeho ID
        dalej_btn.click() # stlačíme ho
        print('Úspešne prihlásený.') # napíše pri úspechu
    except Exception:
        print('Prihlásenie bolo neúspešné.') # napíše pri zlihaní
