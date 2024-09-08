#include<stdio.h>
#include<cs50.h>
int main(){
    char c = get_char("do you agree?[y/n]");
    if (c == 'y'||c=='Y'){
        printf("You have agreeded\n");
    }
    else if(c == 'n'||c=='N'){
        printf("you don't agree\n");
    }
return 0;
}
