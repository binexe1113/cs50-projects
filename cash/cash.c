#include <cs50.h>
#include <stdio.h>
int calculate_quarters(int change);
int calculate_dimes(int change);
int calculate_nickels(int change);
int calculate_pennies(int change);
int main()
{

    // declare variable for the change
    int change;

    // enter prompt to user for variable while checks for boolean expression true
    do
    {
        change = get_int("enter change:");
    }
    while (change < 0);
    // Calculate how many quarters you should give customer
    int quarters = calculate_quarters(change);
    // Subtract the value of those quarters from cents
    change = change - (quarters * 25);
    // calculate how many dimes we should give
    int dimes = calculate_dimes(change);
    // subtract the value of dimes from cents
    change = change - (dimes * 10);
    // calculate how many nickels we should give
    int nickels = calculate_nickels(change);
    change = change - (nickels * 5);
    // calculate how many pennies we should give
    int pennies = calculate_pennies(change);
    change = change - pennies;

    // CALCULATE HOW MUCH CHANGE WE USED COINS//
    printf("%d\n", quarters + dimes + nickels + pennies);

    // returns main
    return 0;
}

// DEFINING FUNCIOTNS TO CALCULATE HOW MANY QUARTERS DIMES NICKELS AND PENNIES SHOULD GIVE //

// QUARTERS
int calculate_quarters(int change)
{
    int quarters = 0;
    while (change >= 25)
    {
        quarters++;
        change = change - 25;
    }
    return quarters;
}

// DIMES
int calculate_dimes(int change)
{
    int dimes = 0;
    while (change >= 10)
    {
        dimes++;
        change = change - 10;
    }
    return dimes;
}
// NICKELS
int calculate_nickels(int change)
{
    int nickels = 0;
    while (change >= 5)
    {
        nickels++;
        change = change - 5;
    }
    return nickels;
}
// PENNIES
int calculate_pennies(int change)
{
    int pennies = 0;
    while (change >= 1)
    {
        pennies++;
        change = change - 1;
    }
    return pennies;
}
