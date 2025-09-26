# Tool Name :- HatanToolX
# Author :- hatanhack
# Date :- 24/9/25

import os
import sys
try:
  import requests
except:
  # Install requests module if missing
  os.system("pip install requests")
  os.system("pip3 install requests")

class sys:
  pac=None
  sys=None
  home=os.getenv("HOME")
  bin=None
  sudo=None
  conf_dir=None
  def __init__(self):

    # checking for system root access (sudo)
    if os.path.exists("/usr/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/lib/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/bin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/usr/sbin/sudo"):
      self.sudo="sudo"
    elif os.path.exists("/sbin/sudo"):
      self.sudo="sudo"

    # checking for configuration dir (THE FIX FOR TERMUX PATH PRIORITY)
    if os.path.exists("/data/data/com.termux/files/usr/etc"): # 1. Check Termux path first
      self.conf_dir="/data/data/com.termux/files/usr/etc"
    elif os.path.exists("/etc"): # 2. Check generic Linux path
      self.conf_dir="/etc"
    elif os.path.exists("/usr/etc"): # 3. Check other Linux paths
      self.conf_dir="/usr/etc"

    # checking for system bin dir and system package manager (no changes needed)
    if os.path.exists("/usr/bin/yum"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="yum"
    elif os.path.exists("/bin/yum"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="yum"
    elif os.path.exists("/usr/sbin/yum"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="yum"
    elif os.path.exists("/sbin/yum"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="yum"
    elif os.path.exists("/usr/bin/apt"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apt-get"
    elif os.path.exists("/bin/apt"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apt-get"
    elif os.path.exists("/usr/sbin/apt"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="apt-get"
    elif os.path.exists("/sbin/apt"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apt-get"
    elif os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
      self.sys="linux"
      self.bin="/data/data/com.termux/files/usr/bin"
      self.pac="pkg"
    elif os.path.exists("/usr/bin/brew"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="brew"
    elif os.path.exists("/bin/brew"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="brew"
    elif os.path.exists("/usr/sbin/brew"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="brew"
    elif os.path.exists("/sbin/brew"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="brew"
    elif os.path.exists("/usr/bin/apk"):
      self.sys="linux"
      self.bin="/usr/bin"
      self.pac="apk"
    elif os.path.exists("/bin/apk"):
      self.sys="linux"
      self.bin="/bin"
      self.pac="apk"
    elif os.path.exists("/usr/sbin/apk"):
      self.sys="linux"
      self.bin="/usr/sbin"
      self.pac="apk"
    elif os.path.exists("/sbin/apk"):
      self.sys="linux"
      self.bin="/sbin"
      self.pac="apk"

  def connection(self):
    # Check for internet connection
    try:
      if requests.get("https://www.google.com").ok:
        return True
    except:
      return False
