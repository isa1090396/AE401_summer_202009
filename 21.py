# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""
from random import randrange
from time import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
ans = randrange(100000001)
def linearSearch():
    for i in range(100000001):
        if i == ans:
            print('答案是'+ str(i))
            print('跑了' + str(time()-startTime))
def BinearySearch():
    startTime = time()
    lower = 0
    upper = 100000000
    while lower<= upper:
        mid = (lower + upper)//2
        if ans < mid:
            upper = mid - 1
        elif ans > mid:
            lower = mid+1
        else:
             print('答案是'+ str(mid))
             print('跑了' + str(time()-startTime))
             break
LinearSearch()
BinearySearch()         
            


            
            
            
            


            
            

        
        



        
        
        
    


        
       
                 