import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def Email(email, nome_laboratorio, responsavel):
    try:
        servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_email.starttls()

        servidor_email.login('diretoriodelaboratorios@uea.edu.br', 'hxqzfhidmggpoetv')

        remetente = 'diretoriodelaboratorios@uea.edu.br'
        assunto = 'Assunto: Criação de Novo Laboratório na UEA'
        destinatarios = email
        mensagem = MIMEMultipart()

        with open('templates/static/images/logo_email.png', 'rb') as img_file:
            imagem = MIMEImage(img_file.read())
            imagem.add_header('Content-ID', '<logo>')
            mensagem.attach(imagem)
                    
        conteudo = """
            <p>Prezado(a) {responsavel},</p>
           <p>
                O Laboratório “ “{nome}” foi cadastrado no Diretório de Laboratórios da Universidade do Estado do Amazonas e encontra-se aguardando preenchimento para certificação pela Pró-Reitoria de Pesquisa e Pós-Graduação-PROPESP.
           </p>

           <p>
        Para tanto, como responsável pelo laboratório, faz-se necessário que realize o acesso ao Diretório por meio do endereço
        <a href="https://dirlab.uea.edu.br/autenticacao/auth/">https://dirlab.uea.edu.br/autenticacao/auth/</a>,
        utilizando seu login institucional. Em seguida, realize o preenchimento das informações e notifique esta Gerência de Pesquisa e Projetos Institucionais para posterior certificação pela PROPESP.
</p>


            <p>Atenciosamente, </p>
            <p>Gerência de Pesquisa e Projetos Institucionais </p>
            <p>Pró-Reitoria de Pesquisa e Pós-Graduação"

            </p>
            
            <img src='cid:logo' alt="Logotipo UEA"
            style="width: 250px; height: 100px;"/>
        """.format(nome=nome_laboratorio, responsavel=responsavel)

        mensagem['From'] = remetente
        mensagem['To'] = destinatarios
        mensagem['Subject'] = assunto

        conteudo = MIMEText(conteudo, 'html', 'utf-8')
        mensagem.attach(conteudo)
        
        servidor_email.sendmail(remetente, destinatarios, mensagem.as_string())

    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    finally:
        servidor_email.quit()

    