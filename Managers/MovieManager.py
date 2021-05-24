from Managers.EntityManager import EntityManager
from libs.Currencies import ConverterCurrency

class MovieManager(EntityManager):
    def __init__(self, entity, tags:list):
        self.entity = entity
        self.getfilmname(tags[1])
        self.getvote(tags[1])
        self.getrating(tags[1])
        self.getscore(tags[1])
        self.gettype(tags[1])
        self.getruntime(tags[1])
        self.getgross(tags[0])
        #self.getgross(tags[1])
        self.getduration(tags[0])
        self.getrelease_date(tags[0])
        self.getrelease_country(tags[0])
        self.getfilminglocation(tags[0])
        self.getbudget(tags[0])
        self.getopening_weekend(tags[0])
        self.getworldwide_gross(tags[0])
        self.getsoundmix(tags[0])
        self.getcolor(tags[0])
        self.getaspect_ratio(tags[0])
        self.getdirector(tags[0])
        self.getwritter(tags[0])
        self.getreview(tags[0])
        self.getstoryline(tags[0])
        
    def getduration(self, tag):
        """ @method getduration
            @param tag: a taget
            @description hydrate the value of duration entity  
        """                     
        try:
            r = tag.find('div', attrs={'class':'subtext'})
            self.entity.__setduration__(r.find('time').text.strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setduration__(None)

    def getrelease_date(self, tag):
        """ @method getrelease_date
            @param tag: a taget
            @description hydrate the value of release entity  
        """                             
        try:
            r = tag.find('div', attrs={'class':'subtext'})
            date = r.find('a', attrs={'title': 'See more release dates'}).text.strip()[0:]
            self.entity.__setrelease_date__(self.formate_date(self.strip_date(date)))
        except (TypeError, AttributeError, IndexError):
            self.entity.__setrelease_date__(None)

    def getrelease_country(self, tag):
        """ @method getrelease_country
            @param tag: a taget
            @description hydrate the value of getrelease country entity  
        """   
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = []
            for elem in r:
                if 'Country:' in elem.find('h4', attrs={'class': 'inline'}).text:
                    list = elem.text.replace(':', ' ').split()
                    return self.entity.__setrelease_country__(list[-1].strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setrelease_country__(None)                                          

    def getfilminglocation(self, tag):
        """ @method getfilminglocation
            @param tag: a taget
            @description hydrate the value of filming location entity  
        """                                     
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            if len(list) == 10:
                self.entity.__setlocation__(list[4].find_all('a')[0].text.replace(',', ';').strip())
            else:
                self.entity.__setlocation__(list[5].find_all('a')[0].text.replace(',', ';').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setlocation__(None)

    def getbudget(self, tag):
        """ @method getbudget
            @param tag: a taget
            @description hydrate the value of budget entity  
        """           
        converter = ConverterCurrency()  
        amount = ''                             
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = []
            for elem in r:
                if elem.find('h4', attrs={'class': 'inline'}).text[:-1] == 'Budget':
                    list = elem.text.replace(':', ' ').split() # replace('BDT', ' ').replace('INR', ' ')
                    amount = ''+ list[1].replace(',','.').strip()
                    return self.entity.__setbudget__(converter.current_convert(amount)) # .replace('$', '')
        except (TypeError, AttributeError, IndexError):
            self.entity.__setbudget__(None)

    def getopening_weekend(self, tag):
        """ @method getopening_weekend
            @param tag: a taget
            @description hydrate the value of getopening weekend entity  
        """                                          
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = []
            for elem in r:
                if 'Opening Weekend' in elem.find('h4', attrs={'class': 'inline'}).text[:-1]:
                    list = elem.text.replace(':', ' ').replace('USA','').split()
                    return self.entity.__setopening_weekend__(list[2].replace('$','').replace(',','').strip()[:-1])
        except (TypeError, AttributeError, IndexError):
            self.entity.__setopening_weekend__(None)
        
    def getgross(self, tag):
        """ @method getgross_
            @param tag: a taget
            @description hydrate the value of getgross entity  
        """                                                  
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = []
            for elem in r:
                if 'Gross' in elem.find('h4', attrs={'class': 'inline'}).text:
                    list = elem.text.replace(':', ' ').replace('USA','').split()
                    return self.entity.__setgross__(list[-1].replace('$','').replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setgross__(None)

    def getworldwide_gross(self, tag):
        """ @method getworldwide_gross
            @param tag: a taget
            @description hydrate the value of worldwide gross entity  
        """        
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = []
            for elem in r:
                if 'Cumulative Worldwide' in elem.find('h4', attrs={'class': 'inline'}).text:
                    list = elem.text.replace(':', ' ').replace('USA','').split()
                    return self.entity.__setworldwide_gross__(list[-1].replace('$','').replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setworldwide_gross__(None)

    def getsoundmix(self, tag):
        """ @method getsoundmix
            @param tag: a taget
            @description hydrate the value of worldwide gross entity  
        """                
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            self.entity.__setsound_mix__(list[13].text[11:].strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setsound_mix__(None)

    def getcolor(self, tag):
        """ @method getcolor
            @param tag: a taget
            @description hydrate the value of color entity  
        """                        
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            self.entity.__setcolor__(list[14].text[7:].strip())#len(list)
        except (TypeError, AttributeError, IndexError):
            self.entity.__setcolor__(None)

    def getaspect_ratio(self, tag):
        """ @method getaspect_ratio
            @param tag: a taget
            @description hydrate the value of aspect_ratio entity  
        """                                
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            self.entity.__setaspect_ratio__(list[15].text[14:].strip())#len(list)
        except (TypeError, AttributeError, IndexError):
            self.entity.__setaspect_ratio__(None)

    def getdirector(self, tag):
        """ @method getdirector
            @param tag: a taget
            @description hydrate the value of director name entity  
        """                                        
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            self.entity.__setdirector__(list[0].find('a').text.strip())#         
        except (TypeError, AttributeError, IndexError):
            self.entity.__setdirector__(None)

    def getwritter(self, tag):
        """ @method getwritter
            @param tag: a taget
            @description hydrate the value of writter name entity  
        """                                          
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            self.entity.__setwritter__(list[1].find('a').text.strip())#len(list)            
        except (TypeError, AttributeError, IndexError):
            self.entity.__setwritter__(None)

    def getreview(self, tag):
        """ @method getreview
            @param tag: a taget
            @description hydrate the value of number of review entity  
        """                       
        try:
            r = tag.find('div', attrs={'class':'titleReviewBarItem titleReviewbarItemBorder'}).find('span', attrs={'class':'subText'})
            val = r.text.split()
            self.entity.__setreview__(val[0].strip().replace(',','').strip())            
        except (TypeError, AttributeError, IndexError):
            self.entity.__setreview__(None)

    def getstoryline(self, tag):
        """ @method getstoryline
            @param tag: a taget
            @description hydrate the value of storyline of movie entity  
        """                               
        array = []
        try:
            r = tag.find('div', attrs={'id':'titleStoryLine'}).find('div', attrs={'class':'inline canwrap'})
#            list = [i for i in r]
#            resp = requests.get('https://www.imdb.com'+str(list[0].find('a')['href'])+'?ref_=tt_ov_dr')
#            result = BeautifulSoup(resp.text, 'html.parser')
#            s1 = result.find('div', attrs={'class': 'filmo-category-section'}).find_all('div', attrs={'class': 'filmo-row'})
#           for i in s1:
            self.entity.__setstoryline__ (r.find('span').text.strip())     
        except (TypeError, AttributeError, IndexError):
            self.entity.__setstoryline__(None)
                                          
    def getvote(self, tag):
        """ @method getvote
            @param tag: a taget
            @description hydrate the value of vote entity  
        """         
        try:
            self.entity.__setvote__(tag.find('span', attrs={'name':'nv'}).text.replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setvote__(None)

    def getrating(self, tag):
        """ @method getrating
            @param tag: a taget
            @description hydrate the value of rating(note) entity  
        """                 
        try:
            self.entity.__setrating__(tag.find('div', attrs={'class':'ratings-imdb-rating'}).find('strong').text.strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setrating__(None)

    def getruntime(self, tag):
        """ @method getruntime
            @param tag: a taget
            @description hydrate the value of runtime entity  
        """                 
        try:
            self.entity.__setruntime__(tag.find('span', attrs={'class':'runtime'}).text.strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setruntime__(None)
        
    def getgross__(self, tag):
        """ @method getgross
            @param tag: a taget
            @description hydrate the value of Gross of the movie entity  
        """             
        """try:
            self.entity.__setgross__(tag.find('span', attrs={'data-value':'28,341,469'}).text.strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setgross__(None) """
        pass   

    def getfilmname(self, tag):
        """ @method getgross
            @param tag: a taget
            @description hydrate the name of film entity  
        """                     
        try:
            self.entity.__settitle__(tag.find('h3', attrs={'class':'lister-item-header'}).find('a').text.strip())
            #return self.entity.__settitle__(tag.find('div', attrs={'class':'title_wrapper'}).find('h1', attrs={'class':''}).text)
        except (TypeError, AttributeError, IndexError):
            self.entity.__settitle__(None)

    def gettype(self, tag):
        """ @method gettype
            @param tag: a taget
            @description hydrate the type of film entity  
        """         
        try:
            self.entity.__settype__(tag.find('span', attrs={'class':'genre'}).text[1:16].replace(',',';').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__settype__(None)

    def getscore(self, tag):
        """ @method getscore
            @param tag: a taget
            @description hydrate the value of film metascore entity  
        """                 
        try:
            self.entity.__setscore__(tag.find('span', attrs={'class':'metascore'}).text.replace(',', '').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setscore__(None)
         
    def convert_to_dollar(self, unit, amount):
        """ @method convert_to_dollar
            @param tag: a taget
            @description conversion the amount to dollar US  
        """                         
        if unit == 'BDT':
            amount = 0.012*amount
        if unit == 'INR':
            amount = 0.014*amount
        return amount
    
    def formate_budget(self, tag):
        """ @method formate_budget
            @param tag: a taget
            @description format the amount
        """       
        if 'BDT' in tag:
            b = tag[3:]
            return self.convert_to_dollarconvert_to_dollar('BDT', int(b))
        if 'INR' in tag:
            b = tag[4:]
            return self.convert_to_dollar('INR', int(b))
                             