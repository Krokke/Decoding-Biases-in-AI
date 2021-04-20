# General 

This was a final project for a class investigating biases in artifical intelligence.  
We tried to detect if there was a bias in YouTube's search algorithm based on the country the search was done in.  
Here is the link to the Github Page for the project.  
https://krokke.github.io/Decoding-Biases-in-AI/

# youtube_search_scraper

This folder contains the scraper we used to collect data about YouTube's search algorithm.  
The code was adapted from here: https://github.com/cRyp70s/youtube_search_scraper.

## Setting up

You will need to install selenium and openpyxl through pip.  
You will also need to download the drivers for your browser of choice or selenium won't be able to interact with it. The drivers should be added to your system path (or just in your /usr/local/bin directory if on MacOSX or Linux.)  
The code runs default with chrome, but works with any major browser. To change the browser, the browser name needs to be passed as an argument through the YoutubeSearchScraper function in main.py. (Look in yt_search_scraper.py for the precise argument names.) 

## Scraping

Run main.py to scrape the top 20 YouTube search results for a given search term, which can be changed in main.py.  
Scraping is done through Selenium, which is completely private, with no storage of search history.  
Results are directly printed in the terminal as a list of 20 dictionaries each containing the URL and Title of a video. They are also written to an excel file, the path of which is defined in yt_search_scraper.py. 

# data.xlsx

This is the dataset combining all the data collected during scraping, polling data from pew (https://www.pewresearch.org/global/) and data on global geopolitics (https://www.ispionline.it/en/pubblicazione/chinas-global-future-mapping-international-support-after-covid-19-26943).  
Minimal data cleaning was done through excel.

# analysis.ipynb

The jupyter notebook used for data treatment and statistical analysis.
