const quoteText = document.querySelector('.quote-generator__quote-text');
const quoteAuthor = document.querySelector('.quote-generator__quote-author');
const quoteButton = document.querySelector('.quote-generator__button');

quoteButton.addEventListener('click', () => {
  fetch('https://api.quotable.io/random')
    .then(response => response.json())
    .then(data => {
      quoteText.textContent = data.content;
      quoteAuthor.textContent = `- ${data.author}`;
    })
    .catch(error => {
      console.error('Ошибка получения цитаты:', error);
      quoteText.textContent = 'Произошла ошибка при получении цитаты';
      quoteAuthor.textContent = '';
    });
});

// Получить первую случайную цитату при загрузке страницы
quoteButton.click();