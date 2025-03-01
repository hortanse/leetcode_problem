#Reverse a linked list
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def reverse_linked_list(head):
        prev = None
        current = head

        while current:
            next_node = current.next #store next node
            current.next = prev # reverse pointer
            prev = current #move prev forward
            current = next_node #move current forward
        
        return prev # new head of reversed list
    