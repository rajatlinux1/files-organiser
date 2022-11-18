#!/usr/bin/env python3
import os, glob, shutil
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve())
list_1 = os.listdir()
for i in list_1:
    if os.path.isfile(i):
        extensions = i.split(".")[1]
        if not os.path.exists(extensions):
            os.makedirs(extensions)
        for file in glob.glob(f"*.{extensions}"):
            if file == BASE_DIR.split("/")[-1]:
                continue
            else:
                shutil.move(file, extensions)
    else:
        continue
print("****Files organised successfully****")