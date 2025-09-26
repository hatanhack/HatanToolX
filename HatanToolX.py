#!/usr/bin/env python3
# Tool Name :- HatanToolX
# Author :- hatanhack (modified)
# Date :- 24/9/2025 (modified)

import os
import sys
from modules.menu import *
from modules.logo import *

if __name__ == "__main__":
    try:
        main.menu()
    except KeyboardInterrupt:
        os.system("clear")
        try:
            logo.exit()
        except Exception:
            # fallback safe exit
            print("\nExiting...")
            sys.exit(0)
