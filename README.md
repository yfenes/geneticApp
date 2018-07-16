**NOTE: This project is currently in active development.**

# geneticApp

Genetic App will be a web app trying to find the optimum DNA (a sentence) over generations with simple genetic algorithm.


## Backend Development

### OS X

**install python3 and pip3**
```
brew install python3
curl https://bootstrap.pypa.io/get-pip.py | python3
python3 # make sure this works
pip3 # make sure this works 
```

**Make sure you add pip3 package bindir to your path (required for running virtualenv later on)**

```
export PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.7/bin
```

**Note that it should be your python version. For example if you have 3.6 you should write:**

```
export PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.6/bin
```


**If you don't have the repository clone it:**

```
git clone https://github.com/yfenes/geneticApp.git
```

**Go to directory**

```
cd geneticApp
```

**Install virtualenv**
```
pip3 install virtualenv

```


**Create the virtual environment**

```
virtualenv geneticappenv
```

**Get inside the virtual environment**

```
source geneticappenv/bin/activate
```

**Install django**

```
pip install Django
```


**Make sure that django is installed**

```
pip freeze | grep Django
```


**Make sure everything is working**

```
cd training
python manage.py runserver
```

**Go to**

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

