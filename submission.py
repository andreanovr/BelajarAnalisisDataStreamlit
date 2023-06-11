import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
 
st.title('Summary Harbolnas 2017\n\n')

# Data Wrangling - Gathering Data
orderItemsData = pd.read_csv("https://github.com/andreanovr/BelajarAnalisisDataStreamlit/blob/main/data/orderItemsData.csv", delimiter=",", error_bad_lines = False)
orderPaymentsData = pd.read_csv("https://github.com/andreanovr/BelajarAnalisisDataStreamlit/blob/main/data/order_payments_dataset.csv", delimiter=",", error_bad_lines = False)
productsData = pd.read_csv("https://github.com/andreanovr/BelajarAnalisisDataStreamlit/blob/main/data/products_dataset.csv", delimiter=",", error_bad_lines = False)
newdf = pd.read_csv("https://github.com/andreanovr/BelajarAnalisisDataStreamlit/blob/main/data/newdf.csv", delimiter=",", error_bad_lines = False)

# Data Wrangling - Cleaning Data
productsData.dropna(axis=0, inplace=True)

# EDA - Question 1
firstTopProductCount = newdf[(newdf.product_id == "5094d0cb28a3e400d90c21c6df262856")].value_counts()
firstTopProductCountFix = firstTopProductCount["order_item_id"]
secondTopProduct = newdf[(newdf.product_id == "f71f42e2381752836563b70beb542f80")].value_counts()
secondTopProductFix = secondTopProduct["order_item_id"]
thirdTopProduct = newdf[(newdf.product_id == "28bdd20184e553872bab0ae75bbcaecf")].value_counts()
thirdTopProductFix = thirdTopProduct["order_item_id"]
otherProduct = newdf.groupby(['product_id']).value_counts()
otherProductsTotal = otherProduct["order_item_id"].sum()
otherProductExcludeTop3 = otherProductsTotal - (firstTopProductCountFix+secondTopProductFix+thirdTopProductFix)
firstTopProduct = productsData[(productsData.product_id == "5094d0cb28a3e400d90c21c6df262856")].product_category_name.values[0]
secondTopProduct = productsData[(productsData.product_id == "f71f42e2381752836563b70beb542f80")].product_category_name.values[0]
thirdTopProduct = productsData[(productsData.product_id == "28bdd20184e553872bab0ae75bbcaecf")].product_category_name.values[0]

# EDA - Question 2
boletoCount = newdf[newdf.payment_type=="boleto"].value_counts()
boletoCountFix = boletoCount["order_item_id"]
creditCardCount = newdf[newdf.payment_type=="credit_card"].value_counts()
creditCardCountFix = creditCardCount["order_item_id"]
debitCardCount = newdf[newdf.payment_type=="debit_card"].value_counts()
debitCardCountFix = debitCardCount["order_item_id"]
voucherCount = newdf[newdf.payment_type=="voucher"].value_counts()
voucherCountFix = voucherCount["order_item_id"]

# Visualization Question 1
st.subheader(
        """Q1 : Produk apakah yang banyak terjual pada Hari Belanja Online Nasional di tahun 2017? Dan berapakah perbandingannya?"""
    )

st.markdown("**Rasio Perbandingan Penjualan Produk Terlaris Dengan Produk Lainnya**")

flavor = (firstTopProduct, secondTopProduct, thirdTopProduct, 'Other Products')
votes1 = (firstTopProductCountFix, secondTopProductFix, thirdTopProductFix, otherProductExcludeTop3)
colors = ('#8B4513', '#ffbf47', '#93C572', '#E67F0D')
explode = (0.1, 0.1, 0.1, 0)

fig2, ax2 = plt.subplots() 
ax2.pie(
    x=votes1,
    labels=flavor,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)

st.pyplot(fig2)

st.write(
        """**Penjelasan** : Produk yang banyak terjual pada Hari Belanja Online Nasional di tahun 2017 adalah cool_stuff diikuti oleh informatica_acessorios dan utilidades_acessorios. Selanjutnya ketiga produk terlaris tersebut hanya menyumbang 5.3% saja dari total seluruh barang yang terjual pada hari itu."""
    )

# Visualization Question 2
st.subheader(
        """Q2 : Tipe pembayaran apa yang banyak digunakan pada Hari Belanja Online Nasional di tahun 2017? dan berapakah perbandingannya?"""
    )

flavors = ('Credit Card', 'Boleto', 'Debit Card', 'Voucher')
votes = (creditCardCountFix, boletoCountFix, debitCardCountFix, voucherCountFix)
colors = ('#8B4513', '#ffbf47', '#93C572', '#E67F0D')
explode = (0.1, 0.1, 0.1, 0.1)
 
fig3, ax3 = plt.subplots() 
ax3.pie(
    x=votes,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)

st.pyplot(fig3)

st.write(
        """**Penjelasan** : Jenis pembayaran yang paling banyak dilakukan pada Hari Belanja Online Nasional di tahun 2017 adalah Credit Card diikuti oleh Boleto, Voucher, dan Debit Card."""
    )