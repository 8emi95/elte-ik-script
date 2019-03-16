require "debug1"


x = 1

while x < 100 

   x = x * 2

end   

# $ ruby -r debug debug2.rb 
# Debug.rb
# Emacs support available.
# 
# debug2.rb:1:require "debug1"
# (rdb:1) list
# [-4, 5] in debug2.rb
# => 1  require "debug1"
#    2  
#    3  
#    4  x = 1
#    5  
# (rdb:1) step
# ./debug1.rb:2:i,j = 0,1
# (rdb:1) step
# ./debug1.rb:3:while j < 100000
# (rdb:1) step
# ./debug1.rb:4:  j *= 3
# (rdb:1) list
# [-1, 8] in ./debug1.rb
#    1  
#    2  i,j = 0,1
#    3  while j < 100000
# => 4    j *= 3
#    5    i += 1
#    6  end
#    7  
#    8  puts "i: #{i}, j: #{j}"
# (rdb:1) 

