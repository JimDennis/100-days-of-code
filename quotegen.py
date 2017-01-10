#!/usr/bin/env python
import json
import random
from bottle import Bottle, route, run
with open('./quotes.json','r') as data:
    quotes = json.load(data)
    
@route('/phrase/latin')
def index():
    return random.choice(quotes)
    
run(host='localhost', port=8888)
