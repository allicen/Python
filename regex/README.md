<h1>Регулярные выражения</h1>
<h2>Задание 1</h2>
<div id="ember4735" class="rich-text-viewer ember-view" data-ready=""><p>Вам дана последовательность строк.<br>Выведите строки, содержащие "<b>cat</b>" в качестве подстроки хотя бы два раза.</p><p><b>Примечание:</b><br>Считать все строки по одной из стандартного потока ввода вы можете, например, так<br></p>
<pre><code class="hljs arduino"><span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword"><span class="hljs-keyword">import</span></span></span></span> sys
<span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in">for</span></span></span></span> <span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in">line</span></span></span></span> in sys.stdin:
<span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in">line</span></span></span></span> = <span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in"><span class="hljs-built_in">line</span></span></span></span>.rstrip()
<span class="hljs-meta"><span class="hljs-meta"><span class="hljs-meta"><span class="hljs-meta"># process </span></span></span><span class="hljs-meta-keyword"><span class="hljs-meta"><span class="hljs-meta-keyword"><span class="hljs-meta"><span class="hljs-meta-keyword"><span class="hljs-meta"><span class="hljs-meta-keyword">line</span></span></span></span></span></span></span></span></code></pre>
</div>
<h2>Задание 2</h2>
<div class="step-wrapper">
<div class="step-inner page-fragment">
<div id="ember7142" class="rich-text-viewer ember-view" data-ready="">Вам дана последовательность строк.<br>Выведите строки, содержащие "<b>cat</b>" в качестве <b>слова</b>.<div><br></div><div><b>Примечание:</b><br></div><div><b></b>Для работы со словами используйте группы символов <b>\b</b> и <b>\B</b>.<br></div><div>Описание этих групп вы можете найти в <a href="https://docs.python.org/3.5/library/re.html" rel="nofollow noopener noreferrer" target="_blank">документации</a>.</div>
</div>
<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">cat
catapult and cat
catcat
concat
Cat
"cat"
!cat?
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">cat
catapult and cat
"cat"
!cat?</pre>

<!---->      </div>
</div>
</div>

<h2>Задание 3</h2>

<div class="step-inner page-fragment">
<div id="ember3038" class="rich-text-viewer ember-view" data-ready="">Вам дана последовательность строк.<div>Выведите строки, содержащие две буквы "<b>z</b>&#65279;", между которыми ровно три символа.</div>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">zabcz
zzxzz</pre>

<!---->      </div>
</div>

<h2>Задание 4</h2>
<div class="step-inner page-fragment">
<div id="ember3795" class="rich-text-viewer ember-view" data-ready="">Вам дана последовательность строк.<div>Выведите строки, содержащие обратный слеш "<b>\</b>&#65279;".</div>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">\w denotes word character
No slashes here
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">\w denotes word character</pre>

<!---->      </div>
</div>

<h2>Задание 5</h2>
<div class="step-inner page-fragment">
<div id="ember7632" class="rich-text-viewer ember-view" data-ready=""><p>Вам дана последовательность строк.<br>В каждой строке замените все вхождения подстроки "<b>human</b>" на подстроку "<b>computer</b>"<b></b>&#65279; и выведите полученные строки.</p>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">I need to understand the human mind
humanity
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">I need to understand the computer mind
computerity</pre>

<!---->      </div>
</div>

<h2>Задание 6</h2>
<div class="step-inner page-fragment">
    <div id="ember9157" class="rich-text-viewer ember-view" data-ready="">Вам дана последовательность строк.<br>В каждой строке замените <b>первое</b> вхождение <b>слова</b>, состоящего только из латинских букв "<b>a</b>" (регистр не важен), на слово "<b>argh</b>".<div><br></div><div><b>Примечание:</b></div><div><b></b>Обратите внимание на параметр <b>count</b> у функции <b>sub</b>.<br></div>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">There’ll be no more "Aaaaaaaaaaaaaaa"
AaAaAaA AaAaAaA
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">There’ll be no more "argh"
argh AaAaAaA</pre>

<!---->      </div>
</div>

<h2>Задание 7</h2>
<div class="step-inner page-fragment">
    <div id="ember10206" class="rich-text-viewer ember-view" data-ready="">Вам дана последовательность строк.<br>В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.<div>Буквой считается символ из группы <b>\w</b>.</div>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">this is a text
"this' !is. ?n1ce,
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">htis si a etxt
"htis' !si. ?1nce,</pre>

<!---->      </div>
</div>

<h2>Задание 8</h2>
<div class="step-inner page-fragment">
    <div id="ember15574" class="rich-text-viewer ember-view" data-ready="">Вам дана последовательность строк.<br>В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.<div>Буквой считается символ из группы <b>\w</b>.<br></div>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">attraction
buzzzz
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
<pre class="step-text__limit-value">atraction
buz</pre>

<!---->      </div>
</div>

<h2>Задание 9</h2>
<div class="step-inner page-fragment">
    <div id="ember18331" class="rich-text-viewer ember-view" data-ready=""><p>Вам дана последовательность строк.<br><span>Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).</span></p>
</div>

<div class="step-text-wrapper">
<p class="step-text__limit-title">
<strong>Sample Input<!---->:</strong>
</p>
<pre class="step-text__limit-value">blabla is a tandem repetition
123123 is good too
go go
aaa
</pre>
<p class="step-text__limit-title">
<strong>Sample Output<!---->:</strong>
</p>
          <pre class="step-text__limit-value">blabla is a tandem repetition
123123 is good too</pre>

<!---->      </div>
  </div>