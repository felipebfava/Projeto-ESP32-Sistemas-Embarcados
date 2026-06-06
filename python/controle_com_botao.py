
import serial
import keyboard
import time

# Altere para a mesma porta em que o ESP32 estiver conectado
PORTA = "COM9"

# Altere para a mesma velocidade de leitura da porta
# A mesma usada no arquivo platformio.ini como monitor_speed
BAUDRATE = 115200

# Define uma distância limite de leitura
LIMITE = 15

# conexão com a serial
ser = serial.Serial(PORTA, BAUDRATE, timeout=1)

# espera conexão com a serial
time.sleep(2)

# para a função do botão
space_pressionado = False


# loop principal
while True:
    try:
        # lê o conteúdo em bytes que está vindo na serial pela porta do ESP32
        # converte para texto, remove espaços e quebras de linha
        linha = ser.readline().decode(errors="ignore").strip()

        # se não for recebido nada pela serial
        if not linha:
            continue

        # reparte a linha recebida pela serial
        partes = linha.split(",") # ["distancia_esquerda", "distancia_direita", "botao"]

        # serial precisa ler os 3 valores: distancia_esquerda, distancia_direita, botao
        if len(partes) != 3:
            continue
        
        esquerda = float(partes[0]) # pega a distancia_esquerda no vetor / lista
        direita = float(partes[1]) # pega a distancia_direita no vetor / lista
        botao = int(partes[2]) # pega o botao no vetor / lista

        # exibe o valor recebido da serial
        print(f"Esq:{esquerda:.1f} Dir:{direita:.1f} Bot:{botao}")


        # sensor esquerdo interage / simula a seta esquerda do teclado
        if esquerda < LIMITE:
            keyboard.press("left") # tecla seta está pressioanada
        else:
            keyboard.release("left") # tecla seta está solta


        # sensor direito interage / simula a seta direita do teclado
        if direita < LIMITE:
            keyboard.press("right")
        else:
            keyboard.release("right")


        # botão interage / simula a tecla espaço do teclado
        if botao == 0 and not space_pressionado:
            keyboard.send("space")
            space_pressionado = True


        elif botao == 1:
            space_pressionado = False


    except Exception as e:
        print("Erro:", e)
