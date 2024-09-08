// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill_amount, float tax_percent, float tip_percent);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    float tip_percent = get_float("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill_amount, float tax_percent, float tip_percent)
{
    float bill = bill_amount;
    float tax = (tax_percent/100)*bill_amount;
    float bill_tax = (bill + tax);
    float tip = (tip_percent/100)*bill_tax;
    float total = bill + tax + tip;
  float each = total/2;
    return each;
}
