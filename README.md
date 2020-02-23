## Local Development instructions

### First time instructions
1. Clone this repo to your machine
2. Open your terminal or command prompt
3. If you don't have it already, pip install virtualenv
4. Change directory into outer folder of this repo and create new virtualenvironment called "virt" by running
	`virtualenv virt`
(note that if you give it a different name, you need to add that new name to the .gitignore).

### Every time instructions
5. Activate your virtualenv: `source/bin/activate`
6. If you're starting a new feature, be sure to start from the master branch
7. Install all packages in requirements file to your virtualenv: `pip install -r requirements.txt`
Note - you don't technically need to do this every time, but you will need to do it every time requirements.txt changes and it doesn't actually hurt to do it as pip won't install anything you already have installed.
8. Run
	`python application.py`
to start your local application
9. If you install new Python packages and add new code that requires them, remember to
	`pip freeze > requirements.txt`
before pushing your code.
10. Commit and push all new code to a feature branch:
* `git checkout -b <your-branch-name>` the first time you want to create it
* `git checkout <your-branch-name>` if it's already created and you want to check it out later
* `git status` to see what you have edited
* `git add <file name>` for every file you want to commit
* `git commit -m <your-message>` to commit a set of files along with a descriptive message of what you did
* `git push origin <your-branch-name>` to push that feature branch
11. Open a new pull request on github when you want to merge it in.

## Deployment instructions
For now, only Emily should manage deployments (as a quality control on our production environment).
1. Developer commits all new changes and pushes feature branch
2. Emily tests locally and merges feature branch in Github
3. Emily checks out master locally
4. From master branch, Emily runs
	eb deploy -m "<commit hash>"
