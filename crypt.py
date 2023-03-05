import pyAesCrypt, animation, sys, os, platform; from colorama import Fore
bufferSize = 256 * 2048
baseanim = ('Working', 'wOrking', 'woRking', 'worKing', 'workIng', 'workiNg', 'workinG')

def banner():
    print(f"""{Fore.GREEN}

          .-'.--':'-.
        .''::: .:    '.   {Fore.CYAN}░█▀▀█ ░█▀▀█ ░█──░█ ░█▀▀█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀▀█{Fore.GREEN}
       /   :::::'      \  {Fore.CYAN}░█─── ░█▄▄▀ ░█▄▄▄█ ░█▄▄█ ─░█── ░█▀▀▀ ─▄▄▄▀▀{Fore.GREEN}
      ;.    ':' `       ; {Fore.CYAN}░█▄▄█ ░█─░█ ──░█── ░█─── ─░█── ░█▄▄▄ ░█▄▄▄█{Fore.GREEN}
      |       '..       | {Fore.WHITE}CSEC Crypting Program - v0.1 - AES Based{Fore.GREEN}
      ; '      ::::.    ; {Fore.WHITE}Use Ctrl + C to exit{Fore.GREEN}
       \       '::::   /
        '.      :::  .'
           '-.___'_.-'
{Fore.RESET}""")

def clear():
    if 'Lin' in platform.system():
        os.system('clear')
    elif 'Win' in platform.system():
        os.system('cls')

def encrypt(filename, password):
    filename=f'./{filename}'
    outname=f'./{filename}.ace'
    @animation.wait(baseanim, color='yellow')
    def basenc(filename, password):
        pyAesCrypt.encryptFile(filename, outname, password, bufferSize)
    try:
        basenc(filename, password)
        clear()
        banner()
        outname_s=outname.replace('./', '')
        print(f'{Fore.WHITE}[{Fore.GREEN}DONE{Fore.WHITE}] - File saved as {os.getcwd()}|{outname_s}')
    except Exception as encE:
        clear()
        banner()
        print(f'{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] - {encE}')
    typem()

def decrypt(filename, password):
    filename=f'./{filename}'
    outname=f'./{filename}'.replace('.ace', '')
    @animation.wait(baseanim, color='yellow')
    def basdec(filename, password):
        pyAesCrypt.decryptFile(filename, outname, password, bufferSize)
    try:
        basdec(filename, password)
        clear()
        banner()
        decname=outname.replace('./', '')
        print(f'{Fore.WHITE}[{Fore.GREEN}DONE{Fore.WHITE}] - File saved as {os.getcwd()}|{decname}')
    except Exception as encE:
        clear()
        banner()
        print(f'{Fore.WHITE}[{Fore.RED}ERROR{Fore.WHITE}] - {encE}')
    typem()
def typem():
    print(f'''{Fore.WHITE}\r*----------------------------*
\r| Make sure that the crypter |
\r| and the encrypted file are |
\r| located in the same folder |
\r| or the crypter is located  |
\r| in $PATH!                  |
\r*----------------------------*{Fore.RESET}''')
    fln=input(f"{Fore.WHITE}Type $FILENAME: ")
    pwd=input(f"{Fore.WHITE}Type $PASSWORD: ")
    if fln.endswith('.ace'):
        decrypt(fln, pwd)
    else:
        encrypt(fln, pwd)
banner()
typem()
