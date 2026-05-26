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

# Shutdown-Nachrichten
SHUTDOWN_LOGS = [
    ("Sending SIGTERM to all running processes", "OK"),
    ("Stopping Void OS Graphical Subsystem", "OK"),
    ("Disconnecting network interfaces (wlan0, eth0)", "OK"),
    ("Saving system entropy state", "OK"),
    ("Unmounting virtual filesystems (/proc, /sys)", "OK"),
    ("Closing encrypted volume 'void_core_crypt'", "OK"),
    ("Syncing cached data to persistent storage", "OK"),
    ("Releasing system memory allocation tables", "OK"),
    ("Powering down Void Kernel v4.2.0-core", "STOP")
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def shutdown_screen():
    clear_screen()
    
    # Teil 1: Absteigender Ladebalken (De-Isolierung)
    bar_width = 30
    print(f"{RED}[!] Initiating Void OS Shutdown Sequence{RESET}\n")
    
    for i in range(bar_width, -1, -1):
        progress = i / bar_width
        percent = int(progress * 100)
        
        filled = "█" * i
        empty = "░" * (bar_width - i)
        
        # UI zusammenbauen
        sys.stdout.write(f"\r{RED}Terminating Core Services  [{filled}{empty}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.05)
        
    print("\n\n" + "_"*50 + "\n")
    
    # Teil 2: System-Dienste stoppen
    for text, status in SHUTDOWN_LOGS:
        sys.stdout.write(f"{WHITE}[  ...  ]{RESET} {text}")
        sys.stdout.flush()
        
        # Schnelles, unregelmäßiges Herunterfahren simulieren
        time.sleep(random.uniform(0.08, 0.25))
        
        # Zeile überschreiben
        color = RED if status == "STOP" else DARK_GRAY
        sys.stdout.write(f"\r{color}[  {status}  ]{RESET} {text}\n")
        sys.stdout.flush()
        
    print("\n" + "_"*50 + "\n")
    time.sleep(0.5)
    
    # Teil 3: "Signalverlust" / Flimmern vor dem Ausgehen
    glitch_text = "SYSTEM HALTED. VOID REACHED."
    for _ in range(3):
        sys.stdout.write(f"\r{DARK_GRAY}{glitch_text}{RESET}")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(f"\r{' ' * len(glitch_text)}")
        sys.stdout.flush()
        time.sleep(0.1)
        
    # Letzter finaler Text, der verschwindet
    sys.stdout.write(f"\r{RED}GOODBYE.{RESET}")
    sys.stdout.flush()
    time.sleep(0.8)
    
    clear_screen()

if __name__ == "__main__":
    shutdown_screen()
