# a = [1,9,9,4,5,6,7,8,56]
# print(a[0])


# p = str(input("ismingizni kiriting = "))
# print(f"mening ismim",p)

# a = [1,2,35,68,90,34,22]
# print(a[-1])


# a = [12]
# print(a[-1])

# a = int(input("istalgan son kirit = "))
# b = 0
# print(1)

# a = ['nexa','damas','lasetti']
# print(a[0],a[1],a[2])


# x = int(input("fungsiya uchun x ni kiriting = "))
# y = 3*(x**2)- 4*x +6
# print(y)

# //////////////////////////////////////////////////////////////////////////////////////

# kasflarni elon qiluvchi funksiya 

# def kasblar(kasb):
#     print("Men "  + kasb)
# kasblar("dasturchi")
# kasblar("talaba")
# kasblar("muhandis")


# har qanday juft sonlarni toq sonlarga 
#aylan turuvchi funksiiya

# def son(x):
#     return 1+x
# print(son(3))
# print(son(5))
# print(son(9))

# :: nuqta teskarisini qaytarib beradi

# avto = ['mashina','maxsulot','airaport',8,10, 12]
# print(avto[::-1])



# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#     salom_ber()


######################################################################3

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, 
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# print(salom_ber.__doc__)
# salom_ber("dilshod")

############################################################
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('dilshod','muhammadiyev')


#######################################################33


# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda")

# yosh_hisobla('dilshod', 2004)




# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)


#######################################################################################



# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

#########################################################


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

#######################################################################333

# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(10,21))

# ///////////////////////////////////////////////////////////////////////////////
# # tuple ()
# [] - lest
# {} - dict

# kurinishi

# fungsiya birnechta buyruqlarni bajarish uchun muljallangan algaretim yigindisi


# ????????????????????????????????????????????????????????????????????????????????????

# var bu uzgaruvchi 

# ruyxatning obektlar soni 4 ta

# ruyxatning ilimentlar soni 3 ta sabab 
# python ruyxatni 0 dan boshlab sanaydi

# ????????????????????????????????????????????????????????????????????????????

# Keling talabalarni baholaydigan funksiya yozamiz.
#  Funksiyamiz talabalar ro'yxatini qabul qilib oladi, 
#  ro'yxatdan har bir talabani sug'urib olib (.pop()), bahosini 
#  kiritishni so'raydi. Talaba ismi 
# va bahosini lug'atga joylab, yakuniy lug'atni foydalanuvchiga qaytaradi.

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)



# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = (talabalar)
# print(talabalar)
# baholar

# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir
#  matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf:(ismlar)
# print(ismlar)

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# kattaismlar=[]
# for ism in ismlar:
#     kattaismlar.append(ism.title())
# # print(kattaismlar)

# Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona
#  qiymatlar ko'rinishida uzatilsa, funksiya 
#  yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments). 
# Quyidagi misolni ko'raylik. summa() nomli 
# funksiyamiz istalgancha sonlarni qabul qilib oladi, va ularning yi'gindisi hisoblaydi:


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,8))




# *args usulida, bacha uzatilgan parametrlar (bir dona bo'lsa ham)
#  funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi. Bundan kelib 
# chiqib, yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:



# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(4,5,6,7))



# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
# print(avto2)




# def avto_info(kompaniya, model, rangi, yili, narxi):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rangi':rangi,
#             'yili':yili,
#             'narxi':narxi
#             }
#     return avto

# print("Avtomobillar ro'yxatini shakillantirish :")
# avtolar = []
# while True:
#     print("Avtomobil ma'lumotlarini kiriting : ", end='')
#     kompaniya = input("Ishlab chiqarilgan kompaniya nomi = ")
#     model = input("Avtomobil modeli = ")
#     rangi = input("Avtomobil rangi = ")
#     yili = input("Avtomobil chiqarilgan yil = ")
#     narxi = input("Avtomobilning narxi = ")
#     avtolar.append(avto_info(kompaniya, model, rangi, yili, narxi))
    
#     javob = input("Yana avtomobil qo'shasizmi Y/N = ")
#     if javob == "N":
#         break
    
# print("Barcha avtomobillar ro'yxati : \n __________________________________________________")
# print(f"Avtomobil kompaniyasi :   {kompaniya} \n"
#       f"Avtomobil modeli : {model} \n"
#       f"Avtomobil rangi : {rangi} \n"
#       f"Avtomobil chiqarilgan til:  {yili}  - yil \n"
#       f"Avtomobil narxi:    {narxi} \n"
#       )
          
          
          
# Vazifa talabalar jurnali funksiyasi



# ism
# familiya
# yoshi
# nechanchi kurs
# institut
# turar joy
# 






# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")






###############################################################################

# Kasblarni e'lon qiluvchi funksiya

# def kasblar(kasb):
#     print("Men " + kasb)
# kasblar("Dasturchi")
# kasblar("talaba")
# kasblar("Muhandis")


###############################################################################

# Har bir toq sonlarni juft sonlarga aylantiruvchi funksiya

# def son(x):
#     return 1+x
# print(son(3))
# print(son(5))
# print(son(9))


###############################################################################

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning ismini kiriting = ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['Ali','Vali','Aziz','Azamat']
# baholar = bahola(talabalar)
# print(baholar)


###############################################################################


# def avto_info(kompaniya, model, rangi, yili):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rangi':rangi,
#         'yili':yili
#     }
#     return avto

# avto1 = avto_info('Chevrolet', 'Onix', 'qizil', 2021)
# avto2 = avto_info('GM', 'Cobalt', 'qora', 2022)
# avtolar = avto1 , avto2
# print('Online avto bazadagi avtomobillar :')
# print(avtolar)


###############################################################################

# Moslashuvchan funksiyalar  ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)-

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))


# ?????????????????????????????????????????????????????????????????
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf:(ismlar)
# # print(ismlar)
# ??????????????????????????????????????????????????????????????????????????????

# import math

# x=400
# print(math.sqrt(x))

# # avto_infoning argumentlari
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
#     avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")    
#         #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#         #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
#         # Yana avto qo'shish-qo'shmaslikni so'raymiz
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob=='no':
#             break
#     return avtolar

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
#           f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
#           f"{avto_info['yil']}-yil, {avto_info['narh']}$")







