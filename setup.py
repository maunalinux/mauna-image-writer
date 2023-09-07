#!/usr/bin/env python3
import os
import subprocess
from shutil import copyfile
from setuptools import setup, find_packages

changelog = "debian/changelog"
version = "0.1.0"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
    f = open('src/__version__', 'w')
    f.write(version)
    f.close()

copyfile("icon.svg", "mauna-image-writer.svg")


def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "mauna-image-writer.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/mauna-image-writer.mo"]))
    return mo


data_files = [
 ("/usr/share/applications/", ["top.mauna.image-writer.desktop"]),
 ("/usr/share/mauna/mauna-image-writer/",
  ["icon.svg", "main.svg", "iso.svg", "disk.svg", "settings.svg", "uefi-ntfs.img"]),
 ("/usr/share/mauna/mauna-image-writer/src",
  ["src/Main.py", "src/MainWindow.py", "src/ISOCopier.py", "src/ImageWriter.py",
   "src/USBDeviceManager.py",
   "src/WinUSB.py", "src/__version__"]),
 ("/usr/share/mauna/mauna-image-writer/ui", ["ui/MainWindow.glade"]),
 ("/usr/share/polkit-1/actions", ["top.mauna.pkexec.mauna-image-writer.policy"]),
 ("/usr/bin/", ["mauna-image-writer"]),
 ("/usr/share/icons/hicolor/scalable/apps/", ["mauna-image-writer.svg"]),
] + create_mo_files()

setup(
    name="Mauna Image Writer",
    version=version,
    packages=find_packages(),
    scripts=["mauna-image-writer"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Mauna Linux",
    author_email="dev@maunalinux.top",
    description="Mauna ISO Image Writer.",
    license="GPLv3",
    keywords="iso usb image burn write",
    url="https://github.com/maunalinux/mauna-image-writer",
)
