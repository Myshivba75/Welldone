from flask import Flask,request
import requests
from NorenApi import NorenApi
import json


app = Flask(__name__)
app.url_map.strict_slashes = False


shoonya=NorenApi()
shoonya.token_setter()

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

@app.route("/workk")
def workk():
    def buy_signal(trasy):

       res=shoonya.place_order(buy_or_sell='B', product_type=pro_type,exchange=exc,
                            tradingsymbol=str(trasy),quantity=qua, discloseqty=dis,
                            price_type=pr_type, price=prc, trigger_price=tr_pr,retention='DAY',
                             remarks='my_order_001')
       return res

    def sell_signal(trasy):

        res=shoonya.place_order(buy_or_sell='S', product_type=pro_type,exchange=exc,
                           tradingsymbol=str(trasy),quantity=qua, discloseqty=dis,
                           price_type=pr_type, price=prc, trigger_price=tr_pr,retention='DAY',
                           remarks='my_order_001')
        return res


    def write_do_to_file(bt,st):
            data1 = {"bt": bt ,"st": st}
            with open("do_key.json", 'w') as json_f:
                json.dump(data1, json_f)



    def read_do_from_file():
            with open("do_key.json",'r') as json_f:
                data2=json.load(json_f)
                return data2


    dd = read_do_from_file()
    bt =   dd['bt']
    st =   dd['st']

    #b_or_s='B' 
    pro_type='C'
    exc='NSE'
    trasy='SOUTHBANK-EQ'
    qua=1
    dis=0
    pr_type='LMT' 
    prc=18.50
    tr_pr=None
    
    
    
    req_d=request.get_json()
    

    do=req_d['do']

    
    

    if (do =="b" and bt ==0):
            if(st==1):
                fff=buy_signal(trasy)
                st=0

            fff=buy_signal(trasy)
            bt=1
            st=st
            write_do_to_file(bt,st)

            print (fff)


    if (do =="exb" and bt ==1):
            fff=sell_signal(trasy)

            bt=0
            st=st
            write_do_to_file(bt,st)
            print (fff)

    if (do =="exs" and st==1):
            fff=buy_signal(trasy)

            bt=bt
            st=0
            write_do_to_file(bt,st)
            print (fff)



    if (do=="s" and st==0):
            if(bt==1):
                fff=sell_signal(trasy)
                bt=0
            fff=sell_signal(trasy)
            st=1
            bt=bt
            write_do_to_file(bt,st)
            print (fff)




    if __name__ == "__main__":
        #app.debug = True
        app.run(host="0.0.0.0",port= 5000)


  

  
  
