from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy

from neuralcrawling.items import QuestionItem, AnswerItem
class MyCrawler(scrapy.Spider):
    name = 'mycrawler'
    #start_urls = ['https://bitcoin.stackexchange.com/questions?tab=newest&page=2']
    start_urls = ['https://money.stackexchange.com/questions?tab=newest&page=1848']
    #start_urls = ['https://iota.stackexchange.com/questions?tab=newest&page=30']

    def parse(self, response):
        questions = response.xpath('//div[@id="questions"]//div[contains(@id, "question-summary")]')
        for question in questions:
            question_item = QuestionItem()
            question_item['title'] = question.xpath('.//h3/a/text()').get()
            question_item['link'] = question.xpath('.//h3/a/@href').get()
            #question_item['category'] = question.xpath('.//div[@class="d-inline mr4 js-post-tag-list-item"]/a/text()').get()
            question_item['category'] = question.xpath('.//ul/li//a/text()').getall()
            yield question_item

            question_link = question.xpath('.//h3/a/@href').get()
            yield response.follow(question_link, self.parse_answers, meta={'question_title': question_item['title']})

        next_page = response.xpath('//a[@rel="next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_answers(self, response):
        question_title = response.request.meta['question_title']
        answers = response.xpath('//div[@id="answers"]//div[contains(@id, "answer")]')
        for answer in answers:
            answer_item = AnswerItem()
            answer_item['question_title'] = question_title
            answer_item['answer'] = answer.xpath('.//div[@class="answercell post-layout--right"]//div[@class="s-prose js-post-body"]/p/text() | .//div[@class="answercell post-layout--right"] //div[@class="s-prose js-post-body"]//a/@href').getall()
            yield answer_item
    