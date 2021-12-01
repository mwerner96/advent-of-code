#include <stdio.h>

int main()
{
    int depth, old_depth, increased = 0;
    scanf("%d\n", &old_depth);
    while (scanf("%d\n", &depth) != EOF)
    {
        increased += depth > old_depth ? 1 : 0;
        old_depth = depth;
    }
    printf("%d\n", increased);
}
