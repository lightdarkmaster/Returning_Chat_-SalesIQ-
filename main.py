import pyautogui
import time

# The exact paragraph
text = """The tiger, Panthera tigris, one of the world's most magnificent and revered animals, faces possible extinction in the wild. Since the turn of the century, its habitat and numbers have been reduced by 95 percent. For a million years the "King of the Jungle" lorded over a territory stretching from eastern Turkey to Russian Far"""

# Wait 5 seconds so you can click where you want the text typed
print("You have 4 seconds to place your cursor...")
time.sleep(4)

# Type the text very fast
pyautogui.write(text, interval=0.215)

print("Done typing!")