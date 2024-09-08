#include <stdio.h>

int main()
{
    int n1 = 0;
    int n2 = 0;
    int add = 0;
    int sub = 0;
    int mult = 0;
    int div1 =0;
    int div2=0;

    printf("valor do número 1:");
    scanf("%i",& n1);

    printf("valor do número 2: ");
    scanf("%i",& n2);

    add = n1+n2;

    sub = n1 - n2;

    mult = n1 * n2;

    if (n2==0){
        printf("nao");
            }
    else    {
        div2 = n1 % n2;
        }
    if (n2==0){
        printf("nao");
        }
    else{
        div1 = n1 / n2;
        }

    printf("Valor da soma: %i \n",add);
    printf("Valor da subtração: %i \n",sub);
    printf("Valor da multiplicação: %i \n",mult);
    if (n2==0){
        printf("Divisão por 0: operações invalidas \n");
        }
    else{
    printf("Valor do quociente: %i \n",div1);
    printf("Resto da divisão: %i \n",div2);}




}
