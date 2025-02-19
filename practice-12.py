class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedListManager:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data: 'Node'):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        node_model = self.head
        while node_model.next:
            node_model = node_model.next
        node_model.next = new_node
        
    def check_length(self, index):
        node_model = self.head
        count = 0
        while node_model:
            count += 1
            node_model = node_model.next
        if count > index:
            return count
        else:
            return False
        
    def insert_at_i(self, data, index):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        if self.check_length(index) != False:
                   
            node_model = self.head
            count = 0
            while node_model and count < index-1 :
                node_model = node_model.next
                count += 1

            new_node.next = node_model.next
            node_model.next = new_node        
        else:
            print("your index number is out of the range!")

    def pop_from_beginning(self):
        if not self.head:
            print("list is empty!")
            return None
        node_model = self.head
        self.head = self.head.next
        return node_model
    
    def pop_from_end(self):
        if not self.head:
            print("list is empty!")
            return None
        if not self.head.next:
            removed_node= self.head.data
            self.head = None
            return removed_node
        node_model = self.head
        while node_model.next.next:
            node_model = node_model.next
        removed_node = node_model.next.data
        node_model.next = None
        return removed_node
    
    def pop_from_i(self, index):
        if index == 0:
            node_model = self.head
            self.head = self.head.next
            return node_model.data 
                      
        if self.check_length(index) != False:
            node_model = self.head 
            count = 0
            while node_model.next and count < index-1:
                node_model = node_model.next
                count += 1
            removed_node = node_model.next.data
            node_model.next = node_model.next.next
            return  removed_node
        else:
            print("your index number is out of the range!")
    
    def data_changing(self, index, new_data):
        if index == 0:
            self.head.data = new_data
            return 
        if self.check_length(index) != False:
            node_model = self.head
            count = 0 
            while node_model.next and count < index-1:
                node_model = node_model.next
                count += 1
            node_model.next.data = new_data
            return node_model.next
        else:
            print("your index number is out of range!")
    
    def list_connecting(self, other:'Node'):
        if not self.head:
            self.head = other.head
            return 
        node_model = self.head
        while node_model.next:
            node_model = node_model.next
        node_model.next = other.head
    
    def data_search(self, data):
            node_model_1 = self.head
            length = 0
            while node_model_1:
                length += 1
                node_model_1 = node_model_1.next
            node_model_2 = self.head
            count = 0
            
            while node_model_2.next and count < length -1:
                node_model_2 = node_model_2.next
                count += 1
                if node_model_2.data == data:
                    print(node_model_2.data, count)
            if self.head.data == data:
                print(self.head.data, 0)

    def index_search(self, input):
        node_model = self.head
        count = 0
        index = input[0]
        while node_model.next and count < index -1:
            count += 1
            node_model = node_model.next
        print(node_model.next.data, index)
        if index == 0 : 
            print(node_model.data, 0)
        
    def list_sorting(self):
        node_model_1 = self.head
        length = 0
        while node_model_1:
            length += 1
            node_model_1 = node_model_1.next
        node_model_2 = self.head
        count = 0
        print(length)
        node_model_2 = self.head
        while count < length:
            count += 1
            node_model_2 = self.head
            for i in range (length-1):
                            
                if node_model_2.data > node_model_2.next.data:
                    node_model_2.data, node_model_2.next.data = node_model_2.next.data, node_model_2.data
            
                node_model_2 = node_model_2.next
            
    def display(self):
        node_model = self.head
        while node_model:
            print(node_model.data, end = ("--->"))
            node_model = node_model.next
        print("none")
            
            
ll = LinkedListManager()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.insert_at_beginning(30)
ll.insert_at_end(40)  
ll.insert_at_end(50)  
ll.display()
ll.insert_at_i(3, 7)
ll.insert_at_i(2, 3)
ll.display()
ll.pop_from_beginning()
ll.display()
ll.pop_from_end()
ll.display()
ll.pop_from_i(0)
ll.display()
ll.data_changing(0, 5)
ll.display()
l2 = LinkedListManager()
l2.insert_at_beginning(10)
l2.insert_at_beginning(20)
l2.insert_at_beginning(30)
l2.insert_at_end(40)  
l2.insert_at_end(50)
ll.list_connecting(l2)
ll.display()
ll.data_search(5)
ll.index_search([2])
ll.list_sorting()
ll.display()