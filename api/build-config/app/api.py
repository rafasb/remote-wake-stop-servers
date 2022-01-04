from fastapi import FastAPI
import paramiko

app = FastAPI()

@app.get("/wolweb/sleep/pctv")
def hello():
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect('192.168.1.123', username='usuario', password='password')
  ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('sudo shutdown -h')
  return {'msg': "Orden de apagado lanzada!"}
  