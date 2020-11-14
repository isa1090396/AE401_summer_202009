# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""


from mcpi.minecraft import Minecraft


mc = Minecraft.create()
x,y,z = mc.player.getTilePos() 

mc.setBlocks(x,y+3,z,x+2,y+3+2,z+2,18)
mc.setBlocks(x+1,y,z+1,x+1,y+4,z+1,17)
  
  
    
        
       
        
        
      
        
        
        
    


        
       
                 