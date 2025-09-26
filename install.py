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
      logo.ins_tnc() # Assuming this shows Terms and Conditions/Welcome
      inp=input("\033[1;33m Do you want to install HatanToolX [Y/n]> \033[00m") # Prompt translated
      if inp=="y" or inp=="Y":
        os.system("clear")
        logo.installing() # Assuming this shows 'Installing...'
        if system.sudo is not None:
          # require root permission
          if os.path.exists(system.conf_dir+"/HatanToolX"):
            pass
          else:
            os.system(system.sudo+" mkdir -p "+system.conf_dir+"/HatanToolX/core")
          os.system(system.sudo+" cp -r modules core HatanToolX.py "+system.conf_dir+"/HatanToolX")
          os.system(system.sudo+" cp -r core/HatanToolX "+system.bin)
          os.system(system.sudo+" cp -r core/hatantoolx "+system.bin)
          os.system(system.sudo+" chmod +x "+system.bin+"/HatanToolX")
          os.system(system.sudo+" chmod +x "+system.bin+"/hatantoolx")
          os.system("cd .. && "+system.sudo+" rm -rf HatanToolX")
          if os.path.exists(system.bin+"/HatanToolX") and os.path.exists(system.conf_dir+"/HatanToolX"):
            os.system("clear")
            logo.ins_sc() # Assuming this shows 'Installation Successful'
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins() # Assuming this shows 'Installation Failed'
            tmp=input("\033[1;36m ##> \033[00m")
            break
        else: # The main fix for non-root environments (Termux)
          if os.path.exists(system.conf_dir+"/HatanToolX"):
            pass
          else:
            # Create the necessary directory including 'core'
            os.system("mkdir -p "+system.conf_dir+"/HatanToolX/core")
          
          # Copy main tool components
          os.system("cp -r modules core HatanToolX.py "+system.conf_dir+"/HatanToolX")

          # Copy essential JSON config files directly (The fix for FileNotFoundError)
          os.system("cp core/data.json "+system.conf_dir+"/HatanToolX/core/")
          os.system("cp core/cat.json "+system.conf_dir+"/HatanToolX/core/") 
          
          # Copy and make executables
          os.system("cp -r core/HatanToolX "+system.bin)
          os.system("cp -r core/hatantoolx "+system.bin)
          os.system("chmod +x "+system.bin+"/HatanToolX")
          os.system("chmod +x "+system.bin+"/hatantoolx")
          os.system("cd .. && rm -rf HatanToolX")
          if os.path.exists(system.bin+"/HatanToolX") and os.path.exists(system.conf_dir+"/HatanToolX"):
            os.system("clear")
            logo.ins_sc() # Assuming this shows 'Installation Successful'
            tmp=input("\033[1;36m ##> \033[00m")
            break
          else:
            os.system("clear")
            logo.not_ins() # Assuming this shows 'Installation Failed'
            tmp=input("\033[1;36m ##> \033[00m")
            break
