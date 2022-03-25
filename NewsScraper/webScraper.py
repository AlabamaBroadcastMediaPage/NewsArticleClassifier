from asyncore import write
import requests
import re
import json
import time
import logging
import pandas as pd
import csv
from collections import OrderedDict
from bs4 import BeautifulSoup #webscraper package

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

class Article: #
    def __init__(self, title, content, comments):
        self.title = title
        self.content = content
        self.comments = comments


class NewsScraper:
    def NewsScraper_Mandiner(self): #Lescrapeli az adatokat az oldalról, majd beleírja a .csv fájlba
        
        #Bejelentkezés (kommentekhez való hozzáférés miatt szükséges)
        with open('credentials_ns.json', 'r') as f:
            credentials = json.load(f)

        client = requests.Session()

        html = client.get(credentials['mainpage']).content
        mainPage_soup = BeautifulSoup(html, "html.parser")

        login_information = {
            'username':credentials['email'],
            'password':credentials['pw'],
            'nodeid':0,
            'authorid':0
            }
            
        client.post(credentials['loginpage'], data=login_information)

        dataFrame = pd.DataFrame()

        articleIndex = 0
        for div in mainPage_soup.findAll('div', attrs={'class':'title'}):
            if(articleIndex<2):
                article_title = "" #cikk címe
                article_content_str = "" #cikk tartalma egy stringben
                article_content= "" #cikk tartalma mondatokra bontva (|-el elvélasztva)
                article_comments= []

                article_title = div.find('a').contents[0] #cikk címe scrape-elve, eltárolva title változóba
                #Belép minden cikkbe linken keresztül és kiszedi a cikk tartalmát + kommenteket
                #URL checker
                if ("https" not in div.find('a')['href']):
                    article_url = "https://mandiner.hu" + div.find('a')['href'] #cikk URL
                else:
                    article_url = div.find('a')['href']
                
                #cikk elérés
                article = requests.get(article_url)
                article_soup = BeautifulSoup(article.content, "html.parser") #cikk tartalma elérve
                
                #cikk szövegének tárolása
                text = article_soup.find('div', class_='text')
                for item in text.find_all('p'):
                    text = "#" + item.text
                    article_content_str += text

                j = 0
                sentence = ""
                while (j<len(article_content_str)-1):
                    if(article_content_str[j]!= "#" and article_content_str[j]!="." and article_content_str[j]!="?" and article_content_str[j]!="!"):
                        sentence += article_content_str[j]
                        j = j+1
                    else:
                        if (article_content_str[j]!= "#"):
                            sentence += article_content_str[j]
                        article_content+= "|"
                        article_content+= str(sentence)
                        sentence = ""
                        j= j+1


                #adatok hozzáadása a dataframehez
                #data = [str(articleIndex), article_title, article_content, article_comments, 0]
                dict = {'title':article_title, 'content': article_content, 'comments':"", 'label': 0}
                dataFrame = dataFrame.append(dict, ignore_index=True)
                print(dataFrame)

                #indexelés
                articleIndex = articleIndex + 1
                print(articleIndex)
        dataFrame.to_csv('data.csv')

    def UploadToDrive(self, filename): #feltölt egy filet a news-scraper nevű Google Drive mappába
        gauth = GoogleAuth()           
        drive = GoogleDrive(gauth)
        gfile = drive.CreateFile({'parents': [{'id': '1jhN3SlUL5OA0KBTCCiCaJltWmjEFi6tF'}]})
        gfile.SetContentFile(filename)
        gfile.Upload() # Upload the file.

    def DownloadFromDrive(self): #letölt minden fájlt a Google Drive mappából
        gauth = GoogleAuth()           
        drive = GoogleDrive(gauth)
        file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format('1jhN3SlUL5OA0KBTCCiCaJltWmjEFi6tF')}).GetList()
        for i, file in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
            print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, len(file_list)))
            file.GetContentFile(file['title'])

ns = NewsScraper()
#ns.NewsScraper_Mandiner()
#ns.DownloadFromDrive()
ns.UploadToDrive("data.csv")