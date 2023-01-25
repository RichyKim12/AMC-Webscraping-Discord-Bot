# AMC Webscraping Discord Bot
The AMC webscraping Discord bot is a personal project coded by both myself (Richard Kim) and Mohit Sharma. The discord bot works by first calling webscrape.py where all movie data will be webscraped. 

This is done by first comitting a GET request on the AMC website for its HTML data which is parsed using Python's BeautifulSoup Library. A unique webscraping loop will then search for all movies and respective data to be stored inside a SQLite3 Database.

main.py is used for Discords bot API and will check for command notations and access the SQLite3 database accordingly to gather and send movie data as messages on a Discord server.

# Notice of secret key exemption
The project will not be able to be run without a secret key which I have intentionally kept hidden for security reasons. This will prevent the bot from working.

# Commands and Features

- !movie - Used for searching for a specific movie, accurate capitalization and spacing is not required to successfully search for a movie however spelling is.
- !remind - Used to set reminders for movie release dates.

# Examples of Command inputs
## !movie
+<img src = >