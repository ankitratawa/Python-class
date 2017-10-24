from flask import Flask, render_template
import urllib.request 
import json

app = Flask(__name__)


@app.route('/')
def index():

    response        = urllib.request.urlopen
('http://api.fixer.io/latest?base=USD')
    data  = json.load(response)

    currency_data         = data["base"]
    country_currency          = data["country_currency"]
    currency_records = []

    for currency in currency_index:
        record_tuple = (country_currency, currency["dates"], currency["rates"])
        currency_records.append(record_tuple)

    return render_template('index.html', records=currency_records)


if __name__ == '__main__':
    # Starts the Flask application server
    app.run(debug=True)
