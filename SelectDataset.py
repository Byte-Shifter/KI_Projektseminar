import csv
from shutil import copyfile
import os
from pathlib import Path


labels = ['Boredom','Engagement','Confusion','Frustration']

def FilterDataset(file):
    SelectedClips = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = 0
        for row in csv_reader:
            #print(row)
            if i != 0:
                row_int = [int(row[1]),int(row[2]),int(row[3]),int(row[4])]

                #Clips with only 1 value x>0
                '''
                for j in range(0,4):
                    if row_int[j] > 0:
                        #test = [row_int[j], row_int[(j+1)%4] , row_int[(j+2)%4], row_int[(j+3)%4]]
                        if row_int[(j+1)%4] == 0 and row_int[(j+2)%4] == 0 and row_int[(j+3)%4] == 0:
                            newClip = [i+1, row[0], labels[j], row_int[j]]
                            SelectedClips.append(newClip)
                        break
                '''
                
                # clips where engagment is not the highest value
                '''
                if row_int[1] < max(row_int):
                    newClip = [i+1, row[0], row_int[0],row_int[1],row_int[2],row_int[3]]
                    SelectedClips.append(newClip)
                '''
                
                # clips with engagement = 0
                '''
                if row_int[1] == 0:
                    newClip = [i+1, row[0], row_int[0],row_int[1],row_int[2],row_int[3]]
                    SelectedClips.append(newClip)
                '''

                # clips with single highest value and it's not engagment
                m = max(row_int)
                j = row_int.index(m)
                if j != 1 and row_int[(j+1)%4] < m and row_int[(j+2)%4] < m and row_int[(j+3)%4] < m:
                    newClip = [i+1, row[0], row_int[0],row_int[1],row_int[2],row_int[3]]
                    SelectedClips.append(newClip)

            i += 1

    with open('FilteredClips.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerows(SelectedClips)
    
    return

def AssignSingleCategory(file):
    NewValueClips = []
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            row_int = [int(row[2]),int(row[3]),int(row[4]),int(row[5])]
            category = row_int.index(max(row_int))
            clip = [row[1], category]
            NewValueClips.append(clip)
    with open('SingleCatLabels.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerows(NewValueClips)
    return

def CopyVideoFiles(type):
    #copyfile('D:/Documents/TU_Freiberg/Projektseminar_KI/PythonCode/DataSet/1100021038.avi', 'D:/Documents/TU_Freiberg/Projektseminar_KI/PythonCode/DataSet/yo/1100021038.avi')
    #Path('DataSet/yo/asf').mkdir(exist_ok=True)
    
    datasetdir_src = r'C:\Users\Christoph Plobner\Desktop\DAiSEE\DataSet'
    datasetdir_dest = r'DataSetSmall/'
    if type == 'train':
        datasetdir_src = r'C:\Users\Christoph Plobner\Desktop\DAiSEE\DataSet\Train'
        datasetdir_dest = r'DataSetSmall\Train'
        file = 'Trainlabels.csv'
    elif type == 'test':
        datasetdir_src = r'C:\Users\Christoph Plobner\Desktop\DAiSEE\DataSet\Test'
        datasetdir_dest = r'DataSetSmall\Test'
        file = 'Testlabels.csv'
    else:
        raise ValueError('Correct argument for CopyVideoFiles is "train" or "test"')

    Clips = []
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            Clips.append(row)
    
    i = 1
    clipAmount = len(Clips)
    for clip in Clips:
        print('Copy File {0} of {1}'.format(i,clipAmount))
        userfolder = clip[0][:6]
        clipfolder = clip[0][:10]
        clip_src = datasetdir_src + '/' + userfolder + '/' + clipfolder + '/' + clip[0]
        clip_dest = datasetdir_dest  + '/' + userfolder + '/' + clipfolder + '/' + clip[0]

        Path(datasetdir_dest + '/' + userfolder).mkdir(exist_ok=True)
        Path(datasetdir_dest + '/' + userfolder + '/' + clipfolder).mkdir(exist_ok=True)

        copyfile(clip_src, clip_dest)
        i +=1    
    
    print('Copy Files completed!')

def DeleteFrames():
    datasetFolder = 'DataSetSmall/'
    dataset = os.listdir(datasetFolder)
    for ttv in dataset:
        users = os.listdir(datasetFolder+ttv+'/')
        for user in users:
            currUser = os.listdir(datasetFolder+ttv+'/'+user+'/')
            for extract in currUser:
                contents = os.listdir(datasetFolder+ttv+'/'+user+'/'+extract+'/')
                if len(contents) > 10:
                    for image in contents:
                        imageNoXT = image.split('.')[0]
                        imageNumber = 0
                        if len(extract) == 9:
                            imageNumber = int(imageNoXT[9:])
                        else:
                            imageNumber = int(imageNoXT[10:])
                        if imageNumber%30 != 1:
                            os.remove(datasetFolder+ttv+'/'+user+'/'+extract+'/' + image)

CopyVideoFiles('test')
#FilterDataset('TestLabels_original.csv')
#AssignSingleCategory('FilteredClips.csv')
#DeleteFrames()