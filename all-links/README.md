<h1>Список сайтов из HTML-документа</h1>
<div id="ember1595" class="rich-text-viewer ember-view" data-ready=""><p>Вашей программе на вход подается ссылка на HTML файл.<br>Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <b>&lt;a ... href="..." ... &gt;</b> и вывести список сайтов, на которые есть ссылка.</p><p>Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида<br><b>&lt;a </b><b></b><b>href="../some_path/index.html"&gt;</b>.<b></b></p><p>Сайты следует выводить в алфавитном порядке.</p><p><b>Пример HTML </b><b>файла:<br></b></p><pre><b><code class="http"></code></b><code class="language-http hljs">&lt;<span class="hljs-attribute"><span class="hljs-attribute"><span class="hljs-attribute"><span class="hljs-attribute">a href="http://stepic.org/courses"&gt;
&lt;a href='https://stepic.org'&gt;
&lt;a href='http://neerc.ifmo.ru:1345'&gt;
&lt;a href="ftp://mail.ru/distib" &gt;
&lt;a href="ya.ru"&gt;
&lt;a href="www.ya.ru"&gt;
&lt;a href="../skip_relative_links"&gt;
</span></span></span></span></code><b><code class="http"><br></code></b></pre>

<p><b>Пример ответа:<br></b></p><pre><code class="language-http hljs"><span class="hljs-attribute"><span class="hljs-attribute"><span class="hljs-attribute"><span class="hljs-attribute">mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru</span></span></span></span></code></pre><br>
</div>