# encoding: UTF-8

puts Dir.entries(".")
# ..
# test1.rb
# doc1.rb
# base15.rb
# test2.rb
# debug2.rb
# profile.rb
# tmp
# .
# doc_pelda
# doc
# doc3.rb
# tmp2
# debug1.rb

puts Dir.pwd
# /home/matej/scny/2015/ea13

Dir.chdir("tmp")
puts Dir.pwd
# /home/matej/scny/2015/ea13/tmp

Dir.chdir("..")

Dir.chdir("tmp"){
   puts Dir.entries(".")
}
# ..
# tmp.txt
# .

puts Dir.pwd
# /home/matej/scny/2015/ea13


Dir.foreach("tmp2"){|n|
  puts n
}
# ..
# tmp2.txt
# .
# subtmp
# tmp5.txt


Dir.chdir("tmp2")

Dir.glob('*.txt'){|n|
  puts n
}
# tmp2.txt
# tmp5.txt

txtfiles = File.join("**", "*.txt")

Dir.glob(txtfiles){|n|
  puts n
}
# tmp2.txt
# subtmp/tmp3.txt
# subtmp/tmp4.txt
# tmp5.txt

puts Dir.pwd
#/home/matej/scny/2015/ea13/tmp2

puts File.directory?("subtmp")
# true

puts File.file?("klkl")
# false

out =  `dir`
puts out
# subtmp	tmp2.txt  tmp5.txt

n = "subtmp"
out = `dir #{n}`
puts out
# tmp3.txt  tmp4.txt

n = "subtmp"
out = %x{dir #{n}}
puts out
# tmp3.txt  tmp4.txt

system("dir")
# subtmp	tmp2.txt  tmp5.txt





