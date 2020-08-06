from sshadaptor import *
import threading

ssh_hostname = '127.0.0.1'
ssh_username = 'debuggerboy'
ssh_password = 'xxxxxxxxxxx'
cpu_used_cmd = "awk '{u=$2+$4; t=$2+$4+$5; if (NR==1){u1=u; t1=t;} else print ($2+$4-u1) * 100 / (t-t1) \"%\"; }' <(grep 'cpu ' /proc/stat) <(sleep 1;grep 'cpu ' /proc/stat)"
mem_used_cmd = "free | grep Mem | awk '{print $3/$2 * 100.0}'"

sshconn(ssh_hostname, ssh_username, ssh_password, cpu_used_cmd)
sshconn(ssh_hostname, ssh_username, ssh_password, mem_used_cmd)