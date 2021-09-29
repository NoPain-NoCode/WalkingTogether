from elasticsearch_dsl import Document, Keyword, Text,tokenizer,analyzer

my_analyzer = analyzer(
    'my_analyzer',
    tokenizer=tokenizer('nori_tokenizer')
)
class PetIndex(Document):
    owner = Text(analyzer=my_analyzer)
    pet_name = Text(analyzer=my_analyzer)
    gender = Keyword()
    introducing_pet = Text(analyzer=my_analyzer)

    class Index:
        name = 'pet-index'
