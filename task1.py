class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value  # Значення вузла
        self.next = next  # Посилання на наступний вузол

class LinkedList:
    def __init__(self):
        self.head = None  # Початковий вузол списку
    
    def append(self, value):
        """Додає новий елемент в кінець списку"""
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)
    
    def print_list(self):
        """Виводить список у консоль"""
        current = self.head
        while current:
            print(current.value, end=' -> ')
            current = current.next
        print('None')
    
    def reverse(self):
        """Реверсує список, змінюючи посилання між вузлами"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def merge_sort(self):
        """Сортує список методом злиття"""
        def merge(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.value < right.value:
                    tail.next, left = left, left.next
                else:
                    tail.next, right = right, right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        def sort_list(node):
            if not node or not node.next:
                return node
            slow, fast = node, node.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            mid, slow.next = slow.next, None
            left, right = sort_list(node), sort_list(mid)
            return merge(left, right)
        
        self.head = sort_list(self.head)
    
    @staticmethod
    def merge_sorted_lists(l1, l2):
        """Об'єднує два відсортовані списки в один"""
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.value < l2.value:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

# Тестовий демонстраційний список
ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(1)
ll.append(3)

print("Оригінальний список:")
ll.print_list()

ll.reverse()
print("Реверсований список:")
ll.print_list()

ll.merge_sort()
print("Відсортований список:")
ll.print_list()
