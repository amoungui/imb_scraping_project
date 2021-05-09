import requests
from bs4 import BeautifulSoup

from Managers.EntityManager import EntityManager

class MovieManager(EntityManager):
    def __init__(self, entity, tags:list):
        self.entity = entity
        self.gettitle(tags[1])
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
        
    ## @method getduration
    ## @param tag: a taget
    ## @return duration value
    def getduration(self, tag):
        try:
            r = tag.find('div', attrs={'class':'subtext'})
            return self.entity.__setduration__(r.find('time').text.strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setduration__(None)

    ## @method getrelease_date
    ## @param tag: a taget
    ## @return release date value
    def getrelease_date(self, tag):
        try:
            r = tag.find('div', attrs={'class':'subtext'})
            return self.entity.__setrelease_date__(r.find('a', attrs={'title': 'See more release dates'}).text.strip()[0:11])
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setrelease_date__(None)

    ## @method getrelease_country
    ## @param tag: a taget
    ## @return getrelease country value class="txt-block"
    def getrelease_country(self, tag):
        try:
            r = tag.find('div', attrs={'class':'subtext'})
            return self.entity.__setrelease_country__(r.find('a', attrs={'title': 'See more release dates'}).text.strip()[12:-1])
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setrelease_country__(None)

    ## @method getfilminglocation
    ## @param tag: a taget
    ## @return filming location value
    def getfilminglocation(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            if len(list) == 10:
                return self.entity.__setlocation__(list[4].find_all('a')[0].text.replace(',', ';').strip())
            else:
                return self.entity.__setlocation__(list[5].find_all('a')[0].text.replace(',', ';').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setlocation__(None)

    ## @method getbudget
    ## @param tag: a taget
    ## @return budget value
    def getbudget(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[6].split()
            return self.entity.__setbudget__(value[2].text[1:].replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setbudget__(None)

    ## @method getopening_weekend
    ## @param tag: a taget
    ## @return getopening weekend value
    def getopening_weekend(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[7].split()
            return self.entity.__setopening_weekend__(value[1].text.strip()[1:].replace(',', '').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setopening_weekend__(None)
        
    ## @method getgross_
    ## @param tag: a taget
    ## @return gross value
    def getgross_(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[8].split()
            return self.entity.__setworldwide_gross__(value[1].text.strip()[1:].replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setworldwide_gross__(None)

    ## @method getworldwide_gross
    ## @param tag: a taget
    ## @return worldwide gross value
    def getworldwide_gross(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            value = list[9].split()
            return self.entity.__setworldwide_gross__(value[1].text.strip()[1:].replace(',','').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setworldwide_gross__(None)

    ## @method getworldwide_gross
    ## @param tag: a taget
    ## @return worldwide gross value
    def getsoundmix(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            return self.entity.__setsound_mix__(list[13].text[11:].strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setsound_mix__(None)

    ## @method getcolor
    ## @param tag: a taget
    ## @return color value
    def getcolor(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            return self.entity.__setcolor__(list[14].text[7:].strip())#len(list)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setcolor__(None)

    ## @method getcolor
    ## @param tag: a taget
    ## @return color value
    def getaspect_ratio(self, tag):
        try:
            r = tag.find('div', attrs={'id':'titleDetails'}).find_all('div', attrs={'class':'txt-block'})
            list = [i for i in r]
            return self.entity.__setaspect_ratio__(list[15].text[14:].strip())#len(list)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setaspect_ratio__(None)

    ## @method getdirector
    ## @param tag: a taget
    ## @return director name
    def getdirector(self, tag):
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            return self.entity.__setdirector__(list[0].find('a').text.strip())#         
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdirector__(None)

    ## @method getwritter
    ## @param tag: a taget
    ## @return writter name
    def getwritter(self, tag):
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            return self.entity.__setwritter__(list[1].find('a').text.strip())#len(list)            
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setwritter__(None)

    ## @method getreview
    ## @param tag: a taget
    ## @return number of review
    def getreview(self, tag):
        try:
            r = tag.find('div', attrs={'class':'titleReviewBarItem titleReviewbarItemBorder'}).find('span', attrs={'class':'subText'})
            val = r.text.split()
            return  self.entity.__setreview__(val[0].strip().replace(',','').strip())            
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setreview__(None)

    ## @method getdirectorfilmographie
    ## @param tag: a taget
    ## @return list of director filmographie
    def getdirectorfilmographie(self, tag):
        array = []
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            resp = requests.get('https://www.imdb.com'+str(list[0].find('a')['href'])+'?ref_=tt_ov_dr')
            result = BeautifulSoup(resp.text, 'html.parser')
            s1 = result.find('div', attrs={'class': 'filmo-category-section'}).find_all('div', attrs={'class': 'filmo-row'})
            for i in s1:
                array.append(i.find('a').text.strip())
            return self.entity.__setdirectorfilmographie__(array)#      
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setdirectorfilmographie__(None)
          
    ## @method getwritterfilmographie
    ## @param tag: a taget
    ## @return list of writter filmographie
    def getwritterfilmographie(self, tag):
        array = []
        try:
            r = tag.find('div', attrs={'id':'title-overview-widget'}).find('div', attrs={'class':'plot_summary_wrapper'}).find_all('div', attrs={'class':'credit_summary_item'})
            list = [i for i in r]
            resp = requests.get('https://www.imdb.com'+str(list[1].find('a')['href'])+'?ref_=tt_ov_dr')
            result = BeautifulSoup(resp.text, 'html.parser')
            s1 = result.find('div', attrs={'class': 'filmo-category-section'}).find_all('div', attrs={'class': 'filmo-row'})
            for i in s1:
                array.append(i.find('a').text.strip())
            return self.entity.__setwritterfilmographie__(array)    
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setwritterfilmographie__(None)
                                
    ## @method getvote
    ## @param tag: a taget
    ## @return vote value
    def getvote(self, tag):
        try:
            return self.entity.__setvote__(tag.find('span', attrs={'name':'nv'}).text.replace(',','.').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setvote__(None)

    ## @method getrating
    ## @param tag: a taget
    ## @return rating(note) value
    def getrating(self, tag):
        try:
            return self.entity.__setrating__(tag.find('div', attrs={'class':'ratings-imdb-rating'}).find('strong').text.strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setrating__(None)

    ## @method getruntime
    ## @param tag: a taget
    ## @return runtime value
    def getruntime(self, tag):
        try:
            return self.entity.__setruntime__(tag.find('span', attrs={'class':'runtime'}).text.strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setruntime__(None)
        
    ## @method getgross
    ## @param tag: a taget
    ## @return Gross value
    def getgross(self, tag):
        try:
            return self.entity.__setgross__(tag.find('span', attrs={'data-value':'28,341,469'}).text.strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setgross__(None)    

    ## @method getfilmname
    ## @param tag: a taget
    ## @return name of film
    def gettitle(self, tag):
        try:
            return self.entity.__settitle__(tag.find('h3', attrs={'class':'lister-item-header'}).find('a').text.strip())
            #return self.entity.__settitle__(tag.find('div', attrs={'class':'title_wrapper'}).find('h1', attrs={'class':''}).text)
        except (TypeError, AttributeError, IndexError):
            return self.entity.__settitle__(None)

    ## @method gettype
    ## @param tag: a taget
    ## @return type of film
    def gettype(self, tag):
        try:
            return self.entity.__settype__(tag.find('span', attrs={'class':'genre'}).text[1:16].replace(',',';').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__settype__(None)

    ## @method getscore
    ## @param tag: a taget
    ## @return film metascore
    def getscore(self, tag):
        try:
            return self.entity.__setscore__(tag.find('span', attrs={'class':'metascore'}).text.replace(',', '').strip())
        except (TypeError, AttributeError, IndexError):
            return self.entity.__setscore__(None)
         
    ## @method getlink
    ## @param tag: a taget
    ## @return link of single page
    def getlink(self, tag):
        target = tag.find('h3', attrs={'class':'lister-item-header'})
        a = target.find('a')
        _link = a['href']
        return _link

    ## @method _setlink
    ## @param tag: a taget
    ## @return link of single page
    def _setlink(self, url):
        return 'https://www.imdb.com/'+ str(url)+'?ref_=adv_li_tt'

    ## @method _setlink
    ## @param tag: a taget
    ## @return link of single page
    def paginate(self, index):
        return 'https://www.imdb.com/search/title/?title_type=feature&num_votes=5000,&sort=user_rating,desc&start='+ str(index)+'&ref_=adv_nxt'

    ## here is the request into the single page of movie
    ## @method getlink
    ## @param tag: a taget
    ## @return link of single page
    def getlink(self, tag):
        target = tag.find('h3', attrs={'class':'lister-item-header'})
        a = target.find('a')
        _link = a['href']
        return _link

    ## end of the request into the single page of movie
