while True:
    first_input = input("Please input first number: ")
    second_input = input("Please input second number: ")

# error handling 
    try:
        result = int(first_input) / int(second_input)

        print(f"The result is {result}")
    except  Exception as e:
        print(e)
# kenapa programnya gak berhenti? karena kita bungkus kodenya di dalam
# try catch (blok kode yang bertugas untuk membuat kode menangkap error saat runtime)

# kenapa program gak boleh berhenti jalan?
# karena pada umumnya, program berjalan pada server yg biasa disebut API
# API (aplication programming interface)
# pengguna (membuat request spt POST, GET) -> client web/app (mengirim request ke API) ->
# db (mengambil data sesuai request) -> API (mengembalikan data) -> client web/app (menampilkan data) -> client
# 