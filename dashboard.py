import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

#membaca file csv data yang sudah bersih
gabungan_data = pd.read_csv("D:/kuliah/SMT 6/Machine Learning/submission/dashboard/all_data.csv")
print(gabungan_data)
gabungan_data.head()

#membuat dataframe data 2012
data2012 = gabungan_data[gabungan_data.yr_x == 1]
data2012.head()

#membuat dataframe data 2011
data2011 = gabungan_data[gabungan_data.yr_x == 0]
data2011.head()

#membuat dataframe data yang dikelompokkan berdasarkan musim
data2 = data2012.groupby(by = 'season_x').agg({
    'cnt_y' : 'sum',
})

#menambahkan gambar sebagai header
st.image("header.jpeg", width=700)

#membuat judul
st.header("Bike-Sharing Rental :bike:")

#menambahkan deskripsi
st.markdown('<div style="text-align: justify;">Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back at another position. Today, there exists great interest in these systems due to their important role in traffic, environmental and health issues. Bike sharing system can be used for sensing mobility in the city.</div>', unsafe_allow_html=True)
st.markdown(f"###")

#membuat statistik 2012 berupa jumlah penyewaan, banyak registered user, dan casual user
st.subheader("2012's Statistics")
 
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = data2012.cnt_y.sum()
    st.metric("Total orders", value=total_orders)
 
with col2:
    total_reg_users = data2012.registered_y.sum()
    st.metric("Total Registered Users", value=total_reg_users)

with col3:
    total_cas_users = data2012.casual_y.sum()
    st.metric("Total Casual Users", value=total_cas_users)


#grafik 1
fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#F9E897"]
sns.barplot(
    y="registered_y",
    x="mnth_x",
    data=data2012.sort_values(by="mnth_x", ascending=True),
    palette=colors,
    ax=ax,
)
colors = ["#FFC374"]
sns.barplot(
    y="casual_y",
    x="mnth_x",
    data=data2012.sort_values(by="mnth_x", ascending=True),
    palette=colors,
    ax=ax,
)
ax.set_title("Users per Month in 2012", loc = "center", fontsize=35)
ax.set_ylabel("Users", size = 25)
ax.set_xlabel("Months in Year", size = 25)
ax.tick_params(axis="x", labelsize=20)
ax.tick_params(axis="y", labelsize=20)
ax.legend(['Registered Users','Casual Users'])
st.pyplot(fig)

#grafik 2
fig2, ax2 = plt.subplots(figsize=(8, 4))
colors = ["#F9E897", "#124076", "#7F9F80", "#FFC374"]
plt.pie(x = data2["cnt_y"],
        autopct='%1.0f%%', colors=colors, labels=["Spring","Summer","Fall","Winter"])
ax2.set_title("Bike Rental per Season in 2012", loc = "center", fontsize=10)
st.pyplot(fig2)

#grafik 3
fig3, ax3 = plt.subplots(figsize=(16, 8))
colors = ["#F9E897"]
sns.barplot(
    y="cnt_y",
    x="weathersit_x",
    data=data2012.sort_values(by="weathersit_x", ascending=True),
    palette=colors,
    ax=ax3
)
ax3.set_title("Bike Rented by Weathersit", loc = "center", fontsize=35)
ax3.set_ylabel("Bike rented", size = 25)
ax3.set_xlabel("Weathersit", size = 25)
ax3.tick_params(axis="x", labelsize=20)
ax3.tick_params(axis="y", labelsize=20)
ax3.legend(loc="upper left", bbox_to_anchor=(1, 1))
st.pyplot(fig3)

#membuat penjelasan mengenai weathersit sesuai kategori
st.write(f"**Weathersit Explanation**")
st.markdown('<div style="text-align: justify;">1: Clear, Few clouds, Partly cloudy, Partly cloudy</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog</div>', unsafe_allow_html=True)

#grafik 4
fig4, ax4 = plt.subplots(figsize=(16, 8))
colors = ["#F9E897"]
sns.lineplot(
    y="cnt_y",
    x="mnth_x",
    data=data2012.sort_values(by="mnth_x", ascending=True),
    palette=colors,
    ax=ax4
)
colors = ["#124076"]
sns.lineplot(
    y="cnt_y",
    x="mnth_x",
    data=data2011.sort_values(by="mnth_x", ascending=True),
    palette=colors,
    ax=ax4
)
ax4.set_title("Bike Rented in 2011 and 2012", loc = "center", fontsize=35)
ax4.set_ylabel("Bike rented", size = 25)
ax4.set_xlabel("Months", size = 25)
ax4.tick_params(axis="x", labelsize=20)
ax4.tick_params(axis="y", labelsize=20)
ax4.legend(['2012','2011'])
st.pyplot(fig4)

text = st.text_area('Feedback :')
