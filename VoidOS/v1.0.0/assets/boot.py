import os
import sys
import time
import random

# Terminal-Farben (ANSI-Escape-Codes)
CYAN = "\033[96m"
DARK_GRAY = "\033[90m"
GREEN = "\033[92m"
RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Boot-Nachrichten
BOOT_LOGS = [
    ("Initializing Void OS Kernel v4.2.0-core", "OK"),
    ("Checking CPU architectures... x86_64 detected", "OK"),
    ("Mounting virtual filesystems (/proc, /sys, /dev)", "OK"),
    ("Initializing entropy source (drand)", "OK"),
    ("Loading encrypted volume 'void_core_crypt'", "OK"),
    ("Starting system logging service", "OK"),
    ("Configuring network interfaces (wlan0, eth0)", "OK"),
    ("Clearing stale temporary files", "OK"),
    ("Loading Void dynamic security modules", "OK"),
    ("Starting D-Bus system message bus", "OK"),
    ("Optimizing memory allocation tables", "OK"),
    ("Launching Void OS Graphical Subsystem", "OK")
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_logo():
    # Stilisiertes, fiktives Void OS Logo
    logo = f"""
{CYAN}██╗   ██╗ ██████╗ ██╗██████╗      ██████╗ ███████╗
██║   ██║██╔═══██╗██║██╔══██╗    ██╔═══██╗██╔════╝
██║   ██║██║   ██║██║██║  ██║    ██║   ██║███████╗
╚██╗ ██╔╝██║   ██║██║██║  ██║    ██║   ██║╚════██║
 ╚████╔╝ ╚██████╔╝██║██████╔╝    ╚██████╔╝███████║
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝      ╚═════╝ ╚══════╝{RESET}
    """
    print(logo)
    print(f"{DARK_GRAY}      --- NOTHINGNESS IS EVERYTHING ---{RESET}\n")

def boot_screen():
    clear_screen()
    draw_logo()
    
    # Teil 1: System-Logs simulieren
    for text, status in BOOT_LOGS:
        sys.stdout.write(f"{WHITE}[  ...  ]{RESET} {text}")
        sys.stdout.flush()
        
        # Zufällige Ladezeit pro Zeile für realistischen Effekt
        time.sleep(random.uniform(0.1, 0.4))
        
        # Zeile überschreiben mit [ OK ]
        sys.stdout.write(f"\r{GREEN}[   {status}   ]{RESET} {text}\n")
        sys.stdout.flush()
        
    print("\n" + "_"*50 + "\n")
    
    # Teil 2: Animierter Ladebalken
    spinner = ["◢", "◣", "◤", "◥"]
    bar_width = 30
    
    for i in range(bar_width + 1):
        progress = i / bar_width
        percent = int(progress * 100)
        
        # Ladebalken-Zeichen
        filled = "█" * i
        empty = "░" * (bar_width - i)
        
        # Rotierendes Symbol
        spin_char = spinner[i % len(spinner)]
        
        # UI zusammenbauen
        sys.stdout.write(f"\r{CYAN}Loading Core Services {spin_char}  [{filled}{empty}] {percent}%")
        sys.stdout.flush()
        
        # Am Ende kurz verlangsamen für "Spannung"
        if percent > 90:
            time.sleep(0.15)
        else:
            time.sleep(0.08)
            
    # System bereit
    print(f"\n\n{GREEN}>> Void OS was successfully initialized.{RESET}\n")

if __name__ == "__main__":
    try:
        boot_screen()
    except KeyboardInterrupt:
        print(f"\n{RED}\n[!] Boot process interrupted by user.{RESET}")
