# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""


from mcpi.minecraft import Minecraft


mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
length = 30
height = 20
width = 40

block = 57
air = 0
lamp = 91

mc.setBlocks(x,y,z+length,y+height,z+width)
mc.setBlocks(x+1,y-1,z+1,x+length-1,y+height-1,z=width-1,air)
mc.setBlocks


        
       
                 