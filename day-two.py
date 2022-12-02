# Rock defeats scissors, Scissors defeats paper, Paper defeats rock
# If both players choose the same one - game ends
# First column => A - rock, B - paper, C - scissors => what the opponent will play
# Second column => X - rock, Y - paper , Z - scissors => 
# Score => 0 - loss, 3 - draw, 6 - won
# Score 2 => 1 - rock, 2 - paper, 3 - scissors

import requests

url = "https://adventofcode.com/2022/day/2/input"
cookies_dict = {"_ga":"GA1.2.1715713647.1668774730",
        "_gid":"GA1.2.879699370.1669870657",
        "session":"53616c7465645f5fdb7c5d0c72a2fcd21a9cf468073936223cddc04755ed890710b7f589202cb44560dd18694fc78c8d5ed6ab4d7ef8202932662aea1104f713"}

wamuyu_it = {"session":"53616c7465645f5fbc56bb64ffea96061d1dae3f8966f25b11375718a41120d6617d9c76278584cd6318f56db3da6b9eebbbfa04d878003bf90767fdbc946468"}

first_column:dict = {"A":1, "B":2, "C":3}
second_column = {"X":1, "Y":2, "Z":3} 
win_loss = {"loss":0, "draw":3, "win":6}


second_column_fat= {"X":"L", "Y":"D", "Z":"W"} 
draw ={"A":"X", "B":"Y", "C":"Z"}
loose ={"A":"Z", "B":"X", "C":"Y"}
win ={"A":"Y", "B":"Z", "C":"X"}
 

def read_input(url:str, cookies_dict:dict)->list:
    input_file = requests.get(url, cookies=cookies_dict)
    list_input = input_file.text.split('\n')
    return list_input

def rock_paper_scissors(list_input:list)-> int:
   
    opponent = 0 # 0 
    me = 0 # 2

    for input in list_input: 
        split_input = input.split(' ')
        if is_win(split_input) :
            opponent = opponent + first_column[split_input[0]] + win_loss["win"]
            me = me + second_column[split_input[1]] + win_loss["loss"]
            
        elif is_draw(split_input):
            #implementation
            opponent = opponent + first_column[split_input[0]] + win_loss["draw"]
            me = me + second_column[split_input[1]] + win_loss["draw"]
            
        elif is_lost(split_input):
            opponent = opponent + first_column[split_input[0]] + win_loss["loss"]
            me = me + second_column[split_input[1]] + win_loss["win"]
    return me

def actual_game(list_input:list):
    me = 0 # 2
    nwpair =list()
    for input in list_input: 
        if input == '' : continue
        split_input = input.split(' ')
        outcome = second_column_fat[split_input[1]]
        if outcome == "L":
            picked_ans = loose[split_input[0]]
            nwpair.insert(0,  split_input[0] )
            nwpair.insert(1,  picked_ans)
        elif outcome == "D":
            picked_ans = draw[split_input[0]]
            nwpair.insert(0,  split_input[0] )
            nwpair.insert(1,  picked_ans)
        elif outcome == "W":
            picked_ans = win[split_input[0]]
            nwpair.insert(0,  split_input[0] )
            nwpair.insert(1,  picked_ans)

        me += calculate_score(nwpair)
    return me
    
def calculate_score(split_input:list):
    opponent = 0 # 0 
    me = 0 # 2
    if is_win(split_input) :
            opponent = opponent + first_column[split_input[0]] + win_loss["win"]
            me = me + second_column[split_input[1]] + win_loss["loss"]
            
    elif is_draw(split_input):
            opponent = opponent + first_column[split_input[0]] + win_loss["draw"]
            me = me + second_column[split_input[1]] + win_loss["draw"]
            
    elif is_lost(split_input):
            opponent = opponent + first_column[split_input[0]] + win_loss["loss"]
            me = me + second_column[split_input[1]] + win_loss["win"]
    return me
def is_draw(play_pair:list)->bool:
    # A(rock) draws with rock (X)
    # B(paper) draws with paper (Y)
    # C(scissors) draws with scissors (Z)
    t=  True if (play_pair[0] == 'A' and play_pair[1] == 'X') or (play_pair[0] == 'B' and play_pair[1] == 'Y') or (play_pair[0] == 'C' and play_pair[1] == 'Z') else  False
    return t
def is_win(play_pair:list)->bool:
    # A(rock) trumps over scissors (Z)
    # B(paper) trumps over rock (X)
    # C(scissors) trumps over paper (Y)
    t=  True if (play_pair[0] == 'A' and play_pair[1] == 'Z') or (play_pair[0] == 'B' and play_pair[1] == 'X') or (play_pair[0] == 'C' and play_pair[1] == 'Y') else  False
    return t
def is_lost(play_pair:list)->bool:
    # A(rock) loses to paper (Y)
    # B(paper) loses to scissors(Z)
    # C(scissors) loses to rock (X)
    t=  True if (play_pair[0] == 'A' and play_pair[1] == 'Y') or (play_pair[0] == 'B' and play_pair[1] == 'Z') or (play_pair[0] == 'C' and play_pair[1] == 'X') else  False
    return t

print(actual_game(read_input(url, cookies_dict)))
print(rock_paper_scissors(read_input(url, cookies_dict)))