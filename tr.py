import requests
def read_input(url:str , cookies_dict)->list:
    input_file = requests.get(url, cookies=cookies_dict)
    list_input = input_file.text.split('\n')
    return list_input