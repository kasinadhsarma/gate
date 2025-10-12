#include <stdio.h>
int main() {
    int a = 57, b = 710;
    int *p = &a, *q = &b;
    *p = *q; // here a = 710  and b = 710
    *q = *p + 2; // here we add 710 + 2 = 712
    printf("%d %d\n", a, b);
    return 0;
}