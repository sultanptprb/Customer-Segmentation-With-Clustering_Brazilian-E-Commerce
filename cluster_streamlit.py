import pandas as pd
import pickle
import streamlit as st

st.title('''
    TABEL SEGMENTASI CUSTOMER
''')


# Menampilkan DataFrame
df_clustering = pd.read_csv('D:\Purwadhika\Data_Science\Final_Project_PWDK_JCDS\dataset\df_final_dataset.csv')

customer_unique_id = st.sidebar.selectbox('customer_unique_id', df_clustering['customer_unique_id'])

df_clustering = df_clustering[df_clustering['customer_unique_id']==customer_unique_id]

kelompok = df_clustering['cluster'].iloc[0]

st.dataframe(df_clustering.T, width=999999999)

st.subheader("Cluster")
st.write(f"customer_unique_id {customer_unique_id} :")

if kelompok == 2:
    st.write("Kelas 2, perusahaan direkomendasikan untuk melakukan pendekatan marketing")
    st.write("Menerapkan Unique Selling Preposition Communication Campaign")
if kelompok == 1:
    st.write("Kelas 1, perusahaan direkomendasikan untuk melakukan pendekatan marketing")
    st.write("Menerapkan Marketing with Storytelling")
elif kelompok == 0 :
    st.write("Kelas 0, perusahaan direkomendasikan untuk melakukan pendekatan marketing")
    st.write("Menerapkan Key Opinion Leader Deployment")

