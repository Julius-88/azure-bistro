# Azure Bistro

Welcome to Azure Bistro, an enchanting restaurant management application developed using Django. This project promises an unforgettable user experience, catering to people of all ages looking to explore new culinary delights.

Azure Bistro is not just about dining; it's about convenience and simplicity. Users can effortlessly create an account, make a reservation, and modify their details as needed. The application is designed with user-friendly interfaces and features that appeal to a diverse audience, from tech-savvy youths to the elderly who appreciate simplicity.

As a school project, Azure Bistro is a testament to the application of Django in creating dynamic web applications. It showcases key functionalities such as user authentication, database management, and responsive web design, aiming to provide a comprehensive learning experience.

Dive into Azure Bistro and discover a world where technology meets culinary artistry!

[Azure Bistro - Deployed Site](https://azure-bistro-v2-df04593043a2.herokuapp.com/)

# Deployment to Heroku

This README outlines the steps necessary to deploy an application to Heroku. It is designed as a guide for users looking to deploy their own applications using Heroku's platform.

## Pre-Requisites

**Before beginning, ensure you have a Heroku account!**

## Steps for Deployment

1.  **Create a New App:**
 - Click on the *new* button in the upper right corner of the Heroku dashboard.
 - Select *Create new app*.

![Heroku new button](./docs/heroku-new-button.JPG)

2. **App Name and Region:**
- Choose an app name. 
- Select a region closest to you for optimal performance.
- Click on *Create app* to confirm.

![Create New App](./docs/heroku-app-name.JPG)

3. **Connecting to GitHub:**
- In the *Deploy* section of your app, select *GitHub* as the *Deployment method*.
- In *Connect to GitHub*, type in the name of your GitHub project.
- Click *Connect* next tot the project you wish to deploy.

![Heroku Connecting to Github](./docs/heroku-project-name.JPG)

4. Manual Deployment
- Scroll down to *Manual deploy* and click on the *Deploy Branch* button to initiate the deployment process.

![Heroku Deploy Branch Button](./docs/heroku-deploy-button.JPG)

# Design

This section outlines the design process and choices for the project, focusing on creating an aesthetically pleasing and functional website.

**Initial Concept:** Explore the initial design concept on [Figma](https://www.figma.com/file/lk5TasgZyj0YGNNZ4hpgdn/Project-4---Restaurant?type=design&node-id=0%3A1&mode=design&t=HIdRRCTGi6cB25rD-1). Changes were made to the original design for improved visual appeal and to remove redundant elements.

**Color Palette:** 
- Azure Blue (#007FFF): Used exclusively for the logo to maintain its uniqueness.
- Midnight Blue (#111B2C): Chosen for the background and dropdown menus for optimal contrast and eye comfort.
- Dark Navy Blue (#1C2E4A): Applied to the navbar and footer for a distinct contrast with the main content.
- Black and White: Standard for text, ensuring readability.
- Coral (#FF7F50): Employed for CTA buttons and links to attract attention.

![Color Scheme](./docs/color-scheme.png)

**Typography:**
- Satisfy: Selected for the logo to embody the elegance of a high-end restaurant.
- Lora & Lato: Used for headings and body text, respectively, offering a balance between similarity and contrast for improved readability.

**Design Evolution:** 

- Simplified Navigation: Reduced the number of buttons, focusing on a single versatile button in the hero section. This button dynamically changes based on user status (anonymous or logged in), enhancing user interaction.

- Enhanced Hero Section: Added introductory text to provide context and encourage account creation. Merged opening hours for clarity.

- Accessibility Improvements: Darkened the blue background for better readability by screen readers.

- Menu Layout: Refined the menu layout for a more uniform appearance.

- Streamlined Table Booking: Revamped the table booking process for efficiency and user convenience. Users can now make reservations with minimal input, receiving instant feedback through the platform.

- Account Management: Simplified password recovery process and considering future enhancements like email confirmations.

- Feedback Mechanism: Utilized Django's built-in messaging for user feedback, aligning with the site's aesthetic and functionality.

- Social Media Integration: Customized social media icons to match the site’s design.

- Optimization: Removed the contact page for a more streamlined user experience.

- Technical Issues: Addressed and temporarily removed the problematic Google image from the footer, planning to resolve the issue later.

# Testing

## HTML
W3C Markup Validation Service, a tool for checking the markup validity of web documents in HTML, was utilized to ensure that the website conforms to web standards.

**Errors in the landing page:** The validator showed the following errors,

![Home Page HTML errors](./docs/html-index-error.JPG)

**Error in the menu page:** The validator showed the following error,

![Menu Page HTML error](./docs/html-menu-error.JPG)

**Restricted Pages:** An error occurred when it tried to analyze the page for users, in the console it wrote *'TypeError: 'AnonymousUser' object is not iterable'* for the following pages,
- Manage Reservations
- Edit Reservation
- Delete Reservation

![Restricted](./docs/html-restricted.JPG)

I have since added @login_required in their views and thereby fixed the issue.
Once I fixed it, it gave me this info,

![Info](./docs/html-bug-fixed.JPG)

I have searched my entire file and cannot find what it is referring too, I think that it has something to do with django, since it only appeared when I added the @login_required to the viewpoints. I will seek assistance regarding this issue.

**Success:** No other pages showed any issues, and after having solved the minor issues shown in the home page and the menu page we are met by a success message,

![Success](./docs/html-success.JPG)

## CSS
W3C CSS validation was used to validate the CSS of this project. No errors where found.

![Success](./docs/css-success.JPG)

## Python
All Python code is written to the standards of PEP8. It has been double checked using the [Code Institute Python Linter](https://pep8ci.herokuapp.com/#)

![Linther](./docs/py-success.JPG)

## Lighthouse

Lighthouse is an open-source tool for improving the quality of web pages. It provides audits for performance, accessibility, progressive web apps, and more. Below are the Lighthouse test results for the Azure Bistro website.

**Home Page - Desktop View**

![Home Page - Desktop View](./docs/lighthouse-index.JPG)

**Home Page - Mobile View**

![Home Page - Mobile View](./docs/lighthouse-index-mobile.JPG)

**Menu Page - Desktop View**

![Menu Page - Desktop View](./docs/lighthouse-menu.JPG)

**Menu Page - Mobile View**

![Menu Page - Mobile View](./docs/lighthouse-menu-mobile.JPG)

**Login Page - Desktop View**

![Login Page - Desktop View](./docs/lighthouse-login.JPG)

**Login Page - Mobile View**

![Login Page - Mobile View](./docs/lighthouse-login-mobile.JPG)

**Sign Up Page - Desktop View**

![Sign Up Page - Desktop View](./docs/lighthouse-signup.JPG)

**Sign Up Page - Mobile View**

![Sign Up Page - Mobile View](./docs/lighthouse-signup-mobile.JPG)

**Reservation Page - Desktop View**

![Reservation Page - Desktop View](./docs/lighthouse-reservation.JPG)

**Reservation Page - Mobile View**

![Reservation Page - Mobile View](./docs/lighthouse-reservation-mobile.JPG)

**Manage Reservation Page - Desktop View**

![Manage Reservation Page - Desktop View](./docs/lighthouse-manage-reservation.JPG)

**Manage Reservation Page - Mobile View**

![Manage Reservation Page - Mobile View](./docs/lighthouse-manage-reservation-mobile.JPG)

**Update Reservation Page - Desktop View**

![Update Reservation Page - Desktop View](./docs/lighthouse-update-reservation.JPG)

**Update Reservation Page - Mobile View**

![Update Reservation Page - Mobile View](./docs/lighthouse-update-reservation-mobile.JPG)

**Delete Reservation Page - Desktop View**

![Delete Reservation Page - Desktop View](./docs/lighthouse-delete-reservation.JPG)

**Delete Reservation Page - Mobile View**

![Delete Reservation Page - Mobile View](./docs/lighthouse-delete-reservation-mobile.JPG)

**Account Deletion Page - Desktop View**

![Account Deletion Page - Desktop View](./docs/lighthouse-account-deletion.JPG)

**Account Deletion Page - Mobile View**

![Account Deletion Page - Mobile View](./docs/lighthouse-account-deletion-mobile.JPG)

**Sign Out Page - Desktop View**

![Sign Out Page - Desktop View](./docs/lighthouse-signout.JPG)

**Sign Out Page - Mobile View**

![Sign Out Page - Mobile View](./docs/lighthouse-signout-mobile.JPG)

**All Reservations - Desktop View**

![All Reservations - Desktop View](./docs/lighthouse-all-reservations.JPG)

**All Reservations - Mobile View**

![All Reservations - Mobile View](./docs/lighthouse-all-reservations-mobile.JPG)

**Admin Update Reservations - Desktop View**

![Admin Update Reservations - Desktop View](./docs/lighthouse-admin-update-reservations.JPG)

**Admin Update Reservations - Mobile View**

![Admin Update Reservations - Mobile View](./docs/lighthouse-admin-update-reservations-mobile.JPG)

**Admin Delete Reservation - Desktop View**

![Admin Delete Reservation - Desktop View](./docs/lighthouse-admin-delete-reservation.JPG)

**Admin Delete Reservation - Mobile View**

![Admin Delete Reservation - Mobile View](./docs/lighthouse-admin-delete-reservation-mobile.JPG)

## Responsivity
The website's responsivity was manually checked through Chrome DevTools and on my Samsung S9+. In mobile view, most elements transition into a column format for easier viewing. The *All Reservations* page is a table on tablets and cards on mobile screens. 

![All Reservations - Desktop](./docs/admin-all-reservations-page.JPG)

![All Reservations - Mobile](./docs/admin-all-reservations-page-mobile.JPG)

# Features

## Home Page

**Hero Section:** When users enter the website, they are greeted by the hero section. If they have not logged in, a clear CTA (Call To Action) button allows them to do so. This button will change to *RESERVE TABLE* once they are logged in for convenience. It also has the restaurants opening hours and informational text.

![Hero Section - Log In Button](./docs/hero-section.JPG)

![Hero Section - Reserve Table Button](./docs/hero-section-login.JPG)

**Main Content:** Beneath the hero section, there are image links to the menu page. Users can click on a category of their choice and will be directed to the corresponding section on the menu page. This allows users to quickly find what they are looking for on our menu.

![Main Content](./docs/home-page.JPG)

## Navbar

The navbar remains at the top of the webpage, no matter where users are on the site. It also scrolls down with the user, ensuring constant access. Before the user is logged in they can only access the Home, Menu and Log In links.

![Navbar - Anonymous](./docs/navbar-anon.JPG)

If they hover over the menu link or click on it on mobile view, a dropdown menu will appear with each section of the menu.

![Navbar - Menu](./docs/navbar-menu.JPG)

Once they login the login link will change to *Account* and a new link will appear called *Reservation*.

![Navbar -  Logged In](./docs/navbar-loggedin.JPG)

The account link will also be a dropdown menu that will show three other links. *Sign Out*, *Manage Reservation* and *Delete Account*. This will allow the user to quickly find relevant information.

![Navbar - Account](./docs/navbar-account.JPG)

Above the navbar is the name of the restaurant which also functions as a link to the home page. When you hover over the various links they will turn color. Only the Menu and Account links wont turn color since they instead activate their dropdown menu. This gives the user feedback on what they are doing.

![Navbar Hover](./docs/navbar-hover.JPG)

## Menu 

On the menu page, the user can find the entire menu and the prices of each item. This will allow them to plan in advance what they wish to eat.

![Menu](./docs/menu-page.JPG)

## Footer

 In the bottom of every page there is the footer. With visiting and contact information and links to our social media. It also contains a small copyright text. This enables users to quickly find out the restaurants contact information no matter where they are on the page.

![Footer](./docs/footer.JPG)

## Login Page 

Here the user can login and click on the remember me box. If they do not have an account, there is a link called *Create Account* which will take them to the account creation page. When the user is on an input field, it will be highlighted.

![Login Page](./docs/login-page.JPG)

an error text will be shown if the user inputs the wrong login information.

![Login Page Error](./docs/login-page-error.JPG)

Once the user has logged in, they will be directed to the home page where a success message will be shown.
![Login Success](./docs/login-success.JPG)

## Create Account Page

If the user does not have an account they can create one in seconds on the Create Account Page. All they need is a user name and password. 

![Sign Up Page](./docs/signup-page.JPG)

If the user name is taken an error message will pop up. An error will also occur if they leave anything but the email address blank.

![Sign Up Page - Error](./docs/signup-page-error.JPG)

![Sign Up Page - Error](./docs/signup-page-empty-field.JPG)

Once they register, they will be taken back to the main page and a success message will appear.

## Reservation Page

In the reservation page they can pick which date, time and the number of people they would like to book for. 

![Reservation Page](./docs/reservation-page.JPG)

If the time is already booked or has passed, an error message will show up.

![Reservation Booked](./docs/reservation-page-booked.JPG)

![Reservation Past](./docs/reservation-page-past.JPG)

Once their reservation is complete, they will be taken back to the main page with a success message. This reservation will be shown in the Manage Reservation page, which they can access from their account.

![Reservation Success](./docs/reservation-success.JPG)

## Manage Reservation

Here the user can view all reservations they have made and the details of it. They can also edit or delete the reservation.

![Manage Reservation Page](./docs/manage-reservation-page.JPG)

**Edit Reservation:** Once the user clicks on the button they will be brought to a page where they can edit their reservation. There is also a button that will take them back if they accidentaly clicked on the wrong reservation.

![Manage Reservation Page Edit](./docs/manage-reservation-page-edit.JPG)

Once complete, they will be brought back to the *Manage Reservation* page and a success message will be seen.

![Manage Reservation Page Success](./docs/manage-reservation-page-edit-success.JPG)

**Delete Reservation:** The user can also choose to delete a reservation by clicking the *Delete Reservation* button.

![Delete Reservation Page](./docs/delete-reservation-page.JPG)

Once complete, they will be brought back to the *Manage Reservation* page and a success message will be seen.

![Delete Reservation Page Success](./docs/delete-reservation-page-success.JPG)

## Sign Out
The user can sign out of their account, by clicking on the sign out link in their account.
Once done they will be taken to the main page where the button on the hero-section and the links in the navbar have reverted back. A success message can also be seen.

![Sign Out Page](./docs/signout-page.JPG)

![Sign Out Page Success](./docs/signout-page-success.JPG)

## Delete Account
The user can also choose to delete their account. This can be done from their account. They will have to confirm their decision by clicking on the *I confirm I want to delete my account:* checkbox.

![Delete Account Page](./docs/delete-account-page.JPG)

Once done, They will be brought back to the main page, where a success message will be shown. This will also delete all of their information from the database.

![Delete Account Page Success](./docs/delete-account-page-success.JPG)

**Admin View:**

Before account deletion.

![Before Account Deletion](./docs/admin-all-reservations-page.JPG)

After account deletion.

![After Account Deletion](./docs/admin-all-reservations-page-account-deletion.JPG)

## Staff

When a staff member logs in there will be two extra links in their account, *Admin Panel* and *All Reservations*. 

If they click on the *Admin Panel* link, they will be taken to the django admin panel.
If they click on *All Reservations*, they will be taken to a page where they can view all the customers whom have made a reservation. 
The staff member can also choose to edit or delete a reservation from this page.

![All Reservations](./docs/admin-all-reservations-page.JPG)

# Recources used
- [Django Project - Forms](https://docs.djangoproject.com/en/5.0/topics/forms/)

- [Django Project - Widgets](https://docs.djangoproject.com/en/5.0/ref/forms/widgets/)

- [Django Project - Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/)

- [Django Project - Models](https://docs.djangoproject.com/en/5.0/topics/db/models/)

- [Django Project - Queries](https://docs.djangoproject.com/en/5.0/topics/db/queries/)

- [Django Project - Request-Response](https://docs.djangoproject.com/en/5.0/ref/request-response/)

- [Django Project - Messages](https://docs.djangoproject.com/en/5.0/ref/contrib/messages/)

- [Python - Datetime](https://docs.python.org/3/library/datetime.html)

- [Geeks For Geeks - args-kwargs-python](https://www.geeksforgeeks.org/args-kwargs-python/)

- [Youtube - Booking System For A Health Clinic](https://www.youtube.com/watch?v=s5xbtuo9pR0&t=102s)

- [Cloudinary](https://cloudinary.com/documentation)

- Conde Institute Projects - I think therefore I blog and Hello Django

# Tech Stach

- **HTML:** Used for structuring the content and layout of the web pages.
- **CSS:** Used to style and visually enhance the HTML elements.
- **Django:** Used for backend functionality, including URL routing, views, and template rendering.
- **Bootstrap:** Used for its grid system, pre-built components and responsive design features.
- **Cloudinary:** Used to upload, store and display media files.
- **ElephantSQL:** Used for managing the application's data in a scalable manner.
- **FontAwesome:** Used for incorporating scalable icons.
- **Figma:** Used to create initial design of web application.
- **Git & GitHub:** Git is used for version control and GitHub is used for hosting repository and backup.
- **Heroku:** Used to deploy, manage and scale the web application.
- **Google Fonts:** Used for a variety of fonts.
- **Coolors:** Used to create a color schema.
- **Favicon:** Used to create favicon.

# Notes

**Media Folder:** This project currently does not use the *media* folder, as it is designed without the need for handling user-uploaded content. The folder is kept in place to allow for easy integration of media files in the future.

## Special Admin Permissions

In the Azure Bistro application, administrators have extended permissions compared to regular users. One key distinction is in the reservation system:

- **Regular Users**: Cannot book a reservation for a date and time that has already been booked by another user. This restriction ensures that double bookings do not occur, maintaining a smooth and efficient reservation process.

- **Administrators**: Have the ability to override this restriction and book reservations even on dates and times that are already booked. This feature is intended to provide flexibility for handling special circumstances or last-minute changes that might require administrative intervention.