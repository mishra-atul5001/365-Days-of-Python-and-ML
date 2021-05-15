# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:25:37 2021

@author: Atul Mishra
"""

'''
Climbing the Leaderboard

An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 1 on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

Example

ranked = [100,90,90,80]
player = [70,80,105]

The ranked players will have ranks 1,2 ,2 , and 3, respectively. If the player's scores are 70, 80 and 105, their rankings after each game are 4th, 3rd and 1st. 
Return [4,3,1].
'''


def climbingLeaderboard(scores,alice):
    currentrank = len(set(scores))
    score_index = 0
    highscore_index = len(scores)-1
    print(highscore_index)
    while score_index!=len(alice):
        while alice[score_index] > scores[highscore_index] and highscore_index>-1:
            highscore_index-=1
            print(highscore_index)
            if scores[highscore_index]!=scores[highscore_index+1]:
                currentrank-=1
                print(currentrank)
        if alice[score_index] == scores[highscore_index]:
            yield currentrank 
        else:
            yield currentrank+1
        score_index+=1
        print(score_index)

print(*climbingLeaderboard([100 ,90 ,90 ,80, 75, 60],[50 ,65, 77, 90, 102]))