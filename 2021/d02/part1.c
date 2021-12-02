#include <stdio.h>
#include <stdlib.h>

int main()
{
    int depth = 0, forward = 0;
    char cmd[10];
    int amount;
    while (scanf("%s %d\n", cmd, &amount) != EOF)
    {
        switch (cmd[0])
        {
        case 'd':
            depth += amount;
            break;
        case 'u':
            depth -= amount;
            break;
        case 'f':
            forward += amount;
            break;
        default:
            exit(1);
        }
    }
    printf("%d\n", depth * forward);
}
