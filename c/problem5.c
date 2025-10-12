// this topic is sets of pointer arithmatic
// pointer to an array of strings

#include <stdio.h>
int main() {
    char *s[] = {"one","two","three","four"}; // array of string literals
    char **p = s; // pointer to pointer to char, initialized to point to the first element of s
    p++; // move pointer to point to the second element of s
    printf("%c",**p); // print the first character of the string pointed to by p, which is 't' from "two"
    p = p+2; // move pointer to point to the fourth element of s
    printf("%c",**p); // print the first character of the string pointed to by p, which is 'f' from "four"  
    return 0; // return 0 to indicate successful execution
}