import time
import pandas as pd
from openpyxl import Workbook
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import ActionChains


class YoutubeSearchScraper():
        SEARCH_URL = 'https://www.youtube.com/results'
        WAIT_LOAD = 20 # Time to wait for more content to load

        def __init__(self, drivername="chrome"):
                drivers = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'opera': webdriver.Opera,
                                        'ie': webdriver.Ie, 'android': webdriver.Android, 'edge': webdriver.Edge }
                driver = drivers.get(drivername, drivers.get('chrome'))
                self.driver = driver()

        def extract(self, match_list):
                results = []
                for i in  match_list:
                        url = i.get_attribute('href')
                        title = i.text
                        if url and title:
                                if len(title) > 10: # Bypasses problem where video length was identified as title
                                        if 'watch?' in url:
                                                result = {'url': url, 'title': title}
                                                results.append(result)
                results = results [0:20] # Selects the first 20 videos only

                df = pd.DataFrame(results)
                writer = pd.ExcelWriter('D:/Masters/Semester2/Decoding AI Biases/youtube_search_scraper/Nuetral_Nations.xlsx', engine = 'openpyxl')
                writer.book = load_workbook('D:/Masters/Semester2/Decoding AI Biases/youtube_search_scraper/Nuetral_Nations.xlsx')
                writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
                #writer = "D:/Masters/Semester2/Decoding AI Biases/youtube_search_scraper/test1.xlsx"
                reader = pd.read_excel('D:/Masters/Semester2/Decoding AI Biases/youtube_search_scraper/Nuetral_Nations.xlsx', engine = 'openpyxl')
                df.to_excel(writer, startrow = len(reader)+2, index=False)
                writer.close()
                
                return results

        def parse_top_results(self, search_term):
                """
                        Returns a list of dictionaries containing the url and titles of top videos with the
                        keys 'url'  and 'title' respectively.
                """
                param = '?search_query=' + search_term
                self.driver.get(self.SEARCH_URL+param)
                #I_Agree = input_username = self.driver.find_element_by_xpath(
                        #'//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc IIdkle"]') # Xref for 'I Agree' button
                #ActionChains(self.driver).move_to_element(I_Agree).click().perform()
                time.sleep(self.WAIT_LOAD) # Gives time to click button before loading results
                results = self.extract(self.driver.find_elements_by_class_name('yt-simple-endpoint'))
                self.driver.quit()
                return results
