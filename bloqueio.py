import getpass
import os
import platform
import socket
from uuid import getnode as get_mac
from ctypes import *
from pynput.mouse import Button, Controller
import asyncio

import fdb

import subprocess, win32con, win32api
from win32api import SetFileAttributes
from winreg import *

import atexit

class conexao:

    def select(self, sql):
        con = fdb.connect(database="C:/_BD/LM.FDB", user="SYSDBA", password="masterkey")
        cur = con.cursor()

        cur.execute(sql)

        dados = cur.fetchall()

        cur.close()
        con.close()

        return dados



def atribuirEspaco(string):
    tamanho = len(string)

    restante = 21 - tamanho
    espaco = ""

    for i in range(restante):
        espaco = espaco + " "

    return espaco

def uMad(event):
    return False

manter = True
cnx = conexao()
retorno = cnx.select("select * from usuarios")

#print("USUARIO              SENHA")
#print("-------------------------------------")

#for x in range(len(retorno)):

    #print(retorno[x][0] + atribuirEspaco(retorno[x][0]) + retorno[x][1])

async def divisao():
    #await asyncio.gather(texto(), loop())
    task1 = asyncio.create_task(texto())
    task2 = asyncio.create_task(loop())

    await task1
    await task2


def texto():
    valor = input("Digite T para sair")
    if(valor == "T"):
        manter = False

def loop():
    while (manter):

        mouse = Controller()
        print('The current pointer position is {0}'.format(
            mouse.position))

        win32api.SetCursorPos((800, 300))


print((socket.gethostbyname(socket.gethostname())))
print((getpass.getuser()))
print((platform.node()))

hex = hex(get_mac())
hex = hex[2:14]

print(hex)



asyncio.run(divisao())



    #tecla = input('Digite T para desbloquear: ')
    #if(tecla == 'T'):
    #    print("Digitou")
    #    manter = False
    #else:
    #    print("Nao digitou")


os.system("pause")

# Note: 1 locks the machine, 0 opens the machine.
UserPolicySetting = 1
# Connect to the correct Windows Registry key and path, then open the key
reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

regpath = r"SYSTEM\\CurrentControlSet\\Control\\Keyboard Layout"
key = OpenKey(reg, regpath, 0, KEY_WRITE)
# Edit registry key by adding new values (Lock-down the PC)
#SetValueEx(key, "Scancode Map", None,  REG_BINARY, '00000000000000000300000000004BE000005CE000000000')

CloseKey(key)







