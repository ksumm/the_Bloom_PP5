 <h1 align="center">The Bloom Art - Testing</h1>

## VALIDATION

## **HTML**

To check markup validity of Web documents as HTML, we used: [W3C Markup Validation Service](https://validator.w3.org/).
Unfortunately since Django tags are conflicting with standard HTML markup, we could not fix those errors.

<details>
<summary>HTML</summary>

![HTML](docs/testing/html.png)
</details>

---
<br>

## **CSS**

The CSS was checked on [Jigsaw Validator](https://jigsaw.w3.org/css-validator/) 

* Results from the [checkout](docs/testing/checkout_css.png) css.
* Results from the [profile](docs/testing//profile_css.png) css.
* Results from the [base](docs/testing//base_css.png) css.

---
<br>

## **PYTHON**


## **Flake8**

In Gitpod python was checked using flake8:

<details>
<summary>Flake8</summary>

![Flake8](docs/testing/flake8.png)
</details>

## **CI Python Linter**

Also the Python was checked on CI Python linter:

<details>
<summary>artclass_views</summary>

![artclass_views](docs/testing/artclass_views.png)
</details>

<details>
<summary>artclass_urls</summary>

![artclass_urls](docs/testing/artclass_urls.png)
</details>

<details>
<summary>artclass_forms</summary>

![artclass_forms](docs/testing/artclass_forms.png)
</details>


<details>
<summary>artclass_models</summary>

![artclass_models](docs/testing/artclass_models.png)
</details>

---
<br>

## **JAVA SCRIPT**

To detect errors and potential problems in our JavaScript code we used: [JSHint](https://jshint.com/)

<details>
<summary>stripe</summary>

![stripe](docs/testing/stripes.png)
</details>

<details>
<summary>countryfield</summary>

![countryfield](docs/testing/countryfield.png)
</details>

---
<br>


## **LIGHTHOUSE**

I used Chrome Developer Tools Lighthouse to test the Performance, Accessibility, Best practices and SEO of this project.
![Lighthouse](docs/testing/lighthouse.png)

---
<br>

## **MANUAL AND AUTOMATED TESTING**

Automated testing relies on scripts and tools to execute predefined test cases swiftly, providing fast and consistent results for regression testing. It requires a higher initial setup cost and is ideal for repetitive tasks. In contrast, manual testing involves human judgment and adaptability, making it effective for exploratory and usability testing. Manual testing may lack the repeatability of automated methods and has a lower initial learning curve. A balanced approach often combines both methods to maximize testing efficiency based on project requirements.

## **AUTOMATED TESTING** 

Automated testing will be implemented in next release

## **MANUAL TESTING**

`Nav Bar`

| Feature          | Expected Outcome                                        | Test Performed                                  | Result                           | Test Outcome |
|------------------|---------------------------------------------------------|-------------------------------------------------|----------------------------------|--------------|
| Logo             | Goes to home page .                                     | Click on the logo.                              | As expected                      | PASS         |
| Register         | Goes to the Signup when user is not logged in.          | Click on the Home menu item.                    | As expected                      | PASS         |
| Login            | Goes to the Login page.                                 | Click on the Login menu item.                   | As expected                      | PASS         |
| Shopping bag     | Goes to the Shopping bag page.                          | Click on the Shopping bag  icon.                | As expected                      | PASS         |
| Logout           | Goes to the Confirm Logout page when user is logged in. | Click on the Logout menu item.                  | As expected                      | PASS         |
| Search           | User can see search results                             | Enter any word in search field. Press Enter     | As expected                      | PASS         |
| Search           | User can see error message if he did not enter any data | Don't enter any data in seach field, press Enter| As expected                      | PASS         |
| About Us         | Goes to the About Us page.                              | Click on the About Us/About us link.            | As expected                      | PASS         |
| Shop All Products| The drop down list is opened.                           | Click on the Shopp All Products link.           | As expected                      | PASS         |
| Seasonal         | The drop down list is opened.                           | Click on the Seasonal link.                     | As expected                      | PASS         |
| Holidays/Events  | User can see error message if he did not enter any data | Don't enter any data in seach field, press Enter| As expected                      | PASS         |
| Art Classes      | The Art Classes page is opened.                         | Click on the Art Classes > Our Art Classes.     | As expected                      | PASS         |


