import pyautogui, pyperclip, keyboard, sys
import pygetwindow as gw

pyautogui.PAUSE = 0.06  # tweak to speed up/slow down crafting

# Screen locations (tuned for 1920x1080, windowed borderless, currency stash tab)
alt_location = (112, 270)
aug_location = (226, 327)
item_location = (334, 454)

# True -> alt spamming for a suffix
# False -> alt spamming for a prefix
looking_for_suffix_mod = False

# Mods you want to see on the item
looking_for_mods = ['Merciless']  # <- CASE SENSITIVE, you may include keywords from the mod (e.g., "Tailwind") or the mod name itself (e.g., "Dictator's")


# ───────────────────────── helpers ─────────────────────────

def cancel_check():
	if keyboard.is_pressed('x'):
		print("Ending session.")
		sys.exit()

def activate_poe():
	if poe_windows := gw.getWindowsWithTitle("Path of Exile"):
		poe = poe_windows[0]
		if not poe.isActive:
			pyautogui.press("altleft")  # gently nudge focus
			poe.activate()
		return True
	return False

def alt_spam_until_open(target_is_suffix: bool) -> bool:
	"""
	Use Alterations (with Shift) until the target affix *group* (Suffix/Prefix) is present.
	Returns True if we hit a state that passes check_for_mods(1) during rolling,
	False if the item loses the target affix group and needs an Aug.
	"""
	cancel_check()
	pyautogui.moveTo(alt_location)
	pyautogui.keyDown('shift')
	pyautogui.rightClick()
	pyautogui.moveTo(item_location)

	target_token = 'Suffix' if target_is_suffix else 'Prefix'

	while True:
		cancel_check()

		# Did we hit at least one desired mod? Stop alt-spam so we can continue crafting.
		if check_for_mods(1):
			pyautogui.keyUp('shift')
			return True

		# Peek current item text to ensure the target group exists.
		text = pyperclip.paste()
		if target_token not in text:
			# We've lost the target affix group -> we need to Aug to restore a missing affix.
			pyautogui.keyUp('shift')
			return False
		else:
			# Keep alt-spamming
			pyautogui.leftClick()

def aug_item():
	cancel_check()
	pyautogui.moveTo(aug_location)
	pyautogui.keyUp('shift')
	pyautogui.rightClick()
	pyautogui.moveTo(item_location)
	pyautogui.leftClick()

def check_for_mods(num: int) -> bool:
	# Copy item to clipboard
	pyautogui.hotkey('ctrl', 'alt', 'c')
	text = pyperclip.paste()
	# Count how many desired mods appear in the text
	matches = sum(1 for mod in looking_for_mods if mod in text)
	return matches >= num

# ───────────────────────── main flow ─────────────────────────

def craft_cycle() -> bool:
	"""
	Alt spam until the *target* affix group (Suffix/Prefix) exists; Aug if we lose it.
	Returns True when check_for_mods(1) succeeds (item COMPLETE).
	"""
	while True:
		if alt_spam_until_open(looking_for_suffix_mod):
			# Success condition met inside alt spam: item complete
			return True
		# Need to restore missing affix group with Aug and try again
		aug_item()

def run():
	# Activate PoE window once up front
	activate_poe()
	
	while True:
		cancel_check()
		if craft_cycle():
			print("Item Finished")
			return

if __name__ == "__main__":
	run()
