# txt2rjson.py
import json
import base64
import numpy as np


def makeRequestDict(txt: str):
    dat = {
        "audioConfig": {"audioEncoding": "LINEAR16", "pitch": 0, "speakingRate": 1},
        "voice": {"languageCode": "ja-JP", "name": "ja-JP-Standard-B"},
    }

    dat["input"] = {"text": txt}
    return dat


dat = makeRequestDict("こにゃにゃちわ、元気ですか〜")

outjson = "request.json"
with open(outjson, "w") as f:
    json.dump(dat, f, indent=2, ensure_ascii=False)
