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
  def tool_footer(self):
    print('''\033[1;36m_______________________________________________
===============================================\033[00m''')


  @classmethod
  def not_ins(self):
    self.tool_header()
    print ('''
\033[1;31m  [ + ]  \033[1;31mWe can't install HatanToolX.\033[1;m
\033[1;31m  [ + ]  \033[1;31mThere are some error.\033[1;m
\033[1;31m  [ + ]  \033[1;31mPlease try again after some time.\033[1;m''')
    self.tool_footer()

  @classmethod
  def ins_tnc(self):
    self.tool_header()
    print ('''
\033[1;33m  [ + ] \033[1;32mUse It At Your Own Risk.
\033[1;33m  [ + ] \033[1;32mNo Warranty.
\033[1;33m  [ + ] \033[1;32mUse it legal purpose only.
\033[1;33m  [ + ] \033[1;32mWe are not responsible for your actions.
\033[1;33m  [ + ] \033[1;32mDo not do things that are forbidden.

\033[1;31m If you are installing this tool.
 that means you are agree with all terms.''')
    self.tool_footer()

  @classmethod
  def ins_sc(self):
    self.tool_header()
    print ('''
\033[1;33m    [ + ] \033[1;32mHatanToolX installed successfully.
\033[1;33m    [ + ] \033[1;32mTo run HatanToolX.
\033[1;33m    [ + ] \033[1;32mType hatantoolx in your terminal.''')
    self.tool_footer()

  @classmethod
  def update(self):
    self.tool_header()
    print ('''
\033[1;33m  [ 1 ] \033[1;32mUpdate your HatanToolX.
\033[1;33m  [ 0 ] \033[1;32mFor Back.\033[00m''')
    self.tool_footer()

  @classmethod
def exit(self):
    print('''\033[1;31m
\033[1;m''')
