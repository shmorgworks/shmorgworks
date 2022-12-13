import sys
import os

#for line in sys.stdin:
 #   sys.stdout.write(line)
 #   print('hello')

os.system('cp -R /var/www/html/static/* ~/Documents/shmorgworks/shmorgworks')
os.system('cd ~/Documents/shmorgworks/shmorgworks')
#making sure we are deploying to the deployment branch
os.system('git checkout deployment')
#add and push all the changes. Git Cli should cache the login information for 
#shmorgworks github
os.system('git add -A')
os.system('git commit -m "new static files generated"')
os.system('git push')

print('operation completed')
#os.system('your command')
