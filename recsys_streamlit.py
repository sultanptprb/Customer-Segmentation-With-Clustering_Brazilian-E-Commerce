import pandas as pd
import numpy as np
import surprise
import pickle
import streamlit as st


# Menampilkan DataFrame
df_recsys = pd.read_csv('D:\Purwadhika\Data_Science\Final_Project_PWDK_JCDS\dataset\df_recsys.csv')

# MEMBUAT PREDIKSI
with open(r'D:\Purwadhika\Data_Science\Final_Project_PWDK_JCDS\dataset\recsys_modell', 'rb') as f:
    final_model = pickle.load(f)

df_recsys_streamlit = df_recsys.groupby('product_category_name_english', as_index= False)[['review_score']].sum()
df_recsys_streamlit = df_recsys_streamlit[['product_category_name_english']]

df_result = pd.DataFrame(columns=['customer_unique_id', 'category'])

st.title('''
    REKOMENDASI PRODUCT CATEGORY
''')

st.write('Ini adalah aplikasi prediksi untuk menentukan kebutuhan produk anda')

customer_unique_id = st.sidebar.selectbox('customer_unique_id', df_recsys['customer_unique_id'])

# mengisi dataframe dengan user dan item yang akan diprediksi
df_result['customer_unique_id'] = [customer_unique_id] * 71
df_result['category'] = df_recsys_streamlit

# menghitung rating untuk tiap film yang akan diprediksi
list_rating = []

for index, value in df_result.iterrows():
  list_rating.append(final_model.predict(value['customer_unique_id'], value['category'])[3])

# menambahkan kolom rating
df_result['rating'] = list_rating

# mengurutkan berdasarkan rating untuk tiap user-
df_result.sort_values('rating', ascending=False)

st.dataframe(df_result[['category', 'rating']].sort_values('rating', ascending=False).reset_index(drop=True), width=999999999)
hasil = df_result.sort_values('rating', ascending=False).reset_index()['category'].iloc[0]

# Membuat hasil rekomendasi sebagai deskripsi
st.write(f'Produk yang kami rekomendasikan untuk id {customer_unique_id} adalah kategori "{hasil}" berdasarkan rating historis anda')
