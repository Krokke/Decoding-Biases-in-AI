# General 

This was a final project for a class investigating biases in artifical intelligence.  
We tried to detect if there was a bias in YouTube's search algorithm based on the country the search was done in.  
Here is the link to the Github Page for the project.  
https://krokke.github.io/Decoding-Biases-in-AI/

# youtube_search_scraper

This folder contains the scraper we used to collect data about YouTube's search algorithm.  
The code was adapted from here: https://github.com/cRyp70s/youtube_search_scraper.

## Scraping

Run main.py to scrape the top 20 YouTube search results for 'xinjiang'.
Scraping is done through Selenium, which is completely private, with no storage of search history. 
Results are directly printed in the terminal as a list of 20 dictionaries each containing the URL and Title of a video.

## Setting up

You will probably need to install selenium through pip install.  
You will also need to download the drivers for your browser of choice or selenium won't be able to interact with it. The drivers should be added to your system path (or just in your /usr/local/bin directory if on MacOSX or Linux.) 


## Customisation

I have only tried running the code with Firefox, which is the default, but normally it should work with any major browser. To change the browser, you need to pass the browser name as an argument through the YoutubeSearchScraper function in main.py. (Look in yt_search_scraper.py for the precise argument names.) The search query can also be changed in main.py.
