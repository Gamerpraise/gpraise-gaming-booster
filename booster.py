#!/usr/bin/env python3
import os, time, json, random

R="\033[91m"; W="\033[97m"; D="\033[90m"; G="\033[92m"; C="\033[96m"; Y="\033[93m"; BOLD="\033[1m"

def load_db():
    try:
        with open('devices.json','r') as f: return json.load(f)
    except: return {}

def find_device(inp_name, db):
    inp = inp_name.lower().strip()
    if not inp: return "generic mid", {"tier":"MID","dpi":400,"boost":0}
    best=None
    for k,v in db.items():
        if k in inp or inp in k:
            if best is None or len(k) > len(best[0]): best=(k,v)
    if best: return best
    low=["a03","a04","a10","a12","hot 10","hot 11","smart","pop","itel","c11","9a"]
    high=["rog","red magic","s23","s24","iphone 1","poco f","poco x","zero","gt neo","oneplus"]
    tier="MID"
    if any(x in inp for x in low): tier="LOW"
    if any(x in inp for x in high): tier="HIGH"
    dpi={"LOW":360,"MID":400,"HIGH":480}[tier]
    return f"generic {tier}", {"tier":tier,"dpi":dpi,"boost":0}

def matrix_rain(duration=2.2):
    os.system('clear')
    w = 42
    h = 14
    cols = [random.randint(0,h) for _ in range(w)]
    start = time.time()
    while time.time() - start < duration:
        os.system('clear')
        for y in range(h):
            line=""
            for x in range(w):
                if cols[x] == y:
                    line+= f"{R}{random.choice(['0','1'])}{W}"
                elif cols[x]-1 == y or cols[x]-2 == y:
                    line+= f"{D}{random.choice(['0','1'])}"
                else:
                    line+= " "
                cols[x] = (cols[x]+1) % (h+random.randint(3,8))
                if random.random() < 0.08: cols[x]=0
            print(line)
        print(f"\n{R}{BOLD} INITIALIZING GPRAISE CORE...{W}")
        time.sleep(0.09)

def banner():
    os.system('clear')
    print(f"{R}{BOLD}")
    print(f" ⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀")
    print(f" ⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠉⠙⠻⣦⡀⠀⠀⠀")
    print(f" ⠀⠀⣰⠏ 👁️ 👁️ ⠹⣆⠀⠀")
    print(f"{W}")
    print(f"{R} ██████╗ ██████╗ ██████╗ █████╗ ██╗███████╗███████╗")
    print(f"{R} ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔════╝")
    print(f"{R} ██║ ███╗██████╔╝██████╔╝███████║██║███████╗█████╗ ")
    print(f"{W} ██║ ██║██╔═══╝ ██╔══██╗██╔══██║██║╚════██║██╔══╝ ")
    print(f"{W} ╚██████╔╝██║ ██║ ██║██║ ██║██║███████║███████╗")
    print(f"{W} ╚═════╝ ╚═╝ ╚═╝ ╚═╝╚═╝ ╚═╝╚═╝╚══════╝╚══════╝{R}")
    print(f"{R} ━━━━━━━━━━━━━━━━ {W}GHOST MODE: ON{R} ━━━━━━━━━━━━━━━━{W}")
    print(f"{D} 99% BOOST | NO BAN | LEGIT{W}\n")

# START
db = load_db()
matrix_rain()
banner()

print(f"{C}[1]{W} Free Fire / Free Fire MAX")
print(f"{C}[2]{W} Blood Strike - 2/3/4 Finger CLAW")
print(f"{C}[3]{W} Call of Duty Mobile")
print(f"{C}[4]{W} PUBG Mobile")
print(f"{C}[5]{W} Farlight 84 / Delta Force\n")

game = input(f"{Y}>> Choose Game [1-5]: {W}").strip()
if game not in ["1","2","3","4","5"]: game="1"

device_input = input(f"{Y}>> Device Name (e.g Infinix Hot 40): {W}").strip()
if not device_input: device_input="Infinix Hot 40"

matched_name, info = find_device(device_input, db)
tier=info["tier"]; dpi=info["dpi"]; boost=info["boost"]

print(f"\n{D}>> Scanning device... {matched_name.upper()} [{tier}] DPI:{dpi} BOOST:{boost:+d}{W}")
time.sleep(0.8)
banner()

# CALC
if tier=="LOW": base=92
elif tier=="MID": base=88
else: base=84
base = max(70,min(100,base+boost))

games={"1":"FREE FIRE","2":"BLOOD STRIKE","3":"COD MOBILE","4":"PUBG MOBILE","5":"FARLIGHT 84"}
print(f"{W}GAME : {R}{games[game]}")
print(f"{W}DEVICE : {C}{device_input} -> {matched_name} [{tier}]")
print(f"{W}DPI : {C}{dpi} {W}CLAW : {C}{claw if 'claw' in locals() else '2'}F\n")
print(f"{Y}══════════════════════════════════════════{W}")

claw="2"
if game in ["2","3","4"]:
    claw = input(f"{Y}>> Fingers [2/3/4]: {W}").strip()
    if claw not in ["2","3","4"]: claw="2"

if game=="1":
    print(f"{G}FREE FIRE - EXACT FOR {device_input.upper()}{W}")
    print(f" {C}GENERAL : {W}{base}")
    print(f" {C}RED DOT : {W}{base-2}")
    print(f" {C}2X : {W}{base-8} {C}4X : {W}{base-12} {C}SNIPER : {W}{base-30}")
    print(f" {C}FREE LOOK : {W}{base-22} {C}DPI : {W}{dpi}")
elif game=="2":
    cam=135+boost+(10 if claw=="4" else 5 if claw=="3" else 0)
    print(f"{G}BLOOD STRIKE - {claw}F CLAW - {device_input}{W}")
    print(f" {C}CAMERA : {W}{cam} {C}ADS : {W}{cam-25} {C}FIRE : {W}{cam-15}")
    print(f" {C}DPI : {W}{dpi} {C}Graphics: Smooth+90FPS")
    if claw=="4": print(f" {R}4F META: L-Index=Fire L, R-Index=Fire R+Jump, Thumbs=Move+Cam{W}")
elif game=="3":
    cam={"LOW":85,"MID":95,"HIGH":110}[tier]+boost
    print(f"{G}CODM - {device_input}{W} {C}CAM {cam} ADS {cam-10} DPI {dpi}{W}")
else:
    print(f"{G}{games[game]} - {device_input}{W} Sens {base+10}% DPI {dpi}")

print(f"\n{Y}══════════════════════════════════════════{W}")
print(f"{G}✓ DONE! Settings optimized for {device_input}{W}")
print(f"{R}99% Boost + Skill = 100% Beast{W}\n")
print(f"{D}──────────────────────────────────────────{W}")
print(f"{W} Credits to {R}{BOLD}Gpraise{W} - Member of Binary Ghosts Org.")
print(f"{D} github.com/Gamerpraise/gpraise-gaming-booster{W}")
print(f"{D}──────────────────────────────────────────{W}\n")