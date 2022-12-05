# the length of the item
# Split it in half by slicing
# match first item with second using re.findall
# assign common characters a priority
# a - z is 1 to 26
# A - Z is 27 to 52

import requests
url = "https://adventofcode.com/2022/day/3/input"
cookies_dict = {"_ga":"GA1.2.1715713647.1668774730",
 "_gid":"GA1.2.879699370.1669870657",
"session":"53616c7465645f5fdb7c5d0c72a2fcd21a9cf468073936223cddc04755ed890710b7f589202cb44560dd18694fc78c8d5ed6ab4d7ef8202932662aea1104f713"}
wamuyu_ooki = {"session":"53616c7465645f5fbc56bb64ffea96061d1dae3f8966f25b11375718a41120d6617d9c76278584cd6318f56db3da6b9eebbbfa04d878003bf90767fdbc946468"}

type_priorities = {chr(i+96):i for i in range(1,27)}
type_priorities.update( {chr(i+38):i for i in range(27,53)})

def read_input(url:str, cookies_dict:dict)->list:
    input_file = requests.get(url, cookies=cookies_dict)
    list_input = input_file.text.split('\n')
    return list_input

def split_item(list_input:list)->int:
    sum = 0
    for item in list_input:
        firstpart, secondpart = item[:len(item)//2], item[len(item)//2:]
        common_types = set(firstpart).intersection(secondpart)
        if common_types is None:
            continue
        sum += type_priorities.get(min(common_types))
    return sum

def part_two(list_input:list):
    sum = 0
    for group in chunker(list_input, 3):
        common_types = set(group[0]).intersection(group[1]).intersection(group[2])
        if common_types is None:
            continue
        sum += type_priorities.get(min(common_types))
        print(sum)

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
        
# split_item(read_input(url, wamuyu_ooki))
part_two(read_input(url, wamuyu_ooki ))

