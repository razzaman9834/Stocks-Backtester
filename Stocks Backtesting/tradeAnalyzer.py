from flask import Flask, render_template, request
from nsetools import Nse
import time

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/result', methods=['POST'])
def result():
    url = request.form.get('url') #STOCK 
    var_2 = request.form.get("var_2", type=int) #QTY
    var_3 = request.form.get("var_3", type=int)  #MIN
    operation = request.form.get("operation")
    if(operation == 'LONG'):
      nse = Nse()
      q = nse.get_quote(url)
      ltp = q.get("lastPrice")
      Quant = int(var_2)
      trade=Quant*ltp
      timing=float(var_3)
      tms=timing*60
      time.sleep(tms)
      st = nse.get_quote(url)
      ltpUP = st.get("lastPrice")
      result=(ltpUP*Quant)-trade
    elif(operation == 'SHORT'):
      nse = Nse()
      q = nse.get_quote(url)
      ltp = q.get("lastPrice")
      Quant = int(var_2)
      trade=Quant*ltp
      timing=float(var_3)
      tms=timing*60
      time.sleep(tms)
      st = nse.get_quote(url)
      ltpUP = st.get("lastPrice")
      result=(trade-(ltpUP*Quant))
        
    else:
        result = 'INVALID CHOICE'
    entry = result
    ltpN=ltp
    ltpUPN=ltpUP
    timingN=timing
    return render_template('result.html', entry=entry,ltpN=ltpN,ltpUPN=ltpUPN,timingN=timingN)

if __name__ == '__main__':
    app.run(debug=True)

  