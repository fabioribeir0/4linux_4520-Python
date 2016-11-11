#!/usr/bin/python


class Carro:


    def __init__(self, cor):
        self.portas = 4
        self.cor = cor
        self.status = 'desligado'
        self.velocidade = 0
        self.status_porta = 'destravada'


    def __str__(self):
        texto = ''
        texto += 'Portas: %s\n' % self.portas
        texto += 'Cor: %s\n' % self.cor
        texto += 'Status: %s\n' % self.status
        texto += 'Velocidade: %s\n' % self.velocidade
        texto += 'Portas: %s' % self.status_porta
        return texto


    def ligar(self):
        self.status = 'ligado'
        self.travar_portas()


    def travar_portas(self):
        self.status_porta = 'travado'


    def acelerar(self):
        if self.status == 'ligado':
            self.velocidade += 10
            self.travar_portas()
        else:
            print 'Carro desligado.'


    def reduzir(self):
        if self.status == 'ligado':
            self.velocidade -= 10
        else:
            print 'Carro desligado.'


if __name__ == '__main__':
    c = Carro('Vermelho')
    print c
    c.ligar()
    print c
    c.acelerar()
    print c
