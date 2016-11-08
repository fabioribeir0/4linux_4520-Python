#!/usr/bin/python

import paramiko as pk


def send_cmd(ssh,cmd):
    #envia comando para servidor
    stdin, stdout, stderr = ssh.exec_command(cmd)
    #verifica se variavel $? do linux e diferente de 0
    if stderr.channel.recv_exit_status() != 0:
        #exibe msg de erro padrao
        return stderr.read()
    else:
        #exibe saida padrao
        return stdout.read()


def main_fn(cmd):
    #cria objeto para conectar com o ssh
    ssh = pk.SSHClient()
    #le arquivo ~/.ssh/know_hosts
    ssh.load_system_host_keys()
    #aceita chave do servidor automaticamente
    ssh.set_missing_host_key_policy(pk.AutoAddPolicy())
    #conecta no servidor
    ssh.connect(hostname='192.168.0.2',username='root',password='4linux')
    
    return send_cmd(ssh, cmd)


if __name__ == '__main__':
    main_fn()

# __name__ e uma variavel que guarda o nome do programa que chamou o arquivo
# Quando chamado direto pelo terminal, recebe __main__, quando importada
# armazena o nome do arquivo principal
