#! /usr/bin/env python3
# coding: utf-8
import sys

from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Models.Movie import Movie as Movie 
from roots.movie import *
from roots.metric import *

def run():
    """[summary: Method that run all the script of the project]

    Args:
        None

    Returns:
        None
    """
    try:
        print ('tapez:\n 1. Pour executer le script de scraping du site imb: \n 2. Pour executer le script de scraping du site macrotrends:'),
        a = int(input())                                                  
        while a != 0: # l'opérateur != signifie "différent de"             
            if a == 1: 
                movie_launcher() # launch the script to scrap the movies informations
            elif a == 2:                                  
                metric_launcher() # launch the script to scrap the GDP informations                  
            else :                                                         
                print ("Un nombre entre 1 et 2, s.v.p.")                
            print ('Voulez-vous continuer le scraping?\n Choisissez un nombre de 1 à 2 (ou zéro pour terminer/ Ctrl + c pour arrter le script) '),
            a = input()                                                    
        print ("Vous avez entré zéro :")                                     
        print ("L'exercice est donc terminé.")
    except (ValueError, AttributeError, IndexError):
        print('veillez entrer un nombre entier 1 ou 2')

if __name__ == '__main__':
    print(run())
