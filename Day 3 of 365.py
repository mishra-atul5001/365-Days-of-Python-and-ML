# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 11:20:54 2021

@author: Atul Mishra
"""

"""

Virus Outbreak (100 Marks)

In the Martian land faraway, a new virus has evolved and is attacking the individuals at a fast pace. The scientists have figured out the virus composition, V. The big task is to identify the people who are infected. The sample of N people is taken to check if they are POSITIVE or NEGATIVE. A report is generated which provides the current blood composition B of the person. 

POSITIVE or NEGATIVE ?

If the blood composition of the person is a subsequence of the virus composition V, then the person is identified as POSITIVE otherwise NEGATIVE.

Example:

Virus Composition, V = coronavirus
Blood Composition of the person , B = ravus

The person in question is POSITIVE as B is the subsequence of the V. 

 
The scientists are busy with their research for medicine and request you to build a program which can quickly figure out if the person is POSITIVE or NEGATIVE. They will provide you with the virus composition V and all the people’s current blood composition. Can you help them?

Note: The virus and blood compositions are lowercase alphabet strings.

Input Format

The first line of the input consists of the virus composition, V
The second line of he input consists of the number of people, N
Next N lines each consist of the blood composition of the ith person, Bi


Constraints
1<= N <=10
1<= |B|<= |V|<= 10^5


Output Format
For each person, print POSITIVE or NEGATIVE in a separate line

Sample TestCase 1

Input:
coronavirus
3
abcde
crnas
onarous

Output:
NEGATIVE
POSITIVE
NEGATIVE
"""

def check_virus():

 # Write code here 
    print('Input Virus Strain')
    virus_strain=str(input())
    print('Input number of patients')
    num_patients=int(input())
    # h=[]
    virus_strain=virus_strain+virus_strain
    for i in range(num_patients):
        print('Input Blood Group:')
        patient_blood_group=str(input())
        po=0

        if(len(virus_strain)==0):
            print('NEGATIVE')
        elif(len(patient_blood_group)==0):
            print('POSITIVE')
        else:
            for k in range(len(patient_blood_group)):
                yu=virus_strain.find(patient_blood_group[k])
                if(yu>=po):
                    po=yu
                else:
                    print('NEGATIVE')
                    break
                if(k>=(len(patient_blood_group)-1)):
                    print('POSITIVE')



check_virus()