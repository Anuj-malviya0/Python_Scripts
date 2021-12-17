import os
#input the project name
project=input('Enter Project Name ')
#if user needs a seperate Environment
env=input('Do you want Saperate Environment Y/N ?')
#getting the current working directory
path = os.getcwd()
#making the project directory
os.mkdir(path+'/'+project)
#changing the directory to newly created directory
os.chdir(path+'/'+project)
#creatinga virtual env if needed 
if env.lower()=='y':
	os.system('python -m venv '+project+'Env')
#getting the new path
path2= os.getcwd()
#creating the new sub directories for beter management
os.mkdir(path2+'/source')
os.mkdir(path2+'/resources')
os.mkdir(path2+'/tests')
