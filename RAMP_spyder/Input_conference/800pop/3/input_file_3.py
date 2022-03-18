# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:28:30 2022

@author: pietr
"""
'''
Paper: Energy sufficiency, lowlands.
User: Low Income Household
'''

from core import User, np
User_list = []

###### COMMUNITY SERVICES ######

#Definig users

Public_lighting = User("Public lighting ", 26)
User_list.append(Public_lighting)

#Appliances

Public_lighting_lamp_post = Public_lighting.Appliance(Public_lighting,12,40,2,310,0,300, 'yes', flat = 'yes')
Public_lighting_lamp_post.windows([0,362],[1082,1440],0.1)


WSS = User("water supply system", 3)
User_list.append(WSS)

#Appliances

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)

#Definig users

SC = User("School type C", 1)
User_list.append(SC)

#Appliances

SC_indoor_bulb = SC.Appliance(SC,27,7,1,60,0.2,10)
SC_indoor_bulb.windows([480,780],[0,0],0.35)

SC_outdoor_bulb = SC.Appliance(SC,7,13,1,60,0.2,10)
SC_outdoor_bulb.windows([480,780],[0,0],0.35)

SC_TV = SC.Appliance(SC,5,60,1,120,0.1,5, occasional_use = 0.5)
SC_TV.windows([480,780],[0,0],0.35)

SC_radio = SC.Appliance(SC,24,4,1,120,0.1,5, occasional_use = 0.5)
SC_radio.windows([480,780],[0,0],0.35)

SC_DVD = SC.Appliance(SC,2,8,1,120,0.1,5, occasional_use = 0.5)
SC_DVD.windows([480,780],[0,0],0.35)

SC_Freezer = SC.Appliance(SC,1,200,1,1440,0,30, 'yes',3)
SC_Freezer.windows([0,1440])
SC_Freezer.specific_cycle_1(200,20,5,10)
SC_Freezer.specific_cycle_2(200,15,5,15)
SC_Freezer.specific_cycle_3(200,10,5,20)
SC_Freezer.cycle_behaviour([580,1200],[0,0],[510,579],[0,0],[0,509],[1201,1440])

SC_PC = SC.Appliance(SC,25,50,1,210,0.1,10)
SC_PC.windows([480,780],[0,0],0.35)

SC_Phone_charger = SC.Appliance(SC,5,2,1,180,0.2,5)
SC_Phone_charger.windows([480,780],[0,0],0.35)

SC_Printer = SC.Appliance(SC,1,20,1,30,0.1,5)
SC_Printer.windows([480,780],[0,0],0.35)

SC_Stereo = SC.Appliance(SC,1,150,1,90,0.1,5, occasional_use = 0.33)
SC_Stereo.windows([480,780],[0,0],0.35)

SC_data = SC.Appliance(SC,1,420,1,60,0.1,5, occasional_use = 0.33)
SC_data.windows([480,780],[0,0],0.35)


