import os
import streamlit as st
import pandas as pd


def save_uploadedfile(uploadedfile):
     with open('rawdata.xlsx',"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

datafile = st.file_uploader("Upload CSV",type=['xlsx'])


if datafile is not None:
    file_details = {"FileName":datafile.name,"FileType":datafile.type}
    df  = pd.read_excel(datafile)
    st.dataframe(df)
    save_uploadedfile(datafile)

else:
    df = pd.read_excel('rawdata.xlsx')
    st.dataframe(df)