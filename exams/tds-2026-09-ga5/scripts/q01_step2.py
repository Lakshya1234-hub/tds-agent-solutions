import subprocess
import shutil

print("Checking available tunneling tools:")
for t in ["ngrok", "lt", "cloudflared"]:
    print(t, shutil.which(t))
