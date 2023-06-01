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

function playGame(playerChoice) {
    const computerChoice = getRandomChoice();
    const winner = determineWinner(playerChoice, computerChoice);
    let resultText = '';

    if (winner === 'draw') {
        resultText = `It's a draw! You both chose ${playerChoice}.`;
    } else if (winner === 'player') {
        resultText = `You win! ${playerChoice} beats ${computerChoice}.`;
    } else {
        resultText = `Computer wins! ${computerChoice} beats ${playerChoice}.`;
    }

    document.getElementById('result').innerText = resultText;
}