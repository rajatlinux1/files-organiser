#!/usr/bin/env python3
import os, shutil
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve())

for i in os.listdir():
    if os.path.isfile(i):
        file_path = Path(i)
        try:
            extensions = str(file_path.suffix).replace(".","")
            if not os.path.exists(extensions):
                os.makedirs(extensions)
            if i == BASE_DIR.split("/")[-1]:
                continue
            shutil.move(i, extensions)

        except IndexError:
            extensions="NoExtension"
            if not os.path.exists(extensions):
                os.makedirs(extensions)
            shutil.move(i, extensions)
        except:
            continue

print("****Files organized successfully****")
