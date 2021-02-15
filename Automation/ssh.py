import paramiko
import time 
print("Wait, creating ssh client")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Wait, connectimg to remote server")
ssh_client.connect(hostname="10.0.0.200", username="rohan", password="rst@123")
time.sleep(3)
cmd1 = "sudo apt-get insatll httpd"
cmd2 = "sudo touch /var/www/html/index.html"
cmd3 = "sudo echo '<html><body bgcolor=Blue><h1><marquee>Welcome to RST Forum<</morquee><body><html>' >> /var/www/html/index.html"
cmd4 = "sudo systemctl restart apache2"
print("Wait, exectuing commands")
stdio, stdout, stderr = ssh_client.exec_command(cmd1)
stdio, stdout, stderr = ssh_client.exec_command(cmd2)
stdio, stdout, stderr = ssh_client.exec_command(cmd3)
stdio, stdout, stderr = ssh_client.exec_command(cmd4)
print("Output:")
time.sleep(10)
stdout = stdout.read()
print(stdout)