<h1>Импорт модулей, работа с датами</h1>
<p>В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.<br>
Во второй строке дано одно число days -- число дней.</p>
<p>Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.</p>
<p>Примечание:</p>
<p>Для решения этой задачи используйте стандартный модуль datetime.</p>
<p>Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.</p>
<p><strong>Sample Input 1:</strong></p>
<pre>
2016 4 20
14
</pre>
<p><strong>Sample Output 1:</strong></p>
<pre>
2016 5 4
</pre>
<p><strong>Sample Input 2:</strong></p>
<pre>
2016 2 20
9
</pre>
<p><strong>Sample Output 2:</strong></p>
<pre>
2016 2 29
</pre>
<p><strong>Sample Input 3:</strong></p>
<pre>
2015 12 31
1
</pre>
<p><strong>Sample Output 3:</strong></p>
<pre>
2016 1 1
</pre>