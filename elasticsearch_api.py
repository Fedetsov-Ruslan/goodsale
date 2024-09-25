from elasticsearch import Elasticsearch
from database.engine import Session
import time 
from database.models import SKU
from database.orm_query import orm_get_all, orm_update_db_simular_sku
from config import ELASTIC_PASSWORD, ELASTIC_HOST


def to_dict(product: SKU):
    product_dict = {}
    for key, value in product.__dict__.items():
        if key == '_sa_instance_state':
            continue
        product_dict[key] = value
    return product_dict


def load_products_to_elasticsearch(session, es):
    for product in orm_get_all(session):
        product_dict = to_dict(product)
        es.index(index='products', id=product.uuid, body={
    'title': product.title,
    'description': product.description,
    'uuid': product.uuid  
})
    session.close()


def search_analog(session, es):
    product_from_db = orm_get_all(session)
    product_analog = {}
    for product in product_from_db:
        response = es.search(index='products', body={
            "query": {
                "more_like_this": {
                    "fields": ["title", "description"],
                    "like": [
                        {
                            "_index": "products",
                            "_id": product.uuid
                        }
                    ],
                    "min_term_freq": 1,
                    "max_query_terms": 12,
                    "minimum_should_match": "30%"
                }
            }
        })
        similar_products = [hit['_id'] for hit in response['hits']['hits']]
        product_analog[product.uuid] = similar_products[:5] 
        orm_update_db_simular_sku(product_analog, session)
        product_analog = {} 
    session.close()      
    return product_analog
 
 
def start_elasticsearch(session):
    es = Elasticsearch(f"http://{ELASTIC_HOST}:9200", basic_auth=('elastic', ELASTIC_PASSWORD))
    index_name = 'products'
    # es.indices.delete(index='products', ignore=[400, 404]) если нужно удалить индекс
    es.indices.create(index=index_name, ignore=400)
    load_products_to_elasticsearch(session, es)
    search_analog(session, es)
