# a pastebin site with django

At first, I wanted to use this project for production purposes but I failed to write a desktop program as I wanted, so I decided to share this project with others for any usage they want.


### concept

Each user has their own account, when they login, they can save their text on the site.
Text will remain private until the user clicks on the share button.
Then the shared text will get a link, links are a hash of the text itself.
When a user clicks on a delete button, the text will be immediately removed from the database.

pastebin sites are famous for not editing the texts.

and the last thing is that this site provides all the functions as API, so you can use
API of the site to add a text, share, delete and, view a text.

site are avilable in both persian and english, to use it in persion, in the django url change
the template url to `template/per`



### API

if you need all the API methods, you can download [api-doc.pdf](/document/api-doc.pdf)
all API and usage explained.

### how to run

1. so at fist clone the repo `git clone https://github.com/shabane/pastebin.git`
2. then if you have linux just cd to project dir and enter `./manage.py runserver`
3. the server will run in `127.0.0.1:8000`, and just open this [url](127.0.0.1:8000) in your browser.

### screenshot
> Home page
> ![pastebin](https://s4.uupload.ir/files/1_5yj.png)

> Logout
> ![pastebin](https://s4.uupload.ir/files/3_bn4c.png)

> Login
> ![pastebin](https://s4.uupload.ir/files/4_p4z6.png)

> Singup
> ![pastebin](https://s4.uupload.ir/files/5_ac24.png)

> Adding Text page
> ![pastebin](https://s4.uupload.ir/files/2_zmiv.png)
