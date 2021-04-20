import yt_search_scraper

scrap = yt_search_scraper.YoutubeSearchScraper()
results = scrap.parse_top_results('xinjiang Uighurs')
print(results)
print('Length: ', len(results))
