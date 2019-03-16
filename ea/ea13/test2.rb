
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
      assert(mySum([5,-10,20]) == mySum(['5','-10','20']))
   
      assert_equal(20, mySum([5,4,6,2,3]))
      
      assert_not_equal(10, mySum(['a','b','c']))
      
      assert_raise( NoMethodError) {mySum([1,2,3]) + mySum(1)}
      
      assert_nothing_raised(NoMethodError) {mySum([1,2,3]) + mySum(1)}
 
   end
end


