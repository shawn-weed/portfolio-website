from flask import Blueprint, render_template
import requests

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
            for i in response:
                projects.append({'name': i['name'], 'desc': i['description'], 'url': i['html_url']})
            return render_template("developer.html", projects=projects)
        else:
            print('no here')
            return render_template('developer.html', code = r.status_code)
            
    except Exception as e:
        error = e
        return render_template('developer.html', error=error)