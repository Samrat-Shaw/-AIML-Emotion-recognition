# -AIML-Emotion-recognition

INTRODUCTION
 
Emotion recognition is a fascinating application of computer vision and machine learning techniques. It involves the development of algorithms and models to analyze facial expressions like anger,fear,disgust,captured through a camera feed in real-time or from images or videos. The goal is to accurately identify and classify the emotional state of individuals based on their facial expressions.

Libraries Used

1)	Tensorflow- version 2.3.0
2)	Keras-version 2.4.3
3)	Opencv  
4)	Os

Requirements For Execution Of The Code
1.	Visual studio 
2.	Make sure your using python version 3.8.5
3.	And import the necessary libraries as mentioned earlier using pip command in command prompt
4.	And  make sure that camera  is working properly

 Steps to execute
In Visual Studio, you can create virtual environments for Python projects using the Python Environments window. Here's how you can do it:

1.Open Visual Studio on your system.
2.Create a Virtual Environment:
*	Make sure u create a folder in any of your directory  and name the folder
*	Open the folder in visual studio
*	To create a new virtual environment. Press crtl+shift+p
*	From the drop down menu  select python:create environment option 
*	Then select environment type (i.e venv)
*	Then select on the python interpreter version 3.8.5 from the drop down menu or else select the python interpreter from the path where the interpreter is located 
*	Then run windows powershell as run as administrator and type command “Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass “and press “a or A”
*	 Then go to visual studio and to Activate the Virtual Environment select new terminal from the “Terminal” option  and type“.venv\Scripts\activate”
*	So your terminal should show “(.venv) path\to\your\virtual\environment folder ”

3.	Then type in the command prompt pip install opencv-python ,pip install tensorflow ==2.3.0 ,pip install keras ==2.4.3 one by one to install packages in your virtual environment
4.	Then download the zip file from githublink Samrat-Shaw/-AIML-Emotion-recognition (github.com)
5.	Extract the files at the folder you  have created virtual environment
6.	Then run the test.py for execution by typing in the virtual environment     terminal “python test.py”
