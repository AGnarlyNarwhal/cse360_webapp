To run this project, first you need to install python. 
If you're using a linux distrobution, python should already be installed. 
You can check this by running 'python' in bash. 
Otherwise, for Windows and Mac, go to the python website, http://www.python.org/download/, and download/install it. 

In Linux, check that pip is installed by typing 'pip' into the terminal. 
If the terminal complains that it doesn't know the command, check that pip is in your system's path. 
Otherwise, go to pip's website, http://pip.readthedocs.org/en/latest/installing.html#install-pip, and install it.
The procedure is the same for Windows and Mac. 

Next, you'll want to install virtualenv, django, and pillow (for handling pictures). 
In command prompt, or mac's terminal, run: 
pip install virtualenv

Then go to (or create) a directory where you'd like to install the project. 
run ' virtualenv "project_name" ' in that directory to create a virtual environment so you don't have to mess 
with your current system configuration, as well as to give you a sterile starting environment. 

Then go to 'project_name'/scripts and run 'activate' to start the virtual environment so you can install the neccessary packages into it. 
After running activate you should see '(project_name)' before your prompt in bash/cmd/terminal. 
You can deactivate the virtual environment at any time by typing 'deactivate' into the terminal/cmd. 
Once you've done this, install the below packages with pip. 

pip install django<br> 
pip install pillow

Note: To get pillow to install in virtualenv you need to make sure you have the 
python dev packages installed so you have the proper headers. 

In linux: <br>
sudo apt-get install python-dev <br>
sudo apt-get install python3.4-dev <br>

For Windows/Mac: 
These should already be installed, but you can get them from the package website. 

For problems with installation of these packages, or enabling pip, please check the pip or respective software's documentation. 
Once these have installed, you should be good to go. Just copy the projects files/directories into your 'project_name' directory. 
Then cd your way into the directory containing manage.py. 
Then run the django server with: 

python manage.py runserver 

And the server should start. 

The homepage of the project is 'localhost:8000/home/'.
