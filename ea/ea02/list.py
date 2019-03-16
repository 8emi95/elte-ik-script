#! /usr/bin/env python
# -*- coding: utf-8 -*-	

# Lista adatszerkezet
#listát könnyen sok mindenre lehet használni

list = [0,1,2,3,4]                 

#1 elem hozzáfűzése
list.append(5)   # list[len(list):] = [5]
print list
# [0, 1, 2, 3, 4, 5]

#több elem hozzáfűzése (másik lista elemeit konkatenálom)
list.extend([6,7,8])   # list[len(list):] = [6,7,8]
print list
# [0, 1, 2, 3, 4, 5, 6, 7, 8]

list.insert(4,"uj_elem") # adott indexu elem ele szur be
print list
# [0, 1, 2, 3, 'uj_elem', 4, 5, 6, 7, 8]

list.insert(42,"uj_elem") #nem létező indexszel meghívva a végére szúrja be
print list
# [0, 1, 2, 3, 'uj_elem', 4, 5, 6, 7, 8, 'uj_elem']

list.remove("uj_elem") #elemek törlése, értéket szedi ki a remove (egy db olyan értéket)
print list
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 'uj_elem']

#list.remove(12) #ha nincs ilyen akkk szól
# ValueError: list.remove(x): x not in list

list = ['nulla','egy','ketto','harom'] #elem kiszedése, vissza is kapom
x = list.pop(2)
print list, ",", x
# ['nulla', 'egy', 'harom'] , ketto

x = list.pop() #paraméterül hívva az utolsó elemet szedi ki
print list, ",", x
# ['nulla', 'egy'] , harom

#x = list.pop(42)
# IndexError: pop index out of range

stack = []
stack.append(1) #pushra át lehet definiálni
stack.append(2)
print stack
# [1, 2]
stack.pop()
print stack
# [1]

print list.index('egy')
# 1

#list.index("uj_elem") #ha nem létezik az elem aminek az indexét kérjük
#ValueError: list.index(x): x not in list

print [1,2,1,3,4,1].count(1) #megszámlálás
# 3

list = [3,2,4,1,5,8,7] 
list.sort() #növekvő rendezés
print list
# [1, 2, 3, 4, 5, 7, 8]

list.reverse() #csökkenő rendezés
print list
# [8, 7, 5, 4, 3, 2, 1]


#--------------------------------------------


#filter: feltételt teljesítő elemeket hagyja meg a listábna, listából listát csinál
#paraméter fv lesz VAGY lambda fv ha nem akarjuk máshol használni
print filter(lambda x: x%3==0, range(1,10)) #range fv alsó indextől felső indexig tartó listát...
# [3, 6, 9]

#listára vár fv-t amit minden elemre tud alkalmazni (pl intnél, int>vmi fv)
#végigmegy listaelemeken, végrehajtja
print map(lambda x: x**2, range(1,10))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

list = range(1,10)
print map(lambda x, y : x+y, list, list) #1. pm fv, a többi annyi lista amennyi paramétert várunk
#2 lista elemeit összeadogatja
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

def fv(x,y) : print x, y; #ha kül hosszú listák, elfogy a lista akk none értéket alkalmaz, hosszabb lista szerint megy
map(fv, range(1,3), range(1,5))
# 1 1
# 2 2
# None 3
# None 4

#mapnek nem adunk fvparamétert, rendezett n-eseket ad vissza
print map(None, range(1,10,2), range(2,11,2)) #1-10 párosak? 2esével léptetve
# [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

#fold - egymás után dolgozza fel a lista elemeit, előzőleg megkapott eredménnyel számol
print reduce(lambda x, y : x+y, range(1,11)) #összegzés, lista elemeit összeadja egymás után
# 55

#+ [1,2,3,4,5 ... 10]
#1+2
# 3+3
#  6+4
#   10+5
#     ...

print reduce(lambda x, y : x+y, range(1,11), 20) # a -> b -> a, [b], a
#sting int -> string
#mint az előző csak 20hoz adja hozzá előbb
# 75

#+ [1,2,3...10] 20
#20+1
#  21+2
#    23+3
#	  ...

print [x**2 for x in range(1,10)] #lista-konstruktor [kifejezés h hogyan számoljuk ki, milyen listából] map rövidebb leírása
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

print [x**2 for x in range(1,10) if x > 5] #filter, feltételekkel
# [36, 49, 64, 81]

print [x*y for x in [2,4] for y in [3,5]] #xbe 2es, keres hozzá yt, yba 3ast aztán 5öst
# [6, 10, 12, 20]

print [x*y for x, y in zip([2,4],[3,5])] #párhuzamosan megy végig listákon, olyan listát vár ahol egy elem egy pár
# [6, 20]

print zip([1,2,3],[5,6])
# [(1, 5), (2, 6)]