#!/usr/bin/python
import json
import os
import pathlib
import random
from time import sleep

config = {
    # your folders you want load walppapers from it.
    "bg_dirs": ["/usr/share/wallpapers"],
    "change_delay": 300,  # yor time delay for changing walpaper
    "accept_suffixes": [".png", ".jpeg", ".jpg"],  # accept image formats.
    "feh_path":"/usr/bin/feh"
}

backgrounds = []

last_bgs = []

if not pathlib.Path(config['feh_path']).exists():
    print("feh not found ")
    print("please install it with pacman -S feh \nor\napt-get install feh")

def index(path: pathlib.Path):
    if path.exists():
        print(f"indexing {path}")
        for i in path.iterdir():
            if i.is_dir():
                path = pathlib.Path(i)
                index(path=path)
            elif i.is_file:
                if i.suffix in config["accept_suffixes"]:
                    i.rename(i.with_name(i.name.replace(" ", "_")))
                    backgrounds.append(i)
                    print(f"founded {i}")
                else:
                    print(f"unknown file prefix {i}")
    else:
        print(f"not exist {path}")


def change_bg():
    while True:
        if backgrounds.__len__() == 0:
            for i in last_bgs:
                backgrounds.append(i)
        bg = random.choice(backgrounds)
        last_bgs.append(bg)
        print(f"current {bg}")
        backgrounds.remove(bg)
        os.system(f"feh --bg-scale {bg}")
        sleep(config["change_delay"])


if __name__ == "__main__":
    for i in config["bg_dirs"]:
        path = pathlib.Path(i)
        index(path=path)
    print(f"founded {len(backgrounds)} images")
    change_bg()
