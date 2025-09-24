import os
import sys

# Tool Name :- HatanToolX
# Author :- hatanhack
# Date :- 24/9/25

class logo:
  @classmethod
  def tool_header(self):
    print('''\007

\033[1;33m
         _____           _    __  __
        |_   _|__   ___ | |   \ \/ /
          | |/ _ \ / _ \| |____\  /
          | | (_) | (_) | |____/  \    
          |_|\___/ \___/|_|   /_/\_\ \033[1;91mv2.1


\033[1;36m =============================================\033[1;m
\033[1;33m| HatanToolX - A Hacking Tools Installer |
\033[1;36m =============================================\033[00m''')

  @classmethod
  def installing(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;32m
      Installing ....\033[00m''')

  @classmethod
  def installed(self,name):
    os.system("clear")
    self.tool_header()
    print(f'''\033[1;32m
      \033[1;33m{name}\033[1;32m Installed Successfully !!\007
      Press Enter To Back...\007''')

  @classmethod
  def not_installed(self,name):
    os.system("clear")
    self.tool_header()
    print(f'''\033[1;31m
      \033[1;33m{name}\033[1;31m Is Not Installed !!
      Press Enter To Back...''')

  @classmethod
  def already_installed(self,name):
    os.system("clear")
    self.tool_header()
    print(f'''\033[1;33m
      \033[1;32m{name}\033[1;33m Is Already Installed !!
      Press Enter To Back...''')

  @classmethod
  def update_error(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;31m
      Sorry The Update Failed !!
      Press Enter To Back...''')

  @classmethod
  def updated(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;32m
      Successfully Updated !!
      Press Enter To Back...''')

  @classmethod
  def nonet(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;31m
      Sorry Check Your Internet Connection !!
      Press Enter To Back...''')

  @classmethod
  def install_tools(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;32m
      [ + ] \033[1;33mAll Tools\033[1;32m''')

  @classmethod
  def back(self):
    print('''\033[1;32m
      [ \033[1;37m00 \033[1;32m] \033[1;33mBack\033[00m''')

  @classmethod
  def update(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;32m
      [ \033[1;37m1 \033[1;32m] \033[1;33mUpdate HatanToolX
      [ \033[1;37m0 \033[1;32m] \033[1;33mBack\033[00m''')

  @classmethod
  def updating(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;32m
      Updating ....\033[00m''')

  @classmethod
  def about(self,total):
    os.system("clear")
    self.tool_header()
    print(f'''
\033[1;33m  Author  : \033[1;36mhatanhack
\033[1;33m  Github  : \033[1;36mhttps://github.com/hatanhack/HatanToolX
\033[1;33m  Version : \033[1;36m2.1
\033[1;33m  Tools   : \033[1;36m{total}\033[00m

\033[1;32m[ \033[1;37m00 \033[1;32m] \033[1;33mBack\033[00m''')

  @classmethod
  def menu(self,total):
    os.system("clear")
    self.tool_header()
    print(f'''
\033[1;33m  [ \033[1;37m1 \033[1;33m] \033[1;32mShow all tools\033[0m
\033[1;33m  [ \033[1;37m2 \033[1;33m] \033[1;32mTools Category\033[0m
\033[1;33m  [ \033[1;37m3 \033[1;33m] \033[1;32mUpdate HatanToolX\033[0m
\033[1;33m  [ \033[1;37m4 \033[1;33m] \033[1;32mAbout Us\033[0m
\033[1;33m  [ \033[1;37mrm -t \033[1;33m] \033[1;32mUninstall HatanToolX\033[0m
\033[1;33m  [ \033[1;37mx \033[1;33m] \033[1;31mFor Exit\033[0m''')

  @classmethod
  def exit(self):
    os.system("clear")
    self.tool_header()
    print('''\033[1;32m
      Thanks For Using !!\007''')
