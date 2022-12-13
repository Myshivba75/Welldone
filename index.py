from flask import Flask
import requests
from NorenApi import NorenApi



app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "API is working fine"

@app.route("/ttt")
def ttt():
    return "API is working fine in ttttt"

@app.route("/test")
def test():
    shoonya=NorenApi()
    shoonya.token_setter()
    return shoonya.get_quotes('NSE','HDFCBANK-EQ')

if __name__ == "__main__":
    #app.debug = True
    app.run(host="0.0.0.0",port= 5000)
  

  

  
  
