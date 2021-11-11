import os
import time
import shutil

pathToProj = os.getcwd()+"/work2/listProjects"
pathToUrlKey = os.getcwd()+"/work2/listUrlKey"
prePathWorkGit = "/tmp/workgit"

if os.path.exists(pathToProj) and os.path.exists(pathToUrlKey):
  readFileTmp = open(pathToUrlKey, 'r').readlines()
  keyS = readFileTmp.splitlines()[0].split("_:_")[0]
  urlS = readFileTmp.splitlines()[0].split("_:_")[1]
  readFileTmp = open(pathToProj, 'r').readlines()
  indexPrj = 0
  for i in readFileTmp:
#    if not i.splitlines()[0].endswith('.git'):
#      continue
    if os.path.exists(prePathWorkGit):
      shutil.rmtree(prePathWorkGit)
    os.system("git clone "+i.splitlines()[0]+" "+prePathWorkGit)
    if not os.path.exists(prePathWorkGit):
      print("error clone repo "+i.splitlines()[0])
      continue
    os.system("cd "+prePathWorkGit+"&&~/sonar-scanner-4.6.1.2450-linux/bin/sonar-scanner -Dsonar.projectKey=proj"+str(indexPrj)+" -Dsonar.sources=. -Dsonar.host.url="+urlS+" -Dsonar.login="+keyS)
    indexPrj += 1
os.system("df -h")
