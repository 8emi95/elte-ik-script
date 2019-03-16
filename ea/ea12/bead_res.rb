# encoding: UTF-8

begin
   f = File.new(ARGV[0], "r")
rescue TypeError
   puts "Adj meg egy file-t!"
rescue Errno::ENOENT
   puts "Nincs ilyen file!"   
else
   f2 = File.new("eredmeny.txt", "w")
   mx = 0
   maxdata = 0
   f.each_line{|line|
      if not line.empty?
         tags = line.split()
         if tags[0] =~ /\d+/
            if tags[7].to_i > mx
               maxdata = tags[0] + ", " + tags[1]
               mx = tags[7].to_i
            end
            if tags[6].to_i > 50
                  f2.write(tags[0] + ", " + tags[1] + ":: " + tags[7] + " " + tags[8] + "\n")
            end        
         end
      end   
   }
   if mx > 0
      f2.write("max 4-es:: " + maxdata + "\n")               
   end
   f.close()
   f2.close() 
   
   
end
