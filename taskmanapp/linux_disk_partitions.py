#encoding=utf-8
#!/usr/bin/env python
import os

def disk_linux_partitions():
    partition_list = []
    a = os.popen("df -h")
    for i in a:
		partition_list.append(i.split()[0])
		print partition_list[1:]
    return partition_list[1:]

if __name__ == "__main__":
    disk_linux_partitions()    
