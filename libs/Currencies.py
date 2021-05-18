import urllib3
import json

class ConverterCurrency:

    rates = {}
    url = ''

    def __init__(self):
        http = urllib3.PoolManager()
        self.url = 'http://data.fixer.io/api/latest?access_key=199ff8d0cee4c477b2c1a44656e07e55'
        request = http.request('GET', self.url)
        data = json.loads(request.data.decode('utf8'))
        self.rates = data["rates"]

    def convert(self, amount, from_currency, to_currency):
        """[summary]

        Args:
            amount ([type]): [description]
            from_currency ([type]): [description]
            to_currency ([type]): [description]

        Returns:
            [type]: [description]
        """
        initial_amount = amount
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR":
            return initial_amount, from_currency, '=', amount, to_currency
        else:
            return initial_amount, from_currency, '=', amount * self.rates[to_currency], to_currency

    def format_to_convert(self, item):
        """[summary]

        Args:
            item (str): description

        Returns:
            [dictionnary]: that contain the currency code and the amount
        """
        dict = {}
        if '$' not in item:
            dict = {
                'code': item[0:3],
                'amount': float(item[3:].replace('.',''))
            }
        if '$' in item:
            dict = {
                'code': 'USD',
                'amount': float(item[3:].replace('.',''))
            }  
            init_current, code, eq, amount, usd = self.convert(dict['amount'], dict['code'], "USD")
        return self.convert(dict['amount'], dict['code'], "USD")
    
    def current_convert(self, obj):
        a,b,c,d,e = (self.format_to_convert(obj))
        return d
        

if __name__ == '__main__':

    converter = ConverterCurrency()
    m1 = 'BDT35.000.000'
    m2 = 'INR15.000.000'

    print(converter.current_convert(m1))