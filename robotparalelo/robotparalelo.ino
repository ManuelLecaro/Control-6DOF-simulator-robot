#include <Servo.h>
#include <Wire.h>
/*Credits to N. Cruz*/

//MIN and MAX PWM pul e sizes, they can be found in servo documentation
#define MAX 2400
#define MIN 600

//Positions of servos mounted in opposite direction
#define INV1 1
#define INV2 3
#define INV3 5

//constants for computation of positions of connection points
#define pi  3.14159
#define deg2rad 180/pi
#define deg30 pi/6
//variables used for proper show of positions on LCD
char shown=0, showPos=0, useIrda=0;
unsigned long time;

char cadena[5]; //Creamos un array que almacenará los caracteres que escribiremos en la consola del PC. Le asignamos  un tope de caracteres, en este caso 30
byte posicion=0;  //Variable para cambiar la posición de los caracteres del array
float valor;  //Variable del valor entero

//Array of servo objects
Servo servo[6];

//Zero positions of servos, in this positions their arms are perfectly horizontal, in us
static int zero[6]={1400,1650,1550,1500,1500,1500};

//In this array is stored requested position for platform - x,y,z,rot(x),rot(y),rot(z)
static float arr[6]={0,0.0,0, radians(0),radians(0),radians(0)};

//Actual degree of rotation of all servo arms, they start at 0 - horizontal, used to reduce
//complexity of calculating new degree of rotation
static float theta_a[6]={0.0,0.0,0.0, 0.0,0.0,0.0};

//Array of current servo positions in us
static int servo_pos[6];

//rotation of servo arms in respect to axis x
const float beta[] = {0,pi,2*pi/3,-pi/3,-2*pi/3,pi/3},

//maximum servo positions, 0 is horizontal position
servo_min=radians(-80),servo_max=radians(80),

//servo_mult - multiplier used for conversion radians->servo pulse in us
//L1-effective length of servo arm, L2 - length of base and platform connecting arm
//z_home - height of platform above base, 0 is height of servo arms
servo_mult=400/(pi/4),L1 = 20,L2 = 170, z_home = 165;

void setup() {
  // put your setup code here, to run once:
  //attachment of servos to PWM digital pins of arduino
   servo[0].attach(3, MIN, MAX);
   servo[1].attach(5, MIN, MAX);
   servo[2].attach(6, MIN, MAX);
   servo[3].attach(9, MIN, MAX);
   servo[4].attach(10, MIN, MAX);
   servo[5].attach(11, MIN, MAX);
//begin of serial communication
   Serial.begin(9600);
//putting into base position
   setPos(arr);

}

void loop() {
  // put your main code here, to run repeatedly:

}
