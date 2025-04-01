from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
import usb_hid
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time


keybow = PMK(Hardware())
keys = keybow.keys


keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
# Strategem database
strategems = {
    #Mines (yellow)
    "Anti-Personnel Mines": {"NAME": "Anti-Personnel Minefield", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Anti-Tank Mines": {"NAME": "MD-17 Anti-Tank Mines", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Incendiary Mines": {"NAME": "Incendiary Mines", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    #Support Strategems (green)
    "Supply Pack": {"NAME": "Supply Pack", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "c", "STRAT_CALL": 5, "STRAT_COOL": 480},
    "Shield Generator Pack": {"NAME": "Shield Generator Pack", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "c", "STRAT_CALL": 5, "STRAT_COOL": 480},
    "Ballistic Shield Backpack": {"NAME": "Ballistic Shield Backpack", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "c", "STRAT_CALL": 5, "STRAT_COOL": 300},
    "Jump Pack": {"NAME": "Jump Pack", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "c", "STRAT_CALL": 5, "STRAT_COOL": 480},
    "Fast Recon Vehicle": {"NAME": "M-102 Fast Recon Vehicle", "STRAT_CODE": [Keycode.TAB, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "c", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Eagle Smoke Strike": {"NAME": "Eagle Smoke Strike", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "c", "STRAT_CALL": 0, "STRAT_COOL": 15},
    "Shield Generator Relay": {"NAME": "Shield Generator Relay", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "C", "STRAT_CALL": 0, "STRAT_COOL": 90},
    #Carried Weapons (purple)
    "Grenade Launcher": {"NAME": "Grenade Launcher", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},    "Laser Cannon": {"NAME": "Laser Cannon", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 2},
    "Arc Thrower": {"NAME": "Arc Thrower", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Guard Dog": {"NAME": "Guard Dog", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 5, "STRAT_COOL": 480},
    "Guard Dog Rover": {"NAME": "Guard Dog Rover", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 5, "STRAT_COOL": 480},
    "Machine Gun": {"NAME": "Machine Gun", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Anti-Material Rifle": {"NAME": "Anti-Material Rifle", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Stalwart": {"NAME": "Stalwart", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Recoilless Rifle": {"NAME": "Recoilless Rifle", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Flamethrower": {"NAME": "Flamethrower", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Autocannon": {"NAME": "Autocannon", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Railgun": {"NAME": "Railgun", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    "Spear": {"NAME": "Spear", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "b", "STRAT_CALL": 3, "STRAT_COOL": 480},
    #Thrown Weapons (Red)   
    "Machine Gun Sentry": {"NAME": "Machine Gun Sentry", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Gatling Sentry": {"NAME": "Gatling Sentry", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Mortar Sentry": {"NAME": "Mortar Sentry", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Rocket Sentry": {"NAME": "Rocket Sentry", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Autocannon Sentry": {"NAME": "Autocannon Sentry", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "EMS Mortar Sentry": {"NAME": "EMS Mortar Sentry", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Orbital Precision Strike": {"NAME": "Orbital Precision Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 4, "STRAT_COOL": 100},
    "Orbital Gas Strike": {"NAME": "Orbital Gas Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 2, "STRAT_COOL": 75},
    "Orbital EMS Strike": {"NAME": "Orbital EMS Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 2, "STRAT_COOL": 75},
    "Orbital Smoke Strike": {"NAME": "Orbital Smoke Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 2, "STRAT_COOL": 100},
    "HMG Emplacement": {"NAME": "HMG Emplacement", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Tesla Tower": {"NAME": "Tesla Tower", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 150},
    "Eagle Strafing Run": {"NAME": "Eagle Strafing Run", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 0, "STRAT_COOL": 15},
    "Eagle Airstrike": {"NAME": "Eagle Airstrike", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 0, "STRAT_COOL": 15},
    "Eagle Cluster Bomb": {"NAME": "Eagle Cluster Bomb", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 0, "STRAT_COOL": 15},
    "Eagle Napalm Airstrike": {"NAME": "Eagle Napalm Airstrike", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "a", "STRAT_CALL": 0, "STRAT_COOL": 15},
    "Eagle 110MM Rocket Pods": {"NAME": "Eagle 110MM Rocket Pods", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (0, 255, 255), "STRAT_CAT": "a", "STRAT_CALL": 0, "STRAT_COOL": 15},
    "Eagle 500KG Bomb": {"NAME": "Eagle 500KG Bomb", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 0, "STRAT_COOL": 0},
    "Orbital Gatling Barrage": {"NAME": "Orbital Gatling Barrage", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "a", "STRAT_CALL": 2, "STRAT_COOL": 80},
    "Orbital Airburst Strike": {"NAME": "Orbital Airburst Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "a", "STRAT_CALL": 2, "STRAT_COOL": 120},
    "Orbital 120MM HE Barrage": {"NAME": "Orbital 120MM HE Barrage", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 5, "STRAT_COOL": 240},
    "Orbital 380MM HE Barrage": {"NAME": "Orbital 380MM HE Barrage", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "b", "STRAT_CALL": 6, "STRAT_COOL": 240},
    "Orbital Walking Barrage": {"NAME": "Orbital Walking Barrage", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 240},
    "Orbital Laser Strike": {"NAME": "Orbital Laser Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 255, 0), "STRAT_CAT": "a", "STRAT_CALL": 3, "STRAT_COOL": 300},
    "Orbital Railcannon Strike": {"NAME": "Orbital Railcannon Strike", "STRAT_CODE": [Keycode.TAB, Keycode.RIGHT_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "a", "STRAT_CALL": 1, "STRAT_COOL": 210},
    "Expendable Anti-Tank": {"NAME": "Expendable Anti-Tank", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (255, 0, 255), "STRAT_CAT": "a", "STRAT_CALL": 2, "STRAT_COOL": 70},
    #Planet Strategems (Color varies, but always on bottom row)
    "Resupply": {"NAME": "Resupply", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.RIGHT_ARROW], "LED_COLOR": (0, 100, 0), "STRAT_CAT": "d", "STRAT_CALL": 3, "STRAT_COOL": 300},
    "SOS Beacon": {"NAME": "SOS Beacon", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW], "LED_COLOR": (0, 0, 255), "STRAT_CAT": "d", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Super Earth Flag": {"NAME": "Super Earth Flag", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.UP_ARROW], "LED_COLOR": (0, 0, 255), "STRAT_CAT": "d", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Upload Data": {"NAME": "Upload Data", "STRAT_CODE": [Keycode.TAB, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW, Keycode.UP_ARROW], "LED_COLOR": (0, 255, 0), "STRAT_CAT": "d", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Hellbomb": {"NAME": "Hellbomb", "STRAT_CODE": [Keycode.TAB, Keycode.DOWN_ARROW, Keycode.UP_ARROW, Keycode.LEFT_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW], "LED_COLOR": (255, 0, 0), "STRAT_CAT": "d", "STRAT_CALL": 3, "STRAT_COOL": 180},
    "Reinforce": {"NAME": "Reinforce", "STRAT_CODE": [Keycode.TAB, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.RIGHT_ARROW, Keycode.LEFT_ARROW, Keycode.UP_ARROW], "LED_COLOR": (100, 0, 0), "STRAT_CAT": "d", "STRAT_CALL": 0, "STRAT_COOL": 0}
     
      }


# Load strategems from file
selected_strategems = []
try:
    with open("strategem.txt", "r") as file:
        for line in file:
            name = line.strip()
            if name in strategems:
                selected_strategems.append(name)
except FileNotFoundError:
    # Auto-fill with Resupply and Reinforce if the file is not found
    selected_strategems = ["Reinforce", "Resupply"]

# If the list is still empty after loading, fill it with defaults
if not selected_strategems:
    selected_strategems = ["Reinforce", "Resupply"]

# Assign buttons & LED colors in one step
category_positions = {"a": [3, 7, 11, 15], "b": [2, 6, 10, 14], "c": [1, 5, 9, 13], "d": [0, 4, 8, 12]}
button_map = {}
category_index = {"a": 0, "b": 0, "c": 0, "d": 0}

for strategem in selected_strategems:
    category = strategems[strategem]["STRAT_CAT"]
    if category_index[category] < len(category_positions[category]):
        button = category_positions[category][category_index[category]]
        button_map[button] = strategem
        keys[button].set_led(*strategems[strategem]["LED_COLOR"])  # Set LED color

        category_index[category] += 1

# Attach handler functions to all of the keys
for key in keys:
    @keybow.on_press(key)
    def press_handler(key):
        if key.number in button_map:
            strategem_name = button_map[key.number]
            strat_code = strategems[strategem_name]["STRAT_CODE"]
            
            # Press each key in the strat_code
            for keycode in strat_code:
                keyboard.press(keycode)
                time.sleep(0.1)  # Short delay to mimic human input
                keyboard.release(keycode)
                time.sleep(0.1)

        
    @keybow.on_release(key)
    def release_handler(key):
        pass

# Main loop
while True:
    keybow.update()  # Update the state of the keys and trigger the handlers
