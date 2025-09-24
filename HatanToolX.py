# Tool Name :- HatanToolX
# Author :- hatanhack
# Date :- 24/9/2025

import os
import sys
from modules.menu import *
from modules.logo import *

if __name__=="__main__":
  try:
    main.menu()
  except KeyboardInterrupt:
    os.system("clear")
    logo.exit()
