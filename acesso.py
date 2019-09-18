from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Login/senha
user = "username"
pwd = "password"

# Inicializacao do driver Firefox
# tODOS TEM QUE ESTAR COM PERMISSÃO DE ADMIN
exe_path = "/home/andre/Projetos/py_login/geckodriver"
log_local = "/home/andre/Projetos/py_login/geckodriver.log"
driver = webdriver.Firefox(executable_path=exe_path, log_path=log_local)

# Abrindo a pagina definida
driver.get("https://ead.uft.edu.br/")

# Entrada do nome do usuário / email
elmnt = driver.find_element_by_id("username")
elmnt.send_keys(user)

# Entrada da senha
elmnt = driver.find_element_by_id("password")
elmnt.send_keys(pwd)

# Pressionando o botão de login
elmnt.send_keys(Keys.RETURN)

# Fechando o driver
#driver.close()
