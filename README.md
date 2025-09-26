# HatanToolX

[![Build Status](https://img.shields.io/github/forks/hatanhack/HatanToolX.svg)](https://github.com/hatanhack/HatanToolX)
[![Build Status](https://img.shields.io/github/stars/hatanhack/HatanToolX.svg)](https://github.com/hatanhack/HatanToolX)
[![License](https://img.shields.io/github/license/hatanhack/HatanToolX.svg)](https://github.com/hatanhack/HatanToolX)
[![Rawsec's CyberSecurity Inventory](https://inventory.rawsec.ml/img/badges/Rawsec-inventoried-FF5050_flat.svg)](https://inventory.rawsec.ml/tools.html#HatanToolX)

------------------------------------------------------------------------

### Introduction

*HatanToolX is a Kali Linux hacking tools installer for Termux and linux system.*
HatanToolX was developed for Termux and other android terminals. Using HatanToolX, you can install almost 370+ hacking tools in Termux (android) and other Linux based distributions. Now HatanToolX is available for Ubuntu, Debian etc.

<br>
<p align="center">
<img width="53%" src="core/hatantoolx.png"/>
<img width="38%" src="core/hatantoolx_cat.png"/>
</p>

------------------------------------------------------------------------

### Operating System Requirements

HatanToolX works on any of the following operating systems:<br>
• **Android** (Using the Termux App) <br>
• **Linux** (Debian Based Systems) <br>

------------------------------------------------------------------------
1. تحديث النظام وتثبيت git و python3



pkg update -y
pkg upgrade -y
pkg install -y git python python3

2. تحميل المستودع من GitHub



cd ~
git clone https://github.com/hatanhack/HatanToolX.git
cd HatanToolX

3. تثبيت HatanToolX عبر سكربت بايثون



python3 install.py

سيقوم هذا بإنشاء مجلدات core و modules في /data/data/com.termux/files/usr/etc/HatanToolX

سيقوم بإنشاء wrapper باسم hatan في /data/data/com.termux/files/usr/bin


4. تشغيل الأداة بعد التثبيت



عبر الاختصار:


hatan

أو مباشرة عبر بايثون:


python3 ~/HatanToolX/HatanToolX.py


  (لإنشاء رابط تشغيلي يتيح لك تشغيل الأداة من أي مكان بكتابة `hatantoolx`.)
