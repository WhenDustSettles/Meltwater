import os 
import pandas as pd
import matplotlib.pyplot as plt
desktop = "C:/Users/Animesh/Desktop"
csv_path = os.path.join(desktop,"Beats.csv") 
beats = pd.read_csv(csv_path)
beats.plot(kind = "kde",x = "beat",y = "num")
fig = beats.plot(kind = "bar",x = "beat",y = "num")
fig.tick_params(axis = 'both', which = 'major', labelsize = 5)
fig.tick_params(axis = 'both', which = 'minor', labelsize = 8)