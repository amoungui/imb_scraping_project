#! /usr/bin/env python3
# coding: utf-8

class Movie:
    def __init__(self):
        self.title = ''
        self.rating = ''
        self.score = ''
        self.vote = ''
        self.director = ''
        self.writter = ''
        self.duration = ''
        self.release_date = ''
        self.release_country = ''
        self.country = ''
        self.location = ''
        self.review = ''
        self.storyline = ''
        self.budget = ''
        self.opening_weekend = ''
        self.gross = ''
        self.worldwide_gross = ''
        self.runtime = ''
        self.sound_mix = ''
        self.color = ''
        self.aspect_ratio = ''
    
    def __gettitle__(self):
        """ @method __gettitle__
            @param None: 
            @return title value
            @description get of the moive entity 
        """                
        return self.title 
    
    def __getrating__(self):
        """ @method __getrating__
            @param None: 
            @return rating value
            @description get of the moive entity 
        """                        
        return self.rating

    def __getscore__(self):
        """ @method __getscore__
            @param None: 
            @return score value
            @description get of the moive entity 
        """         
        return self.score
    
    def __getvote__(self):
        """ @method __getvote__
            @param None: 
            @return vote value
            @description get of the moive entity 
        """                 
        return self.vote    
    
    def __gettype__(self):
        """ @method __gettype__
            @param None: 
            @return type value
            @description get of the moive entity 
        """                         
        return self.type
    
    def __getdirector__(self):
        """ @method __getdirector__
            @param None: 
            @return director value
            @description get of the moive entity 
        """                         
        return self.director   
    
    def __getwritter__(self):
        """ @method __getwritter__
            @param None: 
            @return writter value
            @description get of the moive entity 
        """                         
        return self.writter
    
    def __getduration__(self):
        """ @method __getduration__
            @param None: 
            @return duration value
            @description get of the moive entity 
        """                 
        return self.duration
    
    def __getrelease_date__(self):
        """ @method __getrelease_date__
            @param None: 
            @return release date value
            @description get of the moive entity 
        """                 
        return self.release_date
 
    def __getrelease_country__(self):
        """ @method __getrelease_country__
            @param None: 
            @return release country value
            @description get of the moive entity 
        """                         
        return self.release_country   
    
    def __getcountry__(self):
        """ @method __getcountry__
            @param None: 
            @return country value
            @description get of the moive entity 
        """                                 
        return self.country
    
    def __getlocation__(self):
        """ @method __getlocation__
            @param None: 
            @return location value
            @description get of the moive entity 
        """                              
        return self.location
    
    def __getreview__(self):
        """ @method __getreview__
            @param None: 
            @return review value
            @description get of the moive entity 
        """                 
        return self.review
    
    def __getstoryline__(self):
        """ @method __getstoryline__
            @param None: 
            @return writter filmographie value
            @description get the storyline of movie entity 
        """                         
        return self.storyline
            
    def __getbudget__(self):
        """ @method __getbudget__
            @param None: 
            @return budget value
            @description get of the moive entity 
        """                 
        return self.budget
    
    def __getopening_weekend__(self):
        """ @method __getopening_weekend__
            @param None: 
            @return opening weekend value
            @description get of the moive entity 
        """                 
        return self.opening_weekend
    
    def __getgross__(self):
        """ @method __getgross__
            @param None: 
            @return gross value
            @description get of the moive entity 
        """                 
        return self.gross
    
    def __getworldwide_gross__(self):
        """ @method __getworldwide_gross__
            @param None: 
            @return worldwide gross value
            @description get of the moive entity 
        """                 
        return self.worldwide_gross
    
    def __getruntime__(self):
        """ @method __getruntime__
            @param None: 
            @return runtime value
            @description get of the moive entity 
        """                 
        return self.runtime
    
    def __getsound_mix__(self):
        """ @method __getsound_mix__
            @param None: 
            @return sound mix value
            @description get of the moive entity 
        """                 
        return self.sound_mix
    
    def __getcolor__(self):
        """ @method __getcolor__
            @param None: 
            @return color value
            @description get of the moive entity 
        """                 
        return self.color
    
    def __getaspect_ratio__(self):
        """ @method __getaspect_ratio__
            @param None: 
            @return aspect ratio value
            @description get of the moive entity 
        """                 
        return self.aspect_ratio
    
    ## setter
    def __settitle__(self, tag):
        """ @method __settitle__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                 
        if tag is not None:
            self.title = tag
        else: 
            self.title = 'xxx' 
    
    def __setrating__(self, tag):
        """ @method __setrating__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                         
        if tag is not None:
            self.rating = tag
        else:
            self.rating = 'xxx'

    def __setscore__(self, tag):
        """ @method __setscore__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                        
        if tag is not None:
            self.score = tag
        else:
            self.score = 'xxx'
    
    def __setvote__(self, tag):
        """ @method __setvote__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                             
        if tag is not None:
            self.vote = tag
        else:
            self.vote = 'xxx'   
    
    def __settype__(self, tag):
        """ @method __settype__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                            
        if tag is not None:
            self.type = tag
        else:
            self.type = 'xxx'
    
    def __setdirector__(self, tag):
        """ @method __setdirector__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                            
        if tag is not None:
            self.director = tag 
        else:
            self.director = 'xxx' 
    
    def __setwritter__(self, tag):
        """ @method __setwritter__
            @param tag: 
            @return None
            @description set of the moive entity 
        """              
        if tag is not None:
            self.writter = tag
        else:
            self.writter = 'xxx'
    
    def __setduration__(self, tag):
        """ @method __setduration__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                      
        if tag is not None:
            self.duration = tag
        else:
            self.duration = 'xxx'
    
    def __setrelease_date__(self, tag):
        """ @method __setrelease_date__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                        
        if tag is not None:
            self.release_date = tag
        else:
            self.release_date = 'xxx'
    
    def __setrelease_country__(self, tag):
        """ @method __setrelease_country__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                                
        if tag is not None:
            self.release_country = tag
        else:
            self.release_country = 'xxx'
                
    def __setcountry__(self, tag):
        """ @method __setcountry__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                     
        if tag is not None:
            self.country = tag
        else:
            self.country = 'xxx'
    
    def __setlocation__(self, tag):
        """ @method __setlocation__
            @param tag: 
            @return None
            @description set of the moive entity 
        """             
        if tag is not None:
            self.location = tag
        else:
            self.location = 'xxx'
    
    def __setreview__(self, tag):
        """ @method __setreview__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                     
        if tag is not None:
            self.review = tag
        else: 
            self.review = 'xxx'
    
    def __setstoryline__(self, tag):
        """ @method __setstoryline__
            @param tag: 
            @return None
            @description set the storyline of moive entity 
        """                             
        if tag is not None:
            self.storyline = tag
        else: 
            self.storyline = 'xxx'
        
    def __setbudget__(self, tag):
        """ @method __setbudget__
            @param tag: 
            @return None
            @description set of the moive entity 
        """         
        if tag is not None:
            self.budget = tag
        else:
            self.budget = 'xxx'
    
    def __setopening_weekend__(self, tag):
        """ @method __setopening_weekend__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                 
        if tag is not None:
            self.opening_weekend = tag
        else:
            self.opening_weekend = 'xxx'
            
    def __setgross__(self, tag):
        """ @method __setgross__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                       
        if tag is not None:
            self.gross = tag
        else: 
            self.gross = 'xxx'
    
    def __setworldwide_gross__(self, tag):
        """ @method __setworldwide_gross__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                               
        if tag is not None:
            self.worldwide_gross = tag
        else:
            self.worldwide_gross = 'xxx'
    
    def __setruntime__(self, tag):
        """ @method __setruntime__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                                  
        if tag is not None:
            self.runtime = tag
        else:
            self.runtime = 'xxx'
    
    def __setsound_mix__(self, tag):
        """ @method __setsound_mix__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                
        if tag is not None:
            self.sound_mix = tag
        else:
            self.sound_mix = 'xxx'
    
    def __setcolor__(self, tag):
        """ @method __setcolor__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                 
        if tag is not None:
            self.color = tag
        else:
            self.color = 'xxx'
    
    def __setaspect_ratio__(self, tag):
        """ @method __setaspect_ratio__
            @param tag: 
            @return None
            @description set of the moive entity 
        """                         
        if tag is not None:
            self.aspect_ratio = tag
        else:
            self.aspect_ratio = 'xxx'