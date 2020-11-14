# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""


from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()


time.sleep(5)
x,y,z = mc.player.getTailePos()

mc.setBlock(x,y,z,129)
time.sleep(1)
mc.setBlock(x,y+1,z,129)
time.sleep(1)
mc.setBlock(x,y+2,z,129)
time.sleep(1)
mc.setBlock(x,y+3,z,129)
time.sleep(1)
mc.setBlock(x,y+4,z,129)
time.sleep(1)
mc.setBlock(x,y+5,z,129)
time.sleep(1)
mc.setBlock(x,y+6,z,129)
time.sleep(1)
mc.setBlock(x,y+7,z,129)
time.sleep(1)


        
       
        
         