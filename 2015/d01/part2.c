#include <stdio.h>

int main()
{
    char c;
    int floor = 0;
    int idx = 0;
    while ((c = getchar()) != EOF)
    {
        idx++;
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
        if (floor == -1)
            break;
    }
    printf("%d\n", idx);
    return 0;
}
