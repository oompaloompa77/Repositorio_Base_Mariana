import pyautogui

pyautogui.hotkey('Win', 'r')
pyautogui.sleep(1)
pyautogui.write('Calc')
pyautogui.press('Enter')
pyautogui.sleep(2)
pyautogui.press('8')
pyautogui.sleep(2)
pyautogui.press('+')
pyautogui.sleep(2)
pyautogui.press('2')
pyautogui.press('=')

print('O cálculo de 8 + 2 foi realizado na calculadora do Windows.')
print('Confira o histórico da calculadora')