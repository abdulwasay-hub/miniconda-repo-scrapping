import scrapy
import csv


from datetime import datetime
import logging

class MinicondaSpider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://repo.anaconda.com/miniconda/']
    
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def parse(self, response):
        self.logger.info(f'Response status: {response.status}')
        self.logger.info(f'URL being scraped: {response.url}')

        filename = f'conda-repo.csv'
        
        self.logger.info(f'Page content length: {len(response.body)}')
        self.logger.info('First 500 characters of response: ' + str(response.body[:500]))

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['filename', 'size', 'date'])
            writer.writeheader()
            
            rows = response.xpath('//table//tr')
            if not rows:
                rows = response.css('table tr')
            
            self.logger.info(f'Number of rows found: {len(rows)}')

            for row in rows:
                try:
                    filename = row.xpath('.//a/text()').get() or row.css('a::text').get()
                    if filename:
                        size = row.xpath('.//td[2]/text()').get() or row.css('td:nth-child(2)::text').get()
                        date = row.xpath('.//td[3]/text()').get() or row.css('td:nth-child(3)::text').get()
                        
                        data = {
                            'filename': filename.strip(),
                            'date': date.strip() if date else '',
                            'size': size.strip() if size else ''
                        }
                        self.logger.info(f'Found data: {data}')
                        writer.writerow(data)
                        yield data
                except Exception as e:
                    self.logger.error(f'Error processing row: {e}')

# To run this spider:
# scrapy crawl spidercls


# 1. Create a new Scrapy project: scrapy startproject miniconda_scraper
# 2. Place this spider code in spiders folder
# 3. Run: scrapy crawl spider -o output.json