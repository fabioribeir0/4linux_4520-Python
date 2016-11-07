#!/usr/bin/python

usuarios = []


while True:
    print '1-Cadastrar'
    print '2-Remover'
    print '3-Listar'
    print '4-Autenticar'
    print '5-Sair'

    opcao = input()

    if opcao == 1:
        print 'Cadastrar usuario.'
        novo = {}
        novo['login'] = raw_input('Digite o login do usuario: ')
        novo['senha'] = raw_input('Digite a senha do usuario: ')
        usuarios.append(novo)
        print 'Usuario %s cadastrado com sucesso' %novo['login']

    elif opcao == 2:
        print 'Remover usuario.'
        usuario = raw_input('Digite o login do usuario: ')        
        for u in usuarios:
            if u.get('login') == usuario:
                usuarios.remove(u)
            print 'Usuario %s removido com sucesso.' %usuario
            break
        else:
            print 'Usuario nao encontrado.'

    elif opcao == 3:
        print 'Listar usuarios.'
        for u in usuarios:
            print u

    elif opcao == 4:
        print 'Autenticar usuario.\n'
        user = raw_input('Digite seu login: ')
        senha = raw_input('Digite sua senha:')

        for u in usuarios:
            if u.get('login') == user and u.get('senha') == senha:
                    print 'Login efetuado com sucesso.'
                    break
        else:
            print 'Usuario ou senha invalida.'
        

    elif opcao == 5:
        print 'Saindo do sistema.'        
        break

    else:
        print 'Opcao invalida.'
