# Recobot

The aim of this project is to carry on object classification based on images published by "The occular engine" named "Archillect" on Twitter
Each 30 minutes, Archillect's last tweet is taken and recoBot answers to him with the proboability of what he recognizes according to him
To do so, a Raspberry server is connected to twitter using Twitter API. Each 30 minutes, it takes last Arhillect's tweet and gives it to
a neural network (deployed on the raspberry) using Tensorflow API (Tensorflow Lite).



## Getting started

* A PC (qui l'eut cru) running on Linux

* A Python3 interpreter

* Pip3 as Python package manager


## Prerequisites

#### In order to work, recobot needs some Python dependencies:

* Requests

* Tweepty

* Tensorflow

##### To do so, run the following command lines:

* <code>pip install requests</code>

* <code>pip install tweepy</code>

* <code>pip install tensorflow</code>




## About Tweepy

Tweepy is an API wich uses provides Twitter social network datas.

In order to use this API follow the steps to create a developer twitter account right <a href="https://realpython.com/twitter-bot-python-tweepy/#using-tweepyl">here


## Deployment

### Caution

You may need to use api keys to use Tweepy. The file bot.py imports another file called "apikey.py".
Those keys are the ones Twitter gave to you when you created your Twitter developer account. Hence, in order to make that project work you will have to
fill the list returned by key() with yours.

### Running
Once you edited apikey.py, run the following command line:

<code>python3 bot.py</code>

The project should now be running and printing informations of archillect in your console


# Author
Camille Bamboute (looking for a software engineer position)

### Tips
Bitcoin jar: 1NDCtru1eSm2H46HCPSaBGscNTKTLngbLe

Ethereum jar: 0x41Cd2f693Ac2673AcfA2B89a65E2E9DcD305b525

Dogecoin jar: D9JFfxeDesPfjjBCc7rh1eeS83n72o6Foq
