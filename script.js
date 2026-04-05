let current = document.getElementById("current");
let previous = document.getElementById("previous");

let currentValue = "";
let operator = "";
let firstValue = "";

function addNumber(num) {
    if (num === "." && currentValue.includes(".")) return;
    currentValue += num;
    current.innerText = currentValue;
}

function addOperator(op) {
    if (currentValue === "") return;
    if (firstValue !== "") calculate();

    operator = op;
    firstValue = currentValue;
    previous.innerText = `${firstValue} ${operator}`;
    currentValue = "";
}

function calculate() {
    if (firstValue === "" || currentValue === "") return;

    let result;
    let a = Number(firstValue);
    let b = Number(currentValue);

    switch (operator) {
        case "+": result = a + b; break;
        case "-": result = a - b; break;
        case "*": result = a * b; break;
        case "/": result = b === 0 ? "Erro" : a / b; break;
        case "%": result = a * b / 100; break;
        default: return;
    }

    currentValue = result.toString();
    current.innerText = currentValue;
    previous.innerText = "";
    firstValue = "";
}

function clearAll() {
    currentValue = "";
    firstValue = "";
    operator = "";
    current.innerText = "0";
    previous.innerText = "";
}

function deleteLast() {
    currentValue = currentValue.slice(0, -1);
    current.innerText = currentValue || "0";
}

/* Teclado físico */
document.addEventListener("keydown", (e) => {
    if (!isNaN(e.key)) addNumber(e.key);
    if (["+", "-", "*", "/"].includes(e.key)) addOperator(e.key);
    if (e.key === "Enter") calculate();
    if (e.key === "Backspace") deleteLast();
    if (e.key === ".") addNumber(".");
});