from configparser import ConfigParser

configurations = ConfigParser()
print (configurations.read('mon.ini'))
print ("Sections : ", configurations.sections())
print ("Config Library : ", configurations.get('system','name'))
print ("Log Errors debugged ? : ", configurations.getboolean('debug','log_errors'))
print ("Server1 : ", configurations.get('server1','cfg_host'))
print ("Server2 : ", configurations.get('server2','cfg_host'))
print ("Server3 : ", configurations.get('server3','cfg_host'))