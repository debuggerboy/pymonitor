from sshadaptor import *
from configparser import ConfigParser
import threading

configurations = ConfigParser()
configurations.read('mon.ini')

cpu_used_cmd = "awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) \"%\"; }' <(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat)"
mem_used_cmd = "free | grep Mem | awk '{print $3/$2 * 100.0}'"

i = configurations.getint('system','client_count') + 1
for i in range(1,i):
    server_id = "server" + str(i)
    print("connecting to %s" % server_id)
    ssh_hostname = configurations.get(server_id,'cfg_host')
    ssh_username = configurations.get(server_id,'cfg_user')
    ssh_password = configurations.get(server_id,'cfg_pass')
    sshconn(ssh_hostname, ssh_username, ssh_password, cpu_used_cmd)
    sshconn(ssh_hostname, ssh_username, ssh_password, mem_used_cmd)