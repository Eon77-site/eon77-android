[app]
# (str) Title of your application
title = AION Network

# (str) Package name
package.name = aion_network

# (str) Package domain (needed for android packaging)
package.domain = org.eon77

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,cryptography,requests,urllib3,certifi

# (list) Permissions
android.permissions = INTERNET,BLUETOOTH,BLUETOOTH_ADMIN,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,FOREGROUND_SERVICE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) NDK version - ESSENCIAL para não travar o build
android.ndk = 25b

# (str) Android architecture
android.archs = arm64-v8a

# (bool) Aceitar licenças automaticamente
android.accept_sdk_license = True

# (bool) Wakelock para mineração contínua
android.wakelock = True

[buildozer]
log_level = 2
warn_on_root = 1
