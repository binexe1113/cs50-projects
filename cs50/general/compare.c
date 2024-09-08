#include<stdio.h>
#include<cs50.h>
int main(){
    int x = get_int("insert value of x: ");

    int y = get_int("insert value of y: ");

    if(x>y){
        printf("x is greater than y\n");
    }
    else if(x<y) {
        printf("x is smaller than y\n");
    }
    else {
        printf("x is equal to y\n");
    }
return 0;
}
