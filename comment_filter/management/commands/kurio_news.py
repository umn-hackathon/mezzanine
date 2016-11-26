import json
import requests
from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from urllib.parse import urlparse
import urllib



from mezzanine.blog.models import BlogPost


class Command(BaseCommand):
    args = None
    help = 'pre generate kurio news'

    def handle(self, *args, **options):
        #token = get_access_token()
        token='f0zHLt0nPGDIsDyvdBrDIgCAyZA9t4bfwka7wiRA'
        headers = {'Accept': 'application/json', 'X-Kurio-Client-ID': '99',
                   'X-Kurio-Client-Secret': 'S3VyaW9IYWNrYXRvbjIw',
                   'X-OS': 'android',
                   'X-App-Version': '1',
                   'Authorization': 'Bearer {}'.format(token),
                   }


        response = requests.get('https://hack.kurio.co.id/v1/feed/top_stories', headers=headers)
        articles = response.json()['data']
        for article in articles:
            response = requests.get('https://hack.kurio.co.id/v1/article/{}'.format(article['id']), headers=headers)
            content = (response.json()['content'][1]['text'])
            title = (response.json()['title'])
            user = User.objects.all()[0]
            blog, created = BlogPost.objects.get_or_create(title=title, user_id=user.id)
            blog.content = content
            blog.published_date = datetime.now()
            blog.status = 2

            img_url = response.json()['content'][0]['url']
            name = urlparse(img_url).path.split('/')[-1]
            content = urllib.request.urlopen(img_url).read()

            # problem: content must be an instance of File
            blog.featured_image.save(name, content, save=True)

            blog.save()

        print ('done')


def get_access_token():
    post_data = {"email": "alviandk@gmail.com",
                  "password": "thisisanisecurepassword",
                  "name": "John Derp"
                 }
    headers = {'Accept': 'application/json', 'X-Kurio-Client-ID': '99',
               'X-Kurio-Client-Secret': 'S3VyaW9IYWNrYXRvbjIw',
               'X-OS': 'android',
               'X-App-Version': '1' }
    response = requests.post('https://hack.kurio.co.id/v1/auth/login', data=json.dumps(post_data), headers=headers)
    kurio_token = response.json()['token']['access_token']
    return kurio_token
