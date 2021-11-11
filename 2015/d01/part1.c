#include <stdio.h>

int main()
{
    char c;
    int floor = 0;
    while ((c = getchar()) != EOF)
    {
        switch (c)
        {
        case '(':
            floor++;
            break;
        case ')':
            floor--;
            break;
        default:
            break;
        }
    }
    printf("%d\n", floor);
    return 0;
}
