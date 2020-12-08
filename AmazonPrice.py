#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import smtplib
import time

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

URL = "https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_oneplus_1a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-10&pf_rd_r=DCBQXYVXRA4RQQY571ZT&pf_rd_t=101&pf_rd_p=8f4aeea9-2043-442b-abef-22299b079dc3&pf_rd_i=21439725031"

def checkPrice(URL):

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())

    title = soup.find(id = "productTitle").get_text()

    print(title.strip())
    price = soup.find(id = "priceblock_ourprice").get_text()

    converted_price = float(price[2:].replace(',', ''))

    print(converted_price)

    if converted_price < 50000:
        sendMail()


def sendMail():

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login('nmamatha1808@gmail.com', 'MAMATHAMAMMU')

    subject = "Price has dropped!! YAY!!!"
    body = "Check the link for more details: https://www.amazon.in/gp/product/B07DJ8K2KT/ref=s9_acss_bw_cg_oneplus_1a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-10&pf_rd_r=DCBQXYVXRA4RQQY571ZT&pf_rd_t=101&pf_rd_p=8f4aeea9-2043-442b-abef-22299b079dc3&pf_rd_i=21439725031"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('nmamatha1808@gmail.com',
                    '18wh1a1257@bvrithyderabad.edu.in',
                    msg)
    
    print("MAIL SENT")

    server.quit()

while(True):

    checkPrice(URL)
    time.sleep(60 ** 3)
