📧 Envio Automático de Relatórios por E-mail

Este projeto envia automaticamente um e-mail com um arquivo PDF em anexo (por exemplo, relatórios de vendas).
Utiliza a biblioteca nativa smtplib do Python e a API de e-mail do Gmail com autenticação segura (App Password).

🚀 Funcionalidades

Envio automático de e-mails via conta Gmail

Inclusão de anexo (ex: PDF, planilhas, imagens, etc.)

Mensagem personalizada no corpo do e-mail

Execução simples via terminal Python

🧰 Tecnologias Utilizadas

Python 3.8+

smtplib — Envio de e-mails via SMTP

email.message — Criação e formatação da mensagem

mimetypes — Identificação automática do tipo de arquivo anexado

⚙️ Como Configurar

1.Clone este repositório

git clone https://github.com/seuusuario/envio-relatorio-email.git
cd envio-relatorio-email


2.Crie um App Password no Gmail

Vá até https://myaccount.google.com/apppasswords

Gere uma senha de aplicativo para “E-mail → Dispositivo Personalizado”

Copie essa senha (16 caracteres)

3.Configure as variáveis no código

remetente = 'seuemail@gmail.com'
destinatario = 'destinatario@gmail.com'
senha = 'sua_senha_de_aplicativo'
anexo = 'guia_relatorio.pdf'


4.Execute o script

python enviar_relatorio.py

📨 Exemplo de Saída
E-mail enviado com sucesso!


O destinatário receberá um e-mail com o assunto “Seu relatório chegou!” e o arquivo PDF em anexo.

⚠️ Observações Importantes

Nunca compartilhe sua senha real do Gmail!
Use sempre senhas de aplicativo.

Certifique-se de que o arquivo especificado em anexo exista no mesmo diretório do script.

Caso queira enviar para múltiplos destinatários, basta usar uma lista:

msg['To'] = ', '.join(['email1@gmail.com', 'email2@gmail.com'])

🧑‍💻 Autor

Wenderson Eduardo
📧 wendersonedu110@gmail.com

💻 Projeto de automação simples e funcional com Python.
