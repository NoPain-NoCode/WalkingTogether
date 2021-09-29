from elasticsearch_dsl import Document, Keyword, Text, Integer,Float,tokenizer,analyzer,analysis

my_analyzer = analyzer(
    'my_analyzer',
    tokenizer=tokenizer('nori_tokenizer')
)
class WalkingTrailsIndex(Document):
    category=Text(analyzer=my_analyzer)
    region=Text(analyzer=my_analyzer)
    distance=Text(analyzer=my_analyzer)
    time_required=Text(analyzer=my_analyzer)
    _level=Integer()
    subway=Text(analyzer=my_analyzer)
    transportation=Text(analyzer=my_analyzer)
    course_name=Text(analyzer=my_analyzer)
    course_detail=Text(analyzer=my_analyzer)
    _explain=Text()
    point_number=Integer()
    point_name=Text(analyzer=my_analyzer)
    longitude=Float()
    latitude=Float()
    class Index:
        name = 'walkingtrails-index'

class ReviewIndex(Document):
    walkingtrails=Text(analyzer=my_analyzer)
    user=Text(analyzer=my_analyzer)
    content=Text(analyzer=my_analyzer)
    point=Integer()
    dog_possible=Keyword()
    class Index:
        name = 'review-index'