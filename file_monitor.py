import sys
import os

#for line in sys.stdin:
 #   sys.stdout.write(line)
 #   print('hello')

#if there is an output piped from fswatch into this program, push the static
#folder to the github account, else, do nothing. The output will become the 
#input to this program through sys.stdin

while True:
	if (sys.stdin):

	     #copy the static files 
	     os.system('cp -R /var/www/html/static/* ~/Documents/shmorgworks/shmorgworks')
	     os.system('cd ~/Documents/shmorgworks/shmorgworks')
	     #making sure we are deploying to the deployment branch
	     os.system('git checkout deployment')
	     #add and push all the changes. Git Cli should cache the login information for 
	     #shmorgworks github. downloaded as "gh".
	     os.system('git add -A')
	     os.system('git commit -m "new static files generated"')
	     os.system('git push')

	     #verifying changes occured
	     print('operation completed')
	else:
		continue
#os.system('your command')
