# Mauna Image Writer

Mauna Image Writer is an application for burn ISO and IMG files to USB Flash sticks.

It is currently a work in progress. Maintenance is done by <a href="https://maunalinux.top/">Mauna</a> team.

### **Dependencies**

This application is developed based on Python3 and GTK+ 3. Dependencies:
```bash
gir1.2-glib-2.0 gir1.2-gtk-3.0 python3-gi python3-requests python3-pyudev parted rsync
```

### **Run Application from Source**

Install dependencies
```bash
sudo apt install gir1.2-glib-2.0 gir1.2-gtk-3.0 python3-gi python3-requests python3-pyudev parted rsync
```
Clone the repository
```bash
git clone https://github.com/maunalinux/mauna-image-writer.git ~/mauna-image-writer
```
Run application
```bash
python3 ~/mauna-image-writer/src/Main.py
```

### **Build deb package**

```bash
sudo apt install devscripts git-buildpackage
sudo mk-build-deps -ir
gbp buildpackage --git-export-dir=/tmp/build/mauna-image-writer -us -uc
```

### **Screenshots**

![Mauna Image Writer 1](screenshots/mauna-image-writer-1.png)

![Mauna Image Writer 2](screenshots/mauna-image-writer-2.png)
