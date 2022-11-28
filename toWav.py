# toWav.py
import json
import base64
import numpy as np

inputf = "result.json"
outputf = "result.wav"

with open(inputf) as f:
    df = json.load(f)

b64str = df["audioContent"]
binary = base64.b64decode(b64str)
dat = np.frombuffer(binary, dtype=np.uint8)

with open(outputf, "wb") as f:
    f.write(dat)
