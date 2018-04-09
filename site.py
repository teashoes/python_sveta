from flask import Flask
from weather import get_w 
app = Flask (__name__)
@app.route("/test") #main page route
def index(): #function deals with app route
    return 'hello, sweet baby'

@app.route("/")
def inde():
    return "wooow"

if __name__ == "__main__": #если напрямую то запускается приложение
    app.run()


import requests
def get_w(url):
    res=requests.get(url)
    if res.status_code==200:
        return res.json() #['name'] #json converts into dictionary
    else:
        print('woops')
if __name__ == '__main__':
    data=get_w("http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=6710b438654f51bbf36d184f136cee7a&units=metric")
    print(data)