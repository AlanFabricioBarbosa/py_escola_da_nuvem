# Exercícios Python - Atividades de Programação

Este repositório é uma lista de atividades em Python proposta pela Escola da Nuvem e contém uma coleção de exercícios organizados em três categorias principais, que vão desde conceitos básicos até programas interativos mais avançados.

## Estrutura do Projeto

```
py_edn/
├── Atividade_01/          # Exercícios básicos
├── Atividade_02/          # Cálculos e conversões
├── Atividade_03/          # Programas interativos
└── README.md             # Este arquivo
```

## Objetivo

Desenvolver habilidades fundamentais em Python através de exercícios práticos que abordam:
- Variáveis e tipos de dados
- Operações matemáticas
- Estruturas condicionais
- Entrada e saída de dados
- Validação e tratamento de erros
- Boas práticas de programação

---

## Atividade_01 - Exercícios Básicos

### 1. **greeting.py** - Programa de Saudação
```python
print("Olá, mundo!")
```
**Conceitos:** Função `print()`, strings

### 2. **sum_calculator.py** - Calculadora de Soma
```python
number1 = 12
number2 = 14
sum_result = number1 + number2
print(f"A soma de {number1} + {number2} = {sum_result}")
```
**Conceitos:** Variáveis, operações aritméticas, f-strings

### 3. **volume_calculator.py** - Calculadora de Volume
```python
length = 12 
width = 14 
height = 20 
volume = length * width * height
```
**Conceitos:** Multiplicação, cálculo de volume, formatação de saída

### 4. **total_price_calculator.py** - Calculadora de Preço Total
```python
product_name = "Cadeira Infantil"
unit_price = 12.40
quantity = 3
total_price = unit_price * quantity
```
**Conceitos:** Variáveis string e float, cálculos comerciais, formatação de moeda

---

##  Atividade_02 - Cálculos e Conversões

### 1. **currency_converter.py** - Conversor de Moeda
Converte valores em reais para dólares e euros usando taxas de câmbio fixas.
**Conceitos:** Divisão, conversão de moedas, formatação de números

### 2. **discount_calculator.py** - Calculadora de Desconto
Calcula descontos percentuais em produtos.
**Conceitos:** Porcentagem, subtração, cálculos comerciais

### 3. **school_average_calculator.py** - Calculadora de Média Escolar
Calcula a média aritmética de três notas.
**Conceitos:** Média aritmética, divisão, formatação decimal

### 4. **fuel_consumption_calculator.py** - Calculadora de Consumo de Combustível
Calcula o consumo médio de combustível (km/l).
**Conceitos:** Eficiência, divisão, formatação de resultados

---

##  Atividade_03 - Programas Interativos

### 1. **age_classifier.py** - Classificador de Idade
Classifica usuários por faixa etária:
-  Criança (0-12 anos)
-  Adolescente (13-17 anos)
-  Adulto (18-59 anos)
-  Idoso (60+ anos)

**Conceitos:** `input()`, `if/elif/else`, conversão de tipos

### 2. **bmi_calculator.py** - Calculadora de IMC 
**Versão Aprimorada** com validações e recursos avançados:

#### Funcionalidades:
-  Validação de entrada (peso e altura)
-  Tratamento de erros com `try/except`
-  Classificação detalhada do IMC (6 categorias)
-  Recomendações de saúde personalizadas
-  Interface visual com emojis
-  Tabela de referência completa
-  Organização em funções

####  Classificações IMC:
| IMC | Classificação | Emoji |
|-----|---------------|-------|
| < 18.5 | Abaixo do peso | 🔵 |
| 18.5 - 24.9 | Peso normal | 🟢 |
| 25.0 - 29.9 | Sobrepeso | 🟡 |
| 30.0 - 34.9 | Obesidade grau I | 🟠 |
| 35.0 - 39.9 | Obesidade grau II | 🔴 |
| ≥ 40.0 | Obesidade grau III | 🔴 |

**Conceitos:** Funções, validação, tratamento de exceções, estruturas condicionais aninhadas

### 3. **temperature_converter.py** - Conversor de Temperatura
Converte entre Celsius, Fahrenheit e Kelvin.

#### 🌡️ Fórmulas utilizadas:
- **Celsius para Fahrenheit:** `F = C × 9/5 + 32`
- **Celsius para Kelvin:** `K = C + 273.15`
- **Fahrenheit para Celsius:** `C = (F - 32) × 5/9`
- **Kelvin para Celsius:** `C = K - 273.15`

**Conceitos:** Conversões matemáticas, estruturas condicionais, métodos de string

### 4. **leap_year_checker.py** - Verificador de Ano Bissexto
Determina se um ano é bissexto usando as regras:
-  Divisível por 4 **E**
-  **NÃO** divisível por 100 **OU** divisível por 400

**Conceitos:** Operadores lógicos, módulo (`%`), lógica booleana

---

##  Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado
- Terminal/Command Prompt

### Execução Individual
```bash
# Navegar para a pasta desejada
cd Atividade_01
cd Atividade_02
cd Atividade_03

# Executar um programa específico
python nome_do_arquivo.py
```

### Exemplos:
```bash
# Executar calculadora de IMC aprimorada
cd Atividade_03
python bmi_calculator.py

# Executar conversor de temperatura
python temperature_converter.py

# Executar calculadora de desconto
cd ../Atividade_02
python discount_calculator.py
```

---

##  Conceitos Python Abordados

| Conceito | Descrição | Arquivos |
|----------|-----------|----------|
| **Variáveis** | Armazenamento de dados | Todos |
| **Tipos de Dados** | int, float, string | Todos |
| **Operações Aritméticas** | +, -, *, / | Atividade_01, 02 |
| **F-strings** | Formatação de strings | Todos |
| **Input/Output** | `input()`, `print()` | Atividade_03 |
| **Condicionais** | `if`, `elif`, `else` | Atividade_03 |
| **Funções** | Definição e chamada | bmi_calculator.py |
| **Tratamento de Erros** | `try/except` | bmi_calculator.py |
| **Validação** | Verificação de entrada | bmi_calculator.py |
| **Operadores Lógicos** | `and`, `or`, `not` | leap_year_checker.py |

---

## 🎓 Nível de Dificuldade

| Pasta | Nível | Descrição |
|-------|-------|-----------|
| **Atividade_01** | 🟢 Iniciante | Conceitos básicos, sem interação |
| **Atividade_02** | 🟡 Intermediário | Cálculos mais complexos |
| **Atividade_03** | 🔴 Avançado | Interação, validação, estruturas |

---

##  Próximos Passos

Para continuar aprendendo Python, considere estudar:
-  Listas e dicionários
-  Estruturas de repetição (`for`, `while`)
-  Manipulação de arquivos
-  APIs e requests
-  Interfaces gráficas (tkinter)
-  Análise de dados (pandas, matplotlib)

---

##  Contribuição

Sinta-se à vontade para:
-  Reportar bugs
-  Sugerir melhorias
-  Propor novos exercícios
-  Melhorar a documentação

---

##  Licença

Este projeto é livre para uso educacional e pessoal.

---
