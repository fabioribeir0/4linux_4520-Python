#!/usr/bin/python

import paramiko as pk


class SSH:

    def __init__(self):
        # cria objeto para conectar com o ssh
        self.ssh = pk.SSHClient()
        # le arquivo ~/.ssh/know_hosts
        self.ssh.load_system_host_keys()
        # aceita chave do servidor automaticamente
        self.ssh.set_missing_host_key_policy(pk.AutoAddPolicy())
        # conecta no servidor
        self.ssh.connect(hostname='192.168.0.2',\
                         username='root', password='4linux')


    def executar_comando(self, cmd):
        # envia comando para servidor
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        # verifica se variavel $? do linux e diferente de 0
        if stderr.channel.recv_exit_status() != 0:
            # exibe msg de erro padrao
            return stderr.read()
        else:
            # exibe saida padrao
            return stdout.read()
