CryptoTalk

![Responsive screenshot](https://renwar-p.github.io/cryptalk)

# The purpose with this project

Few subjects today can get people going like crypto. It´s something that almost everyone has an opinion about. Its a topic that many don´t really fully understand. It´s also a subject that people like or dislike for many different reasons. CryptoTalk is a blog for anyone interested in crypto. It´s a way for someone with a opinion on crypto to share that with others. 


Required technologies for this project:

- HTML, CSS, JavaScript, Python+Django
- Relational database (SQL)

A live version of this project can be found at this url: <>


# Table of Content

- [UX](#ux "UX")
  - [User Demographic](#user-demographic "User Demographic")
  - [User Goals](#user-goals "User goals")
  - [User Stories](#user-stories "User Stories")
- [Project Purpose](#project-purpose "Project Purpose")
  - [Design diagram](#design-diagram "Design diagram")
  - [Site Navigation](#site-navigation "Site Navigation")
- [Features](#features "Features")
  - [Existing Features](#existing-features "Existing Features")
    + [Navbar](#navbar-session "Navbar")
    + [Footer](#footer-session "Footer")
    + [Sign In](#sign-in "Sign In")
    + [Sign Up session](#signup-session "Sign Up session")
    - [Post session](#post-session "Post session")
    + [Edit session](#edit-session "Edit session")
    + [Comment session](#comment-session "Comment session")
    - [Delete session](#delete-session "Delete session")    
    - [Sign Out](#sign-out "Sign Out")
  - [Features Left to Implement](#features-left-to-implement "Features Left to Implement")

+ [Languages used](#languages-used "Languages used")
  - [Frameworks and libraries and tools](#frameworks-and-libraries-and-tools "Frameworks and libraries and tools")
  - [Installed packages](#installed-packages "Installed packages")
- [Testing](#testing "Testing")
  - [Bugs during development](#bugs-during-development "Bugs during development")
  - [Validator Testing](#validator-testing "Validator Testing")
  - [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
- [Deployment](#deployment "deployment")
- [Content](#content "Content")
- [Credits](#credits "Credits")



## UX

### User Demographic

This application is ment for:

- Everyone interested in crypto. 

### User Goals

To create a user friendly website that is appealing. To create a website for cryptoentusiasts to share the latest news and with that stay ahead of the curve.  

### User Stories

The following user stories has been implemented in the project. User Stories are based on two types of users, the admin and the user. More user stories will be implemented in future versions.

#### Admin

As a **site admin** I can **create, read, update and delete posts** so that **I can manage my blog content**

As a **site user/admin** I can **view the number of likes on each post** so that **I can see wich is the most polular or viral**

As a **admin** I can **create draft posts** so that **I can finish writing the content later.**

As a **admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**

As a **site user/admin** I can **view comments on a individual post** so that **I can read the conversation**


#### User

As a **site user** I can **view a paginated list of posts** so that **I can easily select a post to view**

As a **site user** I can **register an account** so that **I can comment and like**

As a **site user** I can **click on a post** so that **I can read the full text**

As a **site user** I can **leave comments on a post** so that **I can be involved in the conversation**

As a **site user** I can **like or unlike a post** so that **I can interact with the content**

As a **site user** I can **view a list of posts** so that **I can select one to read**

As a **site user** I can **create posts** so that **I can participate in the conversation**

As a **site user** I can **edit my posts** so that **having the flexibility to change the content**

As a **site user** I can **delete posts** so that **being able to delete unwanted posts**

As a **site user** I can **delete/edit posts** so that **only I can delete/edit my own posts**



### Project Purpose

From Code Institutes assessment guide:

In this project, you'll build a Full-Stack site based on business logic used to control a centrally-owned dataset. You will set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.

### Design diagram

The idea of behind CryptoTalk´s design is simplicity. My main focus here was to implement CRUD and to get the django elemnts working. 

![Wireframe1](static/images-readme/home-bals.png)
![Wireframe2](static/images-readme/signup-bals.png)
![Wireframe3](static/images-readme/signup-bals.png)

### Site navigation

![Site navigation](static/images-readme/SITE_NAVIGATION.png)


## Features

Cryptotalk consists of features avaliable for the site user and admin. 

### Existing Features

#### Home

The homepage contains the latest post and is the common redirect in this project. 

![Home](static/images-readme/home.png)

#### Navbar

The sites navbar is located at the top of each page. This adds to consistency and helps the user to navigate around. 

![Navbar](static/images-readme/navbar.png)

#### Sign Up

The sites sign up page is simple and intuitive. 

![Sign Up](static/images-readme/sign-up.png)

#### Login
The sites login page tells the user what it needs to validate. 

![Login](static/images-readme/sign-in.png)

#### Logout
The sites logout page asks one simple question. 

![Logout](static/images-readme/signout-page.png)

#### Add Post
The sites add post feature also asks for content and body. It also gives the user the option to add a image. 

![Add Post](static/images-readme/add_post.png)

#### PostDetailView

The postdetailview is the body of the post and contains the img, author, title, postdate, likes and depending on autherisation delete/edit links.

![PostDetailView](static/images-readme/post_detail_view.png)

#### Edit 
The sites edit page gives the user the option to reenter the info. The edit page only appears if the user is authenticated and the author of the post. 

![Edit](static/images-readme/edit_post.png)

#### Delete
The sites delete page gives the user the option to delete the post. The delete page only appears if the user is authenticated and the author of the post. 

![Delete](static/images-readme/delete_post.png)

#### Comment
The comment section easily gives users to comment on each others post. They can also like the post. 

![Comment](static/images-readme/comment-1-half.png)
![Comment](static/images-readme/comment-2-half.png)
#### Footer
The sites footer is located in the bottom of the page. It contains socialmedia-links. 

![Footer](static/images-readme/footer.png)



## Features left to implement

- Password reset function using email
- Alert message that tells the user that the post is awaiting approval. 

## Languages used

- HTML5
- CSS3
- Javascript
- Python
- Django
- SQL - Postgres

### Frameworks, libraries and tools

- Codeanywhere
- GitHub
- Django
- Bootstrap
- Cloudinary

### Installed packages

- asgiref==3.7.2
- cloudinary==1.36.0
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.23
- django-allauth==0.58.2
- django-crispy-forms==1.14.0
- django-summernote==0.8.20.0
- gunicorn==21.2.0
- oauthlib==3.2.2
- psycopg2==2.9.9
- PyJWT==2.8.0
- python3-openid==3.2.0
- pytz==2023.3.post1
- requests-oauthlib==1.3.1
- sqlparse==0.4.4

## Testing 
All testing in this project has been done manually during the development process, the project has not followed the principles of test driven development. Testing has for the most part followed the track of the user stories. Everytime a user story is concluded testing has been done to make sure the new feature is working. This has been done by simply clicking on the buttons/links and testing all the functions to see if it produced the desired outcome. All the functions in the project are working. 

Django is a python framework so most of the code is written in python. The part of the code that is in js is the alert messages. They work as expected. CryptoTalk has today no socialmedia so the links go to their respective homepages. 

In the development of this project I encountered several bugs. They are covered in the bugs section. 


## Bugs 
During development of this project I encountered several bugs. Some of them are covered here:

  ### Directory issue with allauth. 
  When running the command ls ../.pip-modules/lib/ it told me that there is no such directory. I understood that I have a issue with the directory. I googled it and found a command to find the path to where python is installed. To do this I used the command "which python3". It gave me the path "/home/codeany/.pyenv/shims/python3". However this did not work. To make sure I hade really installed allauth I searched for a command to check this. I found the command "pip show django-allauth". This gave me info regarding the version of allauth installed and more. In the info I found another path to the directory "/home/codeany/.local/lib/python3.9/site-packages". I tried this path instead and followed the instructions in the video and it worked.
'

### Blocktrans
In the login.html template there is an block of code   " <p>{% blocktrans %}Welcome to CryptoTalk. To leave a comment or like a post, please log in. If you
have not created an account yet, then <a class="link" href="{{ signup_url }}">sign up</a>first.{% endblocktrans %}</p> "

When running this code in the IDE it told me that a {%blocktrans%} cannot have a url path inside it. I removed the {%blocktrans%} tags and the problem was fixed.

### Placeholder image

To change the placeholder image took a little longer then expected. My first thought was that I only needed to change the link in the index.html. However when i did this nothing happened. I tried severeal different images and it gave me the same result. I then understood that it was a Cloudinary issue. I logged in to my cloudinary and added the image to my library. After that it worked. 

### Field required

When as a admin I want to approve a comment, django required that the body field and the content field to be filled. This means that I had to copy the text in the content and adding it to the body field. To fix this I added the blank=True statement to the content field in Post class model. 


## Unfixed bugs 

### Automated testing
I initiated the automated testing. I wanted to test with pythons unittest and to use jest for the little js code in the project. However I could not fix the import issue. When running the tests I got the message that its missing a parent directory and I couldn´t import the block of code I wanted tested. To resolve this I contacted the tutor support that Code Institute provides. That tutor couldn´t locate the problem. Considering the deadline and that its not required for this project, I decided to proceed with only manual testing. 

