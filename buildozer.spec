[app]

# Basic app information
title = EON-77 Aion
package.name = eon77
package.domain = io.aion

# Source code
source.dir = .
source.include_exts = py

# Version
version = 1.0.0

# Requirements - CLEANED (removed heavy libraries)
# Only essential packages for Android compilation
requirements = python3==3.9,kivy==2.2.1

# Orientation
orientation = portrait
fullscreen = 0

# App icon (optional - uncomment if you have icon.png)
# icon.filename = %(source.dir)s/icon.png

# Presplash (optional - uncomment if you have presplash.png)
# presplash.filename = %(source.dir)s/presplash.png

# ═══════════════════════════════════════════════════════════════════════
# BUILDOZER SETTINGS
# ═══════════════════════════════════════════════════════════════════════

[buildozer]

# Log level (0 = no logs, 1 = info, 2 = debug)
log_level = 2

# Warn if running as root
warn_on_root = 1

# Build directory
build_dir = ./.buildozer

# Binary output directory
bin_dir = ./bin

# ═══════════════════════════════════════════════════════════════════════
# ANDROID PERMISSIONS
# ═══════════════════════════════════════════════════════════════════════

[app:android.permissions]

# Essential permissions only
INTERNET
ACCESS_NETWORK_STATE
BLUETOOTH
BLUETOOTH_ADMIN
ACCESS_FINE_LOCATION
WAKE_LOCK

# ═══════════════════════════════════════════════════════════════════════
# ANDROID CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════

[app:android]

# Android API levels - OPTIMIZED for GitHub Actions
# Using stable versions that compile faster
api = 31
minapi = 26
sdk = 31
ndk = 25b

# Architecture - arm64-v8a only for faster compilation
# Add armeabi-v7a if needed: arm64-v8a,armeabi-v7a
archs = arm64-v8a

# Accept SDK licenses automatically
accept_sdk_license = True

# Enable AndroidX
android.enable_androidx = True

# Copy libraries mode
android.copy_libs = 1

# Wakelock support
android.wakelock = True

# Logcat filters
android.logcat_filters = *:S python:D

# Gradle dependencies - MINIMAL
android.gradle_dependencies = androidx.core:core:1.9.0,androidx.appcompat:appcompat:1.5.1

# Skip unnecessary steps for faster build
android.skip_update = False
android.ouya.category = GAME
android.ouya.icon_filename = %(source.dir)s/data/ouya_icon.png

# Meta-data
android.meta_data = surface.transparent=1

# Presplash color
android.presplash_color = #000000

# Enable debug mode for development
# Set to 0 for release builds
p4a.bootstrap = sdl2

# ═══════════════════════════════════════════════════════════════════════
# OPTIMIZATION FLAGS
# ═══════════════════════════════════════════════════════════════════════

# Reduce APK size
android.add_jars = 

# Strip debug symbols (smaller APK)
# Uncomment for release:
# android.release_artifact = apk
# android.strip_libs = 1

# ═══════════════════════════════════════════════════════════════════════
# RELEASE BUILD (Optional - for signing APK)
# ═══════════════════════════════════════════════════════════════════════

# Generate keystore with:
# keytool -genkey -v -keystore eon77.keystore -alias eon77 -keyalg RSA -keysize 2048 -validity 10000

# Then uncomment and configure:
# [app:android.release]
# android.release_artifact = apk
# android.release_keystore = eon77.keystore
# android.release_keystore_passwd = YOUR_PASSWORD
# android.release_key_alias = eon77
# android.release_key_alias_passwd = YOUR_PASSWORD
