//logic of this code is count is a global variable and it is incremented before and after the printf statement
// so the output will be  3 4 5 and final count will be 6

#include <stdio.h>
int count = 0; // global variable to keep track of count
void fun(int n){
    if (n>0){
        count++; fun(n-1); // pre order increment
        printf("%d ",count); // print current count
        count++; // post order increment
    }
}
int main() {
    fun(3); // here n = 3 so the function will be called 3 times
    printf("\n Final count: %d\n", count); // final count will be 6
    return 0; // return 0 to indicate successful execution
}