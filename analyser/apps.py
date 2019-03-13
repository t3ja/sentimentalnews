from django.apps import AppConfig
# from analyser.models import Article
from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key='f98bfb9106634c6ebc6aee41468d1c4c')
COUNTRIES = ['in', 'us', 'uk']


class CrawlNews():
    def __init__(self):
        self.news = None

    # def update_auction(self):
    # 	auction = self.auction
    # 	auction.bid_count = Bid.BidManager.current(auction).count()
    # 	auction.current_bid = format(auction.value, ".2f")
    # 	auction.save()


    # def send_email(self):
    # 	EmailQueue(auction=self.auction).save()


    def crawl(self, country='in', query='', category='general'):
        from .models import Article

        # /v2/top-headlines
        news = newsapi.get_top_headlines(category=category,
                                              language='en',
                                              country=country)
        print('News API response:: ', news, list(news.keys()))
        # news = json.loads(news)
        articles = []
        for ne in news['articles']:
            article = Article()
            article.title = ne.get('title', 'no_title')
            article.content = ne.get('content', 'no_content')
            article.country = ne.get('country', 'in')
            article.published_at = ne.get('publishedAt')
            article.source = ne.get('source').get('name', 'no_source')
            article.url = ne.get('url', 'no_url')
            print('Article saving:: ', ne)
            article.save()
            articles.append(article)

        print('All articles saved', str(len(articles)))
        return articles

        # # /v2/everything
        # all_articles = newsapi.get_everything(q='bitcoin',
        #                                       sources='bbc-news,the-verge',
        #                                       domains='bbc.co.uk,techcrunch.com',
        #                                       from_param='2017-12-01',
        #                                       to='2017-12-12',
        #                                       language='en',
        #                                       sort_by='relevancy',
        #                                       page=2)
        # # /v2/sources
        # sources = newsapi.get_sources()
        # return news


class AnalyserConfig(AppConfig):
    name = 'analyser'

    def ready(self):
        return
        # cn = CrawlNews()
        # cn.crawl()

