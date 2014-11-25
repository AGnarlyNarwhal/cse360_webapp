<h1> README </h1>

To run this project, first you need to install python. 
If you're using a linux distrobution, python should already be installed. 
You can check this by running 'python' in bash. 
Otherwise, for Windows and Mac, go to the python website, http://www.python.org/download/, and download/install it. 

In Linux, check that pip is installed by typing 'pip' into the terminal. 
If the terminal complains that it doesn't know the command, check that pip is in your system's path. 
Otherwise, go to pip's website, http://pip.readthedocs.org/en/latest/installing.html#install-pip, and install it.
The procedure is the same for Windows and Mac. 

Next, you'll want to install virtualenv, django, and pillow (for handling pictures). 
In command prompt, or mac's terminal, run: <br>
pip install virtualenv

Then go to (or create) a directory where you'd like to install the project. 
run ' virtualenv "project_name" ' in that directory to create a virtual environment so you don't have to mess 
with your current system configuration, as well as to give you a sterile starting environment. 

Then go to 'project_name'/bin/scripts and run 'activate' to start the virtual environment so you can install the neccessary packages into it. If you have issues running virtualenv, you can check their documentation at: <br> 

http://virtualenv.readthedocs.org/en/latest/virtualenv.html#installation

After running activate you should see '(project_name)' before your prompt in bash/cmd/terminal. 
You can deactivate the virtual environment at any time by typing 'deactivate' into the terminal/cmd. 
Once you've installed and activated virtualenv, install the below packages with pip. 

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
Run the django server with: 

python manage.py runserver 

And the server should start. 

The homepage of the project is 'localhost:8000/home/'.

<h1> Servers and Proxy Setup, Functional and Load Testing </h1> 
Once you have the project setup and running by following the instructions in the previous section, you are ready to put it into production and test it. 
The menagerie of programs you'll need for this are: <br>
gunicorn <br>
nginx <br>
django_nose<br>
coverage <br>
ab (Apache Benchmark) <br>
sqlite3 (comes with django) <br>
firefox <br>
selenium<br>

You can install these programs via these commands in bash: <br>
```
pip install gunicorn 
sudo apt-get install nginx 
pip install django_nose
pip install coverage
sudo apt-get install apache2-utils (for ab)
```
sqlite3 doesn't need installation if you've already installed django <br>

These programs are a straight forward download from the internet:<br>
download firefox from the mozilla homepage <br>
download selenium (a firefox addon) from the selenium homepage <br>

Once you've installed them, you'll need to add django_nose to the 'INSTALLED_APPS' section in django's settings. <br>
To run reports using coverage, you can use coverage run manage.py test (with additional modules appended to the end)<br>
django_nose will make sure they output in a nice concise manner. 
All of the unit tests for the project's apps and views have been defined each app's respective folder, in tests.py<br> 

To run the functional tests, you can run the django debugging server and open 'Selenium_tests' folder to find the testing suite. They run in firefox, using the Selenium IDE addon. 

Before you run the tests though, you might want to set up nginx and gunicorn so you can run in a production environment. To do that, you'll need to change a few of nginx's settings. 

<a href="http://www.apreche.net/complete-single-server-django-stack-tutorial/">This</a> link will tell you the specifics of where and now to change the nginx default settings to work for any django configuration you want it to. For this project however, we'll just give you the code that works. 

First, you'll need to run these commands to set nginx up for our specific configuration.
```
# remove the default symbolic link
$ sudo rm /etc/nginx/sites-enabled/default

# create a new blank config, and make a symlink to it
$ sudo touch /etc/nginx/sites-available/cse360_webapp
$ cd /etc/nginx/sites-enabled
$ sudo ln -s ../sites-available/cse360_webapp

# edit the nginx configuration file
$ vim /etc/nginx/sites-available/cse360_webapp
```
In that last part, you'll put the text below into your configuraton file. We can't just give you the file since you won't have write permissions in that directory, and you'll have to create the file yourself to edit it, which mean's you'll be copying and pasting anyway. The only thing you need to change is the directory to the project before the 'root' variable, which will be unique to your system. 

```
# define an upstream server named gunicorn on localhost port 8000
upstream gunicorn {
    server localhost:8000;
}

# make an nginx server
server {
    # listen on port 80
    listen 80;

    # for requests to these domains
    server_name localhost;

    # look in this directory for files to serve
    root <Path to wherever you stored the django project>;

    # keep logs in these files
    access_log /var/log/nginx/cse360_webapp.access.log;
    error_log /var/log/nginx/cse360_webapp.error.log;

    # You need this to allow users to upload large files
    # See http://wiki.nginx.org/HttpCoreModule#client_max_body_size
    # I'm not sure where it goes, so I put it in twice. It works.
    client_max_body_size 0;

    # THIS IS THE IMPORTANT LINE
    # this tries to serve a static file at the requested url
    # if no static file is found, it passes the url to gunicorn
    try_files $uri @gunicorn;

    # define rules for gunicorn
    location @gunicorn {
        # repeated just in case
        client_max_body_size 0;

        # proxy to the gunicorn upstream defined above
        proxy_pass http://gunicorn;

        # makes sure the URLs don't actually say http://gunicorn 
        proxy_redirect off;

        # If gunicorn takes > 5 minutes to respond, give up
        # Feel free to change the time on this
        proxy_read_timeout 5m;

        # make sure these HTTP headers are set properly
        proxy_set_header Host            $host;
        proxy_set_header X-Real-IP       $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
``` 

<h2> And then that's it! </h2> 
The project is set up in production. Just make sure that you change Debug=True to False in django's settings. 
You can run and build tests to your hearts content. And should you feel like adding more servers or databases, it's childs play to just add a few lines to the nginx configuration file. 

To start nginx and gunicorn, make sure your in the same directory as django's manage.py file, then run: 
```
sudo service nginx start
gunicorn cse360_webapp.wsgi
```
To close out, just Control+C in the terminal to quit gunicorn, and then: 
```
sudo service nginx stop
```

To run the class standard load test just run: 
```
ab -n 100000 -c 50 http://localhost/home/ #or whatever other project url you want to run
```

The -n denotes the number of requests (users), the -c is for the number of concurrent requests. 
After running Apache Benchmark will print out a nifty report for you on the server's performance and stats. 

We chose to run it on http://localhost/accounts/login.html/ since that authentication and form valitdation was the most server intensive view to load. Our results are in the files above, called 'loadtest_test0.txt'. We even make a dope little graph, it's easy to spot since it's the only .png file in the project. 

Thanks for looking at our project, we hope you enjoyed our work as much as we did. 



