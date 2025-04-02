# import os  # Faylni o‘chirish uchun kerak
#
# FILENAME = "data.txt"  # Ishlatiladigan fayl nomi
#
#
# # 1️⃣ CREATE — Yangi fayl yaratish va ma'lumot yozish
# def create_file():
#     with open(FILENAME, "w") as file:  # Yangi fayl yaratish va yozish rejimi
#         file.write("Salom, bu men Jasurbek!\n")
#         file.write("Bu yerda CRUD operatsiyalari bajariladi.\n")
#     print("✅ Fayl yaratildi va ma'lumot yozildi.")
#
#
# # 2️⃣ READ — Fayldan ma'lumotni o‘qish
# def read_file():
#     with open(FILENAME, "r") as file:  # O‘qish rejimida ochish
#         content = file.read()
#     print("📖 Fayldagi ma'lumotlar:\n" + content)
#
#
# # 3️⃣ UPDATE — Faylga qo‘shimcha ma'lumot qo‘shish
# def update_file():
#     with open(FILENAME, "a") as file:  # Qo‘shimcha yozish rejimi
#         file.write("Yangi qo‘shilgan ma'lumot!\n")
#     print("✍️ Fayl yangilandi (ma'lumot qo‘shildi).")
#
#
# # 4️⃣ DELETE — Faylni o‘chirish
# def delete_file():
#     if os.path.exists(FILENAME):  # Fayl mavjudligini tekshiramiz
#         os.remove(FILENAME)  # Faylni o‘chiramiz
#         print("🗑 Fayl o‘chirildi.")
#     else:
#         print("⚠️ Fayl allaqachon o‘chirilgan yoki mavjud emas.")
#
#
# # ⚡️ CRUD amallarini chaqiramiz
# create_file()   # 1️⃣ Yangi fayl yaratish va yozish
# read_file()     # 2️⃣ Fayldan o‘qish
# update_file()   # 3️⃣ Ma'lumot qo‘shish
# read_file()     # 2️⃣ O‘qishni qayta bajarib tekshirish
# # delete_file()   # 4️⃣ Faylni o‘chirish
#
# delete_file()


# salom = str(input("salom"))
jasurbek = 'Qaxxarov'
print(jasurbek)