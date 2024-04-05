## Testing 
All testing in this project has been done manually during the development process and after. They assumed result of clicking the buttons and testing the features are documented in this Readme file. This has been done by simply clicking on the buttons/links and testing all the functions to see if it produced the desired outcome. All the functions in the project are working. 

Django is a python framework so most of the code is written in python. The part of the code that is in js is the alert messages. They work as expected. CryptoTalk has today no socialmedia today so the links go to their respective homepages.

Because this project was developed with Bootstrap it is fully responsive on all screen sizes.  

In the development of this project I encountered several bugs. They are covered in the bugs section. 


### Automated testing
I initiated the automated testing. I wanted to test with pythons unittest and to use jest for the little js code in the project. However I could not fix the import issue. When running the tests I got the message that its missing a parent directory and I couldn´t import the block of code I wanted tested. To resolve this I contacted the tutor support that Code Institute provides. That tutor couldn´t locate the problem. Considering the deadline and that its not required for this project, I decided to proceed with only manual testing. 



### Validator Testing
-----------------------------------------------------------------------------------------
Testing with <https://validator.w3.org/> shows no errors in html:


#### Signup Page


![Validator testing](static/testing-images/sign_up_page.png)

#### Add Post Page


![Validator testing](static/testing-images/add_post_page.png)

#### Delete Post Page


![Validator testing](static/testing-images/delete_post.png)

#### Edit Post Page


![Validator testing](static/testing-images/edit_post_page.png)

#### Index/Home Page


![Validator testing](static/testing-images/index_page.png)

#### Logout Page


![Validator testing](static/testing-images/log_out_page.png)

#### Login Page


![Validator testing](static/testing-images/login_page.png)



#### Postdetail Page


![Validator testing](static/testing-images/post_detail_page.png)



### Manual Testing
-----------------------------------------
![Validator testing](static/testing-images/testing_cryptotalk.png)






## Lighthouse

Testing with lighthouse gives the following results:

![Validator testing](static/images-readme/lighthouse.png)


## Python Testing

Testing and validating using pep8 validations tools:
Testing with <https://www.pythonchecker.com/>
Testing the pythonchecker.com came back with good results. Testing the base.html file came back 100% no errors. 


## CSS Testing

Testing with <https://jigsaw.w3.org/css-validator/> show no errors in CSS:

![Validator testing](static/images-readme/css-validator.png)