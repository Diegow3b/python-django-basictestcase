# python-django-basictestcase

### External Dependency
Virtualenv
Python Pip
Chrome WebDriver

### Version
chromedriver-installer==0.0.4                                                                                         
coverage==4.0.3                                                                                                       
Django==1.8                                                                                                           
pkg-resources==0.0.0                                                                                                  
selenium==2.53.6                                                                                                      
splinter==0.7.4   

### Installation
Obs.: If you already have virutalenv and python-pip you can jump to step 3
#### 1 - Install virtualenv if you dont have it
```sh
$ sudo apt-get install virtualenv
```
#### 2 - Install python-pip
```sh
$ sudo apt-get update
$ sudo apt-get install python-pip
```
#### 3 - Create and Activate your Virtual Machine (virtualenv)
```sh
$ virtualenv vm
$ vm source/bin/activate
```
#### 4 - Clone the project to your folder and enter on it
```sh
$ git clone https://github.com/Diegow3b/python-django-basictestcase.git
$ cd projeto-teste
```
#### 5 - Install the requirements (Will install django and other internal dependencies)
```sh
$ pip install -r requirements.txt
```
#### 6 - Run the test code
```sh
$ python manage.py test
```
#### 7 - Coverage
```sh
$ ./run_coverage.sh
```

## Further help

To get more help ask me my github or email.e
