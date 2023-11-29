# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()


class AnswerItem(scrapy.Item):
    question_title = scrapy.Field()
    answer = scrapy.Field()
