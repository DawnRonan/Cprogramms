#include <avr/io.h>
#include <stdio.h>
#define F_CPU 8000000
#include <util/delay.h>
#include <avr/interrupt.h>


static volatile uint8_t button_triggered[5] = { 0 };    // tracking button presses

typedef enum {
    STOPWATCH_START,
    STOPWATCH_PAUSE,
    STOPWATCH_RESET
} StopwatchState;   // Enum to represent stopwatch states

void Timer1_Init(void); // Initialize Timer1 for 1 second interval
void Init(void);    // Initialize the system
void Led_out(uint8_t led);
void Button0(void);
void Button1(void);
void Button2(void);
void Button3(void);
void Button4(void);
uint8_t Stopwatch_state();  // Function to handle stopwatch state
void Extract_digits(uint8_t number, uint8_t digits[2]); // Function to extract digits from a number
void display_number(uint8_t number);    // Function to display a number on the 7-segment display dynamically
uint8_t Button_press_detection(uint8_t pin);    // Function to detect button presses

// Selection of 7-segment display bits
const uint8_t bit_select[4] = {
    0X80,
    0X90,
    0XA0,
    0XB0
};
// Global variables
// Initalization of 7-segment display segments
static uint8_t value = 0;
// Initalization of stopwatch value
static volatile StopwatchState state = STOPWATCH_RESET;
// Interival for stopwatch
ISR(TIMER1_COMPA_vect) {
    value = Stopwatch_state();
}

int main(void) {
    Init();
    Timer1_Init();
    // Choose which task to run
    // 1: Button press detection
    // 2: Stopwatch
    static uint8_t task = 1;
    while (1) {
        switch (task)
        {
        case 1: {
            // Button press detection
            Button_press_detection(PG0);
            Button_press_detection(PG1);
            Button_press_detection(PG2);
            Button_press_detection(PG3);
            Button_press_detection(PG4);
            // Check which button was pressed and call the corresponding function
            if (button_triggered[0]) Button0();
            if (button_triggered[1]) Button1();
            if (button_triggered[2]) Button2();
            if (button_triggered[3]) Button3();
            if (button_triggered[4]) Button4();
            else Init();
            break;
        }
        case 2: {
            // Check which button was pressed and call the corresponding stopwatch function
            if (Button_press_detection(PG0)) state = STOPWATCH_START;
            if (Button_press_detection(PG4)) state = STOPWATCH_PAUSE;
            if (Button_press_detection(PG2)) state = STOPWATCH_RESET;
            display_number(value);
            break;
        }
        }
    }
}

void Init(void)
{
    DDRA = 0xFF;
    DDRB = 0xF0;
    DDRD = 0x1F;
    DDRG = 0x1F;
    PORTA = 0x00;
    PORTB = 0x0F;
    PORTD = 0xE0;
    PORTG = 0xE0;
}

void Led_out(uint8_t led)
{
    PORTB &= 0x0F;
    PORTB |= (led << 4);
    PORTD &= 0x0F;
    PORTD |= (led & 0xF0);
}
void Button0(void)
{
    uint8_t led = 0xFF;
    Led_out(led);

}

void Button1(void)
{
    static int led_initialized = 0;
    static uint8_t led;
    static uint8_t direction = 0;
    // Run once to initialize led
    if (!led_initialized) {
        led = 0b11000000;
        led_initialized = 1;
    }

    Led_out(led);
    _delay_ms(100);
    if (direction == 0) {
        led = led >> 1;
        if (led == 0x03) {
            direction = 1;
        }
    }
    else if (direction == 1) {
        led = led << 1;
        if (led == 0xC0) {
            direction = 0;
        }
    }
    Led_out(led);
    _delay_ms(100);
}

void Button2(void)
{
    PORTA = 0xB2;
}

void Button3(void)  // Easier to use a for loop to count from 2 to 8 instead of using a static variable in the function
{
    static int digit_initialized = 0;
    static uint8_t value;
    // Run once to initialize digit
    if (!digit_initialized) {
        value = 0x92;
        PORTA = value;
        _delay_ms(500);
        digit_initialized = 1;
    }
    if (value > 0x97) {
        value = 0x91;
    }
    value++;
    PORTA = value;
    _delay_ms(500);
}

void Button4(void)
{
    PORTA = 0x00;
    PORTB = 0x0F;
    PORTD = 0xE0;
    PORTG = 0xE0;
    // Reset button_triggered array
    for (uint8_t i = 0; i < 5; i++) {
        button_triggered[i] = 0;
        _delay_ms(1000);
    }
}

void Extract_digits(uint8_t number, uint8_t digits[2]) {
    //single digit
    digits[0] = number % 10;
    //tens digit
    digits[1] = (number / 10) % 10;
}

void display_number(uint8_t number) {
    uint8_t digits[2];
    Extract_digits(number, digits);
    for (uint8_t i = 0; i < 2; i++) {
        uint8_t high = (bit_select[i] & 0xF0) >> 4;
        uint8_t low = digits[i] & 0x0F;
        PORTA = (high << 4) | (low & 0x0F);
        //dynamical scan
        _delay_ms(1);
    }
}

uint8_t Button_press_detection(uint8_t pin) {
    if (pin > 7) return 0;
    if ((PING & (1 << pin))) {
        _delay_ms(40);
        if ((PING & (1 << pin))) {
            button_triggered[pin] = 1;
            return 1;
        }
    }
    return 0;
}

uint8_t Stopwatch_state() {
    uint8_t max_value = 59;
    switch (state) {
    case STOPWATCH_START:
        if (value >= max_value) {
            value = 0;
        }
        value++;
        break;

    case STOPWATCH_PAUSE:
        break;

    case STOPWATCH_RESET:
        value = 0;
        break;

    default:
        break;
    }
    return value;
}

void Timer1_Init(void) {
    TCCR1B |= (1 << WGM12); // CTC mode, TOP is OCR1A

    // Set the prescaler to 1024
    TCCR1B |= (1 << CS12) | (1 << CS10); // 1024 division

    // Set comparison value OCR1A, count 7812 times for about 1 second
    OCR1A = 7812;

    // Enable compare match A interrupt
    TIMSK |= (1 << OCIE1A);

    // Enable global interrupts
    sei();
}