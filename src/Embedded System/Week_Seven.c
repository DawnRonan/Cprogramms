/*
 * GccApplication9.c
 *
 * Created: 2025-04-01 1:44:06 PM
 * Author : F4-Laptop-4
 */ 

#include <avr/io.h>
#include <stdint.h>
#define F_CPU 8000000
#include <util/delay.h>

void led_init(void);
void led_out(uint8_t led);
void led_animation1(void);
void led_animation2(void);
void led_animation3(void);

typedef struct {
	uint8_t left : 1;
} Direction;

int main(void)
{
    /* Replace with your application code */
	led_init();
	//led_out(0b11001010);
	//00000011
	//00000110
	//00001100
	//...
	//11000000

	uint8_t led = 0b00000011;
	Direction dir = {0};
	dir.left = 1;
    /*
	while (1) 
    {   
		led_out(led);
		_delay_ms(100);
		//00000011
		//00000110
		//00001100
		//...
		//11000000
		//10000001
		//00000011
		
		led = led<<1;
		if (led == 0b1000 0000) 
		{
			led = 0b1000 0001;
		}else if (led == 0b0000 0010) 
		{
			led = 0b0000 0011;
		}else {
			continue;
		}
		
		if(dir.left){
			if(led == 0b11000000){
				dir.left = 0;
			}
			else {
				led = led<<1;
			}
		}
		else
		{
			if (led == 0b00000011)
			{
				dir.left = 1;
			}
			else {
				led = led>>1;
			}
		}
		
		
    }
	*/
	//led_animation1();
	//led_animation2();
	led_animation2();
}

void led_init(void)
{
	DDRB |= 0xF0;	//0b11110000
	DDRD |= 0xF0;
}

void led_out(uint8_t led)
{
	PORTB &= 0x0F;
	PORTB |= (led<<4);
	PORTD &= 0x0F;
	PORTD |= (led&0xF0);
}
void led_animation1(void)
{
	uint8_t led = 0b00000011;
	_delay_ms(100);
	while(1)
	{
		if (led == 0b11000000)
		{
			led = 0b00000011;
		}
		else
		{
		led = led<<1;	
		}
	}
}

void led_animation2(void)
{
	uint8_t led_left = 0b00000001;
	uint8_t led_right = 0b10000000;
	_delay_ms(100);
	while(1)
	{
		led_out(led_left+led_right);
		if(led_right == 0b00001000)
		{
			led_right = 0b00000001;
			led_left = 0b10000000;
		}
		else
		{
			led_right = led_right<<1;
			led_left = led_left>>1;
		}
	}
}

void led_animation3(void)
{
	uint8_t led_left = 0b00000001;
	uint8_t led_right = 0b10000000;
	_delay_ms(100);
	while(1)
	{
		led_out(led_left+led_right);
		if(led_right == 0b00001000)
		{
			led_right = 0b00000011;
			led_left = 0b11000000;
		}
		else
		{
			led_right = led_right<<1;
			led_left = led_left>>1;
		}
	}
}