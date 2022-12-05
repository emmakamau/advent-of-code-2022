# Read input, loop input and split at "," -> list[raneg1, range2]
# Split range1 at the "-", range(start, stop)
# {range1:[1,2,3]}, {range}

from tr import read_input

url ="https://adventofcode.com/2022/day/4/input"
cookies_dict ={"_ga":"GA1.2.1715713647.1668774730",
 "_gid":"GA1.2.879699370.1669870657",
  "session":"53616c7465645f5fdb7c5d0c72a2fcd21a9cf468073936223cddc04755ed890710b7f589202cb44560dd18694fc78c8d5ed6ab4d7ef8202932662aea1104f713"}

wamuyu_ooki = {"session":"53616c7465645f5fbc56bb64ffea96061d1dae3f8966f25b11375718a41120d6617d9c76278584cd6318f56db3da6b9eebbbfa04d878003bf90767fdbc946468"}
def find_overlaps(url, cookies_dict):
    data = read_input(url, cookies_dict)
    new_data = data[:-1]
    count_a = 0
    count_b = 0

    for item in new_data:
        batches = item.rstrip().split(',')
        x1, y1 = list(map(int, batches[0].split("-")))
        x2, y2 = list(map(int, batches[1].split("-")))
        if (x1 <= x2 and y2 <= y1) or (x2 <= x1 and y1 <= y2):
            count_a += 1 

        if (x2 <= y1 and y2 >= x1) or (x1 <= y2 and y1 >= x2):
            count_b += 1
    print(count_a, count_b)
find_overlaps(url, cookies_dict)