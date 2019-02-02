import buffer_header
import hash_queue
import free_queue

buffers = []
free_list = free_queue.Free_Queue()
hash_list1 = hash_queue.Hash_Queue()


for x in range(10):
    buffers.append(buffer_header.Buffer_Header(x))
    free_list.add_to_tail(buffers[x])


free_list.show()


for x in range(5,10):
    free_list.remove(buffers[x])
    hash_list1.add(buffers[x])



free_list.show()
hash_list1.show()