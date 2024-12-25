#   24.12.2024      4 OY 12 DARS

# Mavzu: Dataclass

# from dataclasses import dataclass
#
# @dataclass
# class PersonData:
#     name: str
#     lastname: str
#     age: int
# pd1 = PersonData("Sobir", "Sobirov", 18)
# print(pd1.lastname)


# ------------------------------------------------------------------

#
# from dataclasses import dataclass, field
#
# @dataclass
# class PersonData:
#     name: str
#     lastname: str
#     age: int
#     info: str = field(init=False)
#     """
#     Bu yerda info initdan tashqarida yasaloyotga atrebut bolib uni tashqarida yasash
#     uchun {field} yordamida none qiymat berib olamiz va bu bizga initda yozilgan atrebut kabi ishlab beradi.
#     """
#
#     def __post_init__(self):
#         self.info: str = f"Person: {self.name} {self.lastname} {self.age}"
# pd1 = PersonData("Sobir", "Sobirov", 18)
# print(pd1)


# ------------------------------------------------------------------

# from dataclasses import dataclass, field
#
# @dataclass
# class PersonData:
#     name: str
#     lastname: str
#     age: int = field(default = 18, compare=False)
#     interests: list = field(default_factory=list)
#     info: str = field(init=False, compare=False)
#     def __post_init__(self):
#         self.info: str = f"Persom {self.name} {self.lastname} {self.age}"
#
# pd1 = PersonData("Sobir", "Sobirov", 18)
# print(pd1)



# ------------------------------------------------------------------

# from dataclasses import dataclass, field
#
# class Days:
#     @staticmethod
#     def my_days():
#         return ["Du", "Se", "Chor", "Pa", "Ju"]
# @dataclass
# class PersonData:
#     current_id = 0
#     id: int = field(init=False)
#     name: str
#     lastname: str
#     age: Any
#     def __post_init__(self):
#         PersonData.current_id += 1
#         self.id = PersonData.current_id
# class Employee(PersonData):
#     age: int
#     salary: int
#     passport: str
#     work_days: list = field(default_factory=Days.my_days)
#     def __psot_init__(self):
#         super().__post_init__()
#         print("Employee ichidan chaqirildi !")


#============================================UYGA VAZIFA=======================================


# 1 vazifa

# from dataclasses import dataclass, field
#
# @dataclass
# class Product:
#     name: str
#     price: float = field(default=0.0)
#     available: bool = field(default=True)
#     def set_price(self, new_price: float):
#         if new_price > 0:
#             self.price = new_price
#         else:
#             raise ValueError("Narx ijobiy bo'lishi kerak!")
#     def product_info(self, search_name: str):
#         if self.name.lower() == search_name.lower() and self.available:
#             return f"Mahsulot mavjud: {self.name} - Narx: {self.price} - Mavjud: {self.available}"
#         else:
#             return f"Mahsulot '{search_name}' tugab qolgan ekan. Kechirasiz!"
# @dataclass
# class ElectronicProduct(Product):
#     warranty_period: int = field(default=12)
# products_list = []
# def add_product(product):
#     products_list.append(product)
#     print(f"Mahsulot '{product.name}' ro'yxatga qo'shildi!")
# def find_product(name):
#     found = False
#     for product in products_list:
#         result = product.product_info(name)
#         print(result)
#         found = True
#     if not found:
#         print(f"Mahsulot '{name}' topilmadi!")
# def show_all_products():
#     if not products_list:
#         print("Ro'yxatda mahsulotlar yo'q.")
#     else:
#         for product in products_list:
#             print(f"{product.name} - Narx: {product.price} - Mavjud: {product.available}")
# def main():
#     while True:
#         print("\n1 - Yangi mahsulot qo'shish")
#         print("2 - Mahsulotni qidirish")
#         print("3 - Barcha mahsulotlarni ko'rish")
#         print("0 - Chiqish")
#         choice = input("Tanlovingizni kiriting: ")
#         if choice == "1":
#             name = input("Mahsulot nomini kiriting: ")
#             try:
#                 price = float(input("Mahsulot narxini kiriting: "))
#                 product = Product(name=name, price=price)
#                 add_product(product)
#             except ValueError as e:
#                 print(f"Xato: {e}")
#         elif choice == "2":
#             search_name = input("Qidirilayotgan mahsulot nomini kiriting: ")
#             print("\nNatija:")
#             find_product(search_name)
#         elif choice == "3":
#             print("\nBarcha mahsulotlar:")
#             show_all_products()
#         elif choice == "0":
#             print("Dasturdan chiqildi. Xayr!")
#             break
#         else:
#             print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
# if __name__ == "__main__":
#     main()


# ------------------------------------------------------------------------------

# 2 vazifa

# from dataclasses import dataclass, field
#
# @dataclass
# class Vehicle:
#     brand: str
#     speed: int
#     technology: str = field(default="No technology specified")
#     def increase_speed(self, increment: int):
#         if self.speed + increment <= 300:
#             self.speed += increment
#         else:
#             print("Tezlik 300 km/h dan oshmasligi kerak!")
#     def vehicle_info(self):
#         return f"Marka: {self.brand}, Tezlik: {self.speed} km/h, Texnologiya: {self.technology}"
# @dataclass
# class Car(Vehicle):
#     speed: int
#     def vehicle_info(self):
#         return f"Marka: {self.brand}, Tezlik: {self.speed} km/h, Texnologiya: {self.technology}"
# @dataclass
# class Bicycle(Vehicle):
#     speed: int
#     def vehicle_info(self):
#         return f"Marka: {self.brand}, Tezlik: {self.speed} km/h, Texnologiya: {self.technology}"
# vehicles_list = []
# def add_vehicle(vehicle):
#     vehicles_list.append(vehicle)
#     print(f"Transport vositasi '{vehicle.brand}' ro'yxatga qo'shildi!")
# def find_vehicle(brand):
#     found = False
#     for vehicle in vehicles_list:
#         if vehicle.brand.lower() == brand.lower():
#             print(vehicle.vehicle_info())
#             found = True
#             break
#     if not found:
#         print(f"Transport vositasi '{brand}' topilmadi!")
# def show_all_vehicles():
#     if not vehicles_list:
#         print("Ro'yxatda transport vositalari yo'q.")
#     else:
#         for vehicle in vehicles_list:
#             print(vehicle.vehicle_info())
# def main():
#     while True:
#         print("\n1 - Yangi transport vositasi qo'shish")
#         print("2 - Transport vositasini qidirish")
#         print("3 - Barcha transport vositalarini ko'rish")
#         print("0 - Chiqish")
#         choice = input("Tanlovingizni kiriting: ")
#         if choice == "1":
#             vehicle_type = input("Transport vositasini tanlang (avtomobil/bisiklet): ").lower()
#             brand = input("Markani kiriting: ")
#             technology = input("Texnologiya haqida ma'lumot kiriting: ")
#             speed = int(input("Tezlikni kiriting (km/h): "))
#             if vehicle_type == "avtomobil":
#                 vehicle = Car(brand=brand, speed=speed, technology=technology)
#             elif vehicle_type == "bisiklet":
#                 vehicle = Bicycle(brand=brand, speed=speed, technology=technology)
#             else:
#                 print("Noto'g'ri transport turi!")
#                 continue
#             add_vehicle(vehicle)
#         elif choice == "2":
#             search_brand = input("Qidirilayotgan transport vositasi markasini kiriting: ")
#             find_vehicle(search_brand)
#         elif choice == "3":
#             print("\nBarcha transport vositalari:")
#             show_all_vehicles()
#         elif choice == "0":
#             print("Dasturdan chiqildi. Xayr!")
#             break
#         else:
#             print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
# if __name__ == "__main__":
#     main()


# ------------------------------------------------------------------------------

# 3 vazifa

# from dataclasses import dataclass, field
#
# @dataclass
# class Book:
#     title: str
#     author: str
#     price: float
#     def __str__(self):
#         return f"Kitob nomi: {self.title}, Muallif: {self.author}, Narx: {self.price} so'm"
#     def set_price(self, new_price: float, user_role: str):
#         if user_role.lower() == "admin":
#             self.price = new_price
#             print(f"Narx {new_price} so'm ga o'zgartirildi.")
#         else:
#             print("Sizda narxni o'zgartirish huquqi yo'q. Faqat adminga ruxsat berilgan.")
# @dataclass
# class EBook(Book):
#     file_size: float
#     def __str__(self):
#         return f"{super().__str__()}, Fayl hajmi: {self.file_size} MB"
# @dataclass
# class PrintedBook(Book):
#     paper_type: str
#     def __str__(self):
#         return f"{super().__str__()}, Qog'oz turi: {self.paper_type}"
# books_list = []
# def add_book(book: Book):
#     books_list.append(book)
#     print(f"Kitob '{book.title}' ro'yxatga qo'shildi!")
# def find_book(title: str):
#     found = False
#     for book in books_list:
#         if book.title.lower() == title.lower():
#             print(book)
#             found = True
#             break
#     if not found:
#         print(f"Kitob '{title}' topilmadi!")
# def show_all_books():
#     if not books_list:
#         print("Ro'yxatda kitoblar yo'q.")
#     else:
#         for book in books_list:
#             print(book)
# def main():
#     while True:
#         print("\n1 - Yangi kitob qo'shish")
#         print("2 - Kitobni qidirish")
#         print("3 - Barcha kitoblarni ko'rish")
#         print("4 - Kitob narxini o'zgartirish")
#         print("0 - Chiqish")
#         choice = input("Tanlovingizni kiriting: ")
#
#         if choice == "1":
#             book_type = input("Kitob turini tanlang (elektron/print): ").lower()
#             title = input("Kitob nomini kiriting: ")
#             author = input("Muallifni kiriting: ")
#             price = float(input("Narxni kiriting: "))
#             if book_type == "elektron":
#                 file_size = float(input("Fayl hajmini kiriting (MB): "))
#                 book = EBook(title=title, author=author, price=price, file_size=file_size)
#             elif book_type == "print":
#                 paper_type = input("Qog'oz turini kiriting: ")
#                 book = PrintedBook(title=title, author=author, price=price, paper_type=paper_type)
#             else:
#                 print("Noto'g'ri kitob turi! Elektron yoki print tanlang.")
#                 continue
#             add_book(book)
#         elif choice == "2":
#             search_title = input("Qidirilayotgan kitob nomini kiriting: ")
#             find_book(search_title)
#         elif choice == "3":
#             print("\nBarcha kitoblar:")
#             show_all_books()
#         elif choice == "4":
#             title_to_update = input("Narxini o'zgartirmoqchi bo'lgan kitob nomini kiriting: ")
#             new_price = float(input("Yangi narxni kiriting: "))
#             user_role = input("Sizning rol'ingiz (admin/foydalanuvchi): ").lower()
#             found = False
#             for book in books_list:
#                 if book.title.lower() == title_to_update.lower():
#                     book.set_price(new_price, user_role)
#                     found = True
#                     break
#             if not found:
#                 print(f"Kitob '{title_to_update}' topilmadi!")
#         elif choice == "0":
#             print("Dasturdan chiqildi. Xayr!")
#             break
#
#         else:
#             print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
# if __name__ == "__main__":
#     main()



# ------------------------------------------------------------------------------

# 4 vazifa


# from dataclasses import dataclass, field
#
# @dataclass
# class Employee:
#     name: str
#     position: str
#     salary: float
#     def __str__(self):
#         return f"Ism: {self.name}, Lavozim: {self.position}, Maosh: {self.salary} so'm"
#     def increase_salary(self, amount: float, user_role: str):
#         if user_role.lower() == "director":
#             self.salary += amount
#             print(f"Maosh {amount} so'm ga ko'paytirildi. Yangi maosh: {self.salary} so'm")
#         else:
#             print("Sizda maoshni ko'paytirish huquqi yo'q. Faqat direktor ruxsat berilgan.")
# @dataclass
# class Manager(Employee):
#     team_size: int
#     def __str__(self):
#         return f"{super().__str__()}, Jamoa a'zolari soni: {self.team_size}"
#     def manage_team(self):
#         print(f"{self.name} jamoasini boshqaradi. Jamoada {self.team_size} nafar xodim mavjud.")
# @dataclass
# class Developer(Employee):
#     programming_languages: list
#     def __str__(self):
#         return f"{super().__str__()}, Bilgan dasturlash tillari: {', '.join(self.programming_languages)}"
#     def write_code(self):
#         print(f"{self.name} kod yozmoqda. {', '.join(self.programming_languages)} tillarida ishlaydi.")
# employees_list = []
# def add_employee(employee: Employee):
#     employees_list.append(employee)
#     print(f"Xodim '{employee.name}' ro'yxatga qo'shildi!")
# def find_employee(name: str):
#     found = False
#     for employee in employees_list:
#         if employee.name.lower() == name.lower():
#             print(employee)
#             found = True
#             break
#     if not found:
#         print(f"Xodim '{name}' topilmadi!")
# def show_all_employees():
#     if not employees_list:
#         print("Ro'yxatda xodimlar yo'q.")
#     else:
#         for employee in employees_list:
#             print(employee)
# def main():
#     while True:
#         print("\n1 - Yangi xodim qo'shish")
#         print("2 - Xodimni qidirish")
#         print("3 - Barcha xodimlarni ko'rish")
#         print("4 - Xodim maoshini ko'paytirish")
#         print("0 - Chiqish")
#         choice = input("Tanlovingizni kiriting: ")
#         if choice == "1":
#             position = input("Lavozimni tanlang (menedjer/dasturchi): ").lower()
#             name = input("Xodim ismni kiriting: ")
#             salary = float(input("Maoshni kiriting: "))
#             if position == "menedjer":
#                 team_size = int(input("Jamoa a'zolari sonini kiriting: "))
#                 employee = Manager(name=name, position=position, salary=salary, team_size=team_size)
#             elif position == "dasturchi":
#                 languages = input("Bilgan dasturlash tillarini kiriting (vergul bilan ajratilgan): ").split(",")
#                 employee = Developer(name=name, position=position, salary=salary, programming_languages=[lang.strip() for lang in languages])
#             else:
#                 print("Noto'g'ri lavozim! Menedjer yoki dasturchi tanlang.")
#                 continue
#             add_employee(employee)
#         elif choice == "2":
#             search_name = input("Qidirilayotgan xodim ismni kiriting: ")
#             find_employee(search_name)
#         elif choice == "3":
#             print("\nBarcha xodimlar:")
#             show_all_employees()
#         elif choice == "4":
#             name_to_update = input("Maoshini ko'paytirmoqchi bo'lgan xodim ismni kiriting: ")
#             amount = float(input("Maoshni qancha ko'paytirishni kiriting: "))
#             user_role = input("Sizning rol'ingiz (director/foydalanuvchi): ").lower()
#             found = False
#             for employee in employees_list:
#                 if employee.name.lower() == name_to_update.lower():
#                     employee.increase_salary(amount, user_role)
#                     found = True
#                     break
#             if not found:
#                 print(f"Xodim '{name_to_update}' topilmadi!")
#         elif choice == "0":
#             print("Dasturdan chiqildi. Xayr!")
#             break
#         else:
#             print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
# if __name__ == "__main__":
#     main()


# ------------------------------------------------------------------------------

# 5 vazifa

# from dataclasses import dataclass, field
#
# @dataclass
# class Athlete:
#     name: str
#     sport_type: str
#     records: list
#     def __str__(self):
#         return f"Ism: {self.name}, Sport turi: {self.sport_type}, Rekordlar: {', '.join(map(str, self.records))}"
#     def update_records(self, new_record: float):
#         if new_record > max(self.records, default=0):
#             self.records.append(new_record)
#             print(f"Rekord yangilandi: {new_record}")
#         else:
#             print(f"Yangi rekord o'tgan rekorddan kichik. Rekordlar o'zgartirilmaydi.")
# @dataclass
# class Runner(Athlete):
#     distance: float
#     def __str__(self):
#         return f"{super().__str__()}, Yugurish masofasi: {self.distance} metr"
#     def run(self):
#         print(f"{self.name} {self.distance} metr yugurmoqda.")
# @dataclass
# class Swimmer(Athlete):
#     pool_size: float
#     def __str__(self):
#         return f"{super().__str__()}, Suzish havzasi o'lchami: {self.pool_size} metr"
#     def swim(self):
#         print(f"{self.name} {self.pool_size} metrli havzada suzmoqda.")
# athletes_list = []
# def add_athlete(athlete: Athlete):
#     athletes_list.append(athlete)
#     print(f"Athlete '{athlete.name}' ro'yxatga qo'shildi!")
# def find_athlete(name: str):
#     found = False
#     for athlete in athletes_list:
#         if athlete.name.lower() == name.lower():
#             print(athlete)
#             found = True
#             break
#     if not found:
#         print(f"Athlete '{name}' topilmadi!")
# def show_all_athletes():
#     if not athletes_list:
#         print("Ro'yxatda sportchilar yo'q.")
#     else:
#         for athlete in athletes_list:
#             print(athlete)
# def main():
#     while True:
#         print("\n1 - Yangi sportchi qo'shish")
#         print("2 - Sportchini qidirish")
#         print("3 - Barcha sportchilarni ko'rish")
#         print("4 - Sportchi rekordini yangilash")
#         print("0 - Chiqish")
#         choice = input("Tanlovingizni kiriting: ")
#         if choice == "1":
#             sport_type = input("Sport turini tanlang (yuguruvchi/suzuvchi): ").lower()
#             name = input("Sportchi ismni kiriting: ")
#             records = list(map(float, input("Rekordlarni kiriting (vergul bilan ajratilgan): ").split(",")))
#             if sport_type == "yuguruvchi":
#                 distance = float(input("Yugurish masofasini kiriting (metr): "))
#                 athlete = Runner(name=name, sport_type=sport_type, records=records, distance=distance)
#             elif sport_type == "suzuvchi":
#                 pool_size = float(input("Suzish havzasi o'lchamini kiriting (metr): "))
#                 athlete = Swimmer(name=name, sport_type=sport_type, records=records, pool_size=pool_size)
#             else:
#                 print("Noto'g'ri sport turi! Yuguruvchi yoki suzuvchi tanlang.")
#                 continue
#             add_athlete(athlete)
#         elif choice == "2":
#             search_name = input("Qidirilayotgan sportchi ismni kiriting: ")
#             find_athlete(search_name)
#         elif choice == "3":
#             print("\nBarcha sportchilar:")
#             show_all_athletes()
#         elif choice == "4":
#             name_to_update = input("Rekordini yangilamoqchi bo'lgan sportchi ismni kiriting: ")
#             new_record = float(input("Yangi rekordni kiriting: "))
#             found = False
#             for athlete in athletes_list:
#                 if athlete.name.lower() == name_to_update.lower():
#                     athlete.update_records(new_record)
#                     found = True
#                     break
#             if not found:
#                 print(f"Sportchi '{name_to_update}' topilmadi!")
#         elif choice == "0":
#             print("Dasturdan chiqildi. Xayr!")
#             break
#         else:
#             print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
# if __name__ == "__main__":
#     main()




#========================================RUSTAMOV ASILBEK=====================================