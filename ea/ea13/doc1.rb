#!/usr/bin/env ruby

# Ez az osztaly ZH-krol tartalmaz infokat... 
class ZH

   # Letrehoz egy ZH objektumot a terem es idopont megadasaval.
      def initialize(terem, ido)
          @hely = terem
          @ido = ido
          @hallgatok = [] 
      end
      
   # Feljelentkezes a ZH-ra.
      def jelentkezes(hallgato)
          @hallgatok += [hallgato]
      end
      
      def print_info
          print(@hely + "\n")
          print(@ido + "\n")
          puts(@hallgatok)
      end    
      
      attr_reader :hallgatok
      
end

zh1 = ZH.new("2.712", "május 20. 12:00") #zh1 letrehozasa
zh1.jelentkezes("Nagy Árpád")
zh1.jelentkezes("Kiss Géza")
zh1.print_info

# Ez a fuggveny megadja annak a vizsganak az adatait, amire 
# feliratkozott a megadott szemely.
def keres (hallgato, zhk)
  zhk.each{|zh|
     zh.print_info if zh.hallgatok.include?(hallgato)
  }
end

keres("Nagy Árpád", [zh1])


# rdoc doc1.rb



