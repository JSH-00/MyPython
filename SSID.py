#coding=utf8
import os
# device = os.popen("adb devices").read()
# print(device)

password = os.popen("adb shell grep wpa_passphrase= data/misc/wifi/hostapd.conf").read()
print(password)

ssid = os.popen("adb shell grep -E \"^ssid=\" data/misc/wifi/hostapd.conf").read()
print(ssid)
