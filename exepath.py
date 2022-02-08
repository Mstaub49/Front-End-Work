import psutil

currentPIDs=psutil.pids()
currentPIDs.remove(0)
print(currentPIDs)
for proc in currentPIDs:
 

    try:
        print(psutil.Process(proc).exe())

    except:
        print('undeterminable path')

   
 
