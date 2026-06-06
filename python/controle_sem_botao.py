
import serial
import keyboard
import time

# Altere para a mesma porta em que o ESP32 estiver conectado
PORTA = "COM9"

# Altere para a mesma velocidade de leitura da porta
# A mesma usada no arquivo platformio.ini como monitor_speed
BAUDRATE = 115200

# Define uma distância limite de leitura
LIMITE = 15  # cm

# conexão com a serial
ser = serial.Serial(PORTA, BAUDRATE, timeout=1)

# espera conexão com a serial
time.sleep(2)


# loop principal
while True:
    try:
        # lê o conteúdo em bytes que está vindo na serial pela porta do ESP32
        # converte para texto, remove espaços e quebras de linha
        linha = ser.readline().decode(errors="ignore").strip()

        # pega a linha e divide ela nas vírgulas usadas
        if "," in linha:
            # define o sensor esquerdo e direito conforme mandado pelo ESP32
            esquerda, direita = linha.split(",")

            # conversão de tipo para um valor float
            esquerda = float(esquerda)
            direita = float(direita)

            # exibe o valor recebido da serial
            print(f"Esq: {esquerda:.1f} | Dir: {direita:.1f}")


            # mão perto do sensor esquerdo
            # simula o pressionar a tecla seta esquerda
            if esquerda < LIMITE:
                keyboard.press("left")  # tecla seta está pressioanada
            else:
                keyboard.release("left") # tecla seta está solta


            # mão perto do sensor direito
            # simula o pressionar a tecla seta direita
            if direita < LIMITE:
                keyboard.press("right")
            else:
                keyboard.release("right")


    except Exception as e:
        print("Erro:", e)

