import os
from time import sleep

def firula(msg):
    print("by JeanOmeg")
    print("=" * 70, "\n")
    print(msg, "\n")
    print("=" * 70, "\n")
    
    
menuprincipal = '0'
while menuprincipal == '0':
    os.system('clear')
    firula("OPÇÕES DO MENU")
    menu = input('[1]MENU-1  [2]MENU-2  [3]SAIR: ')
    
    if menu == '1':
        sleep(1)
        os.system('clear')
        firula('[1]MENU-1 SELECIONADO')
        sleep(2)
        print('EXECUTA ALGUMA COISA')
        sleep(2)
        os.system('clear')
        firula('ACESSAR MENU PRINCIPAL OU SAIR DO PROGRAMA?')
        submenu = input('[1]MENU-PRINCIPAL  [2]SAIR: ')
        while submenu.lower() != '1' and submenu.lower() != '2':
            sleep(2)
            os.system('clear')
            firula('OPÇÃO INVÁLIDA')
            submenu = input('[1]MENU-PRINCIPAL  [2]SAIR: ')
        else:
            if submenu.lower() == '1':
                sleep(2)
                os.system('clear')
                firula('ACESSANDO MENU PRINCIPAL')
                sleep(2)
                menuprincipal = '0'
            else:
                sleep(2)
                os.system('clear')
                firula('FECHANDO PROGRAMA')
                menuprincipal = '1'
            
    elif menu == '2':
        sleep(1)
        os.system('clear')
        firula('Menu [2] foi selecionado')
        print('É executado a função do menu [2], dai passa para o submenu.')
        print('O submenu normalmente é usado para continuar ou sair do programa.')
        sleep(5)
        os.system('clear')
        firula('Deseja continuar ou sair do programa?')
        submenu = input('Escolha [S] para continuar ou [N] para sair: ')
        while submenu.lower() != 's' and submenu.lower() != 'n':
            sleep(2)
            os.system('clear')
            firula('Opção inválida')
            submenu = input('Escolha [S] SIM ou [N] NÃO: ')
        else:
            if submenu.lower() == 's':
                sleep(2)
                os.system('clear')
                firula('O programa vai retornar ao menu principal')
                sleep(2)
                menuprincipal = '0'
            else:
                sleep(2)
                os.system('clear')
                firula('O programa vai ser fechado')
                menuprincipal = '1'
            
    elif menu == '3':
        sleep(1)
        os.system('clear')
        firula('FECHANDO PROGRAMA')
        break
        
    else:
        sleep(2)
        os.system('clear')
        firula('OPÇÃO INVÁLIDA')
        sleep(2)

sleep(2)
os.system('clear')
firula('PROGRAMA FINALIZADO')
