# -*- coding: utf-8 -*-

x = "global_x"

def localfv2() :
    y = "fv2_y" #kicsit lokális, nagyon lokális még eggyel beljebb lenne
    
    def localfv3() :
        global x, y #melyik x,y? legkülső, a teljes modulra vonatkozó akk is ha nem volt ilyen
        x, y = "fv3_x", "fv3_y"
    
    print "Az y értéke kezdetben:", y
    localfv3()    
    print "Az y értéke fv2 végén:", y

print "Az x értéke kezdetben:", x
localfv2()
print "Az x, y értéke végül:", x, y

# Az x értéke kezdetben: global_x
# Az y értéke kezdetben: fv2_y
# Az y értéke fv2 végén: fv2_y
# Az x, y értéke végül: fv3_x fv3_y
