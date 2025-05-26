// https://opentdb.com/api_config.php : API for quiz

const _question = document.getElementById('question');
const _options = document.querySelector('.quiz-options');
const _checkBtn = document.getElementById('check-answer');
const _playAgainBtn = document.getElementById('play-again');
const _result = document.getElementById('result');
const _correctScore = document.getElementById('correct-score');
const _totalQuestion = document.getElementById('total-question');

let correctAnswer = "",
    correctScore = 0,
    askedCount = 0,
    totalQuestion = 10,
    questions = []; // <-- chứa danh sách 10 câu hỏi lấy từ API

// load câu hỏi từ API
async function loadQuestionFromAPI() {
    const APIUrl = 'https://opentdb.com/api.php?amount=10&category=31';
    const result = await fetch(APIUrl);
    const data = await result.json();
    questions = data.results;
    askedCount = 0;
    correctScore = 0;
    _result.innerHTML = "";
    setCount();
    showQuestion(questions[askedCount]);
}

// Hiển thị câu hỏi
function showQuestion(data) {
    _checkBtn.disabled = false;
    correctAnswer = HTMLDecode(data.correct_answer);
    let optionsList = [...data.incorrect_answers.map(HTMLDecode)];
    optionsList.splice(Math.floor(Math.random() * (optionsList.length + 1)), 0, correctAnswer);

    _question.innerHTML = `${HTMLDecode(data.question)} <br> <span class="category"> ${data.category} </span>`;
    _options.innerHTML = `
        ${optionsList.map((option, index) => `
            <li> ${index + 1}. <span>${option}</span> </li>
        `).join('')}
    `;
    selectOption();
}

// chọn đáp án
function selectOption() {
    _options.querySelectorAll('li').forEach(function(option) {
        option.addEventListener('click', function() {
            const selected = _options.querySelector('.selected');
            if (selected) selected.classList.remove('selected');
            option.classList.add('selected');
        });
    });
}

// kiểm tra đáp án
function checkAnswer() {
    _checkBtn.disabled = true;
    const selected = _options.querySelector('.selected');
    if (selected) {
        const selectedAnswer = selected.querySelector('span').textContent;
        if (selectedAnswer === correctAnswer) {
            correctScore++;
            _result.innerHTML = `<p><i class="fas fa-check"></i>Correct Answer!</p>`;
        } else {
            _result.innerHTML = `<p><i class="fas fa-times"></i>Incorrect Answer!</p> 
            <small><b>Correct Answer:</b> ${correctAnswer}</small>`;
        }
        checkCount();
    } else {
        _result.innerHTML = `<p><i class="fas fa-question"></i>Please select an option!</p>`;
        _checkBtn.disabled = false;
    }
}

// chuyển HTML entities về text bình thường
function HTMLDecode(textString) {
    const doc = new DOMParser().parseFromString(textString, "text/html");
    return doc.documentElement.textContent;
}

// xử lý sau mỗi lần trả lời
function checkCount() {
    askedCount++;
    setCount();
    if (askedCount === totalQuestion) {
        _result.innerHTML += `<p>Your score is ${correctScore} out of ${totalQuestion}.</p>`;
        _playAgainBtn.style.display = "block";
        _checkBtn.style.display = "none";
    } else {
        setTimeout(() => {
            showQuestion(questions[askedCount]);
            _result.innerHTML = "";
        }, 300);
    }
}

// cập nhật điểm & số câu đã hỏi
function setCount() {
    _totalQuestion.textContent = totalQuestion;
    _correctScore.textContent = correctScore;
}

// chơi lại
function restartQuiz() {
    _playAgainBtn.style.display = "none";
    _checkBtn.style.display = "block";
    _checkBtn.disabled = false;
    loadQuestionFromAPI();
}

// lắng nghe sự kiện
function eventListeners() {
    _checkBtn.addEventListener('click', checkAnswer);
    _playAgainBtn.addEventListener('click', restartQuiz);
}

document.addEventListener('DOMContentLoaded', function() {
    loadQuestionFromAPI();
    eventListeners();
});
