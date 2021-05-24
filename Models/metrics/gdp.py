#! /usr/bin/env python3
# coding: utf-8

class Metric:
    def __init__(self):
        self.country = ''
        self.year_2018 = ''
        self.year_2017 = ''
        self.year_2016 = ''
        self.year_2015 = ''
        self.year_2014 = ''

    def __getcountry__(self):
        """ @method __getcountry__
            @param None: 
            @return country value
            @description get of the country entity 
        """                
        return self.country 
    
    def __gdp_2018__(self):
        """ @method __year_2018__
            @param None: 
            @return gross value
            @description  
        """                
        return self.year_2018    
    
    def __gdp_2017__(self):
        """ @method __year_2017__
            @param None: 
            @return gross value
            @description  
        """                
        return self.year_2017    
    
    def __gdp_2016__(self):
        """ @method __year_2016__
            @param None: 
            @return gross value
            @description  
        """                
        return self.year_2016       
    
    def __gdp_2015__(self):
        """ @method __year_2015__
            @param None: 
            @return gross value
            @description  
        """                
        return self.year_2015       
    
    def __gdp_2014__(self):
        """ @method __year_2014__
            @param None: 
            @return gross value
            @description  
        """                
        return self.year_2014    
    
    ## setter
    def __setcountry__(self, tag):
        """ @method __setcountry__
            @param tag: 
            @return None
            @description set of the metric entity 
        """                 
        if tag is not None:
            self.country = tag
        else: 
            self.country = 'xxx'     
    
    def __setgdp_2018__(self, tag):
        """ @method __setcountry__
            @param tag: 
            @return None
            @description set of the metric entity 
        """                 
        if tag is not None:
            self.year_2018 = tag
        else: 
            self.year_2018 = 'xxx'     
    
    def __setgdp_2017__(self, tag):
        """ @method __setyear_2017__
            @param tag: 
            @return None
            @description set of the metric entity 
        """                 
        if tag is not None:
            self.year_2017 = tag
        else: 
            self.year_2017 = 'xxx'  
            
    def __setgdp_2016__(self, tag):
        """ @method __setyear_2016__
            @param tag: 
            @return None
            @description set of the metric entity 
        """                 
        if tag is not None:
            self.year_2016 = tag
        else: 
            self.year_2016 = 'xxx'     
            
    def __setgdp_2015__(self, tag):
        """ @method __setyear_2015__
            @param tag: 
            @return None
            @description set of the metric entity 
        """                 
        if tag is not None:
            self.year_2015 = tag
        else: 
            self.year_2015 = 'xxx'             
            
    def __setgdp_2014__(self, tag):
        """ @method __setyear_2014__
            @param tag: 
            @return None
            @description set of the metric entity 
        """                 
        if tag is not None:
            self.year_2014 = tag
        else: 
            self.year_2014 = 'xxx'             