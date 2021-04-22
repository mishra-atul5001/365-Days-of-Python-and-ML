# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:08:21 2021

@author: Atul Mishra
"""

"""

Find Angle

Given a right angled triangle ABC, right angled at B. Find angle ABD, where D is the mid-point of the hypotenuse(side AC).
You will be given two integers denoting sides AB and BC respectively.
Round off your answer to the nearest Integer.

Input Format
First line will contain an Integer denoting side AB.
Second line will contain an Integer denoting side BC.


Constraints
1 <= side AB <= 200
1 <= side BC <= 200

Output Format
Output Angle ABD, rounded off to nearest integer.

Sample TestCase 1
Input:
6
6
Output:
45

"""

import math

def find_alpha_angle(AB,BC):
    tangent = BC/AB
    angle = str(int(math.degrees(math.atan(tangent)))) + ' degrees'
    # angle = str(int(math.degrees(math.atan2(AB,BC)))) + ' degrees' One more way
    return angle

print(find_alpha_angle(6,6))
# 45 degrees
print(find_alpha_angle(6,60))
# 84 degrees
print(find_alpha_angle(6,8))
# 53 degrees
print(find_alpha_angle(12,6))
# 26 degrees