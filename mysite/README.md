Instructions on deploying this on your local machine :     
    Clone this repository to your local directory    
    You should have installed and configured mysql on your local directory     
    create a database called student and import the sql file ( student.sql)     
    packages MySQL-pyton should be installed     
    Change mysql user name and password located at files mysqite/settings.py and dlscapp/views.py     
    Now just you have to run python manage.py runserver. ( manage.py should be inside mysite folder)    
    Your webserver on your local computer will be up and running     

Now you have cloned the repo and started working on it, make your changes ( html, python etc) , test those in your local machines and commit the code to git immedately.     
To commit the code :    
If it is a new file/folder added :    
    git add file/folder   
    git commit -m "message" file/folder 
    git push origin master    
If it is a modification to existing file    
    git commit -m "message" file
    git push origin master    

So by doing this we make sure that whoever clones or downloads this repo, should be able to deploy it with minimal changes.     

As of now we have deployed our project on amazon AWS EC2 instance. Databases have been configured.     
Link ( http://ec2-54-200-233-36.us-west-2.compute.amazonaws.com:8000/ ). There are some configurations left to make it server https traffic. Will work on that.     
We will run git pull and restart the server once a day. So that whatever changes we make will be reflected within a day.     

Lets stick to Django version 1.10.x from now on .     




