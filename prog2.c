#include <stdio.h>

int main(){

    int x = 0;
    printf("x =");
    scanf("%i",&x);

    if (x>0){
        printf("o numéro é positivo \n");
    }
    else if (x<0){
        printf ("o número é negatvo\n");
    }
    else{
        printf("o número é igual a 0\n");
    }


    return 0;

}
