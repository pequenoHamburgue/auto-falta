#programa da faltas justificadas.
import pyautogui
import time

# quantidade de estudantes
qtd = int(input("digite a quantidade de estudantes: "))   # ajuste conforme necessário

print("5 sec pra ativar...")
time.sleep(5)

# ir até o primeiro estudante
pyautogui.press("tab", presses=4)

for _ in range(qtd):
    # executar a ação do estudante atual
    pyautogui.press("enter", presses=11)
    time.sleep(0.3)

    # ir para o próximo estudante (exceto após o último)
    pyautogui.press("tab")

