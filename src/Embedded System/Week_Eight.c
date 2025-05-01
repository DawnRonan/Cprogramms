/*
 * GccApplication19.c
 *
 * Created: 2025-04-15 12:44:00 PM
 * Author : F4-Laptop-4
 */

#include <avr/io.h>
#include <stdio.h>
#define F_CPU 8000000
#include <util/delay.h>

void SevenSegment_Init(void);
void SevenSegment_Display(uint8_t num);
void SevenSegment_Display(uint8_t num);
void Upwards_Counter2();
void extract_digits(uint16_t number, uint8_t digits[4]);
void display_number(uint16_t number);

int main(void)
{
	SevenSegment_Init();


	while (1)
	{
		uint8_t task = 4;
		switch (task)
		{
			case 2:{
				for (uint8_t i = 0; i<4; i++){
					SevenSegment_Display(i);
					_delay_ms(1000);
				}
				PORTA = 0b11001111;
				_delay_ms(1000);
				PORTA = 0B00000000;
				_delay_ms(1000);
				break;
			}
			case 3:{
				Upwards_Counter2();
				break;
			}
			case 4:{
				uint16_t value = 1234;
				display_number(value);
				break;
			}

		}


	}
}

void SevenSegment_Init(void)
{
	DDRA = 0b11111111;   // PORTA OUTPUT
	PORTA = 0b00000000; // initial state
}

const uint8_t digit_segments[10] = {
	0b00000000,
	0b00000001,
	0b00000010,
	0b00000011,
	0b00000100,

	0b00000101,
	0b00000110,
	0b00000111,
	0b00001000,
	0b00001001
};

const uint8_t digit_select[4] = {
	0b10000000,
	0b10010000,
	0b10100000,
	0b10110000
};

void extract_digits(uint16_t number, uint8_t digits[4]){
	//single digit
	digits[0] = number % 10;
	//tens digit
	digits[1] = (number/10) % 10;
	//hundreds digit
	digits[2] = (number/100) % 10;
	//thousand digit
	digits[3] = (number/1000) % 10;
}

//display 4 digital numbers dynamically
void display_number(uint16_t number){
	uint8_t digits[4];
	extract_digits(number,digits);
	for (uint8_t i = 0; i<4; i++){
		uint8_t Seg_Code[4];
		uint8_t Bit_Select[4];
		//obtain segment digit
		Seg_Code[i] = digit_segments[digits[i]];
		//obtain corresponding output port
		Bit_Select[i] = digit_select[i];
		PORTA = Seg_Code[i] | Bit_Select[i];
		//dynamical scan
		_delay_ms(1);
	}
}

ISR(TIMER0_COMPA_vect) {
    static StopwatchState state = STOPWATCH_START;  // 假设初始状态是启动
    uint8_t value = Stopwatch_state(state);  // 获取当前秒表值
    display_number(value);  // 显示当前秒表值
}

//count from zero to nine per second om digit 2
void Upwards_Counter2() {
	for(uint8_t i=0; i<10; i++){
		PORTA = 0b10100000 | (i & 0X0F);
		_delay_ms(1000);
		PORTA = 0b00000000;
		_delay_ms(1000);
	}
}

//" : "blink
void SevenSegment_Display(uint8_t num) {
		PORTA = digit_segments[num];
		_delay_ms(1000);
		PORTA = 0B00000000;
		_delay_ms(1000);
}