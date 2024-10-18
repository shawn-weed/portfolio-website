from flask import Blueprint, render_template
import requests
import os

views = Blueprint(__name__, 'views')

@views.route("/")
def home():
    return render_template('index.html')

@views.route("developer")
def developer():
    try:
        r = requests.get(
            "https://api.github.com/users/shawn-weed/repos"
        )
        projects = []
        if r.status_code == 200:
            response = r.json()
            print(r)
            for i in response:
                projects.append({'name': i['name'], 'desc': i['description'], 'url': i['html_url']})
            return render_template("developer.html", projects=projects)
        else:
            return render_template('developer.html', error = 'Code : ' + str(r.status_code))
            
    except Exception as e:
        error = e
        return render_template('developer.html', error=error)
    
@views.route("developer/hardt4il-website")
def hardt4il():
    return render_template('hardt4il.html')

@views.route("developer/OptiTrack")
def optitrack():
    return render_template('optitrack.html')

@views.route("developer/portfolio-website")
def porfolio():
    return render_template('portfolio.html')

@views.route("creative")
def creative():
    return render_template("creative.html")

@views.route('creative/photography')
def photography():
    action_dir = './static/images/action'
    action = os.listdir(action_dir)

    actionCol1 = action[::3]
    actionImgCol1 = []
    for i in actionCol1:
        actionImgCol1.append(i)

    actionCol2 = action[1::3]
    actionImgCol2 = []
    for i in actionCol2:
        actionImgCol2.append(i)

    actionCol3 = action[2::3]
    actionImgCol3 = []
    for i in actionCol3:
        actionImgCol3.append(i)
    
    products_dir = './static/images/products'
    products = os.listdir(products_dir)

    productsCol1 = products[::3]
    productsImgCol1 = []
    for i in productsCol1:
        productsImgCol1.append(i)

    productsCol2 = products[1::3]
    productsImgCol2 = []
    for i in productsCol2:
        productsImgCol2.append(i)

    productsCol3 = products[2::3]
    productsImgCol3 = []
    for i in productsCol3:
        productsImgCol3.append(i)

    return render_template('photography.html', actionImgCol1=actionImgCol1, actionImgCol2=actionImgCol2, actionImgCol3=actionImgCol3, productsImgCol1=productsImgCol1, productsImgCol2=productsImgCol2, productsImgCol3=productsImgCol3)