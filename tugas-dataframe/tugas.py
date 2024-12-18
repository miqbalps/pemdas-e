#1.
import pandas as pd

df_csv = pd.read_csv('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv')
df_csv

#2.
tahun = 2015
sampah_tahun_tertentu = 0
for i, row in df_csv.iterrows():
  if row['tahun'] == tahun:
    sampah_tahun_tertentu += row['jumlah_produksi_sampah']

df_no2 = pd.DataFrame({"tahun": [tahun], "total_produksi_sampah": [sampah_tahun_tertentu]})
df_no2.to_csv("sampah_tahun_tertentu.csv", index=False)
df_no2.to_excel("sampah_tahun_tertentu.xlsx", index=False)
df_no2

#3.
data_per_tahun = {}
for i, row in df_csv.iterrows():
  if row['tahun'] not in data_per_tahun:
    data_per_tahun[row['tahun']] = 0
  data_per_tahun[row['tahun']] += row['jumlah_produksi_sampah']

print(data_per_tahun)

df_no3 = pd.DataFrame(data_per_tahun.items(), columns=["tahun", "total_produksi_sampah"])
df_no3.to_csv("sampah_per_tahun.csv", index=False)
df_no3.to_excel("sampah_per_tahun.xlsx", index=False)
df_no3

#4.
data_per_kabkot = {}
for i, row in df_csv.iterrows():
    if row['nama_kabupaten_kota'] not in data_per_kabkot:
        data_per_kabkot[row['nama_kabupaten_kota']] = {}
    if row['tahun'] not in data_per_kabkot[row['nama_kabupaten_kota']]:
        data_per_kabkot[row['nama_kabupaten_kota']][row['tahun']] = 0
    data_per_kabkot[row['nama_kabupaten_kota']][row['tahun']] += row['jumlah_produksi_sampah']

print(data_per_kabkot)

df_no4 = pd.DataFrame(data_per_kabkot)
df_no4.to_csv("sampah_per_kabupaten_kota_per_tahun.csv")
df_no4.to_excel("sampah_per_kabupaten_kota_per_tahun.xlsx")
df_no4