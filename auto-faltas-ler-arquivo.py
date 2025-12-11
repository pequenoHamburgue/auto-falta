import pyautogui
import time

# arquivo com dados (ex: C, 1f, 2f, 1j, 2j etc.)
arquivo = "faltas.txt"

with open(arquivo, "r", encoding="utf-8") as f:
    registros = [linha.strip().lower() for linha in f if linha.strip()]

print("5 sec pra ativar...")
time.sleep(5)

# chegar no primeiro aluno
pyautogui.press("tab", presses=4)

for item in registros:
    if item == "c":
        # presença → apenas TAB para próximo aluno
        pyautogui.press("tab")
        continue

    # FALTAS (f)
    if item.endswith("f"):
        n = int(item.replace("f", ""))
        pyautogui.press("enter", presses=n)
        pyautogui.press("tab")
        continue

    # FALTAS JUSTIFICADAS (j)
    if item.endswith("j"):
        n = int(item.replace("j", ""))
        # regra: 1j = 10 enters, 2j = 11 enters, 3j = 12 enters, ...
        total_enters = 9 + n
        pyautogui.press("enter", presses=total_enters)
        pyautogui.press("tab")
        continue
