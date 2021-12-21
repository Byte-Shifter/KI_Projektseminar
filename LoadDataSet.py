import os
import subprocess
import cv2
import csv

def loadDataSet():

    '''
    trainlabels = []
    trainClips = []
    testlables = []
    testClips = []
    '''
    Lables = [[],[]]
    Folders = ["Test","Train"]
    dataset = [[],[]]

    i_train_test = 0
    for folder in Folders:
        with open(folder + 'Labels.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                userfolder = row[0][:6]
                clipfolder = row[0][:10]
                images = os.listdir('DataSetSmall_Pics' + '/' + folder + '/' + userfolder + '/' + clipfolder + '/')
                #images.pop(0)    #remove the .avi file from list
                size = len(images)
                '''
                stepsize = size//10     #only take 10 imagages from each video
                for j in range(0,size,stepsize):
                    img = cv2.imread('DataSet' + '/' + folder + '/' + userfolder + '/' + clipfolder + '/'+ images[j])                    
                    dataset[i_train_test].append(img);
                '''
                for j in range(0, size):
                    img = cv2.imread('DataSet' + '/' + folder + '/' + userfolder + '/' + clipfolder + '/'+ images[j])                    
                    dataset[i_train_test].append(img);

                #Each Label added 10 times
                for j in range(0,10):
                    Lables[i_train_test].append(int(row[1]))

            i_train_test += 1


    


    return dataset[0] , dataset[1], Lables[0], Lables[1]
