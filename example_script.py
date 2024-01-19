from src.GoogleTrendsScraper import GoogleTrendsScraper
import os

os.environ["CHROMEDRIVER"] = '/usr/bin/google-chrome'
gts = GoogleTrendsScraper(sleep=2, path_driver=os.environ['CHROMEDRIVER'], headless=True)
data, related_queries_list, related_topics_list = gts.get_trends(['llm', 'openai'], '2023-07-02', '2023-08-02', 'US')

print(data)
print(related_queries_list)
print(related_topics_list)

del gts
