<div dir=rtl>
<h1>خودنویس</h1>
این یک اسکریپت پایتون است که می‌تواند به همراه gEdit استفاده شود .<br>
هدف این پروژه‌ی سرگرم‌کننده ، پیشنهاد واژه‌های متداول پس از هر واژه است .<br>

<h2>پیش‌نیازها</h2>
ماژول‌های پایتون :<br>
peewee<br>
bs4<br>
hazm<br>
دیگر پیش‌نیازها : <br>
gxmessage<br>

<h2>راهنما</h2>
این برنامه برای استخراج واژه‌ها از farsnews.com آزمایش شده است .مثال : <br>
http://www.farsnews.com/newstext.php?nn=13940503000327<br>
( هرگونه ارتباط این برنامه با فارس‌نیوز و یا هرکجای دیگر تکذیب می‌شود ! )<br>
برای ایجاد پایگاه‌داده ، در پرونده‌ی parser.py ، خط<br>
</div>

```python
#db.create_tables([Word])
```  

<div dir=rtl>
را به<br>
</div>
```python
db.create_tables([Word])
```  
<div dir=rtl>
تغییر دهید .<br>
پرونده‌ی HTML مورد نظر را برای استخراج واژه‌ها ، به شکل زیر در parser.py ذکر کنید :<br>
</div>
```python
f = open("html/f.html")`  
```
<div dir=rtl>
برای استفاده به همراه gEdit ، افزونه‌ی external tools را فعال کنید و یک ابزار جدید با اسکریپت زیر ایجاد کنید :<br>
</div>
```bash
#!/bin/sh
python $HOME/hxodnevis/gedit_tool.py $GEDIT_CURRENT_WORD
```
<div dir=rtl>
میانبر مناسبی مانند = + CTRL  برای آن قرار دهید و Output را برابر Insert at cursor position قرار دهید .<br>
</div>
