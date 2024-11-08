

SELECT

COUNT(IF(login_time BETWEEN '7:00:00' AND '9:00:00' OR login_time BETWEEN '18:00:00' AND '20:00:00', TRUE, NULL)) AS '通勤',

COUNT(IF(login_time BETWEEN '11:00:00' AND '13:00:00', TRUE, NULL)) AS '午休',

COUNT(IF(login_time BETWEEN '22:00:00' AND '24:00:00' OR login_time BETWEEN '00:00:00' AND '1:00:00', TRUE, NULL)) AS '临睡'

FROM login_tb

WHERE DATE_FORMAT(login_date, '%Y-%m')='2021-07';

step1:查找各个时间段的用户数；

step2:通过where限定时间为2021年7月。

IF函数是常用到的条件函数，格式为：if(x=n,a,b)，x=n代表判断条件，如果x=n时，返回结果为a，否则返回b。

OR为逻辑运算符，当所有条件中有取值为真的条件时，结果即为真。

as用法用于对返回的列结果进行重命名；