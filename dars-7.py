
# z = str(input("ismingizni kiriting = "))
# print("aka",z)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# x = int(input("fungsiya uchun x ni kiriting = "))
# y = 3*(x**2)- 4*x +6
# print(y)

# # vazifa bajarildi 

# son = int(input("ixtiyoriy son kiriting = "))
# print("bu son teng",12)

# ///////////////////////////////////////////////////
#  a =int (input("yilingizni kiriting = "))
# print(f"yoshingiz {2022-a} da")



# a = int(input("yoshingizni kiriting = "))
# print(f"yilingiz {2022-a} da")





# radiusi = int(input("aylana radiusini kiriting = "))

# deametr = 2*radiusi
# print(deametr)




# def salom_ber(ism,familiya):
#     print(f"salom hurmatli {ism} {familiya}")
# salom_ber("dilshodbek" , "muhammadiyev")
# print("hush kelibsiz")


# a = int(input("istalgan son kiriting = "))

# son=1000
# print(0)






# a = [23,22,45,67,12]
# print(a[-1])





# beki = (input("istalgan son kiriting = "))
# print(beki [0])




# def yosh_hisoblash(tug_yil, hozirgi_yil=2022):
#     print(f"siznimg yshingiz = {hozirgi_yil-tug_yil}")
# yosh_hisoblash(2004)

# a = int(input("yilingizni kiriting = "))
# print(f"yoshingiz {2022-a} da ")



# 1 masala



# a = {2,3,4,5,6}
# a.pop()
# print(0)

# 2 masala

# a = {1,2,3,4,5,6}
# b = {12,13,14,15,16}
# g = a.union(b)
# print(g)

# 3 masala

# a = (input("son kiriting = "))
# print("ushbu soni teskarisi =",a[::-1])

# 4 masala

# a = [12,23,35,56,78,]
# print(a[-1])

# 5 masala

# a = "salom dunyo"
# print('-'.join(a))


# 6 masala

# def baholash(ismlar):
#  bahola = {}
#  while ismlar:
#     ism = ismlar.pop()
# #pop kalit suzi bu aperator ruyxat ichidagi oxirgi obektni surab oladi
#  baho = input(f"uquvchi {ism.title()} bahosini kiriting = ")
#  baholash[ism]=int[baho]
#  return
# talabalar =["aziz",'azamat','sardor','dilshod']
# talabalar = baholash (talabalar[:])
# print(talabalar)


# a = int(input('birinchi soni kiriting ='))
# b = int(input("ikkinchi soni kiriting ="))
# c = int(input("uchunchi soni kiriting ="))




# D = b**2-4*a*c
# print('tinglamani yichimi',D)

# a = int(input('birinchi soni kiriting ='))
# son = [2,4,5,8]
# print(son[0])



# a = int(input('birinchi soni kiriting ='))
# son = 0-a
# print(son)

# 1 masala

# print(type([1,2,'python']))



# 2 masala


# def foo(var):

#    var = var + '+'
#    var = var * 2
#    return  var
# print(foo("python"))


# 3 masala




# var = ['spam','harm','eggs']
# print(list(enumerate(var)))




# 4 masala

# word ='python'

# print(word[42])



# def dilshod(ism):
#     pass

#pass kalit suzi - obektdan olingan qiymatni bush shaklida qaytaradi , yani xatolik qaytarmaydi

# #argimendsiz funksiya kurinishi 
# def salom():
#     print("salom")
# salom()    


# moslashuvchan fungsiya bu bitta obekta aniqmas bulgan ilf argumentalrni berish uchu n ishlatiladi belgisi :

#** args metodi





# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.

# Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')




# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} so'm")



# kun = (input("Bugun nima kun?"))
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")


# import matplotlib.pyplot as plt
# import numbers as np 
# from matplotlib.colors import ListedColormap

# board = np.tile([1, 0],[8, 4])
# for i in range( board. shape[0] ) :
#     board[i]=np.roll(board[i],i%2)

# cmap = ListedColormap(['#779556','#ebecd0']) 
# plt.matshow(board,cmap=cmap,)   
# plt.xticks([])
# plt.xticks([])
# plt.show()
 

# a = int(input("yoshingizni kiriting = "))
# print("yoshingizni",{2022-a},'da')



# a = int(input("yilingiz kiriting ="))
# print("yilingiz",{18-2022},'da')

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 1 masala

# a = [1,9,9]
# print(a[0])

# 2 masala

# a = [1,9,9]
# print(a[-1])


# 3 masala



# def dilshod(ism):
#   pass

# 4 masala

# a = [1,2,3,4,5,6,7]
# print(a[-1],a[-2],a[-3],a[-4],a[-5],a[-6],a[-7])

# 5 masala

# a = int(input("istalagan son kirit = "))

# a = (0)
# print(-1)

# 6 masala


# dilshod = ['lada','nexa 3 ','koblit']
# print(dilshod[0],dilshod[1],dilshod[2])

# 7 masala

# lest = ['lada', 'koblit', 'lacetti' ,'malibu', 'trekir', 'kapteva ']
# print(lest[3],lest[4],lest[5])

# 8 masala


# a = int(input('birinchi soni kiriting ='))
# b = int(input("ikkinchi soni kiriting ="))
# c = int(input("uchunchi soni kiriting ="))

# print('tinglamani yichimi',b)

# 9 masala

# x = int(input("fungsiya uchun x ni kiriting = "))
# y = 3*(x**2)- 4*x +6
# print(y)

# 10 masala

# d = str(input("ismingiz kiriting = "))
# print(f" ism {d}", 'yosh', 18,'da' )


























