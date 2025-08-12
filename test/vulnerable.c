#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    char buffer[10];
    char *ptr;
    
    // Vulnerability 1: Dangerous function gets()
    printf("Enter your name: ");
    gets(buffer);  // gets() is unsafe - buffer overflow risk
    
    // Vulnerability 2: Unsafe strcpy without bounds checking
    char src[20] = "This is too long for buffer";
    strcpy(buffer, src);  // Potential buffer overflow
    
    // Vulnerability 3: Use after free
    ptr = malloc(100);
    free(ptr);
    printf("Value: %d\n", *ptr);  // Use after free
    
    return 0;
}