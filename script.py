import xml.etree.ElementTree as ET
from lxml import etree

from database.engine import Session
from database.orm_query import orm_add_offer
from elasticsearch_api import start_elasticsearch

session = Session()


def parse_until_categories_end(file_path):
    """Функция парсинга категорий и преоброзования их в словарь"""
    categories = {}
    xml_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if '<category' in line:
                xml_data.append(ET.fromstring(line))
            if '</categories>' in line:
                break
    for category in xml_data:
        categories[category.get('id')] = ([category.get('parentId'),
                                           category.text])
    return categories


def find_category_path(categories: dict, category_id: int):
    """Функция постоения пути"""
    path = []
    current_id = str(category_id)
    while current_id is not None:
        path.append(categories[current_id][1])
        current_id = categories[current_id][0]
    return path[::-1]


def process_offer(offer, session, categories):
    """Функция для обработки и сохранения данных в базу данных"""
    category = find_category_path(categories,
                                  int(offer.findtext('categoryId')))
    offer_data =orm_add_offer(offer, session, category)
    


context = etree.iterparse('elektronika_products_20240923_113957.xml',
                          tag='offer',
                          events=('end',),
                          recover=True)
categories = parse_until_categories_end(
    'elektronika_products_20240923_113957.xml'
    )

for event, elem in context:
    process_offer(elem, session, categories)
    elem.clear()
    while elem.getprevious() is not None:
        del elem.getparent()[0]

del context

start_elasticsearch(session)