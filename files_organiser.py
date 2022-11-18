#!/usr/bin/env python3
import os, glob, shutil
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve())
list_1 = os.listdir()
for i in list_1:
    if os.path.isfile(i):
        try:
            extensions = i.split(".")[1]
            if not os.path.exists(extensions):
                os.makedirs(extensions)
            for file in glob.glob(f"*.{extensions}"):
                if file == BASE_DIR.split("/")[-1]:
                    continue
                else:
                    shutil.move(file, extensions)
        except IndexError:
            extensions="NoExtension"
            if not os.path.exists(extensions):
                os.makedirs(extensions)
            shutil.move(i, extensions)
        except:
            continue

    else:
        continue
print("****Files organized successfully****")
