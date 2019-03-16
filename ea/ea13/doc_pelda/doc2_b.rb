
# Dokumentacios pelda II.

require "doc2_a" # a doc2_a fajl importalasa
 

# Ez az osztaly tantargyakrol tartalmaz infokat.
class Tantargy

   # Letrehoz egy tantargy objektumot a neve megadasaval.
   def initialize(nev)
       @nev = nev
       @zhk = []
   end
   
   # ZH-kat ad hozza a tantargyhoz (a meglevo listat bovitve).
   def addZH(zhk)
      @zhk += zhk
   end
   
   # Kiirja a tantargyhoz tartozo zh-k infoit.
   def print_info
      @zhk.each{|zh|
        zh.print_info
      }   
   end
   
end   

t1 = Tantargy.new("Programozási nyelvek")

zh1 = ZH.new("2.712", "május 20. 12:00") #zh1 letrehozasa
zh1.jelentkezes("Nagy Árpád")
zh1.jelentkezes("Kiss Géza")

zh2 = ZH.new("2.502", "május 25. 12:00") #zh2 letrehozasa
zh2.jelentkezes("Fehér Pál")

t1.addZH([zh1,zh2])
t1.print_info


# rdoc

