import os      #load the library module
directory='.'  #Set the variable directory to be the current directory
dir_size=0     #Set the size to 

fsizedicr={'Byte':1,'kilobyte':float(1)/1024,'megabyte':fload(1)/(1024*1024),'Gigabytes':float(1)/1024*1024*1024}

for(path, dir,files) in os.walk(directory): #walk through all the directories, for each iteration, os.walk returns the folders,subfolders and files in the dir.
   for file in files:
        filename=os.path.join(path,file)    #Get all the files
        dir_size+=os.path.getsize(filename) #Add the size of each file in the root dir to get the total size.
for key in fsizedicr:  #iterating through the dictonary
    print("Foler Size: " + str(round(fsizedicr[key]*dir_size,2))+ " " + key)
    round(4.2384,2)==>4.23
