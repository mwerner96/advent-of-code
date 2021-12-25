#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define EDGE_X 139
#define EDGE_Y 137

#define EMPTY '.'
#define EAST '>'
#define SOUTH 'v'
#define PHANTOM '~'

#define n_x(x) (((x) + 1) == EDGE_X ? 0 : ((x) + 1))
#define n_y(y) (((y) + 1) == EDGE_Y ? 0 : ((y) + 1))

void clear_phantoms(char field[EDGE_X][EDGE_Y])
{
    for (int y = 0; y < EDGE_Y; y++)
        for (int x = 0; x < EDGE_X; x++)
            if (field[x][y] == PHANTOM)
                field[x][y] = EMPTY;
}

char field[EDGE_X][EDGE_Y] = {0};

int main()
{
    char c;
    int x = 0, y = 0;

    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
        {
            assert(x == EDGE_X);
            x = 0;
            y++;
            continue;
        }
        field[x][y] = c;
        x++;
    }
    assert(y == EDGE_Y);

    int i = 0;
    for (bool changed = true; changed; i++)
    {
        changed = false;
        bool skip = false;

        for (y = 0; y < EDGE_Y; y++)
        {
            skip = false;
            for (x = 0; x < EDGE_X; x++)
            {
                if (skip)
                {
                    skip = false;
                    continue;
                }
                if (field[x][y] == EAST)
                    if (field[n_x(x)][y] == EMPTY)
                    {
                        field[n_x(x)][y] = EAST;
                        field[x][y] = PHANTOM;
                        changed = true;
                        skip = true;
                    }
            }
        }

        clear_phantoms(field);

        for (x = 0; x < EDGE_X; x++)
        {
            skip = false;
            for (y = 0; y < EDGE_Y; y++)
            {
                if (skip)
                {
                    skip = false;
                    continue;
                }
                if (field[x][y] == SOUTH)
                    if (field[x][n_y(y)] == EMPTY)
                    {
                        field[x][n_y(y)] = SOUTH;
                        field[x][y] = PHANTOM;
                        changed = true;
                        skip = true;
                    }
            }
        }

        clear_phantoms(field);
    }

    printf("%d\n", i);
}
