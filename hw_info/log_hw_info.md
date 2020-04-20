
# Logar as informações de hardware

## Preparação

1. Instalar Python e Configurar a IDE (como preferir | Apensar para exemplo eu estou o Anaconda https://www.anaconda.com e VS Code https://code.visualstudio.com)
1. Instalar o pacotes necessários
    1. Schedule (para agendar a execução de função de tempos em tempos)
        1. `pip install schedule`
    1. No meu caso não foi necessário, mas talvez teriam que instalar o psutil para ler as informações do hardware:
        1. `pip isntall psutil`


## Exercício:

Complete o arquivo log_hw_info.py de forma que seu scripts leia as informações de CPU, memória e redes do seu computador e os armaze em um arquivo de log.

Este será nosso primeiro exercício, mas gostaría que pudessemos elaborá-lo um pouco mais nas próximas semanas (talvez criando alertas ou enviando as informações para alguma ferramenta).

Como estamos na disciplina de estruturas avançadas e dados também seria interessante aramazenar as informações de CPU ou memórias lidas em uma lista ou array para também aplicarmos os conceitos da disciplina.

### Dicas sobre como fazer isto em Python as informações de hardware:
* https://pypi.org/project/schedule/
* https://www.thepythoncode.com/article/get-hardware-system-information-python
* https://stackoverflow.com/questions/3103178/how-to-get-the-system-info-with-python
