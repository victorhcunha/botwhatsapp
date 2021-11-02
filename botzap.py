from selenium import webdriver
import time

class whatsappBot:
    def __init__(self):
        #mensagem a ser enviada
        self.message = "Mensagem Teste"
        #grupos ou pessoas que devem recebê-la
        self.grupos = ["Mateus Dias IPE"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):
        #<span dir="auto" title="Me" class="emoji-texttt _ccCW FqYAR i0jNr">Me</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="ptt" data-icon="ptt" class="">
        print("iniciando")
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.message)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)           
            botao_enviar.click()
            time.sleep(5)


bot = whatsappBot()
bot.EnviarMensagens()
