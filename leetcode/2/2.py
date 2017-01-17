# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
	def addnumbers(self,l1,l2,carry,node):
		if l1 is None and l2 is None:
			if carry is 0:
				return
			node.next=ListNode(carry)
			return
		if l1 is None or l2 is None:
			if l2 is None:
				l2=l1;
				l1=None;

		if l1 is None:
			if carry is 0:
				node.next=l2
				return
			if carry is not 0:
				res,car=Solution.basicadd(self,0,l2.val,carry)
				node.next=ListNode(res)
				Solution.addnumbers(self,l1,l2.next,car,node.next)
				return
		res,car=Solution.basicadd(self,l1.val,l2.val,carry)
		node.next=ListNode(res)
		Solution.addnumbers(self,l1.next,l2.next,car,node.next)



	def basicadd(self,num1,num2,carry):
		res=num1+num2+carry;
		if res >= 10:
			res=res-10;
			return res,1;
		return res,0;

    	def addTwoNumbers(self, l1, l2):
    		retnode=ListNode(0)
    		Solution.addnumbers(self,l1,l2,0,retnode);
    		retnode=retnode.next
    		return retnode

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """



a = ListNode(5)

b = ListNode(5)

def readval(linklist):
	if linklist.next is not None:
		readval(linklist.next)
	print linklist.val

readval(a)


c=Solution()
d=c.addTwoNumbers(a,b)
readval(d)


