<div dir=rtl>
#خودنویس  
این یک اسکریپت پایتون است که می‌تواند به همراه gEdit استفاده شود .  
هدف این پروژه‌ی سرگرم‌کننده ، پیشنهاد واژه‌های متداول پس از هر واژه است .  

##پیش‌نیازها  
ماژول‌های پایتون :  
peewee  
bs4  
hazm  
دیگر پیش‌نیازها :  
gxmessage  

##راهنما  
این برنامه برای استخراج واژه‌ها از farsnews.com آزمایش شده است .مثال :  
http://www.farsnews.com/newstext.php?nn=13940503000327  
( هرگونه ارتباط این برنامه با فارس‌نیوز و یا هرکجای دیگر تکذیب می‌شود ! )  
برای ایجاد پایگاه‌داده ، در پرونده‌ی parser.py ، خط  
</div>
<div dir=ltr>
`#db.create_tables([Word])`  
</div>
<div dir=rtl>
را به  
</div>
<div dir=ltr>
`db.create_tables([Word])`  
</div>
<div dir=rtl>
تغییر دهید .  
پرونده‌ی HTML مورد نظر را برای استخراج واژه‌ها ، به شکل زیر در parser.py ذکر کنید :  
</div>
<div dir=ltr>
`f = open("html/f.html")`  
</div>
<div dir=rtl>
برای استفاده به همراه gEdit ، افزونه‌ی external tools را فعال کنید و یک ابزار جدید با اسکریپت زیر ایجاد کنید :  
</div>
<div dir=ltr>
```bash
#!/bin/sh
python $HOME/hxodnevis/gedit_tool.py $GEDIT_CURRENT_WORD
```  
</div>
<div dir=rtl>
میانبر مناسبی مانند = + CTRL  برای آن قرار دهید و Output را برابر Insert at cursor position قرار دهید .  
</div>
