import random
row_number=random.sample(range(1,922137),500000)
row_number.sort()
file_read=open("C:/Users/kharb/Desktop/IS/Kyoto2016/2015/01/20150105.txt","r")
file_write=open("C:/Users/kharb/Desktop/IS/dataset.txt","w+")
file_data=[]
for line in file_read:
    file_data.append(line)
file_read.close()
for x in range(1,500000):
    file_write.write(file_data[row_number[x]])
file_write.close()