#!/usr/bin/env python
# coding: utf-8
#

import camera
import dht11
from wxbot import *
import baidu


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        req = ''
        if msg['to_user_id'] == 'filehelper' and msg['content']['type'] == 0:
            req = msg['content']['data']
        elif msg['to_user_id'] == 'filehelper' and msg['content']['type'] == 4:
            self.get_voice(msg['msg_id'])
            os.system('ffmpeg -y -i voice.mp3  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 voice.pcm')
            req = baidu.main()
        if req:
            if u'测试' in req:
                self.send_msg_by_uid(u'hi', 'filehelper')
            elif u'温湿度' in req:
                info = dht11.get()
                self.send_msg_by_uid(u'温度:' + info["TEMP"] + u'℃', 'filehelper')
                self.send_msg_by_uid(u'湿度:' + info["HUMIDITY"] + u'%', 'filehelper')
            elif u'拍照' in req:
                camera.picture()
                self.send_img_msg_by_uid('temp/picture.jpg', 'filehelper')
            elif u'录像' in req:
                camera.video()
                self.send_file_msg_by_uid('temp/video.mp4', 'filehelper')
            elif u'CPU温度' in req:
                res = os.popen('vcgencmd measure_temp').readline()
                tmp = res.replace("temp=", "").replace("'C\n", "")
                self.send_msg_by_uid(u'CPU温度:' + tmp + u'℃', 'filehelper')

def main():
    bot = MyWXBot()
    # bot.DEBUG = True
    # bot.conf['qr'] = 'mail'
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
