# Lumache Spinx Demo  Project
Based on: Sphinx Tutorial: 
https://www.sphinx-doc.org/en/master/tutorial/index.html

## To Start
On *Windows* run: 

```
# Install virtualenv if not installed:
pip install virtualenv

virtualenv --python C:\Path\To\Python\python.exe .venv
# for rights in the powershell
Set-ExecutionPolicy Unrestricted -Scope Process
.\.venv\Scripts\activate

# install requirments
# freeze requirements: pip freeze > requirements.txt
pip install -r requirements.txt
```

On *Linux* run: 
```
virtualenv --python python3.6 .venv
source .venv/bin/activate

# install requirments
# freeze requirements: pip freeze > requirements.txt
pip install -r requirements.txt
```

## Install Sphinx
Manual Install Sphinx (if not used: pip install -r requirements.txt)
```
python -m pip install sphinx
sphinx-build --version
```

## Run Sphinx 

```
sphinx-quickstart docs
# answer setup questions

# build docs 
sphinx-build -b html docs/source/ docs/_build/html

# update docs
cd docs
make html
# on windows
.\make html

# for epub
.\make epub

# for pdf, needs latex (latexmk) installed!
# to fix issues with font errors use: 
# updmap
.\make latexpdf

# doctests
.\make doctest
```