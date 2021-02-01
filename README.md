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
* Make sure to add your own 2 databases in "__init__.py" directory before running flask application.

## Built With

* [Python3.7](https://www.python.org/) -One of the most popular programming language
* [OpenCV(V2.0.0)](https://opencv.org/) - Open Source Computer Vision Library
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web application framework written in Python
* [SQLite](https://www.sqlite.org/index.html) -Used for designing and manipulating of database

## Author -  Aryan Bindal       
        
###Contacts:        

Gmail: aryanbindal2015@gmail.com                 
[Instagram](https://www.instagram.com/aryan__bindal/)          
[linkedin](https://www.linkedin.com/in/aryan-bindal-3077401ab)           
[Facebook](https://www.facebook.com/aryan.bindal.1604)    

##ScreenShots :)           

