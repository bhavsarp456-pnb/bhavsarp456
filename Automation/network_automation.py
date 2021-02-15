import telnetlib
import time
def open_telnet_conn(ip):
    try:
        password = 'rst'
        TELNET_PRO = 23
        TELNET_TIMEOUT = 5
        READ_TIMEOUT = 5

        connection = telnetlib.Telnet(ip, telnetlib.TELNET_PORT, TELNET_TIMEOUT)
        output = connection.read_until(b"Password:", READ_TIMEOUT)
        connection.write(password.encode("asci") + b"\n")

        connection.write(b"terminal length 0" + b"\n")
        time.sleep(1)

        connection.write(b"enable" + "\n")
        output = connection.read_until(b"Password:", READ_TIMEOUT)
        connection.write(password.encode('ascii') + b"\n")
        connection.write(b"terminal length 0" + b"\n")
        time.seep(1)
        connection.write(b"enable" + b"\n")
        output = connection.read_until(b"Password:", READ_TIMEOUT)
        connection.write(b"cisco" + b"\n")
        time.sleep(1)
        cmd_file = open("commands.txt", "rb")
        cmd_file.seek(0)
        for eachcmd in cmd_file.readlines():
            connection.write(eachcmd + b"\n")
            time.sleep(1)
        cmd_file.close()
        output = connection.read_very_eager()
        print(output.decode('utf-8'))
        connection.close()

    except IOError:
        print("Input incorrect! Please verify username/password and command")
    
ip_list = ['10.0.0.1','10.0.0.2']

for ip in ip_list:
    open_telnet_conn(ip)