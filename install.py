#!/usr/bin/env python3
# Tool Name :- HatanToolX installer (fixed)
# Author :- hatanhack (modified)
# Date :- 24/9/2025 (modified)

import os
import sys
import shutil
from time import sleep

HOME = os.path.expanduser("~")
PROJECT = os.path.join(HOME, "HatanToolX")
PREFIX = os.environ.get("PREFIX", "/data/data/com.termux/files/usr")
INSTALL_CONF_DIR = os.path.join(PREFIX, "etc", "HatanToolX")
BIN_DIR = os.path.join(PREFIX, "bin")
WRAPPER_NAME = "hatan"   # change if you want different command name

def ensure_core_files(project_dir):
    core_dir = os.path.join(project_dir, "core")
    os.makedirs(core_dir, exist_ok=True)
    # ensure common json files exist
    for fname in ("data.json", "cat.json"):
        path = os.path.join(core_dir, fname)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write("{}")
    return True

def copy_project_to_conf(project_dir, conf_dir):
    os.makedirs(conf_dir, exist_ok=True)
    # copy modules, core and main script (overwrite if exist)
    src_modules = os.path.join(project_dir, "modules")
    src_core = os.path.join(project_dir, "core")
    src_main = os.path.join(project_dir, "HatanToolX.py")

    # copy directories
    if os.path.exists(src_modules):
        dst_modules = os.path.join(conf_dir, "modules")
        if os.path.exists(dst_modules):
            shutil.rmtree(dst_modules)
        shutil.copytree(src_modules, dst_modules)
    if os.path.exists(src_core):
        dst_core = os.path.join(conf_dir, "core")
        if os.path.exists(dst_core):
            shutil.rmtree(dst_core)
        shutil.copytree(src_core, dst_core)
    # copy main script
    if os.path.exists(src_main):
        shutil.copy2(src_main, os.path.join(conf_dir, "HatanToolX.py"))
    return True

def create_wrapper(conf_dir, bin_dir, wrapper_name):
    os.makedirs(bin_dir, exist_ok=True)
    wrapper_path = os.path.join(bin_dir, wrapper_name)
    # wrapper runs the installed copy in conf_dir if present, otherwise runs project copy
    content = f"""#!/data/data/com.termux/files/usr/bin/env bash
# Wrapper for HatanToolX
if [ -f "{os.path.join(conf_dir, 'HatanToolX.py')}" ]; then
  python3 "{os.path.join(conf_dir, 'HatanToolX.py')}" "$@"
elif [ -f "{os.path.join(HOME, 'HatanToolX', 'HatanToolX.py')}" ]; then
  python3 "{os.path.join(HOME, 'HatanToolX', 'HatanToolX.py')}" "$@"
else
  echo "HatanToolX not found. Please ensure ~/HatanToolX exists or reinstall."
  exit 1
fi
"""
    with open(wrapper_path, "w", encoding="utf-8") as f:
        f.write(content)
    os.chmod(wrapper_path, 0o755)
    return wrapper_path

def main():
    print("=== HatanToolX Installer (fixed) ===")
    print("Project dir:", PROJECT)
    if not os.path.exists(PROJECT):
        print("Error: Project directory not found at", PROJECT)
        print("If you cloned the repo to another path, move it to ~/HatanToolX or edit this script.")
        sys.exit(1)

    ans = input("Install HatanToolX to system (no sudo required)? [Y/n]: ").strip().lower()
    if ans not in ("", "y", "yes"):
        print("Installation cancelled.")
        sys.exit(0)

    print("[*] Ensuring core JSON files...")
    ensure_core_files(PROJECT)

    print("[*] Copying project into", INSTALL_CONF_DIR)
    try:
        copy_project_to_conf(PROJECT, INSTALL_CONF_DIR)
    except Exception as e:
        print("[!] Failed to copy project:", e)
        print("[*] Attempting to continue (wrapper will prefer project folder).")

    print("[*] Creating wrapper in", BIN_DIR)
    try:
        wrapper = create_wrapper(INSTALL_CONF_DIR, BIN_DIR, WRAPPER_NAME)
        print("[+] Wrapper created at:", wrapper)
    except Exception as e:
        print("[!] Failed to create wrapper:", e)
        sys.exit(1)

    print("[+] Installation finished.")
    print("Run with: hatan  (or) python3 ~/HatanToolX/HatanToolX.py")
    sleep(1)

if __name__ == "__main__":
    main()
