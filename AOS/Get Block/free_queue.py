import buffer_header

class Free_Queue():
 
    def __init__(self, head=None, tail=None):
        
        self.head = head
        self.tail = tail
 
    
    
    def add_to_tail(self,  new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev_flist = self.tail
            new_node.next_flist = None
            self.tail.next_flist = new_node
            self.tail = new_node
    
    
    
    
    def add_to_head(self,  new_node):
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next_flist = self.head
            new_node.prev_flist = None
            self.head.prev_flist = new_node
            self.head = new_node
 
    
    def remove(self, current_node):
        
        if self.head == current_node:
            self.head = current_node.next_hqueue
        if self.tail == current_node:
            self.tail = current_node.prev_hqueue

        
        current_node.prev_hqueue.next_hqueue = current_node.next_hqueue
        current_node.next_hqueue.prev_hqueue = current_node.prev_hqueue