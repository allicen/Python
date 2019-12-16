<h1>Переход между HTML-документами</h1>
<div class="step-inner page-fragment">
    <div id="ember14541" class="rich-text-viewer ember-view" data-ready=""><p>Рассмотрим два HTML-документа <b>A </b>и <b>B.<br></b>Из <b>A</b> можно перейти <b></b>в <b>B </b>за один переход, если в <b>A </b>есть ссылка на <b>B</b>, т. е. внутри <b>A </b>есть тег <b>&lt;a href="B"&gt;</b>, возможно с дополнительными параметрами внутри тега.<br>Из <b>A</b> можно перейти в <b>B</b> за два перехода если существует такой документ <b>C</b>, что из <b>A </b>в <b>C </b>можно перейти за один переход и из <b>C </b>в <b>B</b> можно перейти за один переход.</p><p>Вашей программе на вход подаются две строки, содержащие url двух документов <b>A </b>и <b>B</b>.<br>Выведите <b>Yes</b>, если из <b>A </b>в <b>B </b>можно перейти за два перехода, иначе выведите <b>No</b>.</p><p>Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.</p>
</div>
      <div class="step-text-wrapper">
          <p class="step-text__limit-title">
            <strong>Sample Input 1:</strong>
          </p>
          <pre class="step-text__limit-value">https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output 1:</strong>
          </p>
          <pre class="step-text__limit-value">Yes</pre>
          <p class="step-text__limit-title">
            <strong>Sample Input 2:</strong>
          </p>
          <pre class="step-text__limit-value">https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output 2:</strong>
          </p>
          <pre class="step-text__limit-value">No</pre>
          <p class="step-text__limit-title">
            <strong>Sample Input 3:</strong>
          </p>
          <pre class="step-text__limit-value">https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html</pre>
          <p class="step-text__limit-title">
            <strong>Sample Output 3:</strong>
          </p>
          <pre class="step-text__limit-value">Yes</pre>

<!---->      </div>
  </div>