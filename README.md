# Assistente de Infraestrutura Telegram Bot

![License](https://img.shields.io/github/license/DaviAntonaji/python-telegram-bot-reboot?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/DaviAntonaji/python-telegram-bot-reboot?style=flat-square)
## Descrição
Este é um Telegram Bot desenvolvido em Python para auxiliar na gestão de infraestrutura. Ele permite que você execute comandos específicos e interaja com seu servidor remotamente por meio do Telegram.

## Funcionalidades
- **/start**: Inicia o bot e fornece uma mensagem de boas-vindas.
- **/reiniciar**: Reinicia o servidor (apenas para usuários autorizados).
- Autorização baseada em uma lista de permissões.

## Requisitos
- Python 3.7 ou superior
- Bibliotecas Python especificadas em `requirements.txt`
- Um token de API Telegram (obtenha-o registrando seu bot no BotFather do Telegram)

## Instalação
1. Clone este repositório para o seu servidor.
2. Crie um arquivo `.env` na pasta raiz do projeto com seu token de API Telegram:
    ```bash
    TELEGRAM_TOKEN="seu_token_aqui"
    ```
3. Instale as bibliotecas Python necessárias:
    ```bash
    pip install -r requirements.txt ou pip3 install -r requirements.txt

    ```

## Criando um Bot no Telegram usando o BotFather

Neste guia, mostrarei como criar um bot no Telegram usando o BotFather, uma ferramenta oficial do Telegram que permite criar e gerenciar bots. Com o seu bot criado, você poderá usar a API do Telegram para desenvolver aplicativos e bots personalizados. Siga os passos abaixo:

### Passo 1: Abra o Telegram e encontre o BotFather

1. Abra o aplicativo Telegram no seu dispositivo.
2. Na barra de pesquisa, digite "BotFather" e selecione o resultado correspondente.

### Passo 2: Inicie uma conversa com o BotFather

1. Clique no BotFather na lista de resultados de pesquisa.
2. Clique em "Iniciar" ou envie a mensagem "/start" para iniciar uma conversa com o BotFather.

### Passo 3: Crie um novo bot

1. Envie o comando "/newbot" para o BotFather.
2. O BotFather solicitará que você escolha um nome para o seu bot. Digite um nome e pressione Enter.
3. Em seguida, o BotFather solicitará que você escolha um username para o seu bot. Este username deve ser exclusivo e terminar com a palavra "bot" (por exemplo, "@MeuBotTelegram_bot"). Se o username que você escolher estiver disponível, o BotFather o aprovará; caso contrário, você precisará tentar outro.

### Passo 4: Anote o token do seu bot

1. Após escolher um username válido, o BotFather fornecerá um token de acesso para o seu 
bot. Anote esse token, pois você precisará dele para autenticar seu bot e fazer solicitações à API do Telegram.


## Execução
Para rodar o script manualmente, você pode usar o seguinte comando:
    ```
    python app.py ou python3 app.py
    ```


### Configuração como serviço no Windows Server
Se você deseja executar o script como um serviço no Windows Server, recomendo usar o [NSSM (Non-Sucking Service Manager)](https://nssm.cc/). Você pode seguir os seguintes passos:

1. Faça o download e extraia o NSSM em uma pasta no seu servidor.
2. Abra um prompt de comando como administrador e navegue até a pasta do NSSM.
3. Execute o seguinte comando para instalar o bot como serviço:
    ```console
    nssm install NomeDoServico "Caminho\Para\python.exe" "Caminho\Para\app.py"
    ```
    Certifique-se de substituir `"Caminho\Para\python.exe"` e `"Caminho\Para\app.py"` pelos caminhos corretos do Python e do seu script.
4. Você receberá uma janela de configuração do NSSM. Configure as opções conforme necessário.
5. Inicie o serviço usando o seguinte comando:
    ```console
    nssm start NomeDoServico
    ```

### Configuração com Immortal no Linux
O Immortal é uma ferramenta para gerenciar processos no Linux. Para executar seu script com o Immortal, siga os passos abaixo:

1. Instale o Immortal no seu sistema. Você pode encontrá-lo [aqui](https://immortal.run/).
2. Crie um arquivo de configuração para o seu script, por exemplo, `meu_bot.yml`:
    ```yaml
    cmd: python3 /caminho/para/app.py
    cwd: /caminho/para/pasta/do/projeto
    log:
        file: /caminho/para/arquivo_de_log.log
    ```
    Certifique-se de substituir /caminho/para/app.py, /caminho/para/pasta/do/projeto e /caminho/para/arquivo_de_log.log pelos caminhos corretos.
3. Execute seu script com o Immortal:

    ```bash
    immortal -c /caminho/para/meu_bot.yml
    ```

O Immortal garantirá que seu script seja executado como um serviço no Linux e seja reiniciado automaticamente em caso de falhas ou reboots.

Aproveite o seu Telegram Bot de Infraestrutura!

