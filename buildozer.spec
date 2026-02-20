[app]
title = EON-77 Aion
package.name = eon77
package.domain = io.aion
source.dir = .
source.include_exts = py
version = 1.0.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 0

[app:android.permissions]
INTERNET
BLUETOOTH
ACCESS_FINE_LOCATION

[app:android]
api = 31
minapi = 26
sdk = 31
ndk = 25b
archs = arm64-v8a
accept_sdk_license = True
