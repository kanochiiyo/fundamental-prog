data_parking = [
    {"date": "2023-01-01",
     "values": 30
    },
    {"date": "2023-01-02",
     "values": 20
    }
]

data_lost_ticket = [
    {"date": "2023-01-01",
     "values": 30
    },
    {"date": "2023-01-02",
     "values": 20
    }
]

data_date = {
    "2023-01-01": {},
    "2023-01-02": {},
    "2023-01-03": {},
    "2023-01-04": {},
    "2023-01-05": {},
    "2023-01-06": {},
}

# Looping ini digunakan untuk mengambil data parking dan data ticket yang hilang, di mana ada 2 hari ticket hilang yaitu di tanggal 1/1 dan 2/1. Berarti jumah loopingnya adalah 4 kali (tiap looping 2 kali)
for item in data_parking:
    date = item['date']
    if date in data_date:
        data_date[date]['parking'] = item['values']
        
for item in data_lost_ticket:
    date = item['date']
    if date in data_date:
        data_date[date]['lost_ticket'] = item['values']
# Looping di atas menggunakan kompleksitas O(n) yang artinya looping sebanyak n. Jika ada 10 data parking maka looping 10 kali dan 3 data lost ticket maka looping sebanyak 3 kali.

# Array kosong untuk menampung data
merged_data = []

# keys() itu method dari dictionary yang fungsinya untuk ngambil key (kalo di array namanya index)
keys = data_date.keys() # Mengambil semua kolom kiri agar menjadi array, sample: ["2023-01-01", "2023-01-02", "2023-01-03"]

# Looping ini tujuannya ngambil nilai sesuai tanggal di data_date
for item in keys:
    _tmp = {
        "date": item,
        # Ini tuh tujuannya apa sih? Jadi, kalo ada key 'parking' di dalam data_date, maka isi dengan nilai tsb. Maksudnya gimana?
        # Jadi, kan di kode data_parking itu hanya ada 2 tanggal di mana parkirannya ada valuesnya, maka kita harus bikin kondisi kalau lagi gak ada yang parkir, kita isi dengan angka 0 biar gak error.
        # Tapi ['parking'] itu apa? Itu asalnya dari kode line 32 , di mana ['parking'] itu sebenernya data_parking['values']
        "parking": data_date[item]['parking'] if 'parking' in data_date[item] else 0,
        "lost_ticket": data_date[item]['lost_ticket'] if 'lost_ticket' in data_date[item] else 0
    }
    merged_data.append(_tmp) # Kita ngambil data dari dict data_date["2023-01-01"] ketika looping pertama
    
print(merged_data)