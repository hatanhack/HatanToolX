# Tool Name :- HatanToolX
# Author :- hatanhack
# Date :- 24/9/2025

import os
import sys
from time import sleep
from modules.logo import *
from modules.system import *

class tool:
  @classmethod
  def install(self):
    while True:
      system=sys()
      os.system("clear")
      logo.ins_tnc()
      inp=input("\033[1;33m Do you want to install HatanToolX [Y/n]> \033[00m")
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing()
        if system.sudo is not None:
          #require root permission
          if os.path.exists(system.conf_dir+"/HatanToolX"):
            pass
          else:
            os.system(system.sudo+" mkdir "+system.conf_dir+"/HatanToolX")
          os.system(system.sudo+" cp -r modules core HatanToolX.py "+system.conf_dir+"/HatanToolX")
          os.system(system.sudo+" cp -r core/HatanToolX "+system.bin)
          os.system(system.sudo+" cp -r core/hatantoolx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/HatanToolX")
          os.system(system.sudo+" chmod +x "+system.bin+"/hatantoolx")
          os.system("cd .. && "+system.sudo+" rm -rf HatanToolX")
          if os.path.exists(system.bin+"/HatanToolX") and os.path.exists(system.conf_dir+"/HatanToolX"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else:
          if os.path.exists(system.conf_dir+"/HatanToolX"):
            pass
          else:
            os.system("mkdir "+system.conf_dir+"/HatanToolX")
          os.system("cp -r modules core HatanToolX.py "+system.conf_dir+"/HatanToolX")
          os.system("cp -r core/HatanToolX "+system.bin)
          os.system("cp -r core/hatantoolx "+system.bin)
          os.system("chmod +x "+system.bin+"/HatanToolX")
          os.system("chmod +x "+system.bin+"/hatantoolx")
          os.system("cd .. && rm -rf HatanToolX")
          if os.path.exists(system.bin+"/HatanToolX") and os.path.exists(system.conf_dir+"/HatanToolX"):
            os.system("clear")
            logo.ins_sc()
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins()
            tmp=input("\033[1;36m ##> \033[00m")
            break
