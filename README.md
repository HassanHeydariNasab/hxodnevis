پیش‌نیازها :  
    ماژول‌های پایتون :  
        peewee  
        bs4  
        hazm  
    دیگر پیش‌نیازها :  
        gxmessage  

این برنامه اکنون توانایی استخراج واژه‌ها از farsnews.com را دارد . مثال :  
http://www.farsnews.com/newstext.php?nn=13940503000327  
برای ایجاد پایگاه‌داده ، در پرونده‌ی parser.py ، خط  
`#db.create_tables([Word])`   
را به  
 `db.create_tables([Word])`   
 تغییر دهید .
