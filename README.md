[![Build Status](https://travis-ci.org/albeeralkhawri/Albeer.Cars.Sale.svg?branch=master)](https://travis-ci.org/albeeralkhawri/Albeer.Cars.Sale)

![picture](https://www.up-00.com/i/00157/4bs6d7i7vw51.png)
***


##### *Full Stack project :  Frameworks with Django Milestone Project*
###### This project is designed in a simple and user-friendly way enabling the customer to browse and purchase in a very easy way
***

# UX

##### My goal in this project is clear: selling cars, earning money from them, enabling the user to see cars and details for each car, searching through the car model, adding the car to the shopping basket, and then paying the amount, and no user can pay the amount except that he logs in or registers as a new user.

###### This project is designed in a very easy way so that the site can be used by all different societal groups and all ages.


#### <p align="center">This is the sitemap</p>
<p align="center">
<img src="https://www.up-00.com/i/00158/fhr981rx2gzj.png"></p>

#### <p align="center">These are three of the project designs, you can see the rest of the designs in <a href="https://github.com/albeeralkhawri/Albeer.Cars.Sale/tree/master/Project%20Design">Project Design</a></p>
# <p align="center">Cars Page
  <img src="https://www.up-00.com/i/00157/n77p4xdk5b08.png"></p>
  ***
#  <p align="center">Cars Details Page
  <img src="https://www.up-00.com/i/00157/cc8n6izqxg53.png"></p>
  ***
#  <p align="center">Login Page
  <img src="https://www.up-00.com/i/00157/pal6svpdi42p.png"></p>

  ***

  # Database Schema Design
#### <p align="center"> This diagram shows how to chart database </p>

 <p align="center"> <img src="https://www.up-00.com/i/00157/ld4kmn2w1a36.png"></p>

 ***

  # Demo

  ##### Direct view here <a href="https://albeer-cars-sale.herokuapp.com/">Albeer-Cars-Sale</a>

  <img src="https://www.up-00.com/i/00157/tw658cjm52cz.gif">

  ***

# Features

#### This project is distinguished from the rest of the other projects by its simple design and easy to use. I worked on this project to be simple design to avoid confusing the user

## Users can :

- Browse the cars available on the site with the name of the manufacturer, model, image and price of the car
- See detailing of the car when clicking more details
- Search for the car by writing the model of the car in the search field
- Add cars to the cart by entering a certain number, then press Add
- Registering, logging in, logging out, viewing the user's file, and viewing the material available in the cart for each user
- Zoom in on photos by clicking on them
- Items in the cart can be deleted
- The user can only pay if he is registered or logged in
- You can only register if it is within the conditions provided in the registration section, which is the username with number or the like, email and password, and confirm the password
- If you forget your password, you can reset it via Forgot my password, enter an email, and then receive an email to reset the password
- Also, the final price can be seen in the cart and payment also by entering the required information
***

# Technologies Used

- HTML 5
- CSS 3
- JavaScript/ jQuery
- Python 3
- Django
- Font Awesome
- Google Fonts
- Materialize
- bootstrap
- bootswatch
- Stripe
- Postgres/ Sqlite3

***
# Testing

- The project code has been checked by automatic inspection
The tests.py file was run and it was error free as shown in the pictures below. It appears here that theDatabase URL not found. I intentionally stopped it to avoid a mistake.
<img src="https://www.up-00.com/i/00157/1l6uxcmhwvu5.png">

- The html code was checked manually I tried to search for a special validator html template but I did not find the natural validator does not work on the html template but when i was check manually  the html template  didn't found any error or problem

- I checked the CSS code manually and through the CSS checker I did not get any errors or problems and the picture below shows that
<img src="https://www.up-00.com/i/00157/w5e7jstoi6z0.png">

- The Python code was verified manually and by tests.py and also by reviewing the Inspect I didn't see any errors and the project works perfectly.
- The JavaScript script was revised manually in stripe.js. I didn't see any problem and the code works perfectly.
- The site has been tested with different devices to ensure the site works perfectly and is compatible with all devices for devices that have been tested below
   - My laptop dell 
   - My phone iphone 8 plus
   - My tablet Samsung Tab E
   - my friends Phones Samsung Note 8 and samsung Note 9 and iphone 11

###### The initiation was working perfectly and did not encounter any errors

- The register was test in this way below
 - I created multiple accounts and made sure they work
 - After creating several accounts, I checked the admin panel to ensure that it is there in the Users section
 - I confirmed the user’s demands about making the account, which is a name with a number or similar to that, email and password, and confirm the password, should be user do that to make register
 - When register, the user can view the profile
 - When register, the Navbar menu will be change log in to log out and register to profile
 - When register, the user can see the checkout and payment information
 - When register, the user can log in agen if logged out earlier
 - I tried to submit an empty form and got an error message
 - I tried to submit an incomplete form and got an error message
 - I tried to register with a username that already exists

- The Log in was test in this way below
  - When log in, the Navbar menu will be change log in to log out and register to profile
  - When log in, the user can view the profile
  - When log in, the user can see the checkout and payment information
  - I tried to log in with an incorrect username or password says Your username or password are incorrect
  - I tried to submit an empty form and got an error message

- When Log out was test in this way below
 - When log out, the Navbar menu will be change log out to log in and profile to register
 - When log out, the user can't view the profile
 - When log out, the user can't see the checkout and payment information
 - When log out, the user back to cars page

- Password reset
 - I tried to Click forgot my password on the login page
 <img src="https://www.up-00.com/i/00157/vqjobcx7dls4.png">
 - I entered the account email address
 <img src="https://www.up-00.com/i/00157/macdemtj483u.png"> 
 <img src="https://www.up-00.com/i/00157/gzym25r1tmak.png">
 <img src="https://www.up-00.com/i/00157/zak5s30ncv9c.png">
 - Then I received an email from king.alber93@gmail.com to my private email address
 <img src="https://www.up-00.com/i/00157/6i2aflkvh8ct.png">
 <img src="https://www.up-00.com/i/00157/fsis4e1x3ghd.png">
 - The information received by e-mail has been verified as correct information from which the link was followed
 <img src="https://www.up-00.com/i/00157/t1rcmn6gbtse.png">
 - Then enter a new password and re-enter it again for confirmation, and then click on Reset
 <img src="https://www.up-00.com/i/00157/3d1jn5xhcsut.png">
 - I tried to use the link again after setting the password, but it does not work, it only works once, and this picture is below in which shows this
 <img src="https://www.up-00.com/i/00157/lwg0y6lko0k7.png">

 - Cart test when add a cars from cars page can see the cars in cart page if the user didn't write a number can't add items to cart page, and this pictures are below in which shows this
 <p align="center">
 <img width="200" height="200" src="https://www.up-00.com/i/00157/58q0k18yqhjn.png">
 <img width="200" height="200" src="https://www.up-00.com/i/00157/u2m1yhcflcvi.png">
 <img width="200" height="200" src="https://www.up-00.com/i/00157/0tndyxzzjiu4.png">
</p>

- checkout test when the user add the details of payment and press a button of payment and the details are right will be see You have successfully paid
 also, it was confirmed that an empty form or an incomplete form was not sent. This was checked and the user was unable to do this
 and also the admin can see order details receive to me this pictures are below in which shows this
<p align="center">
 <img src="https://www.up-00.com/i/00157/rb4nf8c771pl.png">
 <img src="https://www.up-00.com/i/00157/vs66ye301j6w.png">
 <img src="https://www.up-00.com/i/00157/vbcdfqjhovyc.png">
</p>

- Also, the automatic checking of the whole project was done by Travis, and a Travis tag was added at the beginning of the README file. These pictures below explain that
<p align="center">
 <img src="https://www.up-00.com/i/00157/qsrk7hbhmet1.png">
 <img src="https://www.up-00.com/i/00157/8py2vmkdj97s.png">
</p>

***
# Deployment

- The project was written by gitpod and a storage was created by github and the code was push to <a href="https://github.com/albeeralkhawri/Albeer.Cars.Sale">here</a>
- The project has been published and hosted by heroku <a href="https://albeer-cars-sale.herokuapp.com/">here</a>

### Take the next steps for publication:
- Create file requirements.text has the necessary dependencies to run the project
- Create env.py file containing security variants and add it to .gitignore to avoid posting it in github
- Create a new repository in github
- Created a Heroku app with a albeer-cars-sale name
- Connected Heroku app  with github repository and enabled automatic deploys
- Adjust Postgres database settings with project
- I stored the variables in env.py and put them in Reveal Config Vars to enable heroku to read the variables
- Run python3 manage.py makemigrations and python3 manage.py migrate after adding the data link
- Added the albeer-cars-sale.herokuapp.com to ALLOWED_HOSTS in settings.py file
- Add the Procfile required by Heroku

### Repository site link (https://github.com/albeeralkhawri/Albeer.Cars.Sale)
### The live display link (https://albeer-cars-sale.herokuapp.com/)

## The step of local Deployment

- Project cloning from <a herf="https://github.com/albeeralkhawri/Albeer.Cars.Sale">here</a>
- Create a new workspace and add a project file to workspace
- Install python3 on your workspace
- Install requirements.txt, pip3 install -r requirements.txt
- Install the required dependencies
- Add default variables like secret code and others to a file env.py
- Set the SQLite database to be used for development mode and the PostgreSQL database for deployment
- Run python3 manage.py makemigrations and python3 manage.py migrate to make database
- For databaes start python3 manage.py migrate --run-syncdb 
- Use the following command to create a super user python3 manage.py createsuperuser
- Use the following command to run the project python3 manage.py runserver

# Credits

### Content

 - I designed the site by <a href="https://balsamiq.com/wireframes/desktop/">Balsamiq Mockups 3</a>
 - The site map by <a href="https://www.gloomaps.com/">GlooMaps</a>
 - The chart database <a href="https://dbdiagram.io/home">dbdiagram.io</a>

### Media

- Photos have been obtained from <a href="https://www.google.ie/imghp?hl=ar&tab=wi&authuser=0&ogbl">Google Images</a>
- The videos used in Gif Image are recorded through this program <a href="https://icecreamapps.com/Screen-Recorder/">Icecream Screen Recorder</a>
- Some images have been uploaded with a link through this site <a href="https://www.up-00.com/">UP00</a>
###### *<p align="center"> This is all that was used to make this project. I hope I do not forget anything </p>*
***


- My thanks and appreciation for all that helped me and support me in order to complete this project and thank also the support of teachers at the Code Institute
- I also thanked the Code Institute, from which I learned a lot, and this is the product of my work and Thanks Mentor helped me a lot