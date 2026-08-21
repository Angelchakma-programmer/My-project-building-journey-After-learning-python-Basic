"""
UI Helper for Rangamati Adventure Game.
Provides ANSI colors, ASCII art banners, borders, and formatted printing.
"""

import os
import sys
import time

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    
    # Foreground colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright Foregrounds
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""{Colors.BRIGHT_CYAN}
╔═══════════════════════════════════════════════════════════════════════╗
║   ██████╗  █████╗ ███╗   ██╗ ██████╗  █████╗ ███╗   ███╗ █████╗ ████████╗██╗║
║   ██╔══██╗██╔══██╗████╗  ██║██╔════╝ ██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██║║
║   ██████╔╝███████║██╔██╗ ██║██║  ███╗███████║██╔████╔██║███████║   ██║   ██║║
║   ██╔══██╗██╔══██║██║╚██╗██║██║   ██║██╔══██║██║╚██╔╝██║██╔══██║   ██║   ██║║
║   ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ██║║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝║
║                     🏔️  E X P L O R E R   R P G  🏞️                   ║
║         Discover Subdistricts, Mountain Peaks, Lakes & Foods!         ║
╚═══════════════════════════════════════════════════════════════════════╝{Colors.RESET}"""
    print(banner)

def print_header(title: str, subtitle: str = ""):
    print(f"\n{Colors.BRIGHT_YELLOW}{'='*70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BRIGHT_WHITE}  ➤ {title}{Colors.RESET}")
    if subtitle:
        print(f"{Colors.CYAN}    {subtitle}{Colors.RESET}")
    print(f"{Colors.BRIGHT_YELLOW}{'='*70}{Colors.RESET}")

def print_box(text: str, color=Colors.CYAN):
    lines = text.split("\n")
    max_len = max(len(l) for l in lines) if lines else 0
    width = max(max_len + 4, 60)
    
    print(f"{color}┌{'─' * (width - 2)}┐{Colors.RESET}")
    for line in lines:
        print(f"{color}│ {Colors.RESET}{line.ljust(width - 4)}{color} │{Colors.RESET}")
    print(f"{color}└{'─' * (width - 2)}┘{Colors.RESET}")

def print_status_bar(player):
    energy_bar_len = 20
    filled = int((player.energy / 100) * energy_bar_len)
    bar_color = Colors.BRIGHT_GREEN if player.energy > 50 else (Colors.BRIGHT_YELLOW if player.energy > 20 else Colors.RED)
    bar = f"{bar_color}[{'█' * filled}{'░' * (energy_bar_len - filled)}]{Colors.RESET}"
    
    location_name = player.current_location.capitalize()
    
    print(f"\n{Colors.DIM}----------------------------------------------------------------------{Colors.RESET}")
    print(f" {Colors.BOLD}👤 {player.name}{Colors.RESET} | 📍 {Colors.BRIGHT_CYAN}{location_name}{Colors.RESET} | 💰 {Colors.BRIGHT_YELLOW}৳ {player.money}{Colors.RESET} | ⭐ XP: {Colors.BRIGHT_MAGENTA}{player.xp}{Colors.RESET}")
    print(f" ⚡ Energy: {bar} {player.energy}% | 🏅 Badges: {Colors.BRIGHT_GREEN}{len(player.badges)}{Colors.RESET}/15 | 🎒 Items: {len(player.backpack)}")
    print(f"{Colors.DIM}----------------------------------------------------------------------{Colors.RESET}\n")

def slow_print(text: str, speed: float = 0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def press_enter_to_continue():
    input(f"\n{Colors.DIM}Press [Enter] to continue...{Colors.RESET}")