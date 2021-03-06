# econding=utf-8
import platform
import psutil
from django.shortcuts import render, HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.generic import ListView
import task_learn.settings as settings
import multiprocessing,paramiko
from taskmanapp.models import *
from taskmanapp.linux_disk_partitions import disk_linux_partitions
from taskmanapp.linux_disk_usage import disk_usage_linux



# Create your views here.

def showDashboard(request):
    return render(request, 'index.html')


def getCPUInfo(request):
    a = psutil.cpu_times_percent()
    user_percentage = a.user
    system_percentage = a.system
    print "user and system are ", user_percentage, system_percentage
    return HttpResponse('{"user": %s,"system":%s}' % (user_percentage, system_percentage))


def getMemInfo(request):
    m = psutil.virtual_memory()
    total_mem = m.total / 1024 / 1024
    used_mem_percentage = m.percent
    free_mem_percentage = 100 - m.percent
    print '{"total_mem":%s,"used_mem": %s,"free_mem":%s}' % (total_mem, used_mem_percentage, free_mem_percentage)
    return HttpResponse(
        '{"total_mem":%s,"used_mem": %s,"free_mem":%s}' % (total_mem, used_mem_percentage, free_mem_percentage))

def getDiskioData(request):
    diskioinfo = psutil.disk_io_counters(perdisk=True)
	disk_list = []
    for d in diskioinfo.keys():
		disk_list.append(d)
    print '{"disk_list":%s}' % (disk_list)
    return HttpResponse(
        '{"disk_list":%s}' % (disk_list))

def getDiskInfo(request,disk_name):
    partition_list = []
    device_name = ""
    platform_type = platform.platform()
    if platform_type.startswith("Windows"):
        partition_info = psutil.disk_partitions()
    elif platform_type.startswith("Linux"):
        partition_info = disk_linux_partitions()
    for items in partition_info:
        if platform_type.startswith("Windows"):
            partition_list.append(items.device[:1])
        elif platform_type.startswith("Linux"):
            disk_partition = items.split('/')[-1]
            partition_list.append(disk_partition)
    if platform_type.startswith("Windows"):
        device_name = disk_name + ':\\\\'
        device_usage = psutil.disk_usage(device_name)
        disk_used = device_usage.percent
        disk_free = 100 - device_usage.percent
    elif platform_type.startswith("Linux"):
        disk_used = disk_usage_linux(disk_name).split('%')[0]
        disk_free = 100 - int(disk_used)
    disk_name = '\"' + disk_name + '\"'
    return HttpResponse('{"disk_name":%s,"disk_used": %s,"disk_free":%s}' % (disk_name, disk_used, disk_free))


def file_transfer(request):
    hosts_list = Hosts.objects.all()
    users_list = HostUsers.objects.all()
    return render(request, "file_transfer.html", {"hosts_list": hosts_list, "users_list": users_list})


def command_execution(request):
    hosts_list = Hosts.objects.all()
    t = get_template('command_execution.html')
    # html=t.render(Context({'form_name':'Enter your command:'}))
    html = t.render(Context({'user': request.user,'hosts_list':hosts_list}))
    if request.method == "POST":
		s = paramiko.SSHClient()
		s.load_system_host_keys()
		s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		host_string = request.POST.get("server_list")
		cmd = request.POST.get("command_exe")
		print cmd
		host_list = host_string.split('\n')
		for item in host_list: 
			host = Hosts.objects.get(ip_addr=item.strip())
			port = host.port
			bind_user = BindHosts.objects.get(host=host)
			username = bind_user.host_user.username
			password = bind_user.host_user.password
			s.connect(item,int(port),username,password,timeout=5)
			stdin,stdout,stderr = s.exec_command(cmd)
			result = stdout.read(),stderr.read()
			print result
			
		Pool = multiprocessing.Pool(processes=settings.MaxTaskProcesses)
    return HttpResponse(html)


class HostListView(ListView):
    context_object_name = "hosts_list"
    template_name = "index.html"

    def get_queryset(self):
        hosts_list = Hosts.objects.all()
        return hosts_list

    def get_context_data(self, **kwargs):
        partition_list = []
        platform_type = platform.platform()
        if platform_type.startswith("Windows"):
            partition_info = psutil.disk_partitions()
        elif platform_type.startswith("Linux"):
            partition_info = disk_linux_partitions()
        for items in partition_info:
            if platform_type.startswith("Windows"):
                partition_list.append(items.device[:1])
            elif platform_type.startswith("Linux"):
                disk_partition = items.split('/')[-1]
                partition_list.append(disk_partition)
        """try:

        except KeyError:
            disk_name = partition_list[0]
        device_name = disk_name+':\\\\'
        device_usage = psutil.disk_usage(device_name)
        print "partition",partition_list
        kwargs['disk_name']=disk_name
        kwargs['disk_used']=device_usage.percent
        kwargs['disk_free']=(100-device_usage.percent)"""
        kwargs['default_disk'] = partition_list[0]
        kwargs['partition_list'] = partition_list
        return super(ListView, self).get_context_data(**kwargs)