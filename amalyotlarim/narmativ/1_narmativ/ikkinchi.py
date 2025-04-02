# Maktab sinfi uchun o'quvchilarni boshqarish tizimi

# O'quvchilar ro'yxati
oquvchilar = ["Ali", "Vali", "Laylo", "Mavluda"]

# Reytinglar (tuple)
reytinglar = { "Ali": (5, 4, 3), "Vali": (4, 4, 5), "Laylo": (5, 5, 5), "Mavluda": (3, 4, 3) }

# Tug'ilgan kunlar (dictionary)
tugilgan_kunlar = { "Ali": "2005-05-01", "Vali": "2004-08-15", "Laylo": "2005-09-12", "Mavluda": "2004-12-25" }

# Darsga qatnashayotgan o'quvchilar (set)
darsga_qatnashayotganlar = set()

# Yangi o'quvchi qo'shish
yangi_oquvchi = input("Yangi o'quvchi ismini kiriting: ")
tugilgan_kuni = input(f"{yangi_oquvchi}ning tug'ilgan kunini kiriting (YYYY-MM-DD): ")

# Yangi o'quvchini qo'shamiz
if yangi_oquvchi not in oquvchilar:
    oquvchilar.append(yangi_oquvchi)
    reytinglar[yangi_oquvchi] = (0, 0, 0)  # Yangi o'quvchining reytingi 0 bo'ladi
    tugilgan_kunlar[yangi_oquvchi] = tugilgan_kuni
    print(f"{yangi_oquvchi} ro'yxatga qo'shildi.")
else:
    print(f"{yangi_oquvchi} allaqachon ro'yxatda mavjud.")

# O'quvchi o'chirish
ochiriladigan_oquvchi = input("O'chiriladigan o'quvchi ismini kiriting: ")
if ochiriladigan_oquvchi in oquvchilar:
    oquvchilar.remove(ochiriladigan_oquvchi)
    del reytinglar[ochiriladigan_oquvchi]
    del tugilgan_kunlar[ochiriladigan_oquvchi]
    print(f"{ochiriladigan_oquvchi} ro'yxatdan o'chirildi.")
else:
    print(f"{ochiriladigan_oquvchi} ro'yxatda mavjud emas.")

# Reytinglarni ko'rish
print("\nO'quvchilar va ularning reytinglari:")
for oquvchi, reyting in reytinglar.items():
    print(f"{oquvchi}: {reyting}")
    if reyting == (5, 5, 5):
        print(f" - {oquvchi}ning reytingi a'lo! Tabriklaymiz!")
    elif all(x >= 4 for x in reyting):
        print(f" - {oquvchi}ning reytingi yaxshi!")

# Tug'ilgan kunlarni ko'rish
print("\nO'quvchilarning tug'ilgan kunlari:")
for oquvchi, tugilgan_kuni in tugilgan_kunlar.items():
    print(f"{oquvchi}: {tugilgan_kuni}")

# Darsga qatnashuvchilarni boshqarish
qatnashuvchi = input("\nDarsga qatnashayotgan o'quvchini kiriting: ")
darsga_qatnashayotganlar.add(qatnashuvchi)
print(f"{qatnashuvchi} qatnashuvchilar ro'yxatiga qo'shildi.")

# Darsga kelmagan o'quvchini o'chirish
kelmagan_oquvchi = input("Darsga kelmagan o'quvchi ismini kiriting: ")
if kelmagan_oquvchi in darsga_qatnashayotganlar:
    darsga_qatnashayotganlar.remove(kelmagan_oquvchi)
    print(f"{kelmagan_oquvchi} qatnashuvchilar ro'yxatidan o'chirildi.")
else:
    print(f"{kelmagan_oquvchi} darsga kelmagan.")

# Darsga qatnashayotgan o'quvchilarni ko'rsatish
print("\nDarsga qatnashayotgan o'quvchilar:")
print(darsga_qatnashayotganlar)
