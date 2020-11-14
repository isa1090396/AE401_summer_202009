# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
t=0
while True:
    t=t+1
    mc.postToChat(
    "You are located on X:"+
        str(x)+
        ",Y:" +
        str(y)+
         ",Z:"+
        str(Z))
         
        
    