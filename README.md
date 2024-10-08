Selenium - Automatização Básica no Microsoft Edge
Este repositório contém um script Python que demonstra a automação básica de tarefas no navegador Microsoft Edge utilizando a biblioteca Selenium.

O que o script faz?

Abre o navegador Microsoft Edge.
Navega para o Google (https://www.google.com/).
Localiza a barra de pesquisa do Google (elemento com o nome "q").
Digita "Hello World!" na barra de pesquisa.
Envia a pesquisa pressionando Enter.
Aguarda por 10 segundos (opcional, para demonstrar espera por elementos).
Pré-requisitos:

Python 3.x instalado
Biblioteca Selenium instalada (pip install selenium)
Microsoft WebDriver para Edge baixado e descompactado na pasta drivers do projeto (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
Instruções:

Clone o repositório: git clone https://github.com/Renan-Loureiro/Automacao_com_Selenium
Abra um terminal ou prompt de comando e navegue até a pasta do projeto.
Execute o script: python script.py (substitua script.py pelo nome real do arquivo)
Como funciona o código?

O script utiliza a biblioteca Selenium para controlar o navegador Microsoft Edge. Ele define funções para:

Criar um objeto de navegador Edge com opções personalizáveis.
Localizar elementos na página usando identificadores como "name".
Preencher campos e enviar ações como Enter.
Esperar por elementos que estejam presentes na página.
Observação:

Esse é um exemplo básico de automação. O Selenium oferece uma ampla gama de funcionalidades para interagir com navegadores web de forma programática.

Contribuições:

Sinta-se à vontade para enviar pull requests para melhorias no código ou documentação.
