'''
	-The given code extracts all the frames for the entire dataset and saves these frames in the folder of the video clips.
	-Kindly have ffmpeg (https://www.ffmpeg.org/) (all credits) in order to successfully execute this script.
	-The script must in the a same directory as the Dataset Folder.
'''

import os
import subprocess


datasetFolder = 'DataSetSmall/'
dataset = os.listdir(datasetFolder)

def split_video(video_file, image_name_prefix, destination_path):
    return subprocess.check_output('ffmpeg -i "' + destination_path+video_file + '" ' + image_name_prefix + '%d.jpg -hide_banner', shell=True, cwd=destination_path)

emptyClips = []

for ttv in dataset:
    users = os.listdir(datasetFolder+ttv+'/')
    for user in users:
        currUser = os.listdir(datasetFolder+ttv+'/'+user+'/')
        for extract in currUser:
            contents = os.listdir(datasetFolder+ttv+'/'+user+'/'+extract+'/')
            if len(contents) !=0:
                clip = contents[0]
                print (clip[:-4])
                path = os.path.abspath('.')+ '/' + datasetFolder+ttv+'/'+user+'/'+extract+'/'
                split_video(clip, clip[:-4], path)

                #os.remove(datasetFolder+ttv+'/'+user+'/'+extract+'/' + clip)
            else:
                emptyClips.append(extract)

print ("================================================================================\n")
print ("Frame Extraction Successful")
print ("The following Folders contained no Clips:")
print(emptyClips)