Shaheq Shakeel

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
