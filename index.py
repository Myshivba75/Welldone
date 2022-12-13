from flask import Flask
from NorenApi import NorenApi


app = Flask(__name__)

@app.route('/tst')

def tst():
    return "Finally done something"

  
@app.route('/')
def home():
	return "Finally done something"

  
@app.route('/gli')
     

def gli(): 
  shoonya=NorenApi()
  shoonya.token_setter()
  shoonya.place_order(buy_or_sell='B', product_type='C',
                       exchange='NSE', tradingsymbol='SBIN-EQ', 
                        quantity=1, discloseqty=0,price_type='LMT', price=560.00, trigger_price=199.50,
                        retention='DAY', remarks='my_order_001')
  return shoonya.get_quotes('NSE','HDFCBANK-EQ')

if __name__ == "__main__":
	app.run()    
  
  

  
  
