# passo a passo

## O que vamos usar

- Raspberry PI
- breadboard (para testar o nosso circuito)
- vários cabos
- vários botões
- um switch
- um multímetro (opcional)
- legos :D

## Passos

  1. Desktop - criar um script em python que escrever alguma coisa no ecrã
  2. Desktop - formatar o cartão e escolher o sistema operativo
  3. RPI - meter o cartão, ligar os cabos necessários e ligar o RPI
  4. Desktop - fazer acesso remoto (fazer alguns testes)
  5. RPI - adicionar a breadboard, adicionar 1 led
  6. Desktop - criar um script para o led e executa no RPI
  7. RPI - adicionar um botão à breadboard
  8. Desktop - criar um script para dar um som quando o botão é carregado
  9. RPI - adicionar mais botões à breadboard
  10. Desktop - adicionar mais botões ao script
  11. RPI - adicionar o switch para as várias layers
  12. Desktop - adicionar o suporte para varias layers de audio

# Passo 1

Para começar vamos escrever um pequeno script e executa-lo para ver o que acontece.

Primeiro cria um ficheiro chamado `helloworld.py` e adiciona o seguinte código:

```python
print("hello world")
```

Agora abre um terminal e executa o script escrevendo: 

```bash
python helloworld.py
```

**Nota:** O que aconteceu?

# Passo 2

Para formatar o cartão e instalar o sistema desejado, vamos utilizar a aplicação [Raspberry Pi Imager](https://www.raspberrypi.com/software/).

Para isso, abre a aplicação `Raspberry PI Imager`.

- Escolhe o device que estás a utilizar.
- O OS para este projecto será o `Raspberry Pi OS (other ) -> Raspberry Pi OS Lite (32-bit)`, mas podes usar também o `Raspberry Pi OS` que se encontra logo no inicio
- O storage é o cartão de memória

E agora é so carregar em NEXT

# Passo 3

Agora é hora de ligar o Raspberry Pi.

Liga um cabo de rede ou caso tenhas configurado o WiFi no passo anterior, o Raspberry Pi vai-se ligar automaticamente à rede (se for um Raspberry Pi antigo poderás precisar de uma pen WiFi).

Mete o cartão de memória.

E por fim, liga o cabo USB para dar carga ao Raspberry Pi.

# Passo 4

Agora abre um terminal no desktop e  para te ligares remotamente ao Raspberry Pi utilizando SSH

No terminal escreve:

```bash
ssh hostname.local -l username
```

Onde hostname e username são os dados que definiste no passo 2

Escreve a password e já está:

![raspberry pi screen after ssh login](images/image.png)

Aproveita para saber o teu IP que vais precisar já a seguir, para isso escreve:

```bash
ip addr
```

![alt text](images/image-1.png)

Neste caso o IP é o **192.168.50.186**

Abre também uma ligação SFTP para ser mais fácil transferir ficheiros, podes utilizar uma aplicação chamada [FileZilla](https://filezilla-project.org/).

Utiliza o teu IP **192.168.50.186** (no meu caso), nome de utilizador **username**, a tua **password**, e a porta é a 22

![alt text](images/image-2.png)

![alt text](images/image-3.png)

Agora já consegues a ver os ficheiros dentro do Raspberry Pi.

# Passo 5

Desliga o Raspberry Pi por agora.

Agora liga um cabo entre o pin 6 e a linha com um "-" na breadboard.

Depois liga um cabo entre o GPIO 17 e uma das linhas do meio.

Vais precisar de uma resistência e de um Led.

Liga uma resistência entre a linha do GPIO 17 e a perna mais longa do Led, depois a liga a perna mais curta do Led à linha "-".

![alt text](images/led.drawio.png)

# Passo 6

Agora é preciso controlar o Led, e para isso vais por o Led a piscar.

No desktop cria um ficheiro chamado `led.py` com o seguinte código:

```python
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

Isto vai activar o Led no pin GPIO 17 e depois ligar e desligar enquanto não parares o script.

Agora liga novamente o Raspberry Pi e acede pelo FileZilla.

Copia o ficheiro para o Raspberry Pi.

E por fim liga-te por SSH e escreve `python led.py` e vê a magia a acontecer.

**Nota:** aproveita para brincar com os tempos ou até mesmo alterar o script. Se tiveres um multímetro, podes usar para ver a Voltagem a mudar quando o Led é ligado ou desligado.

# Passo 7

Desliga o Raspberry Pi por agora.

Agora vais adicionar o primeiro botão.

O botão é nada mais que uma peça electronica que só passa corrente quanto carregamos nele, e vais usar isso para enviar dados para o Raspberry Pi.

A ligação é muito simples, encaixa o botão no centro da breadboard.

Liga um cabo entre o GPIO 27 e a linha da breadboard que está ligada a uma das pernas do botão.

E agora mais um fio entre e "-" e a outra perna do botão que está do mesmo lado onde ligaste o fio anterior.

Não te esqueças também de ligar uma coluna ao Jack to Raspberry Pi.

![alt text](images/button.drawio.png)

Hora do código.

# Passo 8

Cria novamente um ficheiro **passo7.py** com o seguinte código:

```python
from gpiozero import LED
from time import sleep
from sound_button import SoundButton

led = LED(17)

SoundButton(
  27,
  [
    "./audio_button1_1.wav"
  ]
)

while (True):
  led.on()
  sleep(1)
  led.off()
  sleep(1)

```

Agora liga novamente o Raspberry Pi e acede pelo FileZilla.

Copia os ficheiros **passo7.py, sound_button.py, sound_file.py e fileParser.py**, para o Raspberry Pi.

Liga-te por SSH e instala as dependências `pip install numpy simpleaudio`.

E por fim `python passo7.py`.

# Passo 9

Nunca ate esqueças, se vais mexer na breadboard, desliga sempre o Raspberry Pi antes de o fazeres.

Utiliza aquilo que aprendeste até agora, e tenta adicionar mais botões à breadboard.

# Passo 10

Agora que tens mais botões, actualiza o script para adicionar esses mesmos botões e mete um som para cada um deles.

# Passo 11

Está tudo a funcionar? Óptimo!

O objectivo agora é adicionar ainda mais opções aos nosso botões.

Vais fazer com que cada um deles suporte até 4 sons, e que possas escolher quais os sons que vão tocar ao carregar num botão.

Para isto vais precisar de mais um botão, mas desta vez esse botão vai definir um estado em vez de fazer um som.

Cada vez que carregares no botão, ele irá activar um novo som para os botões.

Encaixa o botão no centro da breadboard.

Liga um cabo entre o GPIO 16 e a linha da breadboard que está ligada a uma das pernas do botão.

E agora mais um fio entre e "-" e a outra perna do botão que está do mesmo lado onde ligaste o fio anterior.

![alt text](images/layerSwitch.drawio.png)

# Passo 12

Agora tens de actualizar o script.

Adiciona o seguinte ao teu código:

```python
from layer_switch import LayerSwitch

layerSwitch = LayerSwitch(16)
```

Também tens de alterar os teus botões, e adicionar mais um parâmetro:

```python
SoundButton(
  27,
  [
    "./audio_button1_1.wav"
  ],
  layerSwitch
)
```

Repara que agora estamos a passar o layerSwitch como parâmetro para o botão, isto vai fazer com que o botão saiba qual som tem de tocar ao ser clicado.

Nota: O que está a acontecer? Como é que podes melhorar? Que ideias tens para fazer ainda mais?
