#!/usr/bin/python2
# -*- coding: UTF-8 -*-.

import re
import os
import sys
import time
from os import system
from time import sleep

def htrprint(s):
	for t in s + '\n':
		sys.stdout.write(t)
		sys.stdout.flush()
		sleep(0.01)

logo="""
\033[1;93m    _  _ ____ _  _ ____ ____  \033[1;92m ___  ___  
\033[1;93m    |__| |__|  \/  |  | |__/  \033[1;92m |__] |  \ 
\033[1;93m    |  | |  | _/\_ |__| |  \  \033[1;92m |__] |__/ 

\033[1;96m    Bangladeshi Facebook Account Cloner
 \033[1;97m╔═════════════════════════════════════════╗
 \033[1;97m║  \033[1;92mAuthor     \033[1;96m:\033[1;93m   HTR-TECH \033[1;97m|\033[1;93m Tahmid Rayat \033[1;97m║
 \033[1;97m║  \033[1;92mGithub     \033[1;96m:\033[1;93m   github.com/HTR-TECH     \033[1;97m║
 \033[1;97m║  \033[1;92mFacebook   \033[1;96m:\033[1;93m   tahmid.rayat.official   \033[1;97m║
 \033[1;97m╚═════════════════════════════════════════╝
"""

def menu():
    system('rm -rf .num .tmp')
    htrprint ('\n \033[1;96mExcute \033[1;92mpython2 crack.py \033[1;96mto run this tool !\033[1;97m')
    sleep(1)


if __name__=="__main__":
    menu()