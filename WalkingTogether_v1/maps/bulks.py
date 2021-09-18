import os
import sys

maps_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))+'/backend'))
sys.path.append(maps_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from . import models
from .utils import WalkingTrailsIndex, ReviewIndex

es = Elasticsearch([{'host':'203.237.169.237', 'port':'9200'}])
connections.create_connection(hosts=['203.237.169.237'])

def delete_index(index):
    if not es.indices.exists(index=index):
        print('delete')
        return es.indices.delete(index=index)

def bulk_road_indexing():
    WalkingTrailsIndex.init()
    bulk(client=es, actions=(b.indexing() for b in models.WalkingTrails.objects.all().iterator()))

def bulk_review_indexing():
    ReviewIndex.init()
    bulk(client=es, actions=(b.indexing() for b in models.Review.objects.all().iterator()))

