[app]
title = AION Network
package.name = aion_network
package.domain = org.eon77
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

requirements = python3,kivy==2.2.1,cryptography,requests,urllib3,certifi,setuptools,pycparser,cffi

android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,FOREGROUND_SERVICE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.wakelock = True

orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
