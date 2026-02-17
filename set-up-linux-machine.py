#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

# =====================================================
# Utility
# =====================================================


def run(cmd, check=True):
    print(f"\n👉 {cmd}")
    subprocess.run(cmd, shell=True, check=check)


def command_exists(command):
    return (
        subprocess.call(
            f"type {command}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        == 0
    )


# =====================================================
# System Update
# =====================================================


def update_system():
    run("sudo apt update && sudo apt upgrade -y")


# =====================================================
# Flatpak + Flathub
# =====================================================


def install_flatpak():
    if command_exists("flatpak"):
        print("✅ Flatpak already installed")
        return

    run("sudo apt install -y flatpak")
    run(
        "sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo"
    )


# =====================================================
# NVM + Node LTS
# =====================================================


def install_nvm():
    nvm_dir = Path.home() / ".nvm"

    if nvm_dir.exists():
        print("✅ NVM already installed")
        return

    run(
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash"
    )


def install_node_lts():
    print("🔧 Installing Node LTS via NVM")

    run("""
export NVM_DIR="$HOME/.nvm" && \
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
nvm install --lts && \
nvm alias default 'lts/*' && \
nvm use --lts
""")


def enable_corepack():
    run("""
export NVM_DIR="$HOME/.nvm" && \
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
corepack enable
""")


# =====================================================
# Biome
# =====================================================


def install_biome():
    if command_exists("biome"):
        print("✅ Biome already installed")
        return

    run("""
export NVM_DIR="$HOME/.nvm" && \
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \
npm install -g @biomejs/biome
""")


# =====================================================
# uv (Modern Python Toolchain)
# =====================================================


def install_uv():
    if command_exists("uv"):
        print("✅ uv already installed")
