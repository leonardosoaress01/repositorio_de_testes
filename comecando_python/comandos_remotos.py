from audioop import add
from posixpath import split
import re
from sys import stderr, stdin, stdout
import paramiko

addres = '100.0.0.3'
username = 'root'
password = '162908Master'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname=addres, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('ip addr show')
stdin.close()
print(stderr.readline())

ssh.close

mac = ''
interface = ''
ip = ''

for line in stdout.readlines():

    result = line.replace('\n','')

    if 'UP' in line:
        interface = result.split(':')[1]
    if 'ether' in line:
        mac = result.split(' ')[5]
    if 'inet ' in line:
        ip = result.split(' ')[5]  


    print('Interface:'+interface, 'MAC:'+mac, 'IP:'+ip)
    #print(result)




