#!/usr/bin/env ruby


#= Reszletesebb dokumentacio.
#
#== Attributumok
#
#* Az osztaly belso attributumai:
# * hely,
# * ido,
# * hallgatok.
#* Ebbol kintrol elerheto:
# * hallgatok.
#
#== Metodusok
#
#Az osztaly metodusai az *initialize*, *jelentkezes*, *printInfo* 
#reszletezve vannak az alap doksiban, igy arrol
#itt nem irok. 
#
#Ezen kivul van egy _rejtett_ metodus, ami igy fest:
#
# def rejtett_print   
#          puts(@hallgatok)
# end
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
      
      def printInfo
          print(@hely + "\n")
          print(@ido + "\n")
          puts(@hallgatok)
      end
      
      def rejtett_print    #:nodoc:
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

keres("Nagy arpad", [zh1])


# rdoc doc3.rb



