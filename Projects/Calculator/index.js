// Получаем элементы дисплея и кнопок
const display = document.querySelector('.calculator__display-input')
const buttons = document.querySelectorAll('.calculator__button')

display.disabled = true;

// Переменные для выражения и результата
let expression = ''
let result = ''

// Функция для расчета выражения
const calculate = () => {
  try {
    result = eval(expression) || ''
    display.value = result
  } catch (e) {
    alert('Ошибка при расчёте')
  }
}

const hasMathOperation = () => {
    return /[+\-*/]/.test(expression)
}

// Обработка нажатия кнопок
buttons.forEach((button) => {
  button.addEventListener('click', () => {
    // Получаем значение кнопки
    const buttonValue = button.value

    switch (buttonValue) {
      case '=': {
        if(hasMathOperation()){
            calculate()
            expression = ''
        } else {
            alert("Необходимо, чтобы выражение имело хотя бы одну математичсекую опреацию.")
        }
        break
      }
      case 'C': {
        expression = ''
        result = ''
        display.value = ''
        break
      }
      default: {
        expression += buttonValue
        display.value = expression
        break
      }
    }
  })
})

//запрет на нажатие кнопки равно, если не введена хотя бы одна мат. операция. 