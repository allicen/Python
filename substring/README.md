<h1>Замена подстроки</h1>
<p>Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.</p>
<p>За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.</p>
<p>Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.</p>
<p>Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите Impossible.</p>
<p>Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, или Impossible, если операций потребуется более 1000.</p>
<p><strong>Sample Input 1:</strong></p>
<pre>
ababa
a
b
</pre>
<p><strong>Sample Output 1:</strong></p>
<pre>
1
</pre>
<p><strong>Sample Input 2:</strong></p>
<pre>
ababa
b
a
</pre>
<p><strong>Sample Output 2:</strong></p>
<p>1
<p><strong>Sample Input 3:</strong></p>
<pre>
ababa
c
c
</pre>
<p><strong>Sample Output 3:</strong></p>
<pre>
0
</pre>
<p><strong>Sample Input 4:</strong></p>
<pre>
ababac
c
c
</pre>
<p><strong>Sample Output 4:</strong></p>
<pre>
Impossible
</pre>