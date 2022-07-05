import hashlib
import argparse
import random,time, sys
from colorama import *
 
init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
 
def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]
 
    x = """
  (                                             
 )\ )                              )        )  
(()/(   (     )              )  ( /( (   ( /(  
 /(_)) ))\   (     `  )   ( /(  )\()))\  )\()) 
(_))  /((_)  )\  ' /(/(   )(_))(_))/((_)((_)\  
/ __|(_))  _((_)) ((_)_\ ((_)_ | |_  (_)| |(_) 
\__ \/ -_)| '  \()| '_ \)/ _` ||  _| | || / /  
|___/\___||_|_|_| | .__/ \__,_| \__| |_||_\_\  
                  |_|                      
 
     +-------- CREATED BY SEMPATİK--------+
 
                                          """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.06)
logo()

def main(text, hashType):
    encoder = text.encode('utf_8')
    myHash = ''

    if hashType.lower() == 'md5':
        myHash = hashlib.md5(encoder).hexdigest()
    elif hashType.lower() == 'sha1':
        myHash = hashlib.sha1(encoder).hexdigest()
    elif hashType.lower() == 'sha224':
        myHash = hashlib.sha224(encoder).hexdigest()
    elif hashType.lower() == 'sha256':
        myHash = hashlib.sha256(encoder).hexdigest()
    elif hashType.lower() == 'sha384':
        myHash = hashlib.sha384(encoder).hexdigest()
    elif hashType.lower() == 'sha512':
        myHash = hashlib.sha512(encoder).hexdigest()
    else:
        print('[!] Bu hash tipi desteklenmemektedir')
        exit(0)
    print("Hash çıktısı: ", myHash)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Metni hash algoritmasına çevir')
    parser.add_argument('-t', '--text', dest='text', required=True)
    parser.add_argument('-T', '--Type', dest='type', required=True)
    args = parser.parse_args()

    txt = args.text
    hType = args.type
    main(txt, hType)




