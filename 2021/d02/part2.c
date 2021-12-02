#include <stdio.h>
#include <stdlib.h>

int main()
{
    int depth = 0, forward = 0, aim = 0;
    char cmd[10];
    int amount;
    while (scanf("%s %d\n", cmd, &amount) != EOF)
    {
        switch (cmd[0])
        {
        case 'd':
            aim += amount;
            break;
        case 'u':
            aim -= amount;
            break;
        case 'f':
            forward += amount;
            depth += amount * aim;
            break;
        default:
            exit(1);
        }
    }
    printf("%d\n", depth * forward);
}
