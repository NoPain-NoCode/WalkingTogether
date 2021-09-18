import os
import sys

maps_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))+'/backend'))
sys.path.append(maps_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django
django.setup()

from maps.models import WalkingTrails
from django.core import serializers
import json

import requests
from elasticsearch import Elasticsearch

res = requests.get('http://203.237.169.237:9200')
es = Elasticsearch([{'host':'203.237.169.237', 'port':'9200'}])

es.indices.create(
    index='walkingtrails',
    body={
        # nori로 데이터 토크나이징
        "settings": {
            "index": {
                "analysis": {
                    "analyzer": {
                        "my_analyzer": {
                            "type": "custom",
                            "tokenizer": "nori_tokenizer"
                        }
                    }
                }
            }
        },
        # 인덱스 데이터타입 정의
        "mappings": {
            "properties": {
                "point_number": {
                    "type": "long"
                },
                "category": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "region": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "distance": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "time_required": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "_level": {
                    "type": "long"
                },
                "subway": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "Transportation": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "course_name": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "course_detail": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "_explain": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "point_name": {
                    "type": "text",
                    "analyzer": "my_analyzer"
                },
                "longitude": {
                    "type": "float"
                },
                "latitude": {
                    "type": "float"
                }
            }
        }
    }
)



# 여러 개의 데이터를 한 번에 bulk하기 위해서 데이터를 Elasticsearch 형식에 맞게 정제
# url = 'http://203.237.169.237:8001/maps/road_data'
# response = urllib.request.urlopen(url)
# response_message = response.read().decode('utf8')
# json_data = json.loads(response_message)

road_data = WalkingTrails.objects.all()
body = ""

for r in road_data[:5]:
    road = serializers.serialize('json',WalkingTrails.objects.filter(point_number = r.point_number))
    body += json.dumps({"index": {"_index": "walkingtrails", "_id": int(r.point_number)}}) + '\n'
    body += json.dumps(road, ensure_ascii=False) + '\n'


# count = 1
# for i in json_data:
#     body = body + json.dumps({"index": {"_index": "WalkingTrails", "_id": count}}) + '\n'
#     body = body + json.dumps(i, ensure_ascii=False) + '\n'
#     if count == 1:
#         print(body)
#     count += 1

es.bulk(body)