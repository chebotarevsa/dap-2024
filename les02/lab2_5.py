# Определение класса узла списка (обычно уже есть на платформе)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Создаём фиктивный узел для удобства
        dummy = ListNode(-1)
        current = dummy
        
        # Проходим по спискам пока есть элементы
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Присоединяем оставшийся список
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # Возвращаем начало нового списка
        return dummy.next
