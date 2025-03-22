#include <stdio.h>
#include <stdlib.h>
#include <ctype.h> 

void function1(void);//no return value, no input parameter.
void function2(int a, int b);//no return value, with input parameter.
int function3(); //return value, no input parameter.
int function4(int a, int b); 
int function5(int array_size, int *a);//with address.

int main (){
char b[] = "William Shakespeare was a  renowned English poet, \
playwright, and actor born in 1564 in Stratfordupon-Avon. \
His birthday is most commonly celebrated on 23 April (see When was Shakespeare born), \
which is also believed to be the date he died in 1616.";

printf("The string is %s\n", b);

size_t size_b = sizeof(b);

int i;
int lower_case = 0;
int upper_case = 0;
int numbers = 0;
int spaces = 0;
/*
for (i = 0; b[i] != '\0'; i++) {
    if (islower(b[i])) {
        printf("%c", b[i]);
        lower_case += 1;
    }  
}
printf("\n");
*/

lower_case = 0;

while (b[i])
{   
    if (b[i]>='a' && b[i]<='z'){
    lower_case ++;
    printf("%c", b[i]);
    }
    if (b[i]>='A' && b[i]<='Z'){
    upper_case ++;
    printf("%c", b[i]);
    }
    if (b[i]>='0' && b[i]<='9'){
    numbers ++;
    printf("%c", b[i]);
    }
    if (b[i] == ' '){
    spaces ++;
    printf(" ");
    }
    i++;
}

printf("\nThe value of lower_case is %d\n", lower_case);
printf("The value of upper_case is %d\n", upper_case);
printf("The value of numbers is %d\n", numbers);
printf("The value of spaces is %d\n", spaces);
printf("Size of b: %zu\n", size_b);


function1();
function2(10, 5);
int area = function3();
printf("The area is %d\n", area);
printf("The area is %d\n", function3());

int sidel = 9;
printf("The area is %d\n", function4(10, sidel));

int array[] = {2, 7, 11, 0, 13, 5};
//(the total size in bytes of the entire array/size of one element in bytes)
int arrl_element_num =  sizeof(array)/sizeof(array[0]);
int arrl_min = function5(arrl_element_num, array);
printf("\nMin val fron array:%d\n", arrl_min);
return 0;
}


//Function definition
void function1(void){
    printf("This is function1\n");
}

void function2(int a, int b){
    int area = a * b;
    printf("The area is %d\n", area);
}

int function3(){
    int a = 10;
    int b = 5;
    int area = a * b;
    return area;
}

int function4(int a, int b){
    return a * b;
}

int function5(int array_size, int *a){
    int i = 0;
    int min_val = *a;//value at the address
    while (i <= array_size-1){
        if(min_val > *a) {
            min_val = *a;
            a++;
        }
        i++;
    }
    return min_val;
}