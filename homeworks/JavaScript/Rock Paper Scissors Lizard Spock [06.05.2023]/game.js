const score = {
    player: 0,
    computer: 0,
    draws: 0
};

function updateScoreDisplay() {
    document.getElementById('score').innerText = `Player: ${score.player} | Computer: ${score.computer} | Draws: ${score.draws}`;
}

function getRandomChoice() {
    const choices = ['rock', 'paper', 'scissors', 'lizard', 'spock'];
    return choices[Math.floor(Math.random() * choices.length)];
}

function determineWinner(playerChoice, computerChoice) {
    const rules = {
        rock: ['scissors', 'lizard'],
        paper: ['rock', 'spock'],
        scissors: ['paper', 'lizard'],
        lizard: ['spock', 'paper'],
        spock: ['scissors', 'rock']
    };

    if (playerChoice === computerChoice) {
        return 'draw';
    } else if (rules[playerChoice].includes(computerChoice)) {
        return 'player';
    } else {
        return 'computer';
    }
}

function saveScoreToJson() {
    const scoreJson = JSON.stringify(score);
    const blob = new Blob([scoreJson], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'score.json';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

function playGame(playerChoice) {
    const computerChoice = getRandomChoice();
    const winner = determineWinner(playerChoice, computerChoice);
    let resultText = '';

    if (winner === 'draw') {
        resultText = `It's a draw! You both chose ${playerChoice}.`;
        score.draws++;
    } else if (winner === 'player') {
        resultText = `You win! ${playerChoice} beats ${computerChoice}.`;
        score.player++;
    } else {
        resultText = `Computer wins! ${computerChoice} beats ${playerChoice}.`;
        score.computer++;
    }

    document.getElementById('result').innerText = resultText;
    updateScoreDisplay();
}

const saveButton = document.getElementById('save-button');
saveButton.addEventListener('click', saveScoreToJson);