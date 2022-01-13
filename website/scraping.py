from bs4 import BeautifulSoup
import requests
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

sets = Blueprint('sets', __name__)

@sets.route('/celebrations', methods=['GET', 'POST'])
def celebrations():
    name = ""
    number = ""
    price = ""
    packPrice = ""
    found = False
    b = False

    if request.method == 'POST':
        pokemon = request.form.get('pokemon')

        html_text = requests.get('https://shop.tcgplayer.com/price-guide/pokemon/celebrations-classic-collection').text
        soup = BeautifulSoup(html_text, 'lxml')
        cards = soup.find_all('td', class_ = 'product')
        n = soup.find_all('td', class_ = 'number')
        p = soup.find_all('td', class_= 'marketPrice')
 
        nameList = [""]
        numberList = [""]
        priceList = [""]
 
        for card in cards:
            name = card.find('div', class_ = 'productDetail').text
            nameList.append(name)
 
        for ns in n:
            number = ns.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            numberList.append(number)
 
        for ps in p:
            price = ps.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            priceList.append(price)
 
        for i in range(len(nameList)):
            if str(pokemon).lower() in nameList[i].lower() and not str(pokemon) == "":
                name = (f"Name: {nameList[i].strip()}")
                number = (f"Number: {numberList[i].strip()}")
                price = (f"Price: {priceList[i].strip()}")
                found = True
            else:
                b = True

    return render_template("celebrations.html", name = name, number = number, price = price, found = found, b = b, packPrice = packPrice)

@sets.route('/fusion-strike', methods=['GET', 'POST'])
def fusion_strike():
    name = ""
    number = ""
    price = ""
    found = False
    b = False

    if request.method == 'POST':
        pokemon = request.form.get('pokemon')

        html_text = requests.get('https://shop.tcgplayer.com/price-guide/pokemon/swsh08-fusion-strike').text
        soup = BeautifulSoup(html_text, 'lxml')
        cards = soup.find_all('td', class_ = 'product')
        n = soup.find_all('td', class_ = 'number')
        p = soup.find_all('td', class_= 'marketPrice')
 
        nameList = [""]
        numberList = [""]
        priceList = [""]
 
        for card in cards:
            name = card.find('div', class_ = 'productDetail').text
            nameList.append(name)
 
        for ns in n:
            number = ns.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            numberList.append(number)
 
        for ps in p:
            price = ps.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            priceList.append(price)
 
        for i in range(len(nameList)):
            if str(pokemon).lower() in nameList[i].lower() and not str(pokemon) == "":
                name = (f"Name: {nameList[i].strip()}")
                number = (f"Number: {numberList[i].strip()}")
                price = (f"Price: {priceList[i].strip()}")
                found = True
            else:
                b = True
    return render_template("fusion.html", name = name, number = number, price = price, found = found, b = b)

@sets.route('/evolving-skies', methods=['GET', 'POST'])
def evolving_skies():
    name = ""
    number = ""
    price = ""
    found = False
    b = False

    if request.method == 'POST':
        pokemon = request.form.get('pokemon')

        html_text = requests.get('https://shop.tcgplayer.com/price-guide/pokemon/swsh07-evolving-skies').text
        soup = BeautifulSoup(html_text, 'lxml')
        cards = soup.find_all('td', class_ = 'product')
        n = soup.find_all('td', class_ = 'number')
        p = soup.find_all('td', class_= 'marketPrice')
 
        nameList = [""]
        numberList = [""]
        priceList = [""]
 
        for card in cards:
            name = card.find('div', class_ = 'productDetail').text
            nameList.append(name)
 
        for ns in n:
            number = ns.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            numberList.append(number)
 
        for ps in p:
            price = ps.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            priceList.append(price)
 
        for i in range(len(nameList)):
            if str(pokemon).lower() in nameList[i].lower() and not str(pokemon) == "":
                name = (f"Name: {nameList[i].strip()}")
                number = (f"Number: {numberList[i].strip()}")
                price = (f"Price: {priceList[i].strip()}")
                found = True
            else:
                b = True
    return render_template("evolving.html", name = name, number = number, price = price, found = found, b = b)
