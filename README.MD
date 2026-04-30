### CREATING A DJANGO APP WITH DB
- Step 1 : Set up the necessary configs for your project
    For MediaHub our configs are : 
    a. Media files url
    b. Templates directory
    c. Redirect urls
    d. Cloudinary configs for mmedia management
    e. Custom auth model override

- Step 2 : Register our cloudinary credentials
### Accounts a


##  TEMPLATING (creation of user interfaces)
- For our app, our templates directory is set on the root folder
- We will have two app folders for each of our apps interfaces
- A base.html will provide links to stylesheets and other html meta-data information

## For Form fields
- In each app for data collected specify the fields in a forms.py file
- Accounts : UserLoginForm , User



# Path for users to access the pages
- Inside the app's urls.py
# Set up our admin content management for the app
- Inside the app's admin.py
# Configure our apps.py in the apps folder to allow auto incromontotion for our ids
- Inside the app's app.py


## ADMIN CONFIGURATION
- Set up administrative credentials
python manage.py createsuperuser
- Give username, email and password combo
- Access admin by going to the route/ admin
