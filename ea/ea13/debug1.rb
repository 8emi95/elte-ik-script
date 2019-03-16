

i,j = 0,1
while j < 100000
  j *= 3
  i += 1
end

puts "i: #{i}, j: #{j}"



# $ ruby -r debug debug1.rb 
# Debug.rb
# Emacs support available.

# debug1.rb:3:i,j = 0,1
# (rdb:1) list
# [-2, 7] in debug1.rb
#    1  
#    2  
# => 3  i,j = 0,1
#    4  while j < 100000
#    5    j *= 3
#    6    i += 1
#    7  end
# (rdb:1) step
# debug1.rb:4:while j < 100000
# (rdb:1) step
# debug1.rb:5:  j *= 3
# (rdb:1) i
# 0
# (rdb:1) j
# 1
# (rdb:1) step
# debug1.rb:6:  i += 1
# (rdb:1) i
# 0
# (rdb:1) j
# 3
# (rdb:1) step
# debug1.rb:5:  j *= 3
# (rdb:1) j
# 3
# (rdb:1) j = 100
# 100
# (rdb:1) step
# debug1.rb:6:  i += 1
# (rdb:1) j
# 300
# (rdb:1) break 5
# Set breakpoint 1 at debug1.rb:5
# (rdb:1) cont
# Breakpoint 1, toplevel at debug1.rb:5
# debug1.rb:5:  j *= 3
# (rdb:1) cont
# Breakpoint 1, toplevel at debug1.rb:5
# debug1.rb:5:  j *= 3
# (rdb:1) i
# 3
# (rdb:1) j
# 900
# (rdb:1) quit
# Really quit? (y/n) y


# $ ruby -r debug debug1.rb 
# Debug.rb
# Emacs support available.
# 
# debug1.rb:2:i,j = 0,1
# (rdb:1) watch j > 10000
# Set watchpoint 1:j > 10000
# (rdb:1) cont
# Watchpoint 1, toplevel at debug1.rb:5
# debug1.rb:5:  i += 1
# (rdb:1) i
# 8
# (rdb:1) j
# 19683
# (rdb:1) quit
# Really quit? (y/n) y


