# ANPR-Chroma
 Deployment of ANPR model using flask 

Flask is a web application framework written in Python.         
* I have deployed the project of LicensePlateDetector using Flask as an api. This is an easy and quick way to see your models in production.

### Number Plate Recognition System :

An application to recognise the number plate from a given image of a car and verify it from a local database. The application can be used for many purposes like suveillance,security checks etc. 

## Setup

1. Clone the repository
2. Create virtual env.             
   On windows you could do something like: py -m venv env            
   On macOS and Linux: python3 -m venv env           
   {{ Activate the virtual environment env }}
3. Install the needed modules using: pip install -r requirements.txt
4. Run run.py in ANPR_Chroma folder (Make sure Apache server is running)
5. Go to localhost:5000 to see your application in action. (Port 5000 has been configured in run.py)

Note: 
* File [run.py](ANPR_Chroma/run.py) is to run flask application, if you want to test main licence plate recognition program - check [product.py](ANPR_Chroma/flaskblog/product.py)
* Make sure to add your own 2 databases in "__init__.py" directory before running flask application, and update your database path [here](https://github.com/aryaniiit002/ANPR-Chroma/blob/fd89a6f62013caf711c62457cef2f7c8d60ae485/ANPR_Chroma/flaskblog/__init__.py#L14)           
  If you get any issues ask me [here](https://github.com/aryaniiit002/ANPR-Chroma/issues)             
* It may be possible that you would get a lot of errors even after installing requirements so don't give up and copy-paste your errors on ggogle you will definitely find your solutions there.

## Built With

* [Python3.7](https://www.python.org/) -One of the most popular programming language
* [OpenCV(V2.0.0)](https://opencv.org/) - Open Source Computer Vision Library
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web application framework written in Python
* [SQLite](https://www.sqlite.org/index.html) -Used for designing and manipulating of database

## Author -  [Aryan Bindal](https://github.com/aryaniiit002)          

### ScreenShots :)           

* Home Page             

![Home page](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/home.png)

* A little Description

![Description](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/description.png)

* If you try to login with unregistered account

![Login](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/login%20Unsuccesful.png)

* Registration of new checkPost  

![Sign up](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/New%20Login.png)

* Now login again

![Login](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/re-login.png)

* Home page after checkPost login

![Home after Login](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/home%20after%20login.png)

* You can see and update current CheckPost's account

![Account](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/Login%20account.png)

* It's time to upload your vehicle's image and if your vehicle is not registered it will look like this

![ANPR Online Demo](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/upload%20img.png)

* And if your vehicle is not registered a mail is send to higher authority                    
> Note: For Gmail services to work -               
> Write your google account's password [here](https://github.com/aryaniiit002/ANPR-Chroma/blob/fd89a6f62013caf711c62457cef2f7c8d60ae485/ANPR_Chroma/flaskblog/__init__.py#L22)      
> You have to turn off "2 step verification" and turn off "Less secure app access" from your google account settings

![Mail to Authority](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/not%20registered%20mail.png)

* now driver need to register the vehicle

![Registration](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/registration%20of%20vehicle.png)

* If registration is successfull then a mail is send to driver

![Mail to driver](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/mail%20to%20driver.png)

* Vehicle is registered now

![Vehicle registered](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/registered.png)

* When everything is done and CheckPost wants to logout

![Logout](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/logout.png)

* If you try to login an already registered account of CheckPost

![Login](https://github.com/aryaniiit002/ANPR-Chroma/blob/main/ScreenShots/already%20registered.png)
