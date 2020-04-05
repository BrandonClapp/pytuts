import webbrowser
import random
import time

while True:
    vid = random.choice(["UK9_h5Iku64", "FavUpD_IjVY ", "G1IbRujko-A"])
    webbrowser.open(f"https://youtube.com/watch?v={vid}")
    seconds = random.randrange(5, 10)
    time.sleep(seconds)
