#required installs
from bs4 import BeautifulSoup
import requests
from flask import Blueprint, render_template, request

sets = Blueprint('sets', __name__)

#defines home page functionalities
#just returns the home page
@sets.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

#defines celebrations page functionalities
#returns the pokemon's name, number, price and if it's in the celebrations set
#also points to the celebrations html page
@sets.route('/celebrations', methods=['GET', 'POST'])
def celebrations():
    name = ""
    number = ""
    price = ""
    found = False
    notFound = False

    if request.method == 'POST':
        pokemon = request.form.get('pokemon')

        #scrapes data from the tcgplayer website
        html_text = requests.get('https://shop.tcgplayer.com/price-guide/pokemon/celebrations-classic-collection').text
        soup = BeautifulSoup(html_text, 'lxml')
        cards = soup.find_all('td', class_ = 'product')
        n = soup.find_all('td', class_ = 'number')
        p = soup.find_all('td', class_= 'marketPrice')
 
        nameList = [""]
        numberList = [""]
        priceList = [""]

        #appends all the pokemon's data into 3 different lists
        for card in cards:
            name = card.find('div', class_ = 'productDetail').text
            nameList.append(name)
 
        for ns in n:
            number = ns.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            numberList.append(number)
 
        for ps in p:
            price = ps.find('div', class_ = 'cellWrapper').text.replace(' ', '')
            priceList.append(price)

        #checks if the input is in the list
        for i in range(len(nameList)):
            if str(pokemon).lower() in nameList[i].lower() and not str(pokemon) == "":
                name = (nameList[i].strip().upper())
                number = (f"Set Number: {numberList[i].strip()}")
                price = (f"Current Price: {priceList[i].strip()}")
                found = True
            else:
                name = str(pokemon)
                notFound = True
    #returns the celebrations page and associated variables
    return render_template("celebrations.html", name = name, number = number, price = price, found = found, notFound = notFound)

#same functionalities as the celebrations page, just with a different name/set
@sets.route('/fusion-strike', methods=['GET', 'POST'])
def fusion_strike():
    name = ""
    number = ""
    price = ""
    found = False
    notFound = False

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
                name = (nameList[i].strip().upper())
                number = (f"Set Number: {numberList[i].strip()}")
                price = (f"Current Price: {priceList[i].strip()}")
                found = True
            else:
                notFound = True
                name = str(pokemon)     
    return render_template("fusion.html", name = name, number = number, price = price, found = found, notFound = notFound)

#same functionalities as the celebrations page, just with a different name/set
@sets.route('/evolving-skies', methods=['GET', 'POST'])
def evolving_skies():
    name = ""
    number = ""
    price = ""
    found = False
    notFound = False

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
                name = (nameList[i].strip().upper())
                number = (f"Set Number: {numberList[i].strip()}")
                price = (f"Current Price: {priceList[i].strip()}")
                found = True
            else:
                notFound = True
                name = str(pokemon)
    return render_template("evolving.html", name = name, number = number, price = price, found = found, notFound = notFound)
