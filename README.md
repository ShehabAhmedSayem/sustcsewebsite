# SUST CSE WEBSITE

This is the website of CSE department of SUST(Shahjalal University of Science and Technology). We use django as the backend framework.

## How to run this project

### For Ubuntu

First install virtualenv if you don't have it using the command below
(This project is in python3 so check the version of python and according to that you may use pip/pip3)

```
$ pip install virtualenv
```

Then make a project folder and navigate to that

```
$ cd my_project_folder
```

Then create a virtual environment

```
$ virtualenv my_env
```

After that activate your virtualenv with the following command

```
$ source my_env/bin/activate
```

Now clone this project to your project folder

```
(my_env)$ git clone https://github.com/ShehabAhmedSayem/sustcsewebsite.git
```

Navigate to the cloned folder 

```
(my_env)$ cd sustcsewebsite
```

Now use the command below to install all the requirements

```
(my_env)$ pip install -r requirements.txt
```

Run the project 

```
(my_env)$ python3 manage.py runserver
```

The address of django localhost is: http://127.0.0.1:8000/
Use this address to see the website.
