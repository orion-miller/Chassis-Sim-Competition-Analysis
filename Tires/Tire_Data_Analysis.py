import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

os.chdir("D:\\!Orion_Programs\\!Source_Controlled\\Chassis-Sim-Competition-Analysis\\Tires")

#load in data files
df_SA_Curve = pd.read_csv("Front_Tire - SA_Curve.csv")
df_Load_Dep = pd.read_csv("Front_Tire - Load_Dep.csv")
df_FY_IA_Dep = pd.read_csv("Front_Tire - FY_IA_Dep.csv")
df_FX_IA_Dep = pd.read_csv("Front_Tire - FX_IA_Dep.csv")
df_Friction_Circle = pd.read_csv("Front_Tire - Friction_Circle.csv")

#calculate mu for load dep so we can see the sensitivity better, use their "FFact" naming
df_Load_Dep['FFact (-)'] = df_Load_Dep['Fy (kgf)']/df_Load_Dep['Fz (kgf)']

#put camber dep from FX in with FY to plot them together
df_FY_IA_Dep.rename(columns = {'FFact (-)':'FFact Y (-)'}, inplace=True)
df_FY_IA_Dep['FFact X (-)'] = df_FX_IA_Dep['FFact (-)'].copy()

#plot datasets
fig_SA_Curve = px.line(df_SA_Curve,x='SA (deg)',y='FFact (-)',template="plotly_dark",title="Relative Mu-Y vs. Slip Angle",width=600, height=400)
fig_SA_Curve.write_html("fig_SA_Curve.html", auto_open=True)

fig_Load_Dep = px.line(df_Load_Dep,x='Fz (kgf)',y='FFact (-)',template="plotly_dark",title="Relative Mu-Y vs. Load",width=600, height=400)
fig_Load_Dep.write_html("fig_Load_Dep.html", auto_open=True)

fig_FY_IA_Dep = px.line(df_FY_IA_Dep,x='Camber (deg)',y=['FFact Y (-)','FFact X (-)'],template="plotly_dark",title="Relative Mu vs. Camber",width=600, height=400)
fig_FY_IA_Dep.write_html("fig_FY_IA_Dep.html", auto_open=True)

# fig_FX_IA_Dep = px.line(df_FX_IA_Dep,x='Camber (deg)',y='FFact (-)',template="plotly_dark",title="Relative Mu-X vs. Camber",width=600, height=400)
# fig_FX_IA_Dep.write_html("fig_FX_IA_Dep.html", auto_open=True)

fig_Friction_Circle = px.line(df_Friction_Circle,x='Fy (kgf)',y='Fx (kgf)',template="plotly_dark",title="Traction Circle",width=600, height=400)
fig_Friction_Circle.write_html("fig_Friction_Circle.html", auto_open=True)