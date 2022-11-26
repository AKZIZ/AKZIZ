import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import dataframe
st.title("Pandas DataFrame")
df=pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
df

