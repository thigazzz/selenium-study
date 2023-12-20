"""

Action Chains é uma maneira de se comunicar com eventos e executa-los.
Funciona como instruções, voce dece indicar o que tem que ser feito
e no final executar (com a função perform())
Com as actions chains é possível executar eventos mais low-levels,
o que não é possivel usando o Selenium normalmente.

"""



from selenium.webdriver import Edge
from selenium.webdriver.common.by import By




browser = Edge()
browser.implicitly_wait(10)

browser.get("https://selenium.dunossauro.live/exercicio_08")


# browser.quit()