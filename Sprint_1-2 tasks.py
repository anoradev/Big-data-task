Sprint_1a task


#1) 123 rəqəmini string/character ə çevirin və tipini yoxlayın.

num = 123
char_num = str(num)
print(char_num, type(char_num))

#2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.

price = 19.99
int_price = int(price)
print(int_price)

#3) "500" dəyərini numericə çevirin və 2-yə bölüb nəticəni çap edin.

val = "500"
num_val = int(val)
print(num_val / 2)

#4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.

a = 8
b = 12
print(a < b)
print(a == b)


#5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.

x, y, z = 5, 10, 15
print((x < y) and (y < z))

#6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.

print(25 // 4)  # tam bölmə
print(25 % 4)   # qalıq
print(25 / 4)   # adi bölmə

#7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.

print(3 ** 4)

#8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.

qiymet = 75.5
int_qiymet = int(qiymet)
print(int_qiymet, type(int_qiymet))

#9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.

n = 20
print((n > 10) or (n < 5))
print((n > 15) and (n < 25))

#10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın.

val = "42.8"
float_val = float(val)
print(float_val, type(float_val))
int_val = int(float_val)
print(int_val, type(int_val))







Sprint_1b task


#1) s = "Programming" yaradın. Uzunluğunu və ilk simvolunu çap edin.

s = "Programming"
print(len(s), s[0])


#2) s1 = "Hello" və s2 = "World" yaradın. Onları boşluqla birləşdirin və nəticəni çap edin.

s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

#3) text = "Python" yaradın. Son simvolunu çap edin.

text = "Python"
print(text[-1])

#4) s = "Artificial" yaradın. "Art" hissəsini ilə çıxarın və çap edin.

s = "Artificial"
print(s[:3])

#5) word = "Code" yaradın. Tərsinə çevirin və nəticəni çap edin.

word = "Code"
print(word[::-1])

#6) s = "abcdefgh" yaradın. Hər ikinci simvolu alın və çap edin.

s = "abcdefgh"
print(s[::2])

#7) text = "data" yaradın. Onu bir sətrlik kodla böyük hərflərə və kiçik hərflərə çevirib çap edin.

text = "data"
print(text.upper(), text.lower())

#8) s = "Python-R-Java" yaradın. "-" ilə ayırın (split("-")) və nəticəni çap edin.

s = "Python-R-Java"
print(s.split("-"))

#9) ad = "Ayxan" və yaş = 25 yaradın. f-string ilə "Ayxan 25 yaşındadır" çap edin.

ad = "Ayxan"
yas = 25
print(f"{ad} {yas} yaşındadır")

#10) s = "salam-dunya" yaradın. "-"ni boşluqla əvəz edin və nəticəni çap edin.

s = "salam-dunya"
print(s.replace("-", " "))














 Sprint_2a_task


#1) 5, 10, 15, 20 rəqəmlərindən ibarət “rəqəmlər” adlı list/vector yaradın

reqemler = [5, 10, 15, 20]

#2) “rəqəmlər” listinin/vectorunun uzunluğunu tapın

print("Uzunluq:", len(reqemler))

#3) “rəqəmlər” listinə/vectoruna 25 elementini əlavə edin

reqemler.append(25)
print("yeni reqem əlavə olundu:", reqemler)

#4) “rəqəmlər” listinin/vectorunun 2-ci indeksinə 12 elementini əlavə edin

reqemler.insert(2, 12)
print("2-ci indeksə 12 əlavə olundu:", reqemler)


#5) 1, 2, 3 və 4, 5, 6 listlərini/vectorlarını birləşdirin

list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis_list = list1 + list2
print("Birləşmiş list:", birlesmis_list)

#6) “rəqəmlər” listindən/vectorundan 2-ci və 3-cü elementləri seçin

print("2-ci və 3-cü elementlər:", reqemler[2:4])

#7) “rəqəmlər” listinin/vectorunun ilk elementini 50 ilə əvəz edin 

reqemler[0] = 50
print("İlk element 50 ilə əvəz olundu:", reqemler)

#8) “rəqəmlər” listində/vectorunda 19 elementinin olub-olmadığını yoxlayın

print("19 listdə var?", 19 in reqemler)

#9) "a", "b", "a", "c" listində/vectorunda "a" elementinin neçə dəfə təkrarlandığını tapın

herfler = ["a", "b", "a", "c"]
print("'a' neçə dəfə var:", herfler.count("a"))

#10) "x", "y", "x", "z" listindən/vectorundan "x" elementlərini silin

simvollar = ["x", "y", "x", "z"]
while "x" in simvollar:
    simvollar.remove("x")
print("'x' silindikdən sonra:", simvollar)

#11) 7, 2, 9, 1 listini/vectorunu azalan sırayla sıralayın

nums = [7, 2, 9, 1]
nums.sort(reverse=True)
print("Azalan sırayla:", nums)

#12) “rəqəmlər” listindən/vectorundan 10-dan böyük elementləri seçin

boyuk_10 = [x for x in reqemler if x > 10]
print("10-dan böyük elementlər:", boyuk_10)














Sprint_2b_task

import pandas as pd

#1) 10, 20, 30, 40 elementlərindən ibarət s1 adlı series/vector yaradın

s1 = pd.Series([10, 20, 30, 40])

#2) s1-ə 'w', 'x', 'y', 'z' indekslərini təyin edin

s1.index = ['w', 'x', 'y', 'z']
print("s1:\n", s1)

#3) Python: {'p': 5, 'q': 10, 'r': 15} dictionary-dən s2 adlı Series yaradın
    R: list(p = 5, q = 10, r = 15) listindən v2 adlı named vektor yaradın

data_dict = {'p': 5, 'q': 10, 'r': 15}
s2 = pd.Series(data_dict)
print("s2:\n", s2)


#4) s2-dən 'q' indeksli elementi seçin

print("s2['q']:", s2['q'])


#5) s1-dən 25-dən böyük elementləri seçin

print("25-dən böyük elementlər:\n", s1[s1 > 25])


#6) s1-də 20-dən böyük elementləri 10-a bölün 

print("20-dən böyük elementləri 10-a böl:\n", s1[s1 > 20] / 10)

#7) ((1, 2), (3, 4)) listindən/vectorundan df1 adlı dataframe yaradın

df1 = pd.DataFrame([(1, 2), (3, 4)])

#8) df1-ə ('r1', 'r2') sətir və ('c1', 'c2') sütun adlarını təyin edin

df1.index = ['r1', 'r2']
df1.columns = ['c1', 'c2']
print("df1:\n", df1)


#9) Python: {'A': [1, 2], 'B': [3, 4]} dictionary-dən df2 yaradın

df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("df2:\n", df2)

#10) df2-də 'A' sütunu 1-dən böyük olan sətirləri seçin

print("A sütunu 1-dən böyük olan sətirlər:\n", df2[df2['A'] > 1])