import datetime
import time
import tkinter as tk
from tkinter import messagebox
import winsound

def main():
    # Função para definir e iniciar o alarme
    def iniciar_alarme():
        # Obtém o horário atual
        horario_atual = datetime.datetime.now()

        # Calcula o horário daqui a 4 horas
        horario_alarme = horario_atual + datetime.timedelta(hours=4)  # 0.1 horas são 6 minutos

        print(f"Alarme programado para: {horario_alarme}")

        # Loop para verificar a cada minuto se já passaram 4 horas
        while True:
            # Obtém o horário atual novamente
            horario_atual = datetime.datetime.now()

            # Verifica se o horário atual é maior ou igual ao horário do alarme
            if horario_atual >= horario_alarme:
                print("Alarme! Já se passaram 4 horas.")
                # Exibe um popup com a mensagem
                root = tk.Tk()
                root.withdraw()  # Oculta a janela principal do tkinter
                messagebox.showinfo("Alarme", "Já se passaram 4 horas.")
                #winsound.Beep(1000, 1000)  # Frequência de 1000 Hz por 1 segundo
                break  # Sai do loop para reiniciar a contagem

            # Aguarda 1 minuto antes de verificar novamente
            time.sleep(60)

    while True:
        iniciar_alarme()  # Inicia o alarme

if __name__ == "__main__":
    main()
