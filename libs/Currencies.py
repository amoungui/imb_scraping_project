import urllib3
import json

class ConverterCurrency:
    rates = {} # attribut that will containt the rate metric of api
    url = '' # atribut that will containt the url of the api

    def __init__(self):
        http = urllib3.PoolManager() # instantiation the http object
        self.url = 'http://data.fixer.io/api/latest?access_key=de2c3985561299c1a9e57b5d39ef21a9' #hydrate the api url
        request = http.request('GET', self.url) # get request of the api fixer.io
        data = json.loads(request.data.decode('utf8'))# load data to json 
        self.rates = data["rates"] # set the rate

    def convert(self, amount, from_currency, to_currency):
        """[summary]

        Args:
            amount (int or float): [amount that we want to convert]
            from_currency (str): the code of devise we want to convert
            to_currency (str): initial currency of the amount

        Returns:
            tuple: content of information about the convertion
        """
        initial_amount = amount # initialize the amount value
        if from_currency != "EUR": # verify if the current currency of the amount is not an euro
            amount = amount / self.rates[from_currency] # convert
        if to_currency == "EUR": # verify if the current currency of the amount is not an euro
            return initial_amount, from_currency, '=', amount, to_currency # return a tuple of the convertion
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
        if '$' not in item and 'xxx' not in item: # verify if item doesn't containt a $
            dict = {
                'code': item[0:3], # add the code of devise to the dictionnary
                'amount': round(float(item[3:].replace('.','')), 2) # format the amount and convert it in float add the amount 
            }
        if '$' in item:
            dict = {
                'code': 'USD', # we use the USD code by default
                'amount': round(float(item[1:].replace('.','')), 2) # format the amount and convert it in float add the amount
            }  
        if 'xxx' in item:
            dict = {
                'code': 'USD', # we use the USD code by default
                'amount': 0.0 # format the amount and convert it in float add the amount
            }              
        return self.convert(dict['amount'], dict['code'], "USD") # return value convert
    
    def current_convert(self, obj):
        """[summary]

        Args:
            obj (tuple): 

        Returns:
            [dictionnary]: 
        """
        a,b,c,d,e = (self.format_to_convert(obj)) # we get here the value of amount into the tuple
        return round(d, 2) # return the value of amount 
        
if __name__ == '__main__':

    converter = ConverterCurrency()
    d = {
        'm1' :'$25.000.000',
        'm2' :'INR15.000.000',
        'm3': 'xxx'
    }
    for key, value in d.items():
        print(converter.current_convert(value))