# Richard Kim
from bs4 import BeautifulSoup # web scraping websites using HTML and XML
import requests  # Making Http requests and parsing data


html_text = requests.get('https://www.amctheatres.com/movies').text #if you dont use ".text" then you be passing data as bits instead of text
soup = BeautifulSoup(html_text, 'lxml')
#movies = soup.find_all('div', class_ = "Slide")
movies = soup.findAll('div', class_ = "Slide")

for movie in movies:
    moviePosterContent = movie.find('div', class_ = 'PosterContent') #var used to further dive into HTML to look for movie title
    movietitle = moviePosterContent.find('h3').text #need to use .text method otherwise it will return HTML syntax 
    print(movietitle)
    movieimg = movie.find('img') #finds all data starting with img
    movieimgsrc = movieimg['src']
    print(movieimgsrc) #indexing using 'src' to find image source link
    
    movielinktemp1 = movie.find('a')
    moviepartiallink = movielinktemp1['href'] #this for some reason doesn't include the https://www.amctheatres.com part of the link
    
    movielink = 'https://www.amctheatres.com' + moviepartiallink # This movie link will then also be webscraped to scrape movie description data
    print(movielink)
    movietimetemp1 = moviePosterContent.find('div', class_ = 'Headline--eyebrow poster-content-meta')
    
    node = movietimetemp1.find('p')
    
    if node.text == '': #if statement to skip over empty description fields
        continue
    else:
        movietimetemp2 = node
        movietime = movietimetemp2.find('span', class_ = 'u-separator js-runtimeConvert u-inlineFlexCenter').text
        movierelease = movietimetemp2.find('span', class_ = 'MoviePosters__released-month clearfix').text
        print(movietime)
        print(movierelease)
    
    print()


#print(moviedeets)
