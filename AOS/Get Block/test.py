import buffer_header
import hash_queue
import free_queue

buffers = []
free_list = []
for x in range(50):
    buffers.append(buffer_header.Buffer_Header())
    free_list.append(free_queue.Free_Queue(buffers[x]))
    