# function to read data 

# main logic 
    # sum input until encounter a space 
    
import pandas as pd
import requests
from io import StringIO

url = "https://adventofcode.com/2022/day/1/input"

cookies_dict = {"_ga":"GA1.2.1715713647.1668774730", 
                "_gid":"GA1.2.879699370.1669870657",
                "session": "53616c7465645f5fdb7c5d0c72a2fcd21a9cf468073936223cddc04755ed890710b7f589202cb44560dd18694fc78c8d5ed6ab4d7ef8202932662aea1104f713"}

def read_input(url:str)->list:
    input_file = requests.get(url, cookies=cookies_dict)
    list_input = input_file.text.split('\n')
    return list_input

def max_value(list_input:list):
    max_no = []
    sum = 0
    for item in list_input:
        if item != '':
            sum += int(item)
        else:
            max_no.append(sum)
            sum = 0
    max_no.sort(reverse=True)
    print(max_no[0:3])
    return max_no[0:3]

print(sum(max_value(read_input(url))))