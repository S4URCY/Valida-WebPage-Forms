import mechanize
import cookielib

#cria um navegador, um browser de codigo
br = mechanize.Browser()
url = 'https://ead.uft.edu.br/'
user = 'login'
senha = 'senha'
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)


br.set_handle_equiv(True)
br.set_handle_gzip(False)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Do ponto de vista do servidor, o navegador agora o Firefox.
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11;\
 U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615\
Fedora/3.0.1-1.fc9 Firefox/3.0.1')]      

#Navega acessando a URL usando o método HTTP GET
br.open(url)

# Se existirem formulários, você pode selecionar o primeiro (#0), por exemplo...
br.select_form(nr=0)

# Para mostrar os formularios e ver os campos a serem preenchidos,
# use um for sobre o br.forms()
for f in br.forms():
   print f

# Preencher o formulário com os dados
br.form['username'] = user
br.form['password'] = senha

# Enviar o formulário usando o método HTTP POST
br.submit()        

#busca  HTML retornado:
html = br.response().read()
