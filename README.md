[![kinect360ImageEngine3D Homepage](https://img.shields.io/badge/kinect360ImageEngine3D-develop-orange.svg)](https://github.com/davidvelascogarcia/kinect360ImageEngine3D/tree/develop/programs) [![Latest Release](https://img.shields.io/github/tag/davidvelascogarcia/kinect360ImageEngine3D.svg?label=Latest%20Release)](https://github.com/davidvelascogarcia/kinect360ImageEngine3D/tags) [![Build Status](https://travis-ci.org/davidvelascogarcia/kinect360ImageEngine3D.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/kinect360ImageEngine3D)

# Kinect 360: Image Engine 3D (Python API)

- [Introduction](#introduction)
- [Use program](#use-program)
- [Requirements](#requirements)
- [Status](#status)
- [Related projects](#related-projects)


## Introduction

`kinect360ImageEngine3D` module use `freenect` `python` API. The module get image source from `Kinect 360` getting `RGB` image, `Depth` image and `IR` image. Also use `YARP` to send video source using different ports.

## Use program

`kinect360ImageEngine3D` requires `Kinect 360` device conneted to get images sources.

1. Execute [programs/kinect360ImageEngine3D.py](./programs), to start de program.
```python
python3 kinect360ImageEngine3D.py
```
3. Connect video sources to your program.
```bash
yarp connect /kinect360ImageEngine3D/rgb/img:o /yourportRGB
yarp connect /kinect360ImageEngine3D/depth/img:o /yourportDEPTH
yarp connect /kinect360ImageEngine3D/ir/img:o /yourportIR
```

NOTE:

- Video `RGB` results are published on `/kinect360ImageEngine3D/rgb/img:o`
- Video `DEPTH` results are published on `/kinect360ImageEngine3D/depth/img:o`
- Video `IR` results are published on `/kinect360ImageEngine3D/ir/img:o`

## Requirements

`kinect360ImageEngine3D` requires:

* [Install OpenCV 3.0.0+ (with python bindings)](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-opencv.md)
* [Install YARP 2.3.XX+ (with python bindings)](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-yarp.md)
* [Install pip](https://github.com/roboticslab-uc3m/installation-guides/blob/master/install-pip.md)
* [Install freenect (with python wrappers)](https://openkinect.org/wiki/Getting_Started#Manual_Build_on_Linux)

**NOTE:**

Some required libs:

* Linux (Ubuntu 14.04 and 16.04):

```bash
sudo apt-get install git-core cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev cython
```

* Linux (Ubuntu 18.04+):

```bash
sudo apt-get install git-core cmake libglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev cython
```


Tested on: `ubuntu 14.04`, `ubuntu 16.04`, `ubuntu 18.04`, `lubuntu 18.04` and `raspbian`.

`freenect` requires `cmake 3.12.4+`. `Ubuntu 14.04 and 16.04` use `cmake 3.5.1` by default. Some `APT` repositories offers the last `cmake` version like:

```bash
wget -qO - https://apt.kitware.com/keys/kitware-archive-latest.asc |
    sudo apt-key add -

sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ xenial main'
sudo apt-get update
sudo apt-get install cmake
```

**Some possible errors:**

* Installing `python wrappers` some things to do:

On`freenect` building:

```bash
cmake .. -DBUILD_PYTHON3=ON
make
```

After doing `sudo make install` on `freenect/wrappers/python`:

```bash
sudo python3 setup.py install
```

* Use `freenect` without `sudo`:

```bash
sudo adduser $USER video
```

* Add some rules to `Kinect 360` device:

```bash
sudo nano /etc/udev/rules.d/51-kinect.rules
```

Paste:

```bash
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02b0", MODE="0666"
# ATTR{product}=="Xbox NUI Audio"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ad", MODE="0666"
# ATTR{product}=="Xbox NUI Camera"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ae", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02c2", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02be", MODE="0666"
# ATTR{product}=="Xbox NUI Motor"
SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02bf", MODE="0666"
```

* `Kinect 360` autosuspend can be solved with:

```bash
echo -1 | sudo tee -a /sys/module/usbcore/parameters/autosuspend
```

## Status

[![Build Status](https://travis-ci.org/davidvelascogarcia/kinect360ImageEngine3D.svg?branch=develop)](https://travis-ci.org/davidvelascogarcia/kinect360ImageEngine3D)

[![Issues](https://img.shields.io/github/issues/davidvelascogarcia/kinect360ImageEngine3D.svg?label=Issues)](https://github.com/davidvelascogarcia/kinect360ImageEngine3D/issues)

## Related projects

* [OpenKinect: freenect project](https://github.com/OpenKinect/libfreenect)

