__author__ = 'user-icc'

import urllib2
from bs4 import BeautifulSoup


class Google:
    def __init__(self):
        self.user_agent = "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"

    def query(self, search_terms):
        web_request = urllib2.Request('http://www.google.com/search?q=%s'%search_terms)

        news_request = urllib2.Request('http://www.google.com/search?q=%s&tbm=nws'%search_terms)

        web_request.add_header('User-Agent',
                                self.user_agent)
        news_request.add_header('User-Agent',
                                self.user_agent)

        web_response = urllib2.urlopen(web_request)
        news_response = urllib2.urlopen(news_request)
        self.web_response_html = web_response.read()
        self.news_response_html = news_response.read()

    def fetch_web_results(self):
        soup = BeautifulSoup(self.web_response_html, 'html.parser')
        web_soup_body = soup.body
        web_search_links = [r.a.get("href").strip('/url?q=') for r in web_soup_body.find_all("h3")]
        cleaned = [link[:link.index('&sa')] for link in web_search_links]
        return cleaned

    def fetch_news_results(self):
        soup = BeautifulSoup(self.news_response_html, 'html.parser')
        news_soup_body = soup.body
        news_search_links = [r.a.get("href").strip('/url?q=') for r in news_soup_body.find_all("h3")]
        cleaned = [link[:link.index('&sa')] for link in news_search_links]
        return cleaned

if __name__ == '__main__':
    google = Google()
    google.query('hello+world')
    print google.fetch_news_results()
    print google.fetch_web_results()