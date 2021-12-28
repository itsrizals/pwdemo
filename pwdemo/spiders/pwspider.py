import scrapy 
from scrapy_playwright.page import PageCoroutine

class PwspiderSpider(scrapy.Spider):
	name = 'pwspider'

	def start_requests(self):
		headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
        }
        


		yield scrapy.http.Request('https://www.techinasia.com/jobs/search?country_name[]=Indonesia', headers=headers, meta=dict(
             playwright = True,
             playwright_include_page = True,
             playwright_page_coroutines = [
                 PageCoroutine('wait_for_selector', 'article.jsx-1022654950')
                 ]
         ))

	async def parse(self, response):
		for listings in response.css('article.jsx-1022654950'):
			yield {
				'title': listings.css('a[data-cy="job-title"]').get()
			}

