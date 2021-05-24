import urllib3
import json

class ConverterCurrency:

    rates = {}
    url = ''

    def __init__(self):
        http = urllib3.PoolManager()
        self.url = 'http://data.fixer.io/api/latest?access_key=d572ecd6085f71e5427175b2f0239678'
        request = http.request('GET', self.url)
        data = json.loads(request.data.decode('utf8'))
        self.rates = data["rates"]

    def convert(self, amount, from_currency, to_currency):
        """[summary]

        Args:
            amount (int or float): [amount that we want to convert]
            from_currency (str): the code of devise we want to convert
            to_currency (str): initial currency of the amount

        Returns:
            tuple: content of information about the convertion
        """
        initial_amount = amount
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR":
            return initial_amount, from_currency, '=', amount, to_currency
        else:
            return initial_amount, from_currency, '=', amount * self.rates[to_currency], to_currency

    def format_to_convert(self, item):
        """[summary: extract the the amount value and the code of devise]

        Args:
            item (str): description

        Returns:
            [dictionnary]: that contain the currency code and the amount
        """
        dict = {}
        if '$' not in item:
            dict = {
                'code': item[0:3],
                'amount': round(float(item[3:].replace('.','')), 2)
            }
        if '$' in item:
            dict = {
                'code': 'USD',
                'amount': round(float(item[1:].replace('.','')), 2)
            }  
            #init_current, code, eq, amount, usd = self.convert(dict['amount'], dict['code'], "USD")
        return self.convert(dict['amount'], dict['code'], "USD")
    
    def current_convert(self, obj):
        """[summary]

        Args:
            obj (tuple): 

        Returns:
            [dictionnary]: 
        """
        a,b,c,d,e = (self.format_to_convert(obj))
        return round(d, 2)
        

if __name__ == '__main__':

    converter = ConverterCurrency()
    d = {
        'm1' :'$25.000.000',
        'm2' :'INR15.000.000'
    }
    for key, value in d.items():
        print(converter.current_convert(value))