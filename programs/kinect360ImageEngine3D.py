'''
  * ************************************************************
  *      Program: Kinect 360 Image Engine 3D Module
  *      Type: Python
  *      Author: David Velasco Garcia @davidvelascogarcia
  * ************************************************************
  *
  * | OUTPUT PORT                               | CONTENT                                                 |
  * |-------------------------------------------|---------------------------------------------------------|
  * | /kinect360ImageEngine3D/rgb/img:o         | Output RGB image                                        |
  * | /kinect360ImageEngine3D/depth/img:o       | Output depth image                                      |
  * | /kinect360ImageEngine3D/depthColor/img:o  | Output depth with proximity colors image                |
  * | /kinect360ImageEngine3D/ir/img:o          | Output IR image                                         |
  * | /kinect360ImageEngine3D/data:o            | Output pixel depth data in matrix                       |
  *
'''

# Libraries
import cv2
import datetime
import freenect
from freenect import sync_get_depth as get_depth
import numpy as np
import time
import yarp

print("**************************************************************************")
print("**************************************************************************")
print("               Program: Kinect 360 Image Engine 3D Module                 ")
print("                     Author: David Velasco Garcia                         ")
print("                             @davidvelascogarcia                          ")
print("**************************************************************************")
print("**************************************************************************")

print("")
print("Starting system...")

print("")
print("Loading kinect360ImageEngine3D module...")

# Select configuration mode, IR and RGB use same channel and go slow at the same time
print("")
print("")
print("**************************************************************************")
print("Video sources configuration:")
print("**************************************************************************")
print("")
print("")
print("Please, select your configuration.")
print("")
print("1. RGB and depth image.")
print("2. IR and depth image.")
print("")

loopControlConfiguration = 0

# Check correct selection
while int(loopControlConfiguration) == 0:

    configurationSelected = input()

    # Selected RGB
    if str(configurationSelected) == "1":
        print("")
        print("You have selected RGB and depth camera configuration.")
        print("")

        # Exit loop
        loopControlConfiguration = 1

    # Selected IR
    elif str(configurationSelected) == "2":
        print("")
        print("You have selected IR and depth camera configuration.")
        print("")

        # Exit loop
        loopControlConfiguration = 1

    # Configuration not supported
    else:
        print("")
        print("Sorry, option not supported, re-enter configuration mode.")
        print("")

print("")
print("[INFO] Video source configuraction done correctly.")
print("")


print("")
print("")
print("**************************************************************************")
print("YARP configuration:")
print("**************************************************************************")
print("")
print("")
print("Initializing YARP network...")

# Init YARP Network
yarp.Network.init()

# If RGB was selected
if str(configurationSelected) == "1":
    print("")
    print("[INFO] Opening RGB image output port with name /kinect360ImageEngine3D/rgb/img:o ...")

    # Open output image port
    kinect360ImageEngine3D_rgb_portOut = yarp.Port()
    kinect360ImageEngine3D_rgb_portNameOut = '/kinect360ImageEngine3D/rgb/img:o'
    kinect360ImageEngine3D_rgb_portOut.open(kinect360ImageEngine3D_rgb_portNameOut)

print("")
print("[INFO] Opening depth image output port with name /kinect360ImageEngine3D/depth/img:o ...")

# Open output image port
kinect360ImageEngine3D_depth_portOut = yarp.Port()
kinect360ImageEngine3D_depth_portNameOut = '/kinect360ImageEngine3D/depth/img:o'
kinect360ImageEngine3D_depth_portOut.open(kinect360ImageEngine3D_depth_portNameOut)

"""
print("")
print("[INFO] Opening depth color image output port with name /kinect360ImageEngine3D/depthColor/img:o ...")

# Open output image port
kinect360ImageEngine3D_depthColor_portOut = yarp.Port()
kinect360ImageEngine3D_depthColor_portNameOut = '/kinect360ImageEngine3D/depthColor/img:o'
kinect360ImageEngine3D_depthColor_portOut.open(kinect360ImageEngine3D_depthColor_portNameOut)
"""

# If IR was selected
if str(configurationSelected) == "2":
    print("")
    print("[INFO] Opening IR image output port with name /kinect360ImageEngine3D/ir/img:o ...")

    # Open output image port
    kinect360ImageEngine3D_ir_portOut = yarp.Port()
    kinect360ImageEngine3D_ir_portNameOut = '/kinect360ImageEngine3D/ir/img:o'
    kinect360ImageEngine3D_ir_portOut.open(kinect360ImageEngine3D_ir_portNameOut)

"""
print("")
print("[INFO] Opening pixel depth data in matrix output port with name /kinect360ImageEngine3D/data:o ...")

# Open output image port
kinect360ImageEngine3D_data_portOut = yarp.Port()
kinect360ImageEngine3D_data_portNameOut = '/kinect360ImageEngine3D/data:o'
kinect360ImageEngine3D_data_portOut.open(kinect360ImageEngine3D_data_portNameOut)
"""

# Create depth distance bootle
depthDistanceBottle=yarp.Bottle()

# Image size
image_w = 640
image_h = 480

# Prepare output image buffer
out_buf_image = yarp.ImageRgb()
out_buf_image.resize(image_w, image_h)
out_buf_array = np.zeros((image_h, image_w, 3), np.uint8)
out_buf_image.setExternal(out_buf_array.data, out_buf_array.shape[1], out_buf_array.shape[0])


print("")
print("")
print("**************************************************************************")
print("Connecting with Kinect 360 3D image source:")
print("**************************************************************************")
print("")
print("")
print("Connecting with Kinect 360 3D image source ...")
print("")


loopControlGetImage = 0

# Loop process
while True:


    print("")
    print("")
    print("**************************************************************************")
    print("Getting images from Kinect 360 3D image source:")
    print("**************************************************************************")
    print("")
    print("")
    print("Getting images from Kinect 360 3D image source ...")
    print("")

    # Get time frame
    timeFrame = datetime.datetime.now()

    """
    # Prepare depth distance data
    depthDistanceData = "null"

    # Sending depth distance data
    depthDistanceBottle.clear()
    depthDistanceBottle.addString(str(depthDistanceData))
    kinect360ImageEngine3D_data_portOut.write(depthDistanceBottle)
    """

    print("")
    print("")
    print("**************************************************************************")
    print("Sending images:")
    print("**************************************************************************")
    print("")
    print("")

    # Sending Kinect 360 Images
    print("")
    print("Sending Kinect 360 Images ...")
    print("")

    # If RGB was selected
    if str(configurationSelected) == "1":
        # Get and send RGB image
        try:
            print("")
            print("**************************************************************************")
            print("RGB image:")
            print("**************************************************************************")
            print("")
            print("")
            print("Getting RGB image ...")
            print("")

            # Get RGB images
            rgbImageSource,_ = freenect.sync_get_video()
            outputRGBImage = cv2.cvtColor(rgbImageSource, cv2.COLOR_RGB2BGR)
            print("")
            print("[INFO] RGB image obtained correctly.")
            print("")

            # Send RGB image
            print("")
            print("Sending RGB image at " + str(timeFrame) + "...")
            print("")
            out_buf_array[:,:] = rgbImageSource
            rgbImage = out_buf_image
            kinect360ImageEngine3D_rgb_portOut.write(rgbImage)

        # RGB exception
        except:
            print("")
            print("[ERROR] I couldn´t recover RGB image.")
            print("")

    # Get and send depth image
    try:
        print("")
        print("**************************************************************************")
        print("Depth image:")
        print("**************************************************************************")
        print("")
        print("")
        print("Getting depth image ...")
        print("")

        # Get depth images
        depthImageSource,_ = freenect.sync_get_depth()
        outputDepthImage = depthImageSource.astype(np.uint8)
        outputDepthImage = cv2.cvtColor(outputDepthImage, cv2.COLOR_GRAY2RGB)
        print("")
        print("[INFO] Depth image obtained correctly.")
        print("")

        # Send depth image
        print("")
        print("Sending depth image at " + str(timeFrame) + "...")
        print("")
        out_buf_array[:,:] = outputDepthImage
        depthImage = out_buf_image
        kinect360ImageEngine3D_depth_portOut.write(depthImage)

    # Depth exception
    except:
        print("")
        print("[ERROR] I couldn´t recover Depth image.")
        print("")

    # If IR was selected
    if str(configurationSelected) == "2":
        # Get and send IR image
        try:
            print("")
            print("**************************************************************************")
            print("IR image:")
            print("**************************************************************************")
            print("")
            print("")
            print("Getting IR image ...")
            print("")

            # Get IR images
            irImageSource,_ = freenect.sync_get_video(0,freenect.VIDEO_IR_10BIT)
            np.clip(irImageSource, 0, 2**10-1, irImageSource)
            irImageSource >>=2
            outputIRImage = irImageSource.astype(np.uint8)
            outputIRImage = cv2.cvtColor(outputIRImage, cv2.COLOR_GRAY2RGB)
            print("")
            print("[INFO] IR image obtained correctly.")
            print("")

            # Send IR image
            print("")
            print("Sending IR image at " + str(timeFrame) + "...")
            print("")
            out_buf_array[:,:] = outputIRImage
            irImage = out_buf_image
            kinect360ImageEngine3D_ir_portOut.write(irImage)

        # IR exception
        except:
            print("")
            print("[ERROR] I couldn´t recover IR image.")
            print("")

# Close ports
print("")
print("")
print("**************************************************************************")
print("Close YARP ports:")
print("**************************************************************************")
print("")
print("")
print("[INFO] Closing YARP ports ...")

# If RGB was selected
if str(configurationSelected) == "1":
    kinect360ImageEngine3D_rgb_portOut.close()

kinect360ImageEngine3D_depth_portOut.close()
#kinect360ImageEngine3D_depthColor_portOut.close()

# If IR was selected
if str(configurationSelected) == "2":
    kinect360ImageEngine3D_ir_portOut.close()

#kinect360ImageEngine3D_data_portOut.close()

print("")
print("")
print("**************************************************************************")
print("Program finished")
print("**************************************************************************")
print("")
print("kinect360ImageEngine3D program closed correctly.")
print("")
