#!/usr/bin/env python3
# Tool Name :- HatanToolX system helper (fixed)
# Author :- hatanhack (modified)
# Date :- 24/9/25 (modified)

import os
import sys

# do not attempt to pip-install at import time (keeps import lightweight)
try:
    import requests
except Exception:
    requests = None

class sys:
  pac = None
  sys = None
  home = os.getenv("HOME", "/root")
  bin = None
  sudo = None
  conf_dir = None

  def __init__(self):
    # detect sudo presence
    for s in ("/usr/bin/sudo", "/bin/sudo", "/usr/sbin/sudo", "/sbin/sudo", "/usr/lib/sudo", "/lib/sudo"):
      if os.path.exists(s):
        self.sudo = "sudo"
        break

    # detect conf_dir: prefer Termux PREFIX/etc, then /etc, then /usr/etc
    PREFIX = os.environ.get("PREFIX", "/data/data/com.termux/files/usr")
    termux_etc = os.path.join(PREFIX, "etc")
    if os.path.exists(termux_etc):
      self.conf_dir = termux_etc
    elif os.path.exists("/etc"):
      self.conf_dir = "/etc"
    elif os.path.exists("/usr/etc"):
      self.conf_dir = "/usr/etc"
    else:
      # fallback to PREFIX/etc even if not existing (installer will create it)
      self.conf_dir = termux_etc

    # detect package manager and bin paths
    # give priority to Termux's pkg if present
    pkg_path = os.path.join(PREFIX, "bin", "pkg")
    if os.path.exists(pkg_path):
      self.sys = "linux"
      self.bin = os.path.join(PREFIX, "bin")
      self.pac = "pkg"
      return

    # common package managers and their bin locations
    candidates = [
      ("/usr/bin/apt-get", "/usr/bin", "apt-get"),
      ("/bin/apt-get", "/bin", "apt-get"),
      ("/usr/sbin/apt-get", "/usr/sbin", "apt-get"),
      ("/sbin/apt-get", "/sbin", "apt-get"),
      ("/usr/bin/yum", "/usr/bin", "yum"),
      ("/bin/yum", "/bin", "yum"),
      ("/usr/bin/apk", "/usr/bin", "apk"),
      ("/bin/apk", "/bin", "apk"),
      ("/usr/bin/brew", "/usr/bin", "brew"),
      ("/bin/brew", "/bin", "brew"),
    ]
    for exe, bindir, pac in candidates:
      if os.path.exists(exe):
        self.sys = "linux"
        self.bin = bindir
        self.pac = pac
        return

    # fallback: set sensible defaults
    self.sys = "linux"
    # Prefer common PATH entries
    for candidate_bin in ("/data/data/com.termux/files/usr/bin", "/usr/bin", "/bin", "/usr/local/bin"):
      if os.path.exists(candidate_bin):
        self.bin = candidate_bin
        break
    if not self.bin:
      self.bin = "/usr/bin"
    if not self.pac:
      self.pac = "apt-get"  # default assumption

  def connection(self, timeout=3):
    # If requests isn't installed, try a lightweight check using /dev/tcp or ping fallback
    if requests is not None:
      try:
        resp = requests.get("https://www.google.com", timeout=timeout)
        return resp.ok
      except Exception:
        return False
    # fallback: use python's socket to try to connect to 8.8.8.8:53
    try:
      import socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(timeout)
      sock.connect(("8.8.8.8", 53))
      sock.close()
      return True
    except Exception:
      return False
