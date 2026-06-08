### Aluno
Felipe Biava Favarin

### Sobre o Projeto
Projeto destinado a disciplina de Sistemas Embarcados pelo IFC Videira ministrada pelo Professor Jonatan Rafael Rakoski Zientarski

#### Disponibilidade
O projeto é de uso livre, altere como quiser.

Caso tenha dúvida sobre a montagem física. Eu montei o projeto usando o site Wokwi, aqui está o link:
[Wokwi - Público](https://wokwi.com/projects/466087019677550593)

#### Apresentação
Utilize a seguinte apresentação como base
[Slides no Canva - Visualizar](https://canva.link/uqodxno0rdrdse9)

### Ferramentas
As ferramentas utilizadas e que são recomendadas para a utilização foram:
Visual Studio Code junto com a extensão do PlatformIO

#### Sobre o Código
A partir de um Microcontrolador ESP32 conectado em alguma porta COM-X do seu Desktop/Notebook faça o build e upload do código main.cpp a partir do PlatformIO para o Microcontrolador ESP32

Ainda com o ESP32 conectado, vai até a pasta python e crie um ambiente virtual:

```js
python -m venv <nome_do_seu_ambiente>
```

Após criar o ambiente virtual, faça a ativação dele

Com o ambiente virtual iniciado, instale as seguintes bibliotecas:

```js
pip install pyserial keyboard
```

Agora execute o código python conforme os nomes dos arquivos.

### Funcionalidade
Abra o jogo Quebra-Blocos no navegador Google Chrome.

O seu microcontrolador ESP32 irá atuar como um controle, ao clicar no botão, a tecla espaço será pressionada para o jogo iniciar. Agora ao aproximar e afastar sua mão dos sensores, verá que a barrinha irá se mover. É isso, faça a maior pontuação quebrando os blocos e não deixe a bola cair. Tenha um Bom Jogo!
