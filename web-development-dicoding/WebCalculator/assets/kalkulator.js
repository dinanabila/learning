const calculator = {
    displayNumber: '0',
    operator: null,
    firstNumber: null,
    isWaitForSecondNumber: false,
}

//mengupdate angka pada layar
function updateDisplay() {
    document.querySelector('#displayNumber').innerText = calculator.displayNumber;
}

//menghapus data pada kalkulator
function clearCalculator() {
    calculator.displayNumber = '0';
    calculator.operator = null;
    calculator.firstNumber = null;
    calculator.isWaitForSecondNumber = false;
}

//memasukkan angka ke dalam nilai displayNumber kalkulator
function inputDigit(digit) {
    if (calculator.displayNumber === '0') {
        calculator.displayNumber = digit;
    }
    else {
        calculator.displayNumber += digit;
    }
}

function inverseNumber() {
    if(calculator.displayNumber === '0') {
        return;
    }
    calculator.displayNumber = calculator.displayNumber * -1;
}

function handleOperator(operator) {
    if(!calculator.isWaitForSecondNumber){
        calculator.operator = operator;
        calculator.isWaitForSecondNumber = true;
        calculator.firstNumber = calculator.displayNumber;
        //mengatur ulang nilai displayNumber supaya jadi 0 lagi
        calculator.displayNumber = '0';
    }
    else{
        alert('Operator sudah ditetapkan');
    }
}

function performCalculation() {
    if(calculator.firstNumber == null || calculator.operator == null) {
        alert('Anda belum menetapkan operator');
        return;
    }

    let result = 0;
    if(calculator.operator === '+') {
        result = parseInt(calculator.firstNumber) + parseInt(calculator.displayNumber);
    }
    else {
        result = parseInt(calculator.firstNumber) - parseInt(calculator.displayNumber);
    }
    // objek yang akan dikirimkan sebagai argumen fungsi putHistory()
    const history = {
        firstNumber: calculator.firstNumber,
        secondNumber: calculator.displayNumber,
        operator: calculator.operator,
        result: result
    }
    putHistory(history);
    calculator.displayNumber = result;
    renderHistory();
}

//menangkap semua elemen div.button dan memberikan event click pada setiap elemennya
const buttons = document.querySelectorAll('.button');

for (const button of buttons) {
    button.addEventListener('click', function (event) {
        //mendapatkan objek elemen yang diklik
        const target = event.target;

        if(target.classList.contains('clear')) {
            clearCalculator();
            updateDisplay();
            return;
        }

        if (target.classList.contains('negative')) {
            inverseNumber();
            updateDisplay();
            return;
        }

        if (target.classList.contains('equals')) {
            performCalculation();
            updateDisplay();
            return;
        }

        if (target.classList.contains('operator')) {
            handleOperator(target.innerText);
            updateDisplay();
            return;
        }

        inputDigit(target.innerText);
        updateDisplay();
    });
}