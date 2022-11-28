
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

#HeatMap correlation
option= st.sidebar.selectbox(
	    'Choisir un continent',
	    (' US.', ' Japan.', ' Europe.'))


HeatMap= plt.figure(figsize=(14,9))
sns.heatmap((df[df["continent"]==option]).corr(), center=0,vmin=-1, vmax=1,cmap="rocket", annot=True)
sns.color_palette("rocket", as_cmap=True);




fig=sns.pairplot(df, hue="continent")


tab1, tab2 = st.tabs(["HeatMap", "Pairplot"])
with tab1:
   st.header("HeatMap")
   st.pyplot(HeatMap)

with tab2:
   st.header("Pairplot")
   st.pyplot(fig)

