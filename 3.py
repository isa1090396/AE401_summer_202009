# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""


from mcpi.minecraft import Minecraft


mc=Minecraft.create()

x,y,z = mc.player.getTilePos()
blockId = int(input('要放甚麼方塊呢'))
mc.setBlock(x,y,z,blockId)
        
       
                 