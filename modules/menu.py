#!/usr/bin/env python3
import os
import json
from time import sleep
from .logo import *
from .system import *

class main:
  def install_tools(self):
    while True:
      tool = tools()
      num = 1
      total = len(tool.names)
      os.system("clear")
      logo.install_tools()
      print("\007")
      for tool_name in tool.names:
        print (f" \033[01;32m[ \033[01;37m{num} \033[01;32m] \033[01;33minstall \033[01;32m{tool_name}\033[00m")
        num += 1
      print("")
      logo.back()
      cmd = input("\033[1;36m ##> \033[00m")
      if cmd == "00" or cmd == "back":
        self.menu()
        break
      else:
        try:
          if int(cmd) >= 1 and int(cmd) <= int(total):
            os.system("clear")
            logo.installing()
            print("\033[01;32minstalling ....\033[00m")
            tool.install(tool.names[int(cmd)-1])
          else:
            print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
            sleep(1)
        except ValueError:
          print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
          sleep(1)

  def category(self):
    while True:
      tool = tools()
      total = len(tool.category)
      num = 1
      os.system("clear")
      logo.tool_header()
      print("")
      for cat in tool.category:
        print (f"  \033[01;32m[ \033[01;37m{num} \033[01;32m] \033[01;33m{tool.category_data[cat]}\033[00m")
        num += 1
      print("")
      logo.back()
      cmd = input("\033[1;36m ##> \033[00m")
      if cmd == "00" or cmd == "back":
        self.menu()
        break
      else:
        try:
          if int(cmd) in range(1,int(total)+1):
            while True:
              cnt = 1
              os.system("clear")
              logo.tool_header()
              print("")
              tmp_cat_tool = []
              for i in tool.names:
                if tool.category[int(cmd)-1] in tool.data[i]["category"]:
                  tmp_cat_tool.append(tool.data[i]['name'])
                  print(f" \033[01;32m[ \033[00m{cnt} \033[01;32m] \033[01;33minstall \033[01;32m{tool.data[i]['name']}\033[00m")
                  cnt += 1
              print("")
              logo.back()
              tcmd = input("\033[1;36m ##> \033[00m")
              if tcmd == "00" or tcmd == "back":
                break
              else:
                try:
                  cat_total = len(tmp_cat_tool)
                  if int(tcmd) in range(1,int(cat_total)+1):
                    os.system("clear")
                    logo.installing()
                    print("\033[01;32minstalling ....\033[00m")
                    tool.install(tmp_cat_tool[int(tcmd)-1])
                  else:
                    print(f"\007\033[01;31mSorry \033[01;37m: '{tcmd}' \033[01;31minvalid input !!\033[00m")
                    sleep(1)
                except ValueError:
                  print(f"\007\033[01;31mSorry \033[01;37m: '{tcmd}' \033[01;31minvalid input !!\033[00m")
                  sleep(1)
          else:
            print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
            sleep(1)
        except ValueError:
          print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
          sleep(1)

  def update(self):
    while True:
      os.system("clear")
      logo.update()
      cmd = input("\033[1;36m ##> \033[00m")
      if cmd == "1":
        system = sys()
        if system.connection():
          os.system("clear")
          logo.updating()
          if system.sudo != None:
            if os.path.exists(system.home+"/HatanToolX"):
              pass
            else:
              os.system(system.sudo+" git clone https://github.com/hatanhack/HatanToolX.git "+system.home+"/HatanToolX")
            if os.path.exists(system.home+"/HatanToolX/install.aex"):
              os.system("cd "+system.home+"/HatanToolX && "+system.sudo+" sh install.aex")
              if os.path.exists(system.bin+"/HatanToolX") and os.path.exists(system.conf_dir+"/HatanToolX"):
                os.system("clear")
                logo.updated()
                cmd=input("\033[1;36m ##> \033[00m")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("\033[1;36m ##> \033[00m")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("\033[1;36m ##> \033[00m")
          else:
            if os.path.exists(system.home+"/HatanToolX"):
              pass
            else:
              os.system("git clone https://github.com/hatanhack/HatanToolX.git "+system.home+"/HatanToolX")
            if os.path.exists(system.home+"/HatanToolX/install.aex"):
              os.system("cd "+system.home+"/HatanToolX && sh install.aex")
              if os.path.exists(system.bin+"/HatanToolX") and os.path.exists(system.conf_dir+"/HatanToolX"):
                os.system("clear")
                logo.updated()
                cmd=input("\033[1;36m ##> \033[00m")
              else:
                os.system("clear")
                logo.update_error()
                cmd=input("\033[1;36m ##> \033[00m")
            else:
              os.system("clear")
              logo.update_error()
              cmd=input("\033[1;36m ##> \033[00m")
        else:
          os.system("clear")
          logo.nonet()
          tmp=input("\033[1;36m ##> \033[00m")
      elif cmd == "0" or cmd == "back":
        self.menu()
        break
      else:
        print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

  def about(self):
    while True:
      tool = tools()
      total = len(tool.names)
      os.system("clear")
      logo.about(total)
      cmd = input("\033[1;36m ##> \033[00m")
      self.menu()
      break

  @classmethod
  def menu(self):
    while True:
      tool = tools()
      total = len(tool.names)
      os.system("clear")
      logo.menu(total)
      cmd = input("\033[1;36m ##> \033[00m")
      if cmd == "1":
        self.install_tools(self)
        break
      elif cmd == "2":
        self.category(self)
        break
      elif cmd == "3":
        self.update(self)
        break
      elif cmd == "4":
        self.about(self)
        break
      elif cmd=="x" or cmd=="X" or cmd=="exit" or cmd=="uninstall" or cmd=="rm -t":
        system = sys()
        if system.sudo:
          os.system(system.sudo+" rm -rf "+system.bin+"/HatanToolX")
          os.system(system.sudo+" rm -rf "+system.bin+"/hatantoolx")
          os.system(system.sudo+" rm -rf "+system.conf_dir+"/HatanToolX")
        else:
          os.system("rm -rf "+system.bin+"/HatanToolX")
          os.system("rm -rf "+system.bin+"/hatantoolx")
          os.system("rm -rf "+system.conf_dir+"/HatanToolX")
        os.system("clear")
        logo.exit()
        break
      else:
        print(f"\007\033[01;31mSorry \033[01;37m: '{cmd}' \033[01;31minvalid input !!\033[00m")
        sleep(1)

class tools:
  data = None
  names = None
  category = None
  category_data = None

  def __init__(self):
    system = sys()

    # Try system conf_dir first, fallback to local project core folder
    tried = []
    data_loaded = False
    # candidate 1: system conf_dir (installed location)
    if system.conf_dir:
      path1 = os.path.join(system.conf_dir, "HatanToolX", "core", "data.json")
      try:
        with open(path1, "r", encoding="utf-8") as data_file:
          self.data = json.load(data_file)
          data_loaded = True
      except Exception:
        tried.append(path1)

    # candidate 2: project-relative core
    if not data_loaded:
      path2 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core", "data.json")
      try:
        with open(path2, "r", encoding="utf-8") as data_file:
          self.data = json.load(data_file)
          data_loaded = True
      except Exception:
        tried.append(path2)

    if not data_loaded:
      raise FileNotFoundError("data.json not found. tried: " + ", ".join(tried))

    # cat.json / cat data
    tried = []
    cat_loaded = False
    if system.conf_dir:
      cat1 = os.path.join(system.conf_dir, "HatanToolX", "core", "cat.json")
      try:
        with open(cat1, "r", encoding="utf-8") as cat_file:
          self.category_data = json.load(cat_file)
          cat_loaded = True
      except Exception:
        tried.append(cat1)

    if not cat_loaded:
      cat2 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core", "cat.json")
      try:
        with open(cat2, "r", encoding="utf-8") as cat_file:
          self.category_data = json.load(cat_file)
          cat_loaded = True
      except Exception:
        tried.append(cat2)

    if not cat_loaded:
      raise FileNotFoundError("cat.json not found. tried: " + ", ".join(tried))

    self.names = list(self.data.keys())
    self.category = list(self.category_data.keys())

  def install(self, name):
    package_name = self.data[name]["package_name"]
    package_manager = self.data[name]["package_manager"]
    url = self.data[name].get("url", "")
    req = list(self.data[name].get("dependency", []))
    system = sys()

    if system.connection():
      if len(req) != 0 and req[0] != None:
        for dep in req:
          if os.path.exists(os.path.join(system.bin, dep)):
            pass
          else:
            if system.sudo != None:
              os.system(system.sudo + " " + system.pac + " install " + dep + " -y")
            else:
              os.system(system.pac + " install " + dep + " -y")

      if package_manager == "package_manager":
        if os.path.exists(os.path.join(system.bin, package_name)):
          os.system("clear")
          logo.already_installed(name)
          tmp = input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo + " " + system.pac + " install " + package_name + " -y")
          else:
            os.system(system.pac + " install " + package_name + " -y")
          # check tool is installed or not
          if os.path.exists(os.path.join(system.bin, package_name)):
            os.system("clear")
            logo.installed(name)
            tmp = input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp = input("\033[1;36m ##> \033[00m")

      elif package_manager == "git":
        if os.path.exists(os.path.join(system.home, package_name)):
          os.system("clear")
          logo.already_installed(name)
          tmp = input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo + " git clone " + url + " " + os.path.join(system.home, package_name))
          else:
            os.system("git clone " + url + " " + os.path.join(system.home, package_name))
          # check tool is installed or not
          if os.path.exists(os.path.join(system.home, package_name)):
            os.system("clear")
            logo.installed(name)
            tmp = input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp = input("\033[1;36m ##> \033[00m")

      elif package_manager == "wget":
        if os.path.exists(os.path.join(system.home, package_name)):
          os.system("clear")
          logo.already_installed(name)
          tmp = input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo + " wget " + url + " -O " + os.path.join(system.home, package_name))
          else:
            os.system("wget " + url + " -O " + os.path.join(system.home, package_name))
          # check tool is installed or not
          if os.path.exists(os.path.join(system.home, package_name)):
            os.system("clear")
            logo.installed(name)
            tmp = input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp = input("\033[1;36m ##> \033[00m")

      elif package_manager == "curl":
        if os.path.exists(os.path.join(system.home, package_name)):
          os.system("clear")
          logo.already_installed(name)
          tmp = input("\033[1;36m ##> \033[00m")
        else:
          if system.sudo != None:
            os.system(system.sudo + " curl " + url + " -o " + os.path.join(system.home, package_name))
          else:
            os.system("curl " + url + " -o " + os.path.join(system.home, package_name))
          # check tool is installed or not
          if os.path.exists(os.path.join(system.home, package_name)):
            os.system("clear")
            logo.installed(name)
            tmp = input("\033[1;36m ##> \033[00m")
          else:
            os.system("clear")
            logo.not_installed(name)
            tmp = input("\033[1;36m ##> \033[00m")
    else:
      os.system("clear")
      logo.nonet()
      tmp = input("\033[1;36m ##> \033[00m")
