import sys
import numpy as np
import pandas as pd

# print(sys.argv)

import pickle
'''
housing_median_age
total_rooms
total_bedrooms
population
households
median_income
ocean_proximity
'''
args = sys.argv
if len(args)!=8:
    print("Usage :")
    print(" python main.py <housing_median_age> <total_rooms> <total_bedrooms> <population> <households> <median_income> <ocean_proximity>")
    exit()

housing_median_age = float(args[1])
total_rooms        = float(args[2])
total_bedrooms     = float(args[3])
population         = float(args[4])
households         = float(args[5])
median_income      = float(args[6])
ocean_proximity    = float(args[7])

X = np.array([[housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity]])

# load model from saved file
f = open("LR_without_scaling.sav","rb")
model = pickle.load(f)
f.close()
median_house_price = model.predict(X)[0]

print("median house price for your home is $",median_house_price)
