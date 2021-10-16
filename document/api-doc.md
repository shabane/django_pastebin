<div dir='rtl'>

## api's

لیست و توضیح
api
های سایت

### متد های موجود
> تمامی
api
ها با
http
هستند و یک ریکوئست
get
می‌تواند آنها را صدا بزند.
>
> در جواب هر ریکوئست یک دیتا به صورت
json
بر گردانده می‌شود
>
> تمامی
api
ها به بزرگی و کوچکی حروف حساس هستند. و باید با حروف کوچک صدا زده شوند
>
> برای صدا زدن هر
api
باید قبل از نام متد آن کلمه
api
را نوشت.
برای مثال
```
api/gettext
```

<div dir='ltr'>

#### login
> درواقع این متد برای چک کردن درست بودن نام کاربری و رمز عبور استفاده می‌شود

| parameters | type | required | description |
|:----------:|:----:|:--------:|:-----------:|
| user | string | yes | username of the user |
| password | strint | yes | password of the user|
</br>

#### addtext
> برای اضافه کردن یک تکست جدید به کلیپ برد استفاده می‌شود

| parameters | type | required | description |
|:----------:|:----:|:--------:|:-----------:|
| user | string | yes | username of the user |
| password | strint | yes | password of the user|
| text | string | yes | the text that should save on the site |
</br>

#### delete
> برای حذف کردن یک متن استفاده می‌شود

| parameters | type | required | description |
|:----------:|:----:|:--------:|:-----------:|
| user | string | yes | username of the user |
| password | strint | yes | password of the user|
| id | int | yes | uniq id of a single text |
</br>

#### share
> برای گرفتن اشتراک یک متن استفاده می‌شود
> یک لینک از متن تولید و بازگردانده می‌شود

| parameters | type | required | description |
|:----------:|:----:|:--------:|:-----------:|
| user | string | yes | username of the user |
| password | strint | yes | password of the user|
| id | int | yes | uniq id of a single text |
</br>

#### checkchanges
> تمامی
id
های
text
هایی که کاربر دارد را باز‌ می‌گرداند

| parameters | type | required | description |
|:----------:|:----:|:--------:|:-----------:|
| user | string | yes | username of the user |
| password | strint | yes | password of the user|
</br>

#### gettext
> یک
ایدی
یا یک لیست
ایدی
می‌گیرد و
متن
های کاربر را باز می‌گرداند.
>
> برای دادن لیستی از
ایدی
باید چند بار
ایدی
را در آدرس تعریف کنید

| parameters | type | required | description |
|:----------:|:----:|:--------:|:-----------:|
| user | string | yes | username of the user |
| password | strint | yes | password of the user|
| id | int | yes | uniq id(s) of user text(s) |
</br>
</div>

</div>