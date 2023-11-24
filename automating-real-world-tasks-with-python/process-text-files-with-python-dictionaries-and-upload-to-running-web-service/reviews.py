# Thursday 23/11/2023 09:54 AM to 12:59 PM

#! /usr/bin/env python3
import os
import requests
def read_reviews():
    review_list = os.listdir('/data/feedback')
    review_json = []

    for review_file in review_list:
        with open('/data/feedback/' + review_file, 'r') as review:
            review_json.append({"title": review.readline(), "name": review.readline(), "date": review.readline(), "feedback": review.readline()})
    
    return review_json

def post_reviews():
    response = requests.post('http://104.196.238.159/feedback/', json=read_reviews)        
    try:
        response.raise_for_status()
    except Exception as e:
        print('POST Failed with status code')
    else:
        print('POST successful!')

if __name__ == '__main__':
    post_reviews()
