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
    target_garment = './temporal_target_garments/first_garment.jpg'
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
        image=cv2.resize(image,(768,1024))
        input_image_list.append(image)
        count+=1
    step =0

    #input_image_list.reverse()
    n_frame = len(input_image_list)

    for img in input_image_list:
        t1 = time.perf_counter()
        cv2.imwrite("./static/origin_web.jpg", img)
        os.system('cp ' + target_garment + ' ./static/cloth_web.jpg')
        os.system('python main.py')
        result = cv2.imread('./static/finalimg.png')
        h, w, _ = img.shape
        zero_pad = np.zeros((h,w,3)).astype(np.uint8)
        print(img.shape)
        result = cv2.resize(result, (w,h))
        print(result.shape)
        #frame = np.concatenate([img,zero_pad,result],1)

        #frame2 = np.concatenate([img, result], 1)
        video_writer.append(result)


        t2 = time.perf_counter()

        print("elapsed time (s):", (t2 - t1))


        step += 1
    os.makedirs('./results/',exist_ok=True)
    result_path = os.path.join('./results/',video_name)
    video_writer.make_video(outvid=result_path,fps=30)



def main():


    process_video('./yinfei.mp4')
    #process_video('./qualitative_evaluation_short_clamp/method_0/target_0/ichao_result__compose.mp4')



if __name__ == '__main__':
    main()
