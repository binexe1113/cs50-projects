#include <stdio.h>

int main()
{
    float sb;
    float inss;
    float irpf;
    float descontos;
    float salárioLiquido;

    printf("\nDigite seu salário bruto(SB): ");
    scanf("%f", &sb);

    inss = sb * 0.14;
    printf("\nSeu INSS é: R$%.2f", inss);

    if (sb > 10000.00){
        irpf = 0.1 * sb;
    }
    else{
        irpf = 0.08 * sb;
    }
    printf("\nSeu IRPF é: R$%.2f", irpf);

    descontos = inss + irpf;
    printf("\nSeus descontos são: R$%.2f", descontos);

    salárioLiquido = sb - descontos;
    printf("\nSeu salário líquido é: R$%.2f", salárioLiquido);
    

    return 0;
}
