from bs4 import BeautifulSoup # web scraping websites using HTML and XML
import requests  # Making Http requests and parsing data
import re

html_text = requests.get('https://www.amctheatres.com/movies').text #if you dont use ".text" then you be passing data as bits instead of text
soup = BeautifulSoup(html_text, 'lxml')
movies = soup.findAll('div', class_ = "Slide")


# Dictionary:
#    - key: movietitle
#    - val[0]: movie title
#    - val[1]: img link
#    - val[2]: movie link
#    - val[3]: runtime
#    - val[4]: Release date
#    - val[5]: Movie description
moviedict = {}


#How to store all this data, for now store it in dictionary
for movie in movies:
    moviePosterContent = movie.find('div', class_ = 'PosterContent') #var used to further dive into HTML to look for movie title
    moviedata = []
    
    # MOVIE TITLE
    movietitle = moviePosterContent.find('h3').text #need to use .text method otherwise it will return HTML syntax 
    #print(movietitle)
    temp = (movietitle.lower()).replace(" ","") # gets rid of white spaces and makes all letters lowercase
    temp = re.sub(r'[^a-zA-Z0-9]', '', temp) # gets rid of all alphanumeric characters
    moviedict[temp] = []
    
    moviedata.append(movietitle)
    # MOVIE IMAGE
    movieimg = movie.find('img') #finds all data starting with img
    movieimgsrc = movieimg['src']
    #print(movieimgsrc) #indexing using 'src' to find image source link
    moviedata.append(movieimgsrc)
    
    
    # MOVIE LINK
    movielinktemp1 = movie.find('a')
    moviepartiallink = movielinktemp1['href'] #this for some reason doesn't include the https://www.amctheatres.com part of the link
    movielink = 'https://www.amctheatres.com' + moviepartiallink # This movie link will then also be webscraped to scrape movie description data
   # print(movielink)
    moviedata.append(movielink)
    
    
    # MOVIE TIME
    movietimetemp1 = moviePosterContent.find('div', class_ = 'Headline--eyebrow poster-content-meta')
    node = movietimetemp1.find('p')
    #print(node)
    if node.text == '': #if statement to skip over empty description fields
        continue
    else:
        movietimetemp2 = node
        movietime = movietimetemp2.find('span', class_ = 'u-separator js-runtimeConvert u-inlineFlexCenter').text
        movierelease = movietimetemp2.find('span', class_ = 'MoviePosters__released-month clearfix').text
        # print(movietime)
        # print(movierelease)
    
    #print()
    moviedata.append(movietime)
    moviedata.append(movierelease)
    moviedict[temp].append(moviedata)

#navigate to the movie description link and web scrape the description box
for k,v in moviedict.items():
    if len(v) > 0:
        moviedesclink = v[0][2]
        html_text2 = requests.get(moviedesclink).text
        soup = BeautifulSoup(html_text2, 'lxml')
        nodey = soup.find('div', class_ = 'Intro-text col-md-8 col-md-push-4')
        nodey2 = nodey.find('p', itemprop = 'description', class_ = 'show-text')
        moviedict[k][0].append(nodey2.text)

for k,v in moviedict.items():
    print(k)
    print(v)
    
