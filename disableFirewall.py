import telnetlib
import time
HOST = "192.168.96.1"
#HOST = input()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Password: ")
#to be modified
tn.write(b"5\n")

tn.read_until(b"RouterA")
tn.write(b"enable\n")

tn.read_until(b"Password: ")
#to be modified
tn.write(b"5\n")

tn.read_until(b"RouterA#")
tn.write(b"config t\n")

tn.read_until(b"RouterA#(config)")
tn.write(b"banner motd #This was automated#\n")
time.sleep(2)
tn.write(b"exit\n")
