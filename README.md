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


### **Purpose:**

Bloom Art E-commerce is all about bringing art to life in two beautiful ways:

**1. Discover & Decorate:**

Find and bring home stunning watercolor art prints that add a touch of beauty to your space. It's a haven for art lovers and home decor enthusiasts.

**2. Grow Your Artistry:**

Dive into our online art classes to nurture your artistic side. Bloom Art is not just a store; it's a space for you to bloom as an artist and make your personal spaces uniquely yours.
    
In a nutshell, we're here to make your world more vibrant with art and help you discover the artist within.


### **User Stories**

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here -  <a href="https://github.com/users/ksumm/projects/8"> The Bloom Art </a>

<br>

|  N  | Content                                                                                                                                                   |  
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | As a **site user** I want to use the Navigation Bar, so that I can navigate through the website pages                                                     |                   
| 2   | As a **site user** I want to visit and interact with the Home site page, so that I can understand the purpose of the site easily                          |
| 3   | As a **site user** I want to see all the products on a site page, so that I can select some to purchase                                                   |
| 4   | As a **site user** I want to see the Product detail page, so that I can make purchase easily                                                              |                                                                     
| 5   | As a **site user** I want to sort a products by specific category, so that I can quickly choose product that I need                                       |
| 6   | As a **site user** I can use the search form to search for a product, so that I can quickly find products that I am interested in                         |
| 7   | As a **site user** I want to add a product to a shopping bag, so that the product is added                                                                |
| 8   | As a **site user** I want to choose and change the quantity of the selected product, so that the correct quantity is added to the shopping bag            |
| 9   | As a **site user** I want to receive a confirmation email after checkout, so that I am sure that my order is completed successfully                       |
| 10  | As a **site user** I want to access My Profile, so that I can see my profile info and my orders history                                                   |
| 11  | As a **site user** I want to be able to complete the checkout process for my shopping cart so that I can pay for the order                                |
| 12  | As a **site user** I want to remove products from my shopping bag so that I can adjust my order before making a purchase                                  |
| 13  | As a **site user** I want to sign up for newsletters on the website so that I can keep up with updates and deals                                          |
| 14  | As a **site user** I want to access the footer of the website, so that I can visit the site's social media pages                                          |
| 15  | As a **site user** I want to view details about available art classes, so that I can make an informed decision about participating in a class             |
| 16  | As a **site user** I want to be able to book an art class that I'm interested in, so that I can secure my spot for the class                              |
| 17  | As a **site user** I want to be able to contact the website administrators easily, so that I can seek assistance, provide feedback, or address any concerns I may have                                                          
| 18  | As a **site user** I want to be able to delete my profile when needed, so that I can have control over my account information and personal data           |


---
<br/>

### **Design**

### **Wireframes**


<summary>Index</summary>

![Index Wireframe](docs/index.png)


<summary>Products</summary>

![Products Wireframe](docs/products.png)


<summary>Product Details</summary>

![Product Details Wireframe](docs/details.png)


<summary>Art Classes</summary>

![Art Classes Wireframe](docs/artclasses.png)


<summary>Contact Us</summary>

![Contact Us Wireframe](docs/contact.png)


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


</div>
