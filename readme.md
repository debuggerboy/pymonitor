# Mon

Monitor CPU and Memory for GNU/Linux instances.

###

```
x = threading.Thread(target=sshconn(ssh_hostname, ssh_username, ssh_password, mem_used_cmd))
x.start()
y = threading.Thread(target=sshconn(ssh_hostname, ssh_username, ssh_password, mem_used_cmd))
y.start()
```

#### Sources

CPU Usage:

- https://stackoverflow.com/questions/9229333/how-to-get-overall-cpu-usage-e-g-57-on-linux
- https://www.cyberciti.biz/tips/how-do-i-find-out-linux-cpu-utilization.html

Memory Usage:

- https://stackoverflow.com/questions/10585978/how-to-get-the-percentage-of-memory-free-with-a-linux-command

Threading:

- https://realpython.com/intro-to-python-threading/

Socket:

- https://stackoverflow.com/questions/7140438/error-transport-endpoint-is-already-connected