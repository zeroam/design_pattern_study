from abc import ABC, abstractmethod

import requests
from bs4 import BeautifulSoup


class WebScraper(ABC):
    def scrape(self, url: str):
        html = self.get_html(url)
        soup = self.parse_html(html)
        data = self.extract_data(soup)
        self.output_data(data)

    def get_html(self, url: str) -> str:
        response = requests.get(url)
        return response.text

    def parse_html(self, html: str) -> BeautifulSoup:
        return BeautifulSoup(html, "html.parser")

    def output_data(self, data: list[dict]):
        print(data)

    @abstractmethod
    def extract_data(self, soup: BeautifulSoup) -> list[dict]:
        ...


class RedditScraper(WebScraper):
    def extract_data(self, soup: BeautifulSoup) -> list[dict]:
        posts = soup.find_all("div", {"class": "Post"})
        data = []
        for post in posts:
            title = post.find("h3", {"class": "Post__title"}).text
            author = post.find("a", {"class": "Post__authorLink"}).text
            data.append({"title": title, "author": author})
        return data


class HackerNewsScraper(WebScraper):
    def extract_data(self, soup: BeautifulSoup) -> list[dict]:
        posts = soup.find_all("tr", {"class": "athing"})
        data = []
        for post in posts:
            title = post.find("a", {"class": "storylink"}).text
            author = post.find_next_sibling("tr").find("a", {"class": "hnuser"}).text
            data.append({"title": title, "author": author})
        return data


if __name__ == "__main__":
    redditScraper = RedditScraper()
    redditScraper.scrape("https://www.reddit.com/r/Python/")

    hackerNewsScraper = HackerNewsScraper()
    hackerNewsScraper.scrape("https://news.ycombinator.com/")
