

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item, Field

class ProductItem(Item):
    id = Field()
    p_id = Field()
    p_name = Field()
    p_type = Field()
    add_time = Field()


class CommentItem(Item):
    id = Field()
    p_id = Field()
    p_name = Field()
    c_id = Field()
    n_star = Field()
    short = Field()
    sentiment = Field()
    c_time = Field()
    add_time = Field()