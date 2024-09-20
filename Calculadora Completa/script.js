let display = document.getElementById('display');
let operador = '';
let valor1 = '';
let valor2 = '';

function adicionarNumero(numero) {
    display.value += numero;
}

function adicionarOperador(op) {
    if (display.value === '' || operador !== '') return;
    valor1 = display.value;
    operador = op;
    display.value += ' ' + operador + ' '; 
}

function calcular() {
    if (valor1 === '' || display.value === '') return;
    
    valor2 = display.value.split(' ').pop();

    let resultado;
    switch (operador) {
        case '+':
            resultado = parseFloat(valor1) + parseFloat(valor2);
            break;
        case '-':
            resultado = parseFloat(valor1) - parseFloat(valor2);
            break;
        case '*':
            resultado = parseFloat(valor1) * parseFloat(valor2);
            break;
        case '/':
            if (parseFloat(valor2) === 0) {
                display.value = 'Erro';
                return;
            }
            resultado = parseFloat(valor1) / parseFloat(valor2);
            break;
        case '%':
            resultado = (parseFloat(valor1) * parseFloat(valor2)) / 100;
            break;
        default:
            return;
    }

    display.value = resultado;
    valor1 = resultado;
    operador = '';
}

function limpar() {
    display.value = '';
    valor1 = '';
    valor2 = '';
    operador = '';
}

function apagar() {
    display.value = display.value.slice(0, -1);
}

