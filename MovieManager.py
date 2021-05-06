import requests
from bs4 import BeautifulSoup

from EntityManager import EntityManager

class MovieManager(EntityManager):
    def __init__(self, entity, tags:list):
        self.entity = entity
        self.gettitle(tags[0])
        self.getvote(tags[1])
        self.getrating(tags[1])
        self.getscore(tags[1])
    
    ## @method getvote
    ## @param tag: a taget
    ## @return vote value
    def getvote(self, tag):
        try:
            return self.entity.__setvote__(tag.find('span', attrs={'name':'nv'}).text)
        except (TypeError, AttributeError):
            return self.entity.__setscore__(None)

    ## @method getrating
    ## @param tag: a taget
    ## @return rating(note) value
    def getrating(self, tag):
        try:
            return self.entity.__setrating__(tag.find('div', attrs={'class':'ratings-imdb-rating'}).find('strong').text)
        except (TypeError, AttributeError):
            return self.entity.__setscore__(None)

    ## @method getruntime
    ## @param tag: a taget
    ## @return runtime value
    def getruntime(self, tag):
        try:
            return self.entity.__setruntime__(tag.find('span', attrs={'class':'runtime'}).text)
        except (TypeError, AttributeError):
            return self.entity.__setscore__(None)
    ## @method getgross
    ## @param tag: a taget
    ## @return Gross value
    def getgross(self, tag):
        try:
            return self.entity.__setgross__(tag.find('span', attrs={'data-value':'28,341,469'}).text)
        except (TypeError, AttributeError):
            return self.entity.__setscore__(None)    

    ## @method getfilmname
    ## @param tag: a taget
    ## @return name of film
    def gettitle(self, tag):
        try:
            return self.entity.__setscore__(tag.find('div', attrs={'class':'title_wrapper'}).find('h1', attrs={'class':''}).text)
        except (TypeError, AttributeError):
            return self.entity.__setscore__(None)

    ## @method gettype
    ## @param tag: a taget
    ## @return type of film
    def gettype(self, tag):
        try:
            return self.entity.__settype__(tag.find('span', attrs={'class':'genre'}).text)
        except (TypeError, AttributeError):
            return self.entity.__setscore__(None)

    ## @method getscore
    ## @param tag: a taget
    ## @return film metascore
    def getscore(self, tag):
        try:
            return self.entity.__setscore__(tag.find('span', attrs={'class':'metascore'}).text)
        except (TypeError, AttributeError):
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
