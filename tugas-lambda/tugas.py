import pandas as pd
import matplotlib.pyplot as plt

#1
df_csv = pd.read_csv('disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv')

tahun = int(input('Masukkan tahun data yang akan ditampilkan: '))
data_per_tahun = df_csv[df_csv['tahun'] == tahun]
print(data_per_tahun)

plt.figure(figsize=(15, 6))
plt.barh(data_per_tahun['nama_kabupaten_kota'], data_per_tahun['jumlah_produksi_sampah'], color='chartreuse')
plt.xlabel('Satuan (Ton per hari)')
plt.title(f'Data Produksi Sampah Tahun {tahun}')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#2
total_hari_per_tahun = 365
df_csv['total_sampah_per_tahun'] = df_csv['jumlah_produksi_sampah'].apply(lambda x: x * total_hari_per_tahun)
data_per_tahun = df_csv[df_csv['tahun'] == tahun]
print(data_per_tahun)

#3
plt.figure(figsize=(15, 6))
plt.barh(data_per_tahun['nama_kabupaten_kota'], data_per_tahun['total_sampah_per_tahun'], color='chartreuse')
plt.xlabel('Satuan (Ton)')
plt.title(f'Data Produksi Sampah Tahun {tahun}')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

#4
df_csv['kategori'] = df_csv.apply(lambda x: 'Segera tanggulangi' if x['jumlah_produksi_sampah'] > 400 else 'Masih aman', axis=1)
data_per_tahun = df_csv[df_csv['tahun'] == tahun]
print(data_per_tahun)

#5
harga_per_ton = 123000
df_csv['bayaran_sampah_per_hari'] = df_csv.apply(lambda x: x['jumlah_produksi_sampah'] * harga_per_ton, axis=1)
df_csv['bayaran_sampah_per_tahun'] = df_csv.apply(lambda x: x['bayaran_sampah_per_hari'] * total_hari_per_tahun, axis=1)
data_per_tahun = df_csv[df_csv['tahun'] == tahun]
print(data_per_tahun)

#6
df_csv['pajak'] = df_csv.apply(lambda x: harga_per_ton * 0.5 if x['kategori'] == 'Segera tanggulangi' else 0, axis=1)

data_tanggulangi = df_csv[df_csv['kategori'] == 'Segera tanggulangi']
print('Sampah harus segera ditanggulangi:')
print(data_tanggulangi)

print('Sampah masih aman:')
data_aman = df_csv[df_csv['kategori'] == 'Masih aman']
print(data_aman)
