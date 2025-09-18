import time
import sys

# A simple loading animation
for i in range(6):
    sys.stdout.write("\rLoading" + "." * i)  # \r brings cursor back
    sys.stdout.flush()
    time.sleep(0.5)

print("\nDone!")
