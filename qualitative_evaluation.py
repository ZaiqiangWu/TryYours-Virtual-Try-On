import os


def main():
    target_dir = './target_garments'
    filelist = os.listdir(target_dir)
    filelist.sort()
    target_path_list =[]
    for item in filelist:
        if item.endswith('.jpg') or item.endswith('.png'):
            target_path_list.append(os.path.join(target_dir,item))
    input_dir = './input_images'
    filelist = os.listdir(input_dir)
    filelist.sort()
    input_path_list = []
    for item in filelist:
        if item.endswith('.jpg') or item.endswith('.png'):
            input_path_list.append(os.path.join(input_dir, item))

    result_dir = './results'
    os.makedirs(result_dir,exist_ok=True)

    for garment in target_path_list:
        for person in input_path_list:
            garment_name = os.path.basename(garment).split('.')[0]
            person_name = os.path.basename(person).split('.')[0]
            os.system('cp '+person+' ./static/origin_web.jpg')
            os.system('cp ' + garment + ' ./static/cloth_web.jpg')
            os.system('python main.py')
            result_name = person_name+'_'+garment_name+'.jpg'
            os.system('mv ./static/finalimg.png '+os.path.join(result_dir,result_name))


if __name__ == '__main__':
    main()
