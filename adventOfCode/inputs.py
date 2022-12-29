#! /usr/bin/python3
# inputs.py -- reads input data for advent of code

import requests
import json

base = 'https://adventofcode.com/2022/day'
SESSION = '53616c7465645f5f4a288f2160790314a1423495e88d3a2c07bb214a6f04d7ff5f423d89297d727bb0ba0bb74d19d4bb8b4ac43f17794fda84140277dc13ad1e'
cookies = {
    'session': SESSION
}


def readInputs(day:int) -> list: 
    url = f'{base}/{day}/input'
    response = requests.get(url, cookies=cookies)
    data = response.content.decode('UTF-8')
    lines = data.split('\n')

    return lines[:-1]