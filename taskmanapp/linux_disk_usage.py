#econding=utf-8
#! /usr/bin/env python
import os
def disk_usage_linux(disk_name):
    a = os.popen("df -h")
    for i in a:
	if disk_name in i.split()[0]:
	    print disk_name,i.split()[4]
	    return i.split()[4]

if __name__ == "__main__":
    disk_usage_linux('tmpfs')
