import pyautogui as py
from time import sleep
import pyscreeze


py.click(1214,419, duration=1)
sleep(1)
py.write('bmg.shop.oficial')
sleep(1)


py.press('tab')
py.write('Biel1407@')
sleep(1)
py.press('enter')
sleep(7)



botao_de_pesquisa = py.locateCenterOnScreen('teste2.png')
print('localizado02')
sleep(1)

py.click(botao_de_pesquisa, duration=1)
sleep(1)
py.write('biiancadiniz')
sleep(1)

py.click(304,390, duration=2)
sleep(5)


py.click(737,876, duration=1)
sleep(1)
try:

    botao_de_curtir = py.locateCenterOnScreen('teste03.png')
    print('localizado03')
    sleep(2)



    if botao_de_curtir is not None:
        py.click(1113,955, duration=1)
        sleep(1)
        py.write('que lindo')
        sleep(1)
        py.press('enter')
    


except:
    botao_de_curtir02 = py.locateCenterOnScreen('teste04.png')
    print('localizado04')
    sleep(2)
    
    if botao_de_curtir02 is not None:
        py.click(1030,818, duration=1)
        sleep(1)
        py.click(1113,955, duration=1)
        sleep(1)
        py.write('que lindo')
        sleep(1)
        py.press('enter')