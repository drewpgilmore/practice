#! /usr/bin/python3
# inputs.py -- reads input data for advent of code

import requests
import json
from config import SESSION

base = 'https://adventofcode.com/2022/day'
cookies = {
    'session': SESSION
}


def readInputs(day:int) -> list: 
    url = f'{base}/{day}/input'
    response = requests.get(url, cookies=cookies)
    data = response.content.decode('UTF-8')
    lines = data.split('\n')

    return lines[:-1]
