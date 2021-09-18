import os
import sys

maps_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))+'/backend'))
sys.path.append(maps_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from elasticsearch_dsl.connections import connections

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from maps.models import WalkingTrails, Review


es = Elasticsearch([{'host':'203.237.169.237', 'port':'9200'}])
connections.create_connection(hosts=['203.237.169.237'])

def create_index(index):
    if not es.indices.exists(index=index):
        return es.indices.create(index=index)

def delete_index(index):
    if not es.indices.exists(index=index):
        print('delete')
        return es.indices.delete(index=index)

def insert(index, doc_type, body):
    return es.index(index=index, doc_type=doc_type, body=body)

def delete(index, data):
    if data is None:
        data={"match_all":{}}
    else:
        data={"match":data}
    body={"query":data}
    return es.delete_by_query(index, body=body)

def delete_by_id(id):
    return es.delete(id=id)

def update(index, id, doc, doc_type):
    body={
        'doc':doc
    }
    res = es.update(index=index, id=id, body=body, doc_type=doc_type)
    return res


def bulk_road_indexing():
    bulk(client=es, actions=(b.indexing() for b in WalkingTrails.objects.all().iterator()))

def bulk_review_indexing():
    bulk(client=es, actions=(b.indexing() for b in Review.objects.all().iterator()))


delete_index('walkingtrails-index ')
delete_index('road-index')

#bulk_road_indexing()
#bulk_review_indexing()