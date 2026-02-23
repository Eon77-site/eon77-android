[app]
# (str) Title of your application
title = AION Network

# (str) Package name
package.name = aion_network

# (str) Package domain (needed for android packaging)
package.domain = org.eon77

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# Adicionada cryptography para segurança quântica e requests para o Bot Trader
requirements = python3,kivy,cryptography,requests,urllib3,certifi

# (list) Permissions
# Essencial para rede Mesh e comunicação em cenários extremos
android.permissions = INTERNET, BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, FOREGROUND_SERVICE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android architecture to build for
# Focando apenas em 64 bits para acelerar o build no GitHub como o Claude sugeriu
android.archs = arm64-v8a

# (bool) indicates whether the screen should stay on
# Útil para mineração contínua no celular
android.wakelock = True

# (list) The Android archs to build for.
android.archs = arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = hide, 1 = show)
warn_on_root = 1
