# Application
Code for our mobile/web application.

## Key Resources
Django/React setup following the pattern here: https://www.valentinog.com/blog/drf/
(note - I didn't follow their django setup pattern. Just picked up at
Django REST with React: Django and React together)

## Setting up Python environment
This set of steps will allow you to run a local development server and make edits to Python server code. It will serve the React front end, but you need to follow the Setting up NPM steps to actually be able to edit and rebuild the React code
1. Install anaconda
2. Create new anaconda environment with pip
	conda install -n my-accessibility-app pip`
3. Pip install all necessary packages from Requirements.txt file
	pip install -r requirements.txt
4. Run development server
	python manage.py runserver
5. Follow the instructions in your console to find address where you will hit local development server from browser. You can now make changes to the source code, save them, and Django will hot-reload the code.


## Setting up NPM
To compile the React code, we use NPM (Node package manager). NPM gets downloaded automatically when we download Node.
1. Install node.js: https://nodejs.org/en/download/
2. All the dependencies needed for our Javascript build stack are in the package.json file. It includes defined "build scripts" for both dev and production. 
3. To compile new React code, save and edit your code changes, then navigate to the `frontend` folder and run
	npm run dev
This script is defined in package.json to define how to compile the code for the development environment.
1. Install node.js: https://nodejs.org/en/download/
2. All the dependencies needed for our Javascript build stack are in the package.json file. It includes defined "build scripts" for both dev and production. 
3. To compile new React code, save and edit your code changes, then navigate to the `frontend` folder and run
	npm run dev
This script is defined in package.json to define how to compile the code for the development environment. The Django server will hot reload the new compiled javascript if the server is running at the time. 
