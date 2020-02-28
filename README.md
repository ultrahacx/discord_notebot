## Discord NoteBot

This is a simple Discord NoteBot written in Python3 and uses Discord.py API.
This is self-deployment bot any you need to manually host it on your servers in order to make it work.
This repository is built in such a way to directly deploy the heroku hosting service.

## Usage of bot 

- !help : Shows the list of available command

- !showlist : Shows the list of available notes in the database

- !showname {notename} : Shows the full note 

- !addnote {notename} {notedetail} : Adds a new note to the database

- !deletenote {notename} : Deletes a single note

- !deletedb : Deletes all the database i.e. deletes all the saved command 

## How to deploy the bot

* **Step 1:** Make a new application on Discord and change the token in bot.py 

* **Step 1:** git clone https://github.com/ultrahacx/discord_notebot.git

* **Step 2:** Download Heroku CLI [here] (https://devcenter.heroku.com/articles/heroku-cli) and install it.

* **Setp 3:** cd discord_notebot

* **Setp 4:** heroku login

* **Setp 5:** heroku git:clone -a NAME_OF_APP_ON_HEROKU

* **Setp 6:** git add .

* **Setp 7:** git commit -am "First commit | Deployment 1"

* **Setp 8:** git push heroku master
