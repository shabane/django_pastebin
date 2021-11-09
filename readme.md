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

site are avilable in persian and english, to use it in english in the django url change
the template url from `template/per/` to `template`



### API

if you need all the api method, you can download [api-doc.pdf](/document/api-doc.pdf)
all api and usage explained.

### how to run

1. so at fist clone the repo `git clone https://github.com/shabane/pastebin.git`
2. then if you have linux jsut cd to project dir and enter `./manage.py runserver`
3. the server run in `127.0.0.1:8000`, and just turn browser to this [url](127.0.0.1:8000).

### screenshot
> Home page
> ![pastebin](https://s4.uupload.ir/files/cmng_hnm6.jpg)

> Logout
> ![pastebin](https://s4.uupload.ir/files/logout_hg8g.jpg)

> Login
> ![pastebin](https://s4.uupload.ir/files/singin_fzf7.jpg)

> Singup
> ![pastebin](https://s4.uupload.ir/files/singup_8xe.jpg)

> Adding Text page
> ![pastebin](https://s4.uupload.ir/files/addtext_xku.jpg)
