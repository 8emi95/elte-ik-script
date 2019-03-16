
require 'test/unit'

def mySum(list)
    i = 0 
    list.each{|x|
      i += x.to_i
    }
    return i
end


class TestTitleize < Test::Unit::TestCase
   def test_basic
      assert_equal(20, mySum([5,4,6,2,3]))
      assert_equal(30, mySum([5,-10,'20',5,'-4',3,'11']))
      assert_equal(10, mySum(['a','b','c']))
   end
end


