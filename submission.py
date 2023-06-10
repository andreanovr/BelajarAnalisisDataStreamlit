import streamlit as st 
import matplotlib.pyplot as plt
 
st.title('Summary Harbolnas 2017\n\n')

st.subheader(
        """Q1 : Produk apakah yang banyak terjual pada Hari Belanja Online Nasional di tahun 2017? dan berapakah persentasenya dengan penjualan produk lain?"""
    )

st.markdown("**Rasio Perbandingan Penjualan Produk Terlaris Dengan Produk Lainnya (Harga)**")

flavors = ('Cool Stuff', 'Other Product')
votes = ('231.0', '43213.23')
colors = ('#ffbf47', '#fffa6b')
explode = (0.1, 0)

fig1, ax1 = plt.subplots() 
ax1.pie(
    x=votes,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)

st.pyplot(fig1)

st.markdown("**Rasio Perbandingan Penjualan Produk Terlaris Dengan Produk Lainnya (Kuantitas)**")

votes2 = ('7', '351')
fig2, ax2 = plt.subplots() 
ax2.pie(
    x=votes2,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)

st.pyplot(fig2)

st.write(
        """**Penjelasan** : Produk yang banyak terjual pada Hari Belanja Online Nasional di tahun 2017 adalah cool stuff. Lalu secara kuantitas, produk tersebut hanya memiliki bagian 0.5% dari produk lainnya yang terjual di hari itu. Dan secara keuangan, produk tersebut hanya menyumbang 2% saja dari total pembelian di hari tersebut."""
    )

st.subheader(
        """Q2 : Tipe pembayaran apa yang banyak digunakan pada Hari Belanja Online Nasional di tahun 2017? dan berapakah perbandingannya?"""
    )

flavors = ('Credit Card Type', 'Other Payment Type')
votes3 = ("242", "116")
colors = ('#ffbf47', '#fffa6b')
explode = (0.1, 0)
 
fig3, ax3 = plt.subplots() 
ax3.pie(
    x=votes3,
    labels=flavors,
    autopct='%1.1f%%',
    colors=colors,
    explode=explode
)

st.pyplot(fig3)

st.write(
        """**Penjelasan** : Jenis pembayaran yang paling banyak dilakukan pada Hari Belanja Online Nasional di tahun 2017 adalah Credit Card."""
    )