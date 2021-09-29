DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'walkdb',
        'USER': 'npnc',
        'PASSWORD': 'walkingtogether',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

CORS_ORIGIN_WHITELIST = ['https://203.237.169.237:3001','https://www.wannawalk.co.kr:3001',
                        'https://203.237.169.237:3000','https://www.wannawalk.co.kr:3000',
                        'https://localhost:3001', 'https://127.0.0.1:3001',
                        'https://localhost:3000', 'https://127.0.0.1:3000',
                        'http://203.237.169.237:3001','http://www.wannawalk.co.kr:3001',
                        'http://203.237.169.237:3000','http://www.wannawalk.co.kr:3000',
                        'http://localhost:3001', 'http://127.0.0.1:3001',
                        'http://localhost:3000', 'http://127.0.0.1:3000'] 

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': '34.64.244.18:9200'
    },
}

ELASTICSEARCH_HOST = '34.64.244.18'

BASE_URL = "http://203.237.169.237:8001/"

SECRET_KEY = 'django-insecure-5%2(rc!6o#=34^lln)0tr^61_6msvm3fc5#kzxoi9%nsjhltwg'

JWT_SECRET_KEY = 'WalkingTogether'
JWT_ALGORITHM = 'HS256'