#! /usr/bin/env python3
# coding: utf-8
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Models.Movie import Movie as Movie 
from Models.Metric import Metric
from Managers.MovieManager import MovieManager as Manager 
from Managers.MetricManager import MetricManager
from roots.movie import *
from roots.metric import *

def run():
    try:
        print ('tapez:\n 1. Pour executer le script de scraping du site imb: \n 2. Pour executer le script de scraping du site macrotrends:'),
        a = int(input())                                                  
        while a != 0: # l'opérateur != signifie "différent de"             
            if a == 1: 
                movie_launcher()
            elif a == 2:                                  
                metric_launcher()                   
            else :                                                         
                print ("Un nombre entre 1 et 2, s.v.p.")                
            print ('Voulez-vous continuer le scraping?\n Choisissez un nombre de 1 à 2 (ou zéro pour terminer) '),
            a = input()                                                    
        print ("Vous avez entré zéro :")                                     
        print ("L'exercice est donc terminé.")  
    except (ValueError, AttributeError, IndexError):
        print('veillez entrer un nombre entier 1 ou 2')
if __name__ == '__main__':
    print(run())
