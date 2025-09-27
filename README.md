# PoE-AltAug-Automation
A proof-of-concept for automating the efficient use of Alteration Orbs and Orbs of Augmentation in Path of Exile. This project is intended for **educational and research purposes only**.   **Do not use this script in-game.** Automating gameplay may violate **Grinding Gear Games’ Terms of Service** and can result in a permanent ban.

## Features  
- **Smart alteration spam**: Holds Shift and spams Alterations (and, when necessary, augmentations) until the target affix is present
- **Safety cancel**: Press ```x``` (Default) at any time to safetly quit out of the script
- **Auto-focus window**: Finds and activates the *Path of Exile* window before running
- **Configurable pacing**: Throttle your clicks to match server/client latency or speed it up to your desired pace

## Installation  

### Prerequisites  
- Python 3.10+  

## Requirements  

```
pyautogui
pyperclip
keyboard
pygetwindow
Pillow
```

### Setup  

1. Download ```altspammer.py```:
- Open the file and click Raw → Save As...
- Or run:
  
   ```sh
   curl.exe -L -o "altspammer.py" "https://raw.githubusercontent.com/Borping/PoE-AltAug-Automation/main/altspammer.py"
   ```  

2. Install dependencies:  
   ```sh
   pip install -r requirements.txt  
   ```  
   
3. Edit line 16 with your desired mod:  
   ```sh
   looking_for_mods = ['Merciless']  # <- CASE SENSITIVE, you may include keywords from the mod (e.g., "Tailwind") or the mod name itself (e.g., "Dictator's")
   ```  
   
3. Run the application as administrator:  
   ```sh
   python altspammer.py
   ```  
