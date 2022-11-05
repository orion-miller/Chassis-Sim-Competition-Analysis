import os
import pandas as pd
# import numpy as np
import plotly.express as px
# import seaborn as sns

os.chdir("D:\\!Orion_Programs\\!Source_Controlled\\Chassis-Sim-Competition-Analysis\\Tires")

#load in data files
df_SA_Curve = pd.read_csv("Front_Tire - SA_Curve.csv")
df_Load_Dep = pd.read_csv("Front_Tire - Load_Dep.csv")
df_FY_IA_Dep = pd.read_csv("Front_Tire - FY_IA_Dep.csv")
df_FX_IA_Dep = pd.read_csv("Front_Tire - FX_IA_Dep.csv")
df_Friction_Circle = pd.read_csv("Front_Tire - Friction_Circle.csv")

fig_SA_Curve = px.line(df_SA_Curve,x='SA',y='FFact',template="plotly_dark",title="Relative Mu vs. Slip Angle",width=600, height=400)
fig_SA_Curve.show()