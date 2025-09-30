#importações
import smtplib
from email.message import EmailMessage
import mimetypes
#Def os dados de envio 
remetente = 'wendersonedu110@gmail.com'
destinatario = 'wendersonedu110@gmail.com'
assunto = 'seu relatório chegou!'
mensagem = """
Olá, aqui está seu relatorio com os dados de vendas.

att, 
"""
senha = 'bzom ejiq xkop apcp'
anexo = 'guia_relatorio.pdf'
#Criar o e-mail 
msg = EmailMessage()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto
msg.set_content(mensagem)

#Anexar o arrquivo 
mime_type, _ = mimetypes.guess_type(anexo)
mime_type,mime_subtype = mime_type.split('/')

with open(anexo,'rb') as arquivo:
    msg.add_attachment(arquivo.read(),maintype=mime_type,subtype=mime_subtype,filename=anexo)
#Realizar o envio do E-mail 
with smtplib.SMTP_SSL("smtp.gmail.com",465) as email:
    email.login(remetente,senha)
    email.send_message(msg)

print('E-mail enviado com sucesso!')

