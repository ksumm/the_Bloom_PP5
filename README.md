<div style="background-color: #F7F7F7; color: black;">
 
# **The Bloom Art**

Welcome to The Bloom Art, a vibrant and user-friendly e-commerce platform specializing in watercolor prints. This project is developed as a part of the Full Stack Development course at Code Institute. 

 [View the live project here](https://the-bloom-art-3c20c7ea337d.herokuapp.com/)
![](docs/mockup.png)

---
<br/>

## **Table of Contents**

1. [User Experience](#user-experience)
3. [Design](#design)
5. [Features](#features)
6. [Accessibility](#accessibility)
7. [Technologies Used](#technologies-used)
8. [Deployment and Local Development](#deployment-and-local-development)
9. [Testing](#testing)
10. [Credits](#credits)

---
<br/>
    
## **User Experience**
<br/>

### **Purpose:**

Bloom Art E-commerce is all about bringing art to life in two beautiful ways:

**1. Discover & Decorate:**

Find and bring home stunning watercolor art prints that add a touch of beauty to your space. It's a haven for art lovers and home decor enthusiasts.

**2. Grow Your Artistry:**

Dive into our online art classes to nurture your artistic side. Bloom Art is not just a store; it's a space for you to bloom as an artist and make your personal spaces uniquely yours.
    
In a nutshell, we're here to make your world more vibrant with art and help you discover the artist within.


### **User Stories**



### **Design**
<br/>

### **Wireframes**

<details>
<summary>Index</summary>

![Index Wireframe](docs/index.png)

<details>
<summary>Products</summary>

![Products Wireframe](docs/products.png)

<details>
<summary>Product Details</summary>

![Product Details Wireframe](docs/details.png)

<details>
<summary>Art Classes</summary>

![Art Classes Wireframe](docs/artclasses.png)


<details>
<summary>Contact Us</summary>

![Contact Us Wireframe](docs/contact.png)



The UX design for the Bloom Art E-commerce project followed a systematic process to ensure a user-friendly and visually appealing platform. Below are the key stages of the design journey.

### **Wireframes**

The wireframes are mostly adapted versions of the Boutique Ado walkthrough. 

### **Colour Scheme**

The colour scheme was choosen using the [Imagecolorpicker](https://imagecolorpicker.com) 
![Color scheme](docs/color-palette.png)

**The main colors used:**

- #ac8e6e;
- #a02015;
- #5b635b;
- white;
- black;

**Typography**

Google Fonts was used to select and import the fonts on this project:
* [Roboto](https://fonts.google.com/specimen/Roboto) 
* [Lato](https://fonts.google.com/?query=lato)

 
### User Stories

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here -  <a href="https://github.com/users/ksumm/projects/8"> The Bloom Art </a>


### Database Schema

![Database schema](docs/database.png)


## Agile Development Process
This project used GitHub Projects Tool to create the Scrum board and use agile methodology.<a href="https://github.com/users/ksumm/projects/8"> Link to the Agile Board </a>

## Technologies Used

### Languages Used
  - HTML5
  - CSS3
  - JavaScript
  - Python

### Frameworks, Libraries & Programs Used
* [Git](https://git-scm.com/) for version control.
* [GitHub](https://github.com/) to store the project files.
* [Canva](https://www.canva.com/) to create the wireframes.
* [Django](https://www.djangoproject.com/) as the Python Framework.
* [Heroku](https://www.heroku.com/home/) to deploy the website.
* [ElephantSQL](https://www.elephantsql.com/) to host the database.
* [Cloudinary](https://cloudinary.com/) to host images
* [Django-allauth](https://django-allauth.readthedocs.io/en/latest/) to create accounts.
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to create the forms based on the models.
* [Gunicorn](https://gunicorn.org/) as the webserver to host Django on Heroku.
* [dj-database-url](https://pypi.org/project/dj-database-url/) to create DATABASE_URL to configure the Django application.
* [psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL adapter.
* [Whitenoise](https://whitenoise.readthedocs.io/en/latest/index.html) to host static files.
* [Tables Generator](https://www.tablesgenerator.com/markdown_tables) to create tables for TESTING.md
* [RandomKeyGen](https://randomkeygen.com/) to create the SECRET_KEY for the project.
* [Google Fonts](https://fonts.google.com/) to import the fonts used on the website.
* [Bootstrap](https://getbootstrap.com/) for layout.
* [Lucidchart](https://lucid.app/) for database schema.

## Testing

Please check the [TESTING.md](TESTING.md) file for all the tests.

### Remote Deployment

Before deploying, run 'pip3 freeze > requirements.txt' on the terminal of your IDE of choice.

The site was deployed to Heroku. The steps to deploy are as follows: 
  1. Create an account and log in your [Heroku](https://id.heroku.com/login) account. 
  2. On the dashboard, click on the button New -> Create new app on the right side of the page.
  3. Choose a name and select your region. Click on Create app.
  4. Go to the Settings tab. Scroll down to Config Vars. 
  - Add key PORT and value 8000.
  - Add key DATABASE_URL and add the value of your database on ElephantSQL or other host of choice.
  - Add key CLOUDINARY_URL and add the value of your cloudinary host link.
  - Add key SECRET_KEY and add the value of your choice for this secret key.
  - Add key DISABLE_COLLECTSTATIC and add the value of 1. (Don't forget to remove this key before the final deployment.)
  5. Go to the Deploy tab. Select GitHub as Deployment Method. Connect your account.
  6. Enter the name of the repository that you forked, search and connect.
  7. Select the branch and click Deploy Branch.

The live link can be found here - [https://github.com/ksumm/the_Bloom_PP5](https://the-bloom-art-3c20c7ea337d.herokuapp.com)

### Local Deployment

#### How to Fork

  1. Log In or Sign Up to GitHub.
  2. Go to this project repository [https://github.com/ksumm/the_Bloom_PP5](https://github.com/ksumm/the_Bloom_PP5)
  2. On the top right of the page, there's a button with the option Fork. Click on it.
  3. A new page, "Create a new fork", will open. If you wish, you can edit the name.
  4. At the end of the page, click on "Create fork".
  5. Now, you have a copy of the project in your repositories.

#### How to Clone

  1. Log In or Sign Up to GitHub.
  2. Go to this project repository [https://github.com/ksumm/the_Bloom_PP5](https://github.com/ksumm/the_Bloom_PP5)
  3. Click on the Code button and select if you would like to clone with HTTPS, SSH or GitHub CLI and copy the link.
  4. Open the terminal in the code editor of your choice and change the current working directory to the one you will use for to clone the repository.
  5. Type 'git clone' into the terminal and then paste the link you copied before and press Enter.

## Credits


#### Using Gitpod
If you would like to edit your copy of this repository on Gitpod, you will need to: 
  1. On your browser of choice, install the Gitpod extension/add-on.
  2. On GitHub, open the project repository you forked before.
  3. On the top of the page, over the files, there is a green button on the right side of the page saying "Gitpod". Click it.
  4. It will open the Gitpod website. On the first time, you will select to connect with your GitHub account and Authorize gitpod-io. After that, you'll create an account.
  5. It might take a while after that because Gitpod will create your workspace.
  After the workspace is loaded, you can edit it on Gitpod.

### Acknowledgments

- I would like to thank my Code Institute mentor, Rory Patrick Sheridan for his support and feedback throughout this project.
- I would like to thank my daughter for her understanding, patience and support while I developed this project.


