Shaheq Shakeel

__SETTING_UP_WEBSERVICES__
To run web server on Mac Os you will need virtual environment for python (venvosx):
from root project directory (aka ./yxefoodbank) in terminal write
    mkdir venvosx  
    cd venvosx 
    virtualenv -p python3 .    
    source ./bin/activate
    cd ..    
    python manage.py runserver

To get out of virtual environment:
from terminal write
    CTRL+C
    deactivate

On next launch you only need to use commands:
    source ./bin/activate
    cd ..    
    python manage.py runserver
 
__WEB_BROWSER__
website runs at default 127.0.0.1:8000/

__DIR__
./templates holds all our files that each page on our website uses
./base/templates holds all our pages that are not associated with account management
./account/templates currently only hold register.html page

