# Version: CAM v.0.0.2 | Last modified: 2016.12.26

import picamera
from time import sleep
from datetime import datetime
# Load configuration camera settings from 'config_cam_settings.py' file
from config_cam_settings import *


class Camera_Rec():
    

    def __init(self):

        pass

    def video_filename(self):

        vid_name = 'Dumb-o-Bot_REC_' + datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S') + '.h264'

        return vid_name

    def start_rec(self):

            self.camera = picamera.PiCamera()

            self.camera.resolution = cam_resol
            self.camera.brightness = cam_bright
            self.camera.contrast = cam_contr
            self.camera.saturation = cam_satur
            self.camera.framerate = cam_fps
            self.camera.hflip = cam_hflip
            self.camera.vflip = cam_vflip
            self.camera.awb_mode = cam_awb
            self.camera.image_effect = cam_effect
            self.camera.exposure_mode = cam_exp
            self.camera.annotate_text = self.video_filename()
            self.camera.annotate_text_size = cam_annotate_text_size
            
            self.camera.start_recording(self.camera.annotate_text)

            return self.camera   # Return camera, so stop_rec can cuse it

    def stop_rec(self):

            self.camera.stop_recording()
            self.camera.close()

    def rec_to_stream(self):

        # Open for implementation

        # See: http://picamera.readthedocs.io/en/release-1.12/recipes1.html
        # v.3.10
        pass
