# buat dictionary data panen
data_panen = {
  'lokasi1': {
    'nama_lokasi': 'Kebun A',
    'hasil_panen': {
      'padi': 1200,
      'jagung': 800,
      'kedelai': 500
    }
  },
  'lokasi2': {
    'nama_lokasi': 'Kebun B',
    'hasil_panen': {
      'padi': 1500,
      'jagung': 900,
      'kedelai': 450
    }
  },
  'lokasi3': {
    'nama_lokasi': 'Kebun C',
    'hasil_panen': {
      'padi': 1100,
      'jagung':750,
      'kedelai': 600
    }
  },
  'lokasi4': {
    'nama_lokasi': 'Kebun D',
    'hasil_panen': {
      'padi': 1300,
      'jagung': 850,
      'kedelai': 550
    }
  },
  'lokasi5': {
    'nama_lokasi': 'Kebun E',
    'hasil_panen': {
      'padi': 1400,
      'jagung': 950,
      'kedelai': 480
    }
  }
}

# 1
for i in data_panen.values():
  print(f'Nama lokasi: {i['nama_lokasi']}')
  print(f'Hasil Panen: Padi = {i['hasil_panen']['padi']}, Jagung: {i['hasil_panen']['jagung']}, Kedelai: {i['hasil_panen']['kedelai']}\n')

print()