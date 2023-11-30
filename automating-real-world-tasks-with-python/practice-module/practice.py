# Thursday 23/11/2023 9:24
# Practice.py

import requests
import json

def retreive_reviews():
    with open('reviews.json', 'w') as reviews_json:
        reviews = json.load(reviews_json)
        review_post = requests.post('192.168.1.1', json=reviews)