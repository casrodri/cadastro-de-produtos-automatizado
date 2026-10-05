import pyautogui
import time
import pandas as pd

pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=595, y=400)

pyautogui.write("teste@example.com")
pyautogui.press("tab")
pyautogui.write("senha_teste")

pyautogui.click(x=816, y=543)

tabela = pd.read_csv("produtos.csv")

colunas = [
    "codigo",
    "marca",
    "tipo",
    "categoria",
    "preco_unitario",
    "custo",
    "obs"
]

for linha in tabela.index:
    time.sleep(3)
    pyautogui.click(x=574, y=294)

    for coluna in colunas:
        valor = tabela.loc[linha, coluna]

        if pd.notna(valor):
            pyautogui.write(str(valor))

        pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.press("home")