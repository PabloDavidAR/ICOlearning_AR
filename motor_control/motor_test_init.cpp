#include "motor_class.hpp"
#include <iostream>

// GPIO via Matrix Creator
#define  TB6612_RIGHT_MOTOR_PWMA        15 // (Orange)
#define  TB6612_LEFT_MOTOR_PWMB         14 // (Green)
#define  TB6612_RIGHT_MOTOR_AIN1        13 // (Blue)
#define  TB6612_RIGHT_MOTOR_AIN2        12 // (Brown)
#define  TB6612_LEFT_MOTOR_BIN1         11 // (Grey)
#define  TB6612_LEFT_MOTOR_BIN2         10 // (Pink)

uint16_t GetGPIOValues();

int main() {

    // Create MatrixIOBus object for hardware communication
	matrix_hal::MatrixIOBus bus;
    int speed {0};
    int dir {0};
    
    // Initialize bus and exit program if error occurs
    if (!bus.Init())
	return false;

    // Create GPIOControl object
	matrix_hal::GPIOControl gpio;

	// Set gpio to use MatrixIOBus bus
	gpio.Setup(&bus);

    Motor left(TB6612_LEFT_MOTOR_PWMB, TB6612_LEFT_MOTOR_BIN1, TB6612_LEFT_MOTOR_BIN2, &gpio);
    Motor right(TB6612_RIGHT_MOTOR_PWMA, TB6612_RIGHT_MOTOR_AIN1, TB6612_RIGHT_MOTOR_AIN2, &gpio);

    left.setMotorSpeedDirection(&gpio, 0, 0);
    right.setMotorSpeedDirection(&gpio, 0 , 0);


    speed = 45;
    dir = 1;
	
    std::cout << "Before 1" << std::endl;
    left.setMotorSpeedDirection(&gpio, speed, dir);

    std::cin.get();



    dir = 1;
    std::cout << "Before 2" << std::endl;
    left.setMotorSpeedDirection(&gpio, speed, dir);

    std::cin.get();



    dir = 1;
    std::cout << "Before 3" << std::endl;
    right.setMotorSpeedDirection(&gpio, speed , dir);

    std::cin.get();



    dir = 1;
    std::cout << "Before 4" << std::endl;
    right.setMotorSpeedDirection(&gpio, speed , dir);

    std::cin.get();



    right.setMotorSpeedDirection(&gpio, 0 , dir);
    left.setMotorSpeedDirection(&gpio, 0 , dir);

    
    return 0;
}
