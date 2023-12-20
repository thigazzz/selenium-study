"""

Events Listeners é uma maneira de se comunicar, manipular, etc com eventos no Selenium.
Um Listener ficar 'escutando' ou 'vigiando' um evento.
Com o uso do Listener é possivel executar ações antes e depois de eventos, como:
clique, ações do mouse, etc.

"""


from selenium.webdriver import Edge
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.by import By

class MyListener(AbstractEventListener):
    def after_click(self, element, driver) -> None:
        if element.tag_name == 'input':
            attr = element.get_attribute("id")
            print(driver.find_element(By.ID, f'l{attr}').text)


browser = Edge()
browser.implicitly_wait(10)

wrapper = EventFiringWebDriver(browser, MyListener())
wrapper.get("https://selenium.dunossauro.live/exercicio_07")

input_el = wrapper.find_element(By.ID, 'nome').click()
input_el = wrapper.find_element(By.ID, 'email').click()
input_el = wrapper.find_element(By.ID, 'senha').click()


# browser.quit()