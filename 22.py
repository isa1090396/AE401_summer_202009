# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:15:38 2020

@author: carols1107
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
myId=mc.getPlayerEntityId('Id')
mc.postToTitle(myId,'你好')







