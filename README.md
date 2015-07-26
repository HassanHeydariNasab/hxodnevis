```html
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8">
	<title></title>
	<meta name="generator" content="LibreOffice 4.2.8.2 (Linux)">
	<meta name="created" content="0;0">
	<meta name="changed" content="20150726;211914485118599">
	<style type="text/css">
	<!--
		@page { margin: 2cm }
		p { margin-bottom: 0.25cm; line-height: 120% }
		pre.cjk { font-family: "Droid Sans Fallback", monospace }
		a:link { so-language: zxx }
	-->
	</style>
</head>
<body lang="zh-CN" dir="ltr">
<p align="right" style="margin-top: 0.42cm; margin-bottom: 0.21cm; line-height: 100%; page-break-after: avoid">
<font face="Droid Arabic Naskh"><font size="6" style="font-size: 28pt"><span lang="fa-IR"><b>خودنویس</b></span></font></font></p>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="fa-IR">این
یک اسکریپت پایتون است که می‌تواند به
همراه </span></font><font face="Droid Arabic Naskh"><span lang="en-US">gEdit
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">استفاده
شود </span></font><font face="Droid Arabic Naskh"><span lang="en-US">.</span></font></pre>
<pre class="ctl" align="right" style="background: transparent; font-weight: normal">
<span style="background: transparent"><font face="Droid Arabic Naskh"><span lang="fa-IR">هدف
این پروژه‌ی سرگرم‌کننده ، پیشنهاد
واژه‌های متداول پس از هر واژه است </span></font><font face="Droid Arabic Naskh"><span lang="en-US">.</span></span></font></pre>
<pre class="ctl" align="right"><br>
</pre>
<pre class="ctl" align="right" style="background: #dddddd"><span style="background: transparent"><font face="Droid Arabic Naskh"><span lang="fa-IR">پیش‌نیازها
</span></font><font face="Droid Arabic Naskh"><span lang="en-US">:</span></span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><span style="background: transparent"><font face="Droid Arabic Naskh"><span lang="fa-IR">ماژول‌های
پایتون </span></font><font face="Droid Arabic Naskh"><span lang="en-US">:</span></span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US"><span style="background: transparent">peewee</span></span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US"><span style="background: transparent">bs4</span></span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US"><span style="background: transparent">hazm</span></span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><span style="background: transparent"><font face="Droid Arabic Naskh"><span lang="fa-IR">دیگر
پیش‌نیازها </span></font><font face="Droid Arabic Naskh"><span lang="en-US">:</span></span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US"><span style="background: transparent">gxmessage</span></span></font></pre>
<pre class="ctl" align="right"><br>
</pre>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="fa-IR">این
برنامه برای استخراج واژه‌ها از
</span></font><font face="Droid Arabic Naskh"><span lang="en-US">farsnews.com
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">آزمایش
شده است </span></font><font face="Droid Arabic Naskh"><span lang="en-US">.
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">مثال
</span></font><font face="Droid Arabic Naskh"><span lang="en-US">:</span></font></pre>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="en-US"><a href="http://www.farsnews.com/newstext.php?nn=13940503000327"><span style="font-style: normal"><span style="text-decoration: none">http://www.farsnews.com/newstext.php?nn=13940503000327</span></span></a></span></font></pre>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="en-US"><i>(
</i></span></font><font face="Droid Arabic Naskh"><span lang="fa-IR"><i>هرگونه
ارتباط این برنامه با فارس‌نیوز و یا
هرکجای دیگر تکذیب می‌شود </i></span></font><font face="Droid Arabic Naskh"><span lang="en-US"><i>!
)</i></span></font></pre>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="fa-IR">برای
ایجاد پایگاه‌داده ، در پرونده‌ی
</span></font><font face="Droid Arabic Naskh"><span lang="en-US">parser.py
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">،
خط</span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US">#db.create_tables([Word])</span></font></pre>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="fa-IR">را
به</span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd">
<font face="Droid Arabic Naskh"><span lang="en-US">db.create_tables([Word])</span></font></pre>
<pre class="ctl" align="right"> <font face="Droid Arabic Naskh"><span lang="fa-IR">تغییر
دهید </span></font><font face="Droid Arabic Naskh"><span lang="en-US">.</span></font></pre>
<pre class="ctl" align="right"><font face="Droid Arabic Naskh"><span lang="fa-IR">پرونده‌ی
</span></font><font face="Droid Arabic Naskh"><span lang="en-US">HTML
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">مورد
نظر را برای استخراج واژه‌ها ، به شکل
زیر در  </span></font><font face="Droid Arabic Naskh"><span lang="en-US">parser.py
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">ذکر
کنید </span></font><font face="Droid Arabic Naskh"><span lang="en-US">:</span></font></pre>
<pre class="ctl" align="right" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US">f
= open(&quot;html/f.html&quot;)</span></font></pre>
<pre class="ctl" align="right" style="background: transparent"><font face="Droid Arabic Naskh"><span lang="fa-IR">برای
استفاده به همراه </span></font><font face="Droid Arabic Naskh"><span lang="en-US">gEdit
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">،
افزونه‌ی </span></font><font face="Droid Arabic Naskh"><span lang="en-US">external
tools </span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">را
فعال کنید و یک ابزار جدید با اسکریپت زیر
ایجاد کنید </span></font><font face="Droid Arabic Naskh"><span lang="en-US">:</span></font></pre>
<pre class="ctl" align="left" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US">#!/bin/sh
</span></font></pre>
<pre class="ctl" align="left" style="background: #dddddd"><font face="Droid Arabic Naskh"><span lang="en-US">python
$HOME/hxodnevis/gedit_tool.py $GEDIT_CURRENT_WORD
</span></font></pre>
<pre dir="rtl" class="ctl" align="right" style="background: transparent">
 <font face="Droid Arabic Naskh"><span lang="fa-IR">میانبر
مناسبی مانند </span></font><font face="Droid Arabic Naskh"><span lang="en-US"><span style="background: #eeeeee">=
+ CTRL</span><span style="background: transparent">  </span></span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">برای
آن قرار دهید و </span></font><font face="Droid Arabic Naskh"><span lang="en-US">Output
</span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">را
برابر </span></font><font face="Droid Arabic Naskh"><span lang="en-US">Insert
at cursor position </span></font><font face="Droid Arabic Naskh"><span lang="fa-IR">قرار
دهید </span></font><font face="Droid Arabic Naskh"><span lang="en-US">.
</span></font>
</pre>
</body>
</html>
```