#!/usr/bin/env ruby
# Dokumentacios pelda I.


# Ez az osztaly ZH-krol tartalmaz infokat... 
class ZH

   # Letrehoz egy ZH objektumot a terem és idopont megadasaval.
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

# Ez a fuggveny megadja annak a vizsganak az adatait, amire 
# feliratkozott a megadott szemely.
def keres (hallgato, zhk)
  zhk.each{|zh|
     zh.print_info if zh.hallgatok.include?(hallgato)
  }
end







