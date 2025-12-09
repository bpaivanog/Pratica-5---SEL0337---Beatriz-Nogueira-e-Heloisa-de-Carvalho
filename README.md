# Pratica-5---SEL0337---Beatriz-Nogueira-e-Heloisa-de-Carvalho
Repositório contendo a entrega da Prática 5 da disciplina de Projetos em Sistemas Embarcados. Feito pelas alunas Beatriz Nogueira e Heloísa de Carvalho.

1. Objetivo da Prática

- Esta prática tem como objetivo implementar o controle de um LED utilizando a Raspberry Pi através de:
- Scripts em Bash e Python para manipulação de GPIO.
- Serviços systemd que inicializam automaticamente no boot.
- Versionamento do projeto com Git e GitHub.
- Registro completo do histórico de comandos executados.

2. Estrutura do Diretório da Prática

/home/sel/4060/pratica5

├── blink.sh

├── blinkoff.sh

├── blink_python.py

├── blinkLED.service

├── blink_python.service

├── historico_git.txt

├── historico_terminal.txt

└── README.md

3. Montagem Física no GPIO

O LED utilizado foi conectado da seguinte forma:
- GPIO 18 (pino físico 12) → resistor → anodo do LED e catodo → GND da Raspberry Pi.

Montagem completa do circuito: 
[Circuito Montado.png](https://github.com/bpaivanog/Pratica-5---Projetos-em-Sistemas-Embarcados---Beatriz-Nogueira-e-Heloisa-de-Carvalho/blob/99fb00a3b1af6d15185041962d016e6bc631941d/Circuito%20Montado.png)

4. Instalação e Execução dos Serviços

Copiar serviços para o diretório systemd:

sudo cp blinkLED.service /lib/systemd/system/

sudo cp blink_python.service /lib/systemd/system/


Recarregar daemon:
sudo systemctl daemon-reload


Iniciar serviços:
sudo systemctl start blinkLED

sudo systemctl start blink_python


Verificar status:
sudo systemctl status blinkLED

sudo systemctl status blink_python


Parar:
sudo systemctl stop blinkLED

sudo systemctl stop blink_python


Habilitar para iniciar no boot:
sudo systemctl enable blinkLED

sudo systemctl enable blink_python


5. Evidências de Funcionamento

5.1 Captura de tela do serviço blinkLED em execução:
[Serviço BlinkLED.png](https://github.com/bpaivanog/Pratica-5---Projetos-em-Sistemas-Embarcados---Beatriz-Nogueira-e-Heloisa-de-Carvalho/blob/99fb00a3b1af6d15185041962d016e6bc631941d/Servi%C3%A7o%20BlinkLED.png)
BlinkLED em Python:
[Serviço Blink Python.png](https://github.com/bpaivanog/Pratica-5---SEL0337---Beatriz-Nogueira-e-Heloisa-de-Carvalho/blob/6860ced9c416843fa24de1c803026776fe9d31a7/Servi%C3%A7o%20Blink%20Python.png)

5.2 Saída do serviço blinkLED.service (script Bash)

Abaixo está um trecho da saída capturada durante a execução do serviço blinkLED, demonstrando o LED piscando corretamente via sysfs.
Essas mensagens aparecem no terminal ao rodar:

sudo systemctl status blinkLED -n 200

ou ao monitorar com:

journalctl -u blinkLED -f


Captura da saída real:
[OK] Started Blink LED

22:52:22 LED ON

22:52:22 LED OFF

22:52:23 LED ON

22:52:23 LED OFF

22:52:23 LED ON

22:52:23 LED OFF

22:52:23 LED ON

22:52:24 LED OFF

22:52:24 LED ON

22:52:24 LED OFF

22:52:24 LED ON

22:52:24 LED OFF

22:52:25 LED ON

22:52:25 LED OFF

22:52:25 LED ON

22:52:25 LED OFF

22:52:25 LED ON

22:52:26 LED OFF

22:52:26 LED ON

22:52:26 LED OFF

22:52:26 LED ON

22:52:26 LED OFF

22:52:27 LED ON

22:52:27 LED OFF

22:52:27 LED ON

22:52:27 LED OFF

22:52:27 LED ON

22:52:28 LED OFF

22:52:28 LED ON

...

22:53:02 LED OFF

22:53:02 LED ON

Serviço parado


6. Versionamento com Git

Instalação do Git:
sudo apt install git -y


Configuração global:
git config --global user.name "Beatriz"

git config --global user.email "beatriz.paiva@usp.br"


Inicialização do repositório:
git init


Adicionando arquivos:
git add .


Commit inicial:
git commit -m "Initial commit: Prática 5"


Conexão com o GitHub:
git remote add origin https://github.com/bpaivanog/Pratica-5-Projetos-Sistemas-Embarcados.git

git branch -M main

git push -u origin main


Registro do histórico no arquivo:
git log > historico_git.txt


7. Arquivo historico_git.txt

O arquivo contém o log de commits organizados da prática, incluindo datas e mensagens.

8. Conclusão

Nesta prática foram aplicados conceitos de sistemas embarcados envolvendo:

- controle de GPIO em Bash e Python
- uso do systemd como gestor de serviços em Linux
- inicialização automática de processos no boot
- organização e versionamento com Git

O projeto demonstrou corretamente o piscar de um LED tanto por script quanto por serviço systemd, além de realizar versionamento completo no GitHub.
