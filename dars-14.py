
# Eski uslub funksiya
# def yigindi(son1, son2):
#     summa = son1+son2
#     print(summa)
# yigindi(1,2)


#########################################################################################


# funksiya orqali takrorlanish operatori bilan list ko'rinishidagi sonlar yig'indisini topish

# def summa(raqamlar):
#     natija = 0
#     for x in raqamlar:
#         natija += x
#     return natija

# sonlar = [1, 2, 3, 4]
# print(summa(sonlar))


############################################################################################




# def yigindi(*argumentlar):
#     natija = 0
#     for x in argumentlar:
#         natija += x
#     return natija

# print(yigindi(1, 2, 3, 4))

#####################################################################################


# Moslashuvchan funsiyada sonlar bilan ishlashda alohida listlar bilan qiymat qaytarganida args usuli qo'llaniladi


# def yigindi(*args):
#     qiymat = 0
#     for x in args:
#         qiymat += x
#     return qiymat

# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8, 9]
# son = list1+list2+list3

# print(yigindi(*son))









#############################################################################




# Berilgan matnni hafma harf kiritish


# matn = [*"Assalomu alaykum"]
# print(matn)










######################################################################################
#Vazifa_1

# def shartnoma(talaba_ism,talaba_familiya,**malumotlar):
#     malumotlar['ism']=talaba_ism
#     malumotlar['familiya']=talaba_familiya
#     return malumotlar

# t1 = shartnoma('Asilbek','Ahmadov', yosh=20, yil = 1998, kurs= "3-kurs talabasi", guruh=305)
# t2 = shartnoma("E'zozbek ",'Shokirov', yil = 2001, kurs="4-kurs talabasi")
# print(t1,t2)





# def shartnoma (talaba_ism,talaba_familiya,**malumotlar):
#     malumotlar['ism']=talaba_ism
#     malumotlar['familiya']=talaba_familiya
#     return malumotlar

# t1 = shartnoma('dilshodbek', 'muhammadiyev', yosh=18, yil = 2004, kurs = "1- kurs talabasi", guruh=305)
# t2 = shartnoma('azizbek','gulomov', yosh=20, yil=2002,kurs= "1-kurs talabasi" )
# print(t1,t2)

# def yigindi (son1, son2):
#  summa = son1+son2
#  print(summa)
 
# yigindi(1,2,)


# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar


# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

# print(avto2)




# import math

# x=400
# print(math.sqrt(x))

# print(pow(5,5))


# from math import pi
# print(pi)
# # ////////////////////////////////////////////////////////////////////////////////////////////////
# import math
# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))def daraja(n):

# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja (3)
# print(f"3-ning kvadirati {kvadrat(3)} ga,kubi {kub(3)} ga teng ")



# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar))) # sonlar ning kvadratini hisoblaymiz

# kvadratlar = []
# for son in kvadratlar:
#   kvadratlar.append(son*son)
# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)


# mevalar4 = list(filter(lambda meva:len(meva)<=5, 'mevalar'))
# print(mevalar4)

# v = 0b1011
# print(hex(v))

# print(6 or 8)

# sonlar = [1,2,3,4,5,6]
# for son in sonlar:
#     print(sonlar)


# moslashuvchan funksiya bu funksiyaga berilgan argumentlarni
#  istalgancha kurinshda istalgancha turkumda qabul qilishdan iborat


# def summa(*sonlar):

#sonlar- bu funksiyaning argumenti args metodi buylab 
#     yigindi=0
#yigindi= 10 bu funksiya oraligini boshlanishi 

#     for son in sonlar:
#         yigindi+=son
#         return yigindi
# print (summa(1,2,3))

# gavargs ** ishlatiladi 
# def avto_info(ism,familiya,malumot):
#     malumot['ism']==ism
#     malumot['familiya']==familiya
#     return malumot
#     t1(talaba_info("dilshod"" muhammadiyev",18))
#     t2(talaba_info("aziz""gullomov",20))
#     print(t1+t2)




# def baholar(ism,familiya,**bahosi):
#     bahosi['ism']=ism
#     bahosi['familiya']=familiya

#     return bahosi

# natij1 =baholar("dilshod","muhammadiyev",baho = 5, fan='dasturlash')
# print("uquvchi haqida malumot",natij1)
    



def Iels (lestenig,reading,writing,speaking):
    umumiy = {
        'listening':lestenig,
        'reading':reading,
        'writing':writing,
        'speaking':speaking,

    }
    return umumiy
tekshirish = []

while True:
  lestenig=input("Listening kiriting = ")
  reading=input("Reading kiriting = ")
  writing=input("Wri kiriting = ")
  speaking=input("Speak kiriting = ")
  tekshirish.append(Iels(lestenig,reading,writing,speaking))
  break


print(f"{lestenig}, {reading}, {writing} {speaking}")




























