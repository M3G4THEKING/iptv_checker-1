#github.com/vladlonov/iptv_checker
print("IPTV Checker by Lonov\n\n")
import threading,time,sys
try:
    import requests
except:
    print("Please install requests module!")
    sys.exit()
    
path=input("File (example: file.m3u) => ")
out=path+"_out.txt"

try:
    with open(path, 'r') as file_in:
        lines = file_in.read().splitlines()
except:
    print("File error or not found!")

file_out=open(out, "w")
#print(str(lines))

all = len(lines)
print(all)
worked=0
print("Scanning {} lists... Worked will write in {}".format(all,out))
time.sleep(5)
def check(i):
    global worked
    thisline=str(i)
    file_out.write(thisline+"\n")
    if thisline.startswith("#") == False:
    
        print("Checking "+thisline+"...")
        
        
        if "m3u8" not in thisline:
            if thisline.endswith("/") == False:
                thisline=thisline+".m3u8"
            else:
                thisline=thisline+"/index.m3u8"
        
            
        try:
            req=str(requests.get(thisline, timeout=(2,5)).status_code)
            if req == "200" or (req == "302"):
                print("OK. "+thisline)
                worked+=1
                #write here
                file_out.write(thisline+"\n")
        except:
            print("ERROR. "+thisline)   
            

for i in lines:
    threading.Thread(target=check,args=(i,)).start()

