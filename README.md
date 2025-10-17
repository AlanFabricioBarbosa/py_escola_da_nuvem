# 🐍 Exercícios Python - Atividades de Programação

Este repositório contém uma coleção completa de exercícios Python organizados em seis atividades progressivas, desde conceitos básicos até integração com APIs externas.

## 📁 Estrutura do Projeto

```
py_edn/
├── 📂 Atividade_01/          # Exercícios básicos
│   ├── greeting.py
│   ├── sum_calculator.py
│   ├── volume_calculator.py
│   └── total_price_calculator.py
├── 📂 Atividade_02/          # Cálculos e conversões
│   ├── currency_converter.py
│   ├── discount_calculator.py
│   ├── school_average_calculator.py
│   └── fuel_consumption_calculator.py
├── 📂 Atividade_03/          # Programas interativos
│   ├── age_classifier.py
│   ├── bmi_calculator.py
│   ├── temperature_converter.py
│   └── leap_year_checker.py
├── 📂 Atividade_04/          # Estruturas de controle e loops
│   ├── calculator.py
│   ├── grade_manager.py
│   ├── password_validator.py
│   └── number_analyzer.py
├── 📂 Atividade_05/          # Funções avançadas
│   ├── tip_calculator.py
│   ├── palindrome_checker.py
│   ├── discount_calculator.py
│   └── days_alive_calculator.py
├── 📂 Atividade_06/          # APIs e bibliotecas externas
│   ├── password_generator.py
│   ├── random_user_api.py
│   ├── cep_lookup.py
│   └── currency_lookup.py
├── 📄 requirements.txt
└── 📄 README.md
```

## 🎯 Objetivo

Desenvolver habilidades fundamentais e avançadas em Python através de exercícios práticos que abordam:
- **Básico**: Variáveis, tipos de dados, operações matemáticas
- **Interativo**: Estruturas condicionais, entrada e saída de dados
- **Estruturas de Controle**: Loops, funções, tratamento de erros
- **Funções Avançadas**: Manipulação de strings, datas, validações
- **APIs Externas**: Requisições HTTP, JSON, integração com serviços
- **Boas Práticas**: Validação robusta, código limpo, documentação

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

## 📂 Atividade_04 - Estruturas de Controle e Loops

### 1. **calculator.py** - Calculadora Completa
Calculadora interativa com operações básicas (+, -, *, /) e menu de opções.
**Conceitos:** Funções, loops `while`, tratamento de erros, menu interativo

### 2. **grade_manager.py** - Sistema de Notas
Sistema para registrar notas de alunos e calcular estatísticas da turma.
**Conceitos:** Listas, loops, estatísticas, aprovação/reprovação

### 3. **password_validator.py** - Validador de Senha
Verifica se senhas atendem critérios de segurança (8+ caracteres, números).
**Conceitos:** Regex, validação, análise de string, critérios de segurança

### 4. **number_analyzer.py** - Analisador de Números
Classifica números como pares/ímpares e gera relatórios estatísticos.
**Conceitos:** Análise matemática, contadores, classificação, relatórios

---

## 📂 Atividade_05 - Funções Avançadas

### 1. **tip_calculator.py** - Calculadora de Gorjeta
Calcula gorjetas de restaurante baseada no valor e porcentagem desejada.
**Conceitos:** Funções com parâmetros/retorno, documentação, cálculos financeiros

### 2. **palindrome_checker.py** - Verificador de Palíndromo
Verifica se palavras/frases são palíndromos, ignorando espaços e pontuação.
**Conceitos:** Manipulação de strings, regex, algoritmos de comparação

### 3. **discount_calculator.py** - Calculadora de Desconto
Calcula preço final após aplicar desconto percentual com formatação.
**Conceitos:** Cálculos percentuais, formatação de moeda, funções reutilizáveis

### 4. **days_alive_calculator.py** - Contador de Dias de Vida
Calcula quantos dias uma pessoa está viva baseado na data de nascimento.
**Conceitos:** Módulo `datetime`, cálculos temporais, validação de datas

---

## 📂 Atividade_06 - APIs e Bibliotecas Externas

### 1. **password_generator.py** - Gerador de Senhas
Gera senhas aleatórias seguras com opções personalizáveis de caracteres.
**Conceitos:** Módulo `random`, `string`, análise de força de senha

### 2. **random_user_api.py** - API de Usuários Fictícios
Consulta a API RandomUser para obter dados de usuários fictícios.
**Conceitos:** Biblioteca `requests`, JSON, tratamento de erros de API

### 3. **cep_lookup.py** - Consulta de CEP
Consulta informações de CEP usando a API ViaCEP (endereço, cidade, estado).
**Conceitos:** API REST, validação de CEP, regex para formatação

### 4. **currency_lookup.py** - Cotação de Moedas
Consulta cotações de moedas em tempo real via AwesomeAPI.
**Conceitos:** APIs financeiras, análise de dados, formatação de data/hora

---

##  Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado
- Terminal/Command Prompt
- Para Atividade_06: `pip install requests`

### Execução Individual
```bash
# Navegar para a pasta desejada
cd Atividade_01  # Exercícios básicos
cd Atividade_02  # Cálculos e conversões
cd Atividade_03  # Programas interativos
cd Atividade_04  # Estruturas de controle
cd Atividade_05  # Funções avançadas
cd Atividade_06  # APIs externas

# Executar um programa específico
python nome_do_arquivo.py
```

### Exemplos de Execução:
```bash
# Atividade_01 - Básicos
cd Atividade_01
python greeting.py

# Atividade_03 - Interativos  
cd Atividade_03
python bmi_calculator.py
python temperature_converter.py

# Atividade_04 - Estruturas de Controle
cd Atividade_04
python calculator.py
python grade_manager.py

# Atividade_05 - Funções Avançadas
cd Atividade_05
python tip_calculator.py
python days_alive_calculator.py

# Atividade_06 - APIs (requer biblioteca 'requests')
cd Atividade_06
pip install requests
python currency_lookup.py
python cep_lookup.py
```

### Instalação de Dependências
```bash
# Para atividades que usam APIs externas
pip install -r requirements.txt
```

---

## 📚 Conceitos Python Abordados

| Conceito | Descrição | Arquivos |
|----------|-----------|----------|
| **Variáveis** | Armazenamento de dados | Todas as atividades |
| **Tipos de Dados** | int, float, string, bool | Todas as atividades |
| **Operações Aritméticas** | +, -, *, /, %, ** | Atividades 01, 02, 04, 05 |
| **F-strings** | Formatação de strings | Todas as atividades |
| **Input/Output** | `input()`, `print()` | Atividades 03, 04, 05, 06 |
| **Condicionais** | `if`, `elif`, `else` | Atividades 03, 04, 05 |
| **Loops** | `while`, `for`, controle de fluxo | Atividades 04, 05 |
| **Funções** | Definição, parâmetros, retorno | Atividades 04, 05 |
| **Listas** | Criação, manipulação, iteração | Atividades 04, 05 |
| **Tratamento de Erros** | `try/except`, validação | Atividades 03, 04, 05, 06 |
| **Regex** | Expressões regulares | Atividades 04, 05, 06 |
| **Módulo Random** | Geração de números/dados aleatórios | Atividade 06 |
| **Módulo Datetime** | Manipulação de datas e horários | Atividades 05, 06 |
| **Requests HTTP** | APIs REST, JSON | Atividade 06 |
| **Validação** | Verificação robusta de entrada | Atividades 04, 05, 06 |
| **Operadores Lógicos** | `and`, `or`, `not` | Atividades 03, 04, 05 |

---

## 🎓 Nível de Dificuldade

| Pasta | Nível | Descrição |
|-------|-------|-----------|
| **Atividade_01** | 🟢 Iniciante | Conceitos básicos, sem interação |
| **Atividade_02** | � Iniciante | Cálculos simples, formatação |
| **Atividade_03** | � Intermediário | Interação, validação, estruturas condicionais |
| **Atividade_04** | 🟡 Intermediário | Loops, funções, estruturas de controle |
| **Atividade_05** | 🟠 Avançado | Funções complexas, manipulação de dados |
| **Atividade_06** | 🔴 Especialista | APIs externas, bibliotecas, integração |

---

##  Próximos Passos

Após completar todas as atividades, você terá uma base sólida em Python! Para continuar evoluindo:

### 🔥 **Conceitos Avançados**
-  **Programação Orientada a Objetos (POO)**: Classes, objetos, herança
-  **Estruturas de Dados**: Pilhas, filas, árvores, grafos
-  **Algoritmos**: Ordenação, busca, recursão
-  **Decorators e Context Managers**: Funcionalidades avançadas

### 📊 **Análise de Dados**
-  **Pandas**: Manipulação de dados tabulares
-  **NumPy**: Computação científica
-  **Matplotlib/Seaborn**: Visualização de dados
-  **Jupyter Notebooks**: Ambiente interativo

### 🌐 **Desenvolvimento Web**
-  **Flask/Django**: Frameworks web Python
-  **FastAPI**: APIs modernas e rápidas
-  **HTML/CSS/JavaScript**: Frontend
-  **Bancos de Dados**: SQL, PostgreSQL, MongoDB

### 🚀 **DevOps e Cloud**
-  **Git/GitHub**: Controle de versão
-  **Docker**: Containerização
-  **AWS/Azure**: Computação em nuvem
-  **CI/CD**: Integração e deploy contínuo

### 🤖 **Machine Learning/IA**
-  **Scikit-learn**: Algoritmos de ML
-  **TensorFlow/PyTorch**: Deep Learning
-  **OpenCV**: Visão computacional
-  **NLTK/spaCy**: Processamento de linguagem natural

---

##  Contribuição

Sinta-se à vontade para:
-  Reportar bugs
-  Sugerir melhorias
-  Propor novos exercícios
-  Melhorar a documentação

---

## ⭐ Destaques das Novas Atividades

### 🎯 **Atividade_04** - Destaque: `calculator.py`
```python
# Calculadora interativa com menu e tratamento de erros
def calculator():
    print("=== CALCULADORA ===")
    while True:
        choice = input("Escolha uma operação (1-4) ou 'q' para sair: ")
        # ... código com validação robusta
```

### 🔧 **Atividade_05** - Destaque: `days_alive_calculator.py`
```python
# Calcula dias de vida com análises detalhadas
def calculate_days_alive(birth_date):
    today = date.today()
    days_alive = (today - birth_date).days
    return days_alive
# Inclui: semanas, meses, horas, próximo aniversário
```

### 🌐 **Atividade_06** - Destaque: `currency_lookup.py`
```python
# Consulta cotações em tempo real
def fetch_currency_info(currency_code):
    url = f"https://economia.awesomeapi.com.br/json/last/{currency_code}-BRL"
    response = requests.get(url, timeout=10)
    # ... processamento com análise de tendência
```

### 🛡️ **Recursos Avançados Implementados**
- ✅ **Tratamento robusto de erros** em todas as operações
- ✅ **Validação de entrada** para prevenir crashes
- ✅ **Interfaces intuitivas** com menus e feedback visual
- ✅ **Integração com APIs reais** funcionais
- ✅ **Análises estatísticas** e relatórios detalhados
- ✅ **Documentação completa** com docstrings

##  Licença

Este projeto é livre para uso educacional e pessoal.

---
