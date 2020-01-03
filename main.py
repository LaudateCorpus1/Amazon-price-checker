import requests
import time
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.co.uk/Neos-SmartCam-Vision-Camera-Warranty/dp/B07JY7K3SZ/ref=sr_1_3?crid=NWL1Z5GY7U00&keywords=neos+smart+cam&qid=1565809301&s=gateway&sprefix=neos%2Caps%2C143&sr=8-3"
gmail_user = ''
gmail_password = ''

headers = {
    "User-Agent":
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="priceblock_ourprice").getText()
    convertedPrice = float(title[1:6])

    if (convertedPrice < 24.99):
        sendMail()


def sendMail():

    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(gmail_user, gmail_password)
        print("connected!")
    except:
        print('Something went wrong...')
    server_ssl.sendmail(
        gmail_user, gmail_user,
        "Subject: Price drop on those cameras buddy!\n\n " + URL)


while True:
    checkPrice()
    print("Price was checked!")
    time.sleep(2)
