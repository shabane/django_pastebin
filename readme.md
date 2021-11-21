# a pastebin site with django

at first i wanted to use this project for production purpose but i failed to write
desktop program as i wanted, so i decide to share this project to other for any usage
you want.


### concept

each user have thier own account, whene they login, they can save their text in site.
text will remain private until user click on the share button.
then shared text will got a link, links are a hash of the text it self.
whene a user click on a delete button, text will immediatly remove from data base.

pastebin sites are famouse for don't dont editing the text's.

and the last thing is that this site provide all the functions as API, so you can use
API of the site to add a text, share, delete and view a text.

site are avilable in both persian and english, to use it in persion, in the django url change
the template url to `template/per`

![pastebin](https://s4.uupload.ir/files/cmng_hnm6.jpg)


### API

if you need all the api method, you can download [api-doc.pdf](/document/api-doc.pdf)
all api and usage explained.

### how to run

1. so at fist clone the repo `git clone https://github.com/shabane/pastebin.git`
2. then if you have linux jsut cd to project dir and enter `./manage.py runserver`
3. the server run in `127.0.0.1:8000`, and just turn browser to this [url](127.0.0.1:8000).
