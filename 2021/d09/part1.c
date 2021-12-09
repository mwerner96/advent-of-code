#include <stdio.h>
#include <assert.h>

#define EDGE 100
#define OUTER (EDGE + 2)

int main()
{
    char area[OUTER][OUTER];

    // build frame
    for (int x = 0; x < OUTER; x++)
        for (int y = 0; y < OUTER; y++)
            area[x][y] = 10;

    // read area
    char c;
    int x = 0, y = 0;
    while ((c = getchar()) != EOF)
    {
        switch (c)
        {
        case '\n':
            assert(x == EDGE);
            assert(y < EDGE);
            x = 0;
            y++;
            break;
        default:
            area[x + 1][y + 1] = c - '0';
            x++;
            break;
        }
    }

    int risk = 0;
    for (int x = 0; x < EDGE; x++)
    {
        for (int y = 0; y < EDGE; y++)
        {
            char cur = area[x + 1][y + 1];
            if (
                (cur < area[x][y + 1]) &&
                (cur < area[x + 2][y + 1]) &&
                (cur < area[x + 1][y]) &&
                (cur < area[x + 1][y + 2]))
            {
                risk += cur + 1;
            }
        }
    }

    printf("%d\n", risk);
}
