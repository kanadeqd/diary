class Solution:
    def isUnique(self, astr: str) -> bool:
        #return len(set(astr)) == len(astr) 
        # nothing to say.
		mark = 0
		for i in astr:
			num = ord(i) - ord("a")
			if (mark & (1 << num)) != 0:
				return False
			else:
				mark |= (1 << num)
		return True
		
		# 位运算, 当&后为1证明重复
		