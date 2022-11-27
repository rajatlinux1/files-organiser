#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path
from datetime import datetime
from plyer import notification

current_time = datetime.now().strftime('%I:%M %p')

BASE_DIR = str(Path(__file__).resolve())


for file in os.listdir():

    if os.path.isfile(file) and not file.startswith('.'):
        file_path = Path(file)

        try:
            extensions = str(file_path.suffix).replace(".", "")
            if not os.path.exists(extensions):
                os.mkdir(extensions)
            # To ignore this files or directories
            if file == BASE_DIR.split("/")[-1] or file == sys.prefix.split("/")[-1] or file == sys.prefix.split("\\")[-1]:
                continue
            shutil.move(file, extensions)

        except IndexError:
            extensions = "NoExtension"
            if not os.path.exists(extensions):
                os.makedirs(extensions)
            shutil.move(file, extensions)

        except Exception as e:
            notification.notify(
                title=f"Files Organizer {current_time}",
                message=e,
                # app_icon="icon.ico",
                timeout=5000
            )

if not Exception:
    notification.notify(
        title=f"Files Organizer {current_time}",
        message="Files organized successfully",
        # app_icon="icon.ico",
        timeout=5000
    )
