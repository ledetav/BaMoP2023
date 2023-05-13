const cells = document.querySelectorAll('[data-cell]');
const restartButton = document.querySelector('[data-restart]');
let currentPlayer = 'X';

function handleClick(event) {
  const cell = event.target;
  if (cell.textContent !== '') return;

  cell.textContent = currentPlayer;
  cell.classList.add(`game__cell--${currentPlayer}`);

  if (checkWin(currentPlayer)) {
    alert(`Игрок ${currentPlayer} выиграл!`);
    restartGame();
  } else if (isBoardFull()) {
    alert('Ничья!');
    restartGame();
  } else {
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
  }
}

function checkWin(player) {
  const winConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];

  return winConditions.some((condition) =>
    condition.every((index) => cells[index].textContent === player)
  );
}

function isBoardFull() {
  return [...cells].every((cell) => cell.textContent !== '');
}

function restartGame() {
  cells.forEach((cell) => {
    cell.textContent = '';
    cell.classList.remove('game__cell--X', 'game__cell--O');
  });
  currentPlayer = 'X';
}

cells.forEach((cell) => cell.addEventListener('click', handleClick));
restartButton.addEventListener('click', restartGame);