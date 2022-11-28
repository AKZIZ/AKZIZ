import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

#option_s = st.checkbox(' US.')
#option_u = st.checkbox(' Japan.')
#option_v = st.checkbox(' Europe.')
#option1= [option_s,option_u,option_v]


#option_a=st.checkbox("cylinders")
#option_b=st.checkbox("hp")
#option_c=st.checkbox("weightlbs")
#option_d=st.checkbox("cubicinches")
#option2=[option_a,option_b,option_c,option_d]

option1 = st.sidebar.radio("choice a continent",
                    (' US.', ' Japan.', ' Europe.'))

option2 = st.sidebar.radio("choice a column",
                    ("cylinders","hp","weightlbs","cubicinches"))



df=pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

Histogramme_plotly = px.histogram(df[df["continent"]==option1], x=option2,nbins=20,
                   opacity=0.8)



Boxplot= plt.figure(figsize=(10,6))
sns.boxplot(x=df[option2])


tab1, tab2 = st.tabs(["Histogramme_plotly", "Boxplot_seaborn"])

with tab1:
   st.header("Histogramme_plotly")
   barplot_chart = st.write(Histogramme_plotly)

with tab2:
   st.header("Boxplot_seaborn")
   st.pyplot(Boxplot)







