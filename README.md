# Blessed Blog

## Author

- Kirui Vincent

## Description of the Project

- This is an app that allows users to sign up/in and post blogs .They can also comment on quotes

## USER Story

- Comment on the different quotes posted py other users.
- See the quotes posted by super user
- Register to be allowed to log in to the application
- Submit quote to a specific category of their choice.

# BDD 

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *Page Loads on browser*  | Get all posts, select between signup and login |
| Select signup | *Email, Username, Password* | Redirect to login  |
| Select Login  | *Username and Password* | Redirect to ap pitches based on categories |
| Select comment button | *Comment*  | Load Form that you input comment |
| Click on submit | *Enter: * |  Redirect to all comments template with your comment and other comments |


## Development Installation 

1. Cloning the repo:

    https://github.com/BlessedAssurance/Blessed-Blog

2. Move to the folder and install requirements

    cd pitch
    pip install -r requirements.txt

3. Exporting Configurations

4. Running the application

    python3.6 run.py server

5. Testing the application

   python3.6 run.py test

Open the application on your browser 127.0.0.1:5000.

## Technology used
- Python3.6
- Flask
- Heroku

## Contact Information

-  engineervinceblair@gmail.com 

## License
- *MIT* License