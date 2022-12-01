

# while takrorlanish sikli (operatori)


#while bu toki degan ma'moni anglatib, True qiymat olsa - abadiy ishlayveradi
# False yoki biror chegara berilsa, shu chegaraga borib to'xtaydi

#####################################################################################


# # i o'zgaruvchi berib, uni 1ga tenglashtiramiz
# i = 1
# # ya'ni i o'zgaruvchi 6 soniga borgunicha
# while i <= 6:
# # shu i sonni qaytarsin (print)
#   print(i)
#   # har birini birga qo'shib ketaversin
#   i += 2




#####################################################################################



# break kalit so'zi - berilgan o'zgaruvchi yoki buyruq operatoriga shu buyruq berilsa, hammasini to'xtatadi


# i = 1
# while i < 6:
#   print(i)
#   if i == 5:
#     break
#   i += 1


# def summa (*sonlar):
#     "kiritilgan sonlar yigindisini hisoblaydigan funksiya "
#     #sum kalit suzi berilgan qiymatlarni yigindisini qaytaradi
#     return sum (sonlar)
# print(summa(4,5,6,7))



# Yuqoridagi misloda biz 10 ta Malibu mashinasidan iborat ro'yxat tuzdik. E'tibor qiling, 'rang' kalitiga qiymat
#  bermadik va None deb qoldirdik. Endi ishlab chiqarish jarayonida mashinalarga turli ranglarni
#  berishimiz mumkin.  Misol uchun birinchi 3 ta mashinaga qizil rang beramiz:









# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }
# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")  



# ism = input("Ismingiz nima? ")
# print(f'salom,{ism.title()}')

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)

#input() funktsiyasi har qanday kiritilgan qiymatni 
# matn sifatida qabul qilib oladi. Agar foydalanuvchidan 
# son talab qilinsa, foydalanuvchi kiritgan qiymatni butun 
# (integer) yoki on'lik (float) son ko'rinishiga o'tkazib olish kerak.
#Buning uchun int() yoki float() funktsiyalaridan foydalanamiz.



# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa




# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.


# avval son degan o'zgaruvchi yaratdik va unga 1 qiymatini berdik. 
# 2-qatorda esa toki son 5 dan kichik yoki teng ekan 3-4-qatorlarni bajar dedik. 
# 3-qatorda son ni konsolga chiqardik
# 4-qatorda son ga 1 qo'shdik. 
# 4-qatordan so'ng kod yana 2-qatorga qaytadi va son<=5 shartini tekshiradi, agar shart bajarilsa 3-4 qator qayta-qayta bajarilaveradi. 
# 5-qadamdan so'ng son=5 bo'lganda while tsikli to'xtaydi.




# Pythonda += operatori bor. Bu operator o'ng tarafdagi qiymatni chap tarafdagi qiymatga qo'shadi.
#  Misol uchun, yuqorida son = son + 1 o'rniga son += 1 deb yozishimiz mumkin.


# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)



# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")



# son = 0
# while son<10:    
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son += 1


# a = int(input("son="))
# a = 1>2>3 
# b = int(input("son="))
# b = 1<2<3
# c = int(input("son="))
# c = 1>2<3
# print(a,b,c)


# def salom_ber(ism,familiya):
#     print(f"salom hurmatli {ism} {familiya}")
# salom_ber("farrux" , "muhammadiyev")
# print("hush kelibsiz")
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1 masala

# mevalar = ['olma','banan','uzum','anor']
# for meva in mevalar:
#     print(meva)


# 2 masala


# odamlar = ['zafar','sardor','aziz','dilshod']
# for odam in odamlar:
#     print(odam)


# 3 masala

# mehmon = ['farruh','sherali','pirim bek']
# for mehmonlar in mehmon:
#     print(mehmonlar)


# 4 masala

# d = str(input("ismingizni kiriting ="))

# print(f"mening ismim",d)

# 5 masala

# ism = input("Ismingiz nima? ")
# print(f'Salom, {ism.title()}')

# titil funksiyasi bu so'z va matnlarni ajratib bosh barfni katta qilib beradi

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.


# son = 1
# while son <=10:
#     print(son, end=' ')
#     son = son + 1

# Shu paytgacha yozgan dasturlarimiz faqatgina bir martta bajarilayotgan edi. while tsikli yordamida dasturni to'xtatish imkoniyatini foydalanuvchiga berishimiz mumkin.

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# Break operatori for tsiklini to'xtatish uchun ham ishlatiladi.

# sonlar = list(range(1,11))
# for son in sonlar: 
#  if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
# print(f"{son} ning kvadrati {son**2} ga teng")






# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun '0' deb yozing): "


# # Takroriy ketaversin
# while True:
#     qiymat = int(input(savol))
#     if qiymat<0:
#         # davom etsin
#         continue
#     elif qiymat==0:
#         break
#     # dasturni to'liq to'xtatadi
#     else:
#         yigindi = qiymat+10
#         print(f"{qiymat} ning 10ga qo'shilgani =  {yigindi} ga teng")





# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun '0' deb yozing): "
# while True :
#     qiymat = int (input(savol))
#     if qiymat<0:
#         continue 
#     # cantinu bu  
#     elif qiymat ==0:
#         break
#     else:
#         yigindi = qiymat + 10
#         print(f"{qiymat}ning 10ga qushilgani = {yigindi} ga teng")



# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break

# ismlar = ("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     pprint("Do'stlaringiz yoshini saqlaymiz.")rint(ismlar.title())

# Yuqoridagi usul bilan lu'gatlarni ham shakllantirishimiz mumkin. Quyidagi kodda ism bu kalit, yosh esa klaitga mos keluvchi qiymat. while tsiklining davomiyligi esa ishora ning qiymatiga bog'liq.


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# def salom_ber():
#     """salom beruvchi funksiya"""
#     print("assalomu alaykum!")

# salom_ber()



























