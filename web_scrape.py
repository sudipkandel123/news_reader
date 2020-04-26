#INPUTS -> Date,title, text , link 

##LIBRARIES
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyttsx3
import time
import speech_recognition as sr  


##GLOBAL VARS
web = "https://inshorts.com"
website = "https://inshorts.com/en/read"
##CLASS
class web_scrape:
    def __init__(self,website):
        self.website = website

    def websiteToScrape(self):
        self.title_list = []
        self.date_list = []
        self.link_list = []
        self.content_list = []
        source = requests.get(self.website).text #Scrapes the entire sorce code
        soup = BeautifulSoup(source,"lxml")

        for news in soup.find_all("div",class_ = "news-card z-depth-1"):
            date = news.find("span",clas = "date").text
            title = news.find("span",itemprop = "headline").text
            content = news.find("div",itemprop = "articleBody").text
            link = news.find("a",class_ = "clickable",href = True)['href']
            link = web+link
            self.title_list.append(title)
            self.date_list.append(date)
            self.link_list.append(link)
            self.content_list.append(content)
        df = pd.DataFrame(list(zip(self.date_list,self.title_list,self.content_list,self.link_list)),columns = ['Date','Title','Content','Link'])
        #df.to_csv(r"/Users/sudip/Desktop/Data Science/python-webscraping/inshort_scrape.csv",index = False)

    def text_to_speech(self):
        news_final = self.title_list
        news_final = news_final
        engine = pyttsx3.init()
        # voices = engine.getProperty('voices')
        # for voice in voices:
        #     engine.setProperty('voice', voice.id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-50)
        engine = pyttsx3.init()
        engine.say('Hi Mr. Sudip Kandel ')
        engine.say('These are Top 5 News Tailored for you ')
        for ele in news_final:
            engine.say(ele)
            engine.say("Next Newsss ")
        engine.say(", if you want more news please select option 2 ... Thank you Mr. Sudip. These are all the news we have for you ")
        engine.runAndWait()
        
            

        #     print("\n")


        

### MAIN 
scrape_Obj = web_scrape(website)

scrape_Obj.websiteToScrape()
# get audio from the microphone                                                                       
r = sr.Recognizer()     
                                                                              
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
    
voice = r.recognize_google(audio)

try:
    print("You said " + r.recognize_google(audio))
    if voice == 'news':
        print("okay ")
        scrape_Obj.text_to_speech()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))




#BREAK BELOW
# from bs4 import BeautifulSoup
# with open("test.html") as html_file:
#     soup = BeautifulSoup(html_file,'lxml')

# print(soup.prettify())
# # match = soup.h1.text #Gives the first tag from the page
# # print(match)
