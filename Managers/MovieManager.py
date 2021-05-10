import requests
from bs4 import BeautifulSoup

from Managers.EntityManager import EntityManager

class MovieManager(EntityManager):
    def __init__(self, entity, tags:list):
        self.entity = entity
        self.getfilmname(tags[1])
        self.getvote(tags[1])
        self.getrating(tags[1])
        self.getscore(tags[1])
        self.gettype(tags[1])
        self.getruntime(tags[1])
        self.getgross(tags[1])
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
        self.getdirectorfilmographie(tags[0])
        self.getwritterfilmographie(tags[0])
        
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
            self.entity.__setrelease_date__(r.find('a', attrs={'title': 'See more release dates'}).text.strip()[0:11])
        except (TypeError, AttributeError, IndexError):
            self.entity.__setrelease_date__(None)

    def getrelease_country(self, tag):
        """ @method getrelease_country
            @param tag: a taget
            @description hydrate the value of getrelease country entity  
        """                                     
        try:
            r = tag.find('div', attrs={'class':'subtext'})
            self.entity.__setrelease_country__(r.find('a', attrs={'title': 'See more release dates'}).text.strip()[12:-1])
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
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[6].split()
            self.entity.__setbudget__(value[2].text[1:].replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setbudget__(None)

    def getopening_weekend(self, tag):
        """ @method getopening_weekend
            @param tag: a taget
            @description hydrate the value of getopening weekend entity  
        """                                          
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[7].split()
            self.entity.__setopening_weekend__(value[1].text.strip()[1:].replace(',', '').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setopening_weekend__(None)
        
    def getgross_(self, tag):
        """ @method getgross_
            @param tag: a taget
            @description hydrate the value of getgross entity  
        """                                                  
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[8].split()
            self.entity.__setworldwide_gross__(value[1].text.strip()[1:].replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setworldwide_gross__(None)

    def getworldwide_gross(self, tag):
        """ @method getworldwide_gross
            @param tag: a taget
            @description hydrate the value of worldwide gross entity  
        """        
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[9].split()
            self.entity.__setworldwide_gross__(value[1].text.strip()[1:].replace(',','').strip())
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

    def getdirectorfilmographie(self, tag):
        """ @method getdirectorfilmographie
            @param tag: a taget
            @description hydrate the value of list of director filmographie entity  
        """                               
        array = []
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            resp = requests.get('https://www.imdb.com'+str(list[0].find('a')['href'])+'?ref_=tt_ov_dr')
            result = BeautifulSoup(resp.text, 'html.parser')
            s1 = result.find('div', attrs={'class': 'filmo-category-section'}).find_all('div', attrs={'class': 'filmo-row'})
            for i in s1:
                array.append(i.find('a').text.strip())
            self.entity.__setdirectorfilmographie__(array)#      
        except (TypeError, AttributeError, IndexError):
            self.entity.__setdirectorfilmographie__(None)
          
    def getwritterfilmographie(self, tag):
        """ @method getwritterfilmographie
            @param tag: a taget
            @description hydrate the value of writter filmographie entity  
        """         
        array = []
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            resp = requests.get('https://www.imdb.com'+str(list[1].find('a')['href'])+'?ref_=tt_ov_dr')
            result = BeautifulSoup(resp.text, 'html.parser')
            s1 = result.find('div', attrs={'class': 'filmo-category-section'}).find_all('div', attrs={'class': 'filmo-row'})
            for i in s1:
                array.append(i.find('a').text.strip())
            self.entity.__setwritterfilmographie__(array)    
        except (TypeError, AttributeError, IndexError):
            self.entity.__setwritterfilmographie__(None)
                                
    def getvote(self, tag):
        """ @method getvote
            @param tag: a taget
            @description hydrate the value of vote entity  
        """         
        try:
            self.entity.__setvote__(tag.find('span', attrs={'name':'nv'}).text.replace(',','.').strip())
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
        
    def getgross(self, tag):
        """ @method getgross
            @param tag: a taget
            @description hydrate the value of Gross entity  
        """             
        try:
            self.entity.__setgross__(tag.find('span', attrs={'data-value':'28,341,469'}).text.strip())
        except (TypeError, AttributeError, IndexError):
            self.entity.__setgross__(None)    

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
         
    def getlink(self, tag):
        """ @method getlink
            @param tag: a taget
            @return link of single page
            @description find the specific target where is the liste of movie  
        """                       
        target = tag.find('h3', attrs={'class':'lister-item-header'})
        a = target.find('a')
        _link = a['href']
        return _link


    def _setlink(self, url):
        """
            ## @method _setlink
            ## @param tag: a taget
            ## @return link of single page
        """
        return 'https://www.imdb.com/'+ str(url)+'?ref_=adv_li_tt'


    def paginate(self, index):
        """
            ## @method _setlink
            ## @param tag: a taget
            ## @return link of single page
        """        
        return 'https://www.imdb.com/search/title/?title_type=feature&num_votes=5000,&sort=user_rating,desc&start='+ str(index)+'&ref_=adv_nxt'

    def getlink(self, tag):
        """ 
            ## here is the request into the single page of movie
            ## @method getlink
            ## @param tag: a taget
            ## @return link of single page
        """        
        target = tag.find('h3', attrs={'class':'lister-item-header'})
        a = target.find('a')
        _link = a['href']
        return _link