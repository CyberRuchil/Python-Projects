from flask import Flask,render_template, request
import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ['API_KEY']

endpoint1 = "http://api.marketstack.com/v2/tickerslist"
endpoint2 = "http://api.marketstack.com/v2/eod/latest"

def stock_data(stock_name):
    '''
    This function returns the EOD data for a stock.

    Parameters
    ----------
    stock_name : The name of the stock for which we want eod data.

    Returns
    -------
    out : returns lists of dictionary of eod data for the stock.
    '''

    exchange = 'XNSE'
    symbol_params = {
        'access_key' : API_KEY,
        'exchange' : exchange,
        'search': stock_name,
    }

    symbol_response = requests.get(url=endpoint1, params=symbol_params)
    symbol_data = symbol_response.json()
    stock_symbol = symbol_data['data'][0]['ticker']

    params = {
        'access_key' : API_KEY,
        'exchange' : exchange,
        'symbols': stock_symbol,
    }

    response = requests.get(url=endpoint2, params=params)
    data = response.json()
    return data['data']


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    data = None
    if request.method == 'POST':
        stock_name = request.form['stock-name']
        try:
            data = stock_data(stock_name)
        except:
            data = None
    return render_template('index.html', stock_data=data)


if __name__ == '__main__':
    app.run(debug=True)