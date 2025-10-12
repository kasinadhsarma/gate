// logic of 5,6 is the code of this is small matrix pointer arithmatic
// here 3*3 matrix is given and we need to find the value of p[0] and *(p+1)
// here p is pointing to a[1][1] that is 5 and p+1 is pointing to a[1][2] that is 6
#include <stdio.h>
int main() {
    int a [3] [3] = { {1,2,3}, {4,5,6}, {7,8,9} };
    int *p = (int *) a+4;
    printf("%d %d\n",p[0],*(p+1));
    return 0;
}