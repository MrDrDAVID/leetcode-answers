class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) :
        """
        function that takes in two list nodes and adds the reversed values of the linked list
        then returns the value within a linked list 
        """
        str1 = ''
        str2 = ''
        
        while l1 is not None :
            str1 = str(l1.val) + str1
            l1 = l1.next
            
        while l2 is not None : 
            str2 = str(l2.val) + str2
            l2 = l2.next

        int1 = int(str1)
        int2 = int(str2)

        final_int = int1 + int2
        final_str = str(final_int)

        root_node = ListNode(int(final_str[0]))
        for val in final_str[1:] :
            temp_node = ListNode(int(val))
            temp_node.next = root_node
            root_node = temp_node
        
        return root_node