# python-django-basictestcase

### External Dependency
Virtualenv
Chrome WebDriver

### Version
chromedriver-installer==0.0.4                                                                                         
coverage==4.0.3                                                                                                       
Django==1.8                                                                                                           
pkg-resources==0.0.0                                                                                                  
selenium==2.53.6                                                                                                      
splinter==0.7.4   

### Installation
Obs.: If you already have virutalenv and python-pip you can jump to step 2
#### 1 - Install virtualenv if you dont have it
```sh
$ sudo apt-get install virtualenv
```
```
#### 2 - Create and Activate your Virtual Machine (virtualenv)
```sh
$ virtualenv vm
$ vm source/bin/activate
```
#### 3 - Clone the project to your folder and enter on it
```sh
$ git clone https://github.com/Diegow3b/python-django-basictestcase.git
$ cd projeto-teste
```
#### 4 - Install the requirements (Will install django and other internal dependencies)
```sh
$ pip install -r requirements.txt
```
#### 5 - Run the test code
```sh
$ python manage.py test
```
#### 6 - Coverage
```sh
$ ./run_coverage.sh
```

## Further help

To get more help ask me my github or email.e
