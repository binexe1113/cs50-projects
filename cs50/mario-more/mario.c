#include <cs50.h>
#include <stdio.h>

int main()
{
    // declares interger y
    int y;
    // asks user for input to y until meets the condition of boolean expression
    do
    {
        y = get_int("Height ");
    }
    while (y < 1 || y > 8);

    // Defining interger r for number of rows
    for (int r = 1; r <= y; r++)
    {
        // print spaces for alignment
        for (int s = 0; s < y - r; s++)
        {
            printf(" ");
        }

        // making left hashes
        for (int lefthash = 0; lefthash < r; lefthash++)
        {
            printf("#");
        }
        // making double spaces for pyramid
        printf("  ");

        // making right piramid hashes
        for (int righthash = 0; righthash < r; righthash++)
        {
            printf("#");
        }
        // move to the next line
        printf("\n");
    }
    return 0;
}
