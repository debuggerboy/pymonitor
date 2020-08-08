import socket
from ssh2.session import Session
from logzero import logger

def sshconn(host, user, password, cmd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, 22))
    session = Session()
    session.handshake(sock)
    session.userauth_password(user, password)
    
    channel = session.open_session()
    channel.execute(cmd)
    
    size, data = channel.read()
    while size > 0:
        print(data.decode())
        size, data = channel.read()
    channel.close()
    a = channel.get_exit_status()
    if a == 0:
        logger.info("Exit status: {0}".format(channel.get_exit_status()))
    else:
        logger.error("Exit status: {0} - verify the command".format(channel.get_exit_status()))