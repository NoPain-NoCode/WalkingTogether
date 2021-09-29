import os
import sys

user_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))+'/backend'))
sys.path.append(user_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from . import models
from .utils import PetIndex

from my_settings import *

es = Elasticsearch([{'host':ELASTICSEARCH_HOST, 'port':'9200'}])
connections.create_connection(hosts=[ELASTICSEARCH_HOST])

def delete_index(index):
    if not es.indices.exists(index=index):
        print('delete')
        return es.indices.delete(index=index)

def bulk_pet_indexing():
    PetIndex.init()
    bulk(client=es, actions=(b.indexing() for b in models.Pet.objects.all().iterator()))
