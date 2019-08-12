#!/usr/bin/python3

#### execute this program like below
#### python3 -m pdb <filename.py>

def yes_or_no():
    answer=input("please enter yes or no")
    while answer.lower() != 'yes' and answer.lower() != 'no':
        answer=input("please enter yes or no")
    return answer.lower()

yes_or_no()
