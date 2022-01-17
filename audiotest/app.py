import os
import numpy as np
import cv2
import time
from switch import TestThreading

from watch import Watcher,TimeLimit
from camera_thread import VideoStreamWidget
from just import predict
import subprocess

# import dot


w = Watcher(0)
t = TimeLimit()

if __name__ == "__main__":
    src = os.getenv("STREAM_SRC") #175.101.82.215:1024/Streaming/Channels/502
    print(src)

    video_stream_widget = VideoStreamWidget(src)
    time.sleep(1)

    while True:

        count = predict(video_stream_widget.frame)

        if count is None:
            time.sleep(10)
            continue

        watch = w.variable < count
        print(watch,w.variable,count)

        if count >= 1 and watch and t.check_value() > 40:
            command = "echo 21 > /sys/class/gpio/export; echo out > /sys/class/gpio/gpio21/direction; echo 1 > /sys/class/gpio/gpio21/value"
            ret = subprocess.run(command, capture_output=True, shell=True)
            print(ret.stdout.decode())
            TestThreading(os.getenv("SCREENLY_ASSET"))
            print('request sent')
            command = "echo 21 > /sys/class/gpio/unexport"
            ret = subprocess.run(command, capture_output=True, shell=True)
            print(ret.stdout.decode())
            t = TimeLimit(int(time.time()))

        w.check_value(count)
        #video_stream_widget.show_frame()
        #key = cv2.waitKey(1)
        #if key & 0xFF == ord('q'):
            #break
