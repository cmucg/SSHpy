# py --list
# py -3.11 -m pip install paramiko
import paramiko , time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.50.128', username='cgR001', password='myPassWord')
cgSh = ssh.invoke_shell()
def c():
    ssh.close()

def l(order='w'):
    """send order"""
    cgSh.send(order+'\n')
    while not cgSh.recv_ready():
        time.sleep(0.2)
    output = cgSh.recv(1024).decode()
    print(output)

# l('w')
# l('pwd')
# l('ip a')
# l('ss -tunlp')
