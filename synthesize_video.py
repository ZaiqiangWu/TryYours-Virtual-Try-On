import os

import numpy as np

from util.image2video import Image2VideoWriter
import time
import cv2

def process_video(video_path):
    video_name=os.path.basename(video_path)
    vidcap = cv2.VideoCapture(video_path)
    success = True
    input_image_list = []
    target_garment = './temporal_target_garments'
    video_writer = Image2VideoWriter()
    video_writer2 = Image2VideoWriter()
    count=0
    while success:
        success, image = vidcap.read()
        #if count>5:
        #    break
        if not success:
            break
        h,w,_ = image.shape
        input_image_list.append(image[:,0:w//3,:])
        count+=1
    step =0
    for img in input_image_list:
        t1 = time.perf_counter()
        cv2.imwrite("./static/origin_web.jpg", img)
        os.system('cp ' + target_garment + ' ./static/cloth_web.jpg')
        os.system('python main.py')
        result = cv2.imread('./static/finalimg.png')
        h, w, _ = img.shape
        zero_pad = np.zeros((h,w,3)).astype(np.uint8)
        frame = np.concatenate([img,zero_pad,result],1)
        frame2 = np.concatenate([img, result], 1)
        video_writer.append(frame)
        video_writer2.append(frame2)

        t2 = time.perf_counter()

        print("elapsed time (s):", (t2 - t1))
        if step%20==0 and step>10:
            video_writer2.make_video(outvid=os.path.join('./','step'+str(step).zfill(3)+'_'+video_name), fps=30)

        step += 1
    os.makedirs('./qualitative_evaluation_short_clamp/method_3/target_0/',exist_ok=True)
    result_path = os.path.join('./qualitative_evaluation_short_clamp/method_3/target_0/',video_name)
    video_writer.make_video(outvid=result_path,fps=30)



def main():
    target_dir = './qualitative_evaluation_short_clamp/method_0/target_0/'
    filelist = os.listdir(target_dir)
    filelist.sort()
    target_path_list =[]
    for item in filelist:
        if item.endswith('.mp4'):
            target_path_list.append(os.path.join(target_dir,item))

    #process_video('./qualitative_evaluation_short_clamp/method_0/target_0/yinfei_result__compose.mp4')
    process_video('./qualitative_evaluation_short_clamp/method_0/target_0/ichao_result__compose.mp4')



if __name__ == '__main__':
    main()
