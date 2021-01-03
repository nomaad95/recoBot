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
