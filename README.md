# BinaryAPI
REST service for storing binary data. Test task for employment. 


Technologies:
	- Flask
	- Python 3.6
	- Dropbox API

Application should be started by Makefile. The only requirement - ([PIP](https://pip.pypa.io/en/stable/installing/)) and ([virtualenv](https://virtualenv.pypa.io/en/latest/installation/)) must be installed on your workstation.


### Install dependencies:
'cd' to the application root folder and run 'make deps' command. This will create venv
```
$ cd ~/path/to/app_root
~/path/to/app_root$ make deps
```


### Starting application:
Then you can start project by executing next 'make' command:
```
~/path/to/app_root$ make run
```


### Start unit tests:
I made some simple unit tests, which are covering mostly all application logic. You can start them like this:
```
~/path/to/app_root$ make test
```
