# I'm Just Gonna Write You a Love Song


### Setting up
1. Modify `start_urls` in  `{project}/lyric_scraper/lyric_scraper/spiders/{spider}` so that it contains the URLs of the artists whose songs you want to scrape.
1. Start the scraper by changing directories to `{project}/lyric_scraper/` and running `scrapy crawl {spider_name} -o ../data/songs/batch/{target_filename}.json`
1. Clean out any of the files you don't want from `{project}/data/songs/batch/`
1. Run `python {project}/scripts/extract_artists.py`
	1. This will ask you to fix any titles and artists that couldn't be scraped.
	1. Then, it will separate the batch files into artist files