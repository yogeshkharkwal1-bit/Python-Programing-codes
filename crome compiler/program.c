#include <stdio.h>
#define PI 3.14159   // PI define kiya

int main() {
    float radius, area;
    printf("Enter radius: ");
    scanf("%f", &radius);  // radius input liya
    area = PI * radius * radius;  // area calculate
    printf("The area of circle is %.2f\n", area);  // 2 decimal tak print
    return 0;
}
