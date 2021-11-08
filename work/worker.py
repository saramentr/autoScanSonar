import os
import time
import shutil

pathGenGit = "/tmp/gengit"
prePathWorkGit = "/tmp/workgit"
pathToList = pathGenGit+"/work/listProjects"
repoToList = "https://github.com/saramentr/autoScanSonar.git"

if True:
  if os.path.exists(pathGenGit):
    shutil.rmtree(pathGenGit)
  os.system("git clone "+repoToList+" "+pathGenGit)
  if not os.path.exists(pathToList):
    if os.path.exists(prePathWorkGit):
      shutil.rmtree(prePathWorkGit)
  else:
    if not os.path.exists(prePathWorkGit):
      os.system("mkdir "+prePathWorkGit)
    listWorkLine = open(pathToList, 'r').readlines()
#file pathToList format
# prjkey_:_urlPort_:_prjlgn_:_organ_:_repo
    for i in listWorkLine:
      sepListTmp = i.splitlines()[0].split("_:_")
      if len(sepListTmp) != 5:
        print("error parsing line "+i)
        continue
      if os.path.exists(prePathWorkGit+"/"+sepListTmp[3]+"_"+sepListTmp[4]):
        continue
      os.system("git clone https://github.com/"+sepListTmp[3]+"/"+sepListTmp[4]+".git "+prePathWorkGit+"/"+sepListTmp[3]+"_"+sepListTmp[4])
      if not os.path.exists(prePathWorkGit+"/"+sepListTmp[3]+"_"+sepListTmp[4]):
        print("error clone repo https://github.com/"+sepListTmp[3]+"/"+sepListTmp[4]+".git ")
        continue
# fix not work without full path $PATH  user runner
      os.system("cd "+prePathWorkGit+"/"+sepListTmp[3]+"_"+sepListTmp[4]+"&&~/sonar-scanner-4.6.1.2450-linux/bin/sonar-scanner -Dsonar.projectKey="+sepListTmp[0]+" -Dsonar.sources=. -Dsonar.host.url="+sepListTmp[1] +" -Dsonar.login="+sepListTmp[2])
  os.system("df -h")
