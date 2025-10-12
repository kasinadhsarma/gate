// here qution what will the value of temp when i = 5 itteration
//to solve this problem we need to understand static variables in C
//static variable is a variable that retains its value between function calls
#include <stdio.h>

int temp=0;
void func(){
    static int x =0;
    x++;
    temp =temp+x;
}

int main(){
    for (int i = 0; i < 7; i++)
        func();
    printf("%d\n", temp);
    return 0;
}
