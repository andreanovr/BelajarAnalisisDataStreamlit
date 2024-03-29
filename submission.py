import streamlit as st 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
 
st.title('Summary Harbolnas 2017\n\n')

# Data Wrangling - Gathering Data
# orderItemsData = pd.read_csv(r"C:\Users\User\Downloads\Submission\data\order_items_dataset.csv", delimiter=",")
# orderPaymentsData = pd.read_csv(r"C:\Users\User\Downloads\Submission\data\order_payments_dataset.csv", delimiter=",")
# productsData = pd.read_csv(r"C:\Users\User\Downloads\Submission\data\products_dataset.csv", delimiter=",")

orderItemsData = pd.read_csv("https://raw.githubusercontent.com/andreanovr/BelajarAnalisisDataStreamlit/main/data/order_items_dataset.csv", delimiter=",")
orderPaymentsData = pd.read_csv("https://raw.githubusercontent.com/andreanovr/BelajarAnalisisDataStreamlit/main/data/order_payments_dataset.csv", delimiter=",")
productsData = pd.read_csv("https://raw.githubusercontent.com/andreanovr/BelajarAnalisisDataStreamlit/main/data/products_dataset.csv", delimiter=",")

# Data Wrangling - Cleaning Data
productsData.dropna(axis=0, inplace=True)

# EDA - Mengubah timestamp menjadi format tanggal pada kolom shipping_limit_date
orderItemsData['shipping_limit_date'] = pd.to_datetime(orderItemsData['shipping_limit_date'])
orderItemsData['shipping_limit_date'] = orderItemsData['shipping_limit_date'].dt.normalize()
orderItemsData['shipping_limit_date'] = orderItemsData['shipping_limit_date'].dt.floor('D')

# EDA - Merger dataset orderItemsData dan orderPaymentsData
orders_items_payments_data = pd.merge(
    left=orderItemsData,
    right=orderPaymentsData,
    how="outer",
    left_on="order_id",
    right_on="order_id"
)

# EDA - Filter Data
newdf = orders_items_payments_data[(orders_items_payments_data.shipping_limit_date == "2017-12-12")]

# EDA - Question 1
firstTopProductCountFix = (newdf["product_id"] == "5094d0cb28a3e400d90c21c6df262856").sum()
secondTopProductFix = (newdf["product_id"] == "f71f42e2381752836563b70beb542f80").sum()
thirdTopProductFix = (newdf["product_id"] == "f71f42e2381752836563b70beb542f80").sum()
otherProduct = newdf.groupby(['product_id']).count()
otherProductsTotal = otherProduct["order_item_id"].sum()
otherProductExcludeTop3 = otherProductsTotal - (firstTopProductCountFix+secondTopProductFix+thirdTopProductFix)
firstTopProduct = productsData[(productsData.product_id == "5094d0cb28a3e400d90c21c6df262856")].product_category_name.values[0]
secondTopProduct = productsData[(productsData.product_id == "f71f42e2381752836563b70beb542f80")].product_category_name.values[0]
thirdTopProduct = productsData[(productsData.product_id == "f71f42e2381752836563b70beb542f80")].product_category_name.values[0]

# EDA - Question 2
boletoCount = newdf[newdf.payment_type=="boleto"].count()
boletoCountFix = boletoCount["order_item_id"]
creditCardCount = newdf[newdf.payment_type=="credit_card"].count()
creditCardCountFix = creditCardCount["order_item_id"]
debitCardCount = newdf[newdf.payment_type=="debit_card"].count()
debitCardCountFix = debitCardCount["order_item_id"]
voucherCount = newdf[newdf.payment_type=="voucher"].count()
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