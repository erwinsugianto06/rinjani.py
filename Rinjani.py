import streamlit as st
import datetime

import time
from PIL import Image

col1, col2, col3 = st.columns(3)
with col1:
    st.write(" ")
with col2:
    st.image("rinjani-removebg-preview.png")
with col3:
    st.write(" ")
st.write("""
# Website Persewaan Alat Outdoor
Rinjani adalah toko persewaan alat outdoor yang terlengkap dengan harga yang sangat terjangkau
""")
st.sidebar.title('HOME')
test = st.sidebar.selectbox("Navigation", ['About Us', 'Contact Us'])
st.video("videorinjani.mp4")
                          

st.write("------- Kode Barang--------------------Nama Barang----------------------------- Harga Sewa/Hari------------------")
st.write(" 1.       001        |         Tenda 2 org           |         25000          ")
st.write(" 2.       002        |         Tenda 4 org           |         45000          ")
st.write(" 3.       003        |         Tenda 6 org           |         50000          ")
st.write(" 4.       004        |         Matras                |         5000           ")
st.write(" 5.       005        |         Kompor Portable       |         10000          ")
st.write(" 6.       006        |         Sleeping Bag          |         10000          ")
st.write(" 7.       007        |         Tas Carrier           |         20000          ")
st.write(" 8.       008        |         Nesting               |         5000           ")
st.write(" 9.       009        |         Flysheet              |         5000           ")
st.write(" 10.      010        |         Headlamp              |         3000           ")
st.write(" 11.      011        |         Sepatu                |         15000          ")
st.write(" 12.      012        |         Gas                   |         3000           ")
st.write(" 13.      013        |         Senter                |         5000           ")
st.write("------------------------------------------------------------------------------")
st.write("")

Nama =st.text_input("Nama Penyewa : ")
Nomor =st.text_input("No Telepon : ")
Jumlah =st.number_input("Jumlah Barang yang Disewa : ", 0)
Lama =st.number_input("Berapa hari anda ingin menyewa : ", 0)
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Tanggal mulai sewa', today)
end_date = st.date_input('Tanggal akhir sewa', tomorrow)
if start_date < end_date:
    st.success('Tanggal mulai sewa: `%s`\n\nTanggal akhir sewa:`%s`' % (start_date, end_date))
else:
    st.error('Error: Tanggal akhir sewa must fall after Tanggal mulai sewa.')

Kode =st.text_input("Kode Barang : ")
Barang = []
Harga = []
while Kode :
    if Kode=="001":
        Barang.append("Tenda 2 org")
        Harga = int(25000)
        break
    elif Kode=="002":
        Barang.append("Tenda 4 org")
        Harga = int(45000)
        break
    elif Kode=="003":
        Barang.append("Tenda 6 org")
        Harga = int(50000)
        break
    elif Kode=="004":
        Barang.append("Matras")
        Harga = int(5000)
        break
    elif Kode=="005":
        Barang.append("Kompor Portable")
        Harga = int(10000)
        break
    elif Kode=="006":
        Barang.append("Sleeping Bag")
        Harga = int(10000)
        break
    elif Kode=="007":
        Barang.append("Tas Carrier")
        Harga = int(20000)
        break
    elif Kode=="008":
        Barang.append("Nesting")
        Harga = int(5000)
        break
    elif Kode=="009":
        Barang.append("Flysheet")
        Harga = int(5000)
        break
    elif Kode=="010":
        Barang.append("Headlamp")
        Harga = int(3000)
        break
    elif Kode=="011":
        Barang.append("Sepatu")
        Harga = int(15000)
        break
    elif Kode=="012":
        Barang.append("Gas")
        Harga = int(3000)
        break
    elif Kode=="013":
        Barang.append("Senter")
        Harga = int(5000)
        break
    else :
        Kode=st.text_input("Kode salah, Masukan Ulang Kode Barang : ")

Note =st.text_area('Catatan')

st.write()
if Jumlah ==3: potongan = (Jumlah*Harga)*7/100
elif Jumlah >3: potongan = (Jumlah*Harga)*10/100
else : potongan =0

Total = (Jumlah*Harga*Lama)-potongan
Pajak = int(Total*0.11)
Jumlah_bayar = int(Total+Pajak)
def garis():
    st.write("-------------------------------------------------------------------")
garis()
st.write("PENYEWAAN BARANG OUTDOOR")
st.write("Nama Penyewa :", Nama)
st.write("No Telepon :", Nomor)
st.write("Kode Barang :", Kode)
st.write("Jumlah Barang yang Disewa :", Jumlah)
st.write("Jumlah hari Disewa :", Lama)
st.write("Harga : Rp", Harga)
st.write("Potongan Harga : Rp", round(potongan))
st.write("PPN 11% : Rp", round(Pajak))
st.write("Catatan : ", Note)
garis()
st.write("Pembayaran Sewa Barang")
st.write("Jumlah Pembayaran : Rp", round(Jumlah_bayar))

choice = st.selectbox("Pilih satu", ["Tunai", "Mobile Banking"])

while choice :
    if choice=="Tunai":
        st.info("Pembayaran secara Tunai dapat dilakukan di store.")
        break
    if choice=="Mobile Banking":
        st.info("Apabila anda melakukan pembayaran dengan Mobile Banking harap upload bukti pembayaran di bawah ini.")
        break
garis()  
data = st.file_uploader("Unggah Bukti Bayar")

garis()
st.title("ENJOY YOUR DAY")
st.title("HAVE A NICE DAY")
