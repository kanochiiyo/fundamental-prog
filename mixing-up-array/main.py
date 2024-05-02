# Array biasa
x = [2, 4, 5, 7, 8, 9]

for i in x:
    if int(i) % 2 == 0:
        print(f"{i} adalah genap")
    else:
        print(f"{i} adalah ganjil")

# Set / Dictionary (Struct) / Hashmap
data_dict = {
    "kebayoran": 2,
    "kampung_baru": 1,
    "grogol": 12,
}

data_array = [
    {
        "name": "kebayoran",
        "values": 2
    },
    {
        "name": "kampung_baru",
        "values": 1
    },
    {
        "name": "grogol",
        "values": 2
    },
]
# Print dengan dict
print(data_dict['kebayoran'])

# Print dengan array
for i in data_array:
    if i['name'] == "kebayoran":
        print(i['values'])


# TIPS
# Gunakan tipe data array jika harus menampilkan secara urut, contoh:
# Menampilkan: timeline sosmed, daftar kehadiran, daftar produk


# Gunakan tipe data dict jika harus menggabungkan dua data terpisah sebelum digabung jadi array
# Contohnya ada di sample_merged_data.py