from sys import breakpointhook
from bs4 import BeautifulSoup # web scraping websites using HTML and XML
import requests  # Making Http requests and parsing data
import re
import sqlite3

conn = sqlite3.connect('movie.db')
c = conn.cursor()

# Creates table
c.execute("""CREATE TABLE IF NOT EXISTS movies
            (search text PRIMARY KEY,
            title text,
            img_link text,
            movie_link text,
            runtime text,
            release_date text,
            movie_description text)""")



html_text = requests.get('https://www.amctheatres.com/movies').text #if you dont use ".text" then you be passing data as bits instead of text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.findAll('div', class_ = "Slide")



# for movie in movies:
#     moviePosterContent = movie.find('div', class_ = 'PosterContent') #var used to further dive into HTML to look for movie title
    
    
#     # MOVIE TITLE
#     movietitle = moviePosterContent.find('h3').text #need to use .text method otherwise it will return HTML syntax 
#     search_temp = (movietitle.lower()).replace(" ","") # gets rid of white spaces and makes all letters lowercase
#     search_title = re.sub(r'[^a-zA-Z0-9]', '', search_temp) # gets rid of all alphanumeric characters
#     print(movietitle)
    
#     # MOVIE IMAGE
#     movieimg = movie.find('img') #finds all data starting with img
#     movieimgsrc = movieimg['src']
    
    
    
#     # MOVIE LINK
#     movielinktemp1 = movie.find('a')
#     moviepartiallink = movielinktemp1['href'] #this for some reason doesn't include the https://www.amctheatres.com part of the link
#     movielink = 'https://www.amctheatres.com' + moviepartiallink # This movie link will then also be webscraped to scrape movie description data
     
#     # MOVIE DESCRIPTION
#     html_text2 = requests.get(movielink).text
#     soup = BeautifulSoup(html_text2, 'lxml')
#     nodey = soup.find('div', class_ = 'Intro-text col-md-8 order-md-last')
#     nodey2 = nodey.find('p', itemprop = 'description', class_ = 'show-text')
#     moviedesc = nodey2.text

#     # MOVIE TIME
#     movietimetemp1 = moviePosterContent.find('div', class_ = 'Headline--eyebrow')
#     # node = movietimetemp1.find('p')
#     node = movietimetemp1
    
#     if node.text == '': #if statement to skip over empty description fields
#         continue
#     else:
#         movietime = node.find('span', class_ = 'js-runtimeConvert u-inlineFlexCenter').text
#         movierelease = node.find('span', class_ = 'MoviePosters__released-month').text
#         c.execute('''INSERT OR IGNORE INTO movies VALUES(?,?,?,?,?,?,?)''',\
#                  (search_title,movietitle,movieimgsrc,movielink,movietime,movierelease, moviedesc))
conn.commit()     
# c.execute("SELECT * FROM movies WHERE search='amsterdam'") 
# print(c.fetchone())  
# c.close()
       
