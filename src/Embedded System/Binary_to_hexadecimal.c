#include <stdio.h>

int main() {
    unsigned int binary = 0b11010111; // C99支持0b前缀的编译器才可以
    printf("十六进制为：0x%X\n", binary); // 输出 0xD7
    return 0;
}
