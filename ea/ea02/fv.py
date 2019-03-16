# -*- coding: utf-8 -*- 

#csak fv (no eljárás?)
#ha nem adunk meg visszatérési értéket akk is lesz neki none visszatérési értéke
def fib(x) : #def név(paraméterek), 0 paraméternél ()
    "Az x. Fibonacci-szamot kiszamito fuggveny." #dokumentációs string, 3as "-ban több soros
    a = 0
    b = 1

    if x <= 0 :
        b = 0
    elif x == 1 :
        pass #skip utasítás, nem kell csinálnia semmit itt
    else :
        for i in range(x-1) :
            b , a = a+b, b         
    print "A(z)", x, ". Fibonacci-szam:"
    print "fib-en belul: ", b
    return b   #érték visszaadása, ha kihagyjuk akk az elején lévőt adja vissza, elágazásba is mehet return

n = input("Irj be egy szamot: ")
x = fib(n) #meghívás, érték amivel meghívjuk, változóba bepakoljuk és csinálhatunk vele dolgokat
print "fv-nek atadas utan: ", x
print fib.__doc__
