import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(
    page_title="Quete_streamlit",
    page_icon="👋",
)

option1 = st.sidebar.radio("choice a continent",
                    (' US.', ' Japan.', ' Europe.'))

option2 = st.sidebar.radio("choice a column",
                        ("cylinders","hp","weightlbs","cubicinches"))

selected2 = option_menu(None, ["Quete_streamlit", "Data", "Correlations", 'Distribution'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

selected2

if selected2 == "Quete_streamlit":

    st.header("Welcome to my Application streamlit! 👋")

    from PIL import Image
    image = Image.open('chartss.jpeg')

    st.image(image)

    st.sidebar.success("Select a demo above.")

elif selected2 == "Data":
    #import dataframe
    st.title("Pandas DataFrame")
    df=pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
    df
elif selected2== "Correlations":
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

elif selected2== 'Distribution':
    
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



