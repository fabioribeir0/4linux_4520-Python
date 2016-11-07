#!/usr/bin/python

usuarios = []
senhas = []

while True:
    print '1-Cadastrar'
    print '2-Remover'
    print '3-Listar'
    print '4-Autenticar'
    print '5-Sair'

    opcao = input()

    if opcao == 1:
        print 'Cadastrar usuario.'
        novo = raw_input('Digite o login do usuario: ')
        usuarios.append(novo)
        new_pass = input('Digite a senha do usuario: ')
        senhas.append(new_pass)
        print 'Usuario %s cadastrado com sucesso' %novo

    elif opcao == 2:
        print 'Remover usuario.'
        usuario = raw_input('Digite o login do usuario: ')
        senhas.pop(usuarios.index(usuario))        
        usuarios.remove(usuario)
        print 'Usuario %s removido com sucesso.' %usuario

    elif opcao == 3:
        print 'Listar usuarios.'
        for u in usuarios:
            print u, senhas[usuarios.index(u)]

    elif opcao == 4:
        print 'Autenticar usuario.\n'
        user = raw_input('Digite seu login: ')
        senha = input('Digite sua senha:')

        for u in usuarios:
            if u == user:
                if senha == senhas[usuarios.index(u)]:
                    print 'Login efetuado com sucesso.'
                    break
        else:
            print 'Usuario ou senha invalida.'
        

    elif opcao == 5:
        print 'Saindo do sistema.'        
        break

    else:
        print 'Opcao invalida.'
