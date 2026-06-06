#include <Arduino.h>


// pinos do sensor ultrassom esquerdo
#define TRIG_LEFT 25
#define ECHO_LEFT 34


// pinos do sensor ultrassom direito
#define TRIG_RIGHT 33
#define ECHO_RIGHT 35


// pino do botão
#define BUTTON_PIN 27


float medirDistancia(int trigPin, int echoPin)
{
    //geração do pulso do Trig
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);


    // Manda o pulso para o TRIG
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10); // espera 10 microssegundos 10⁻⁵ segundos ou 0,00001 segundos
    digitalWrite(trigPin, LOW);


    long duracao_pulso = pulseIn(echoPin, HIGH); // Mede o tempo de resposta / pulso do ECHO


    // Calcula a distância usando a velocidade do som (aproximadamente 343 m/s)
    // Divide por 2 para pegar a distância real do sensor até o objeto
    // a distância total é aquela que vai do sensor ao objeto e volta ao sensor.
    // baseado na fórmula da velocidade média
    // distância real = tempo de duração × velocidade do som / 2
    float distancia = duracao_pulso * 0.0343 / 2.0;
   
    return distancia;
}


void setup()
{
    Serial.begin(115200);

    // sensor ultrassom esquerdo
    pinMode(TRIG_LEFT, OUTPUT);
    pinMode(ECHO_LEFT, INPUT);


    // sensor ultrassom direito
    pinMode(TRIG_RIGHT, OUTPUT);
    pinMode(ECHO_RIGHT, INPUT);


    // botão
    pinMode(BUTTON_PIN, INPUT_PULLUP);
}


void loop()
{  
   
    // pega distancia do sensor ultrassom esquerdo
    float esquerda = medirDistancia(TRIG_LEFT, ECHO_LEFT);
    delay(30);


    // pega distancia do sensor ultrassom direito
    float direita = medirDistancia(TRIG_RIGHT, ECHO_RIGHT);


    // leitura do botão pull-up - 0 = pressionado, 1 = solto
    int botao = digitalRead(BUTTON_PIN);


    // Exibe na serial nessa ordem - Sensor Esquerdo, Sensor Direito, Botão
    Serial.print(esquerda);
    Serial.print(",");
    Serial.print(direita);
    Serial.print(",");
    Serial.println(botao);


    delay(50);
}
