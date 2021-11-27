#include <stdbool.h>
#include <stdio.h>

#define CYCLES 6
#define INIT_SIZE 8
#define EDGE ((CYCLES + 1) * 2 + INIT_SIZE)

int main()
{
    bool dimension[EDGE][EDGE][EDGE][EDGE] = {false};
    bool next_dim[EDGE][EDGE][EDGE][EDGE] = {false};
    char c;
    int x = CYCLES + 1;
    int y = CYCLES + 1;
    int z = CYCLES + 1;
    int w = CYCLES + 1;
    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
        {
            x = CYCLES + 1;
            y++;
        }
        else
        {
            dimension[x][y][z][w] = c == '#';
            x++;
        }
    }
    int cycle = CYCLES;
    int count;
    while (cycle--)
    {
        count = 0;
        for (int x = 1; x < EDGE - 1; x++)
            for (int y = 1; y < EDGE - 1; y++)
                for (int z = 1; z < EDGE - 1; z++)
                    for (int w = 1; w < EDGE - 1; w++)
                    {
                        int live = 0;
                        bool active = dimension[x][y][z][w];
                        for (int _x = -1; _x <= 1; _x++)
                            for (int _y = -1; _y <= 1; _y++)
                                for (int _z = -1; _z <= 1; _z++)
                                    for (int _w = -1; _w <= 1; _w++)
                                        live += dimension[_x + x][_y + y][_z + z][_w + w] ? 1 : 0;
                        if (active && ((live == 3) || (live == 4)))
                            active = true;
                        else if (!active && (live == 3))
                            active = true;
                        else
                            active = false;
                        next_dim[x][y][z][w] = active;
                    }
        for (int x = 0; x < EDGE; x++)
            for (int y = 0; y < EDGE; y++)
                for (int z = 0; z < EDGE; z++)
                    for (int w = 0; w < EDGE; w++)
                    {
                        dimension[x][y][z][w] = next_dim[x][y][z][w];
                        count += dimension[x][y][z][w] ? 1 : 0;
                    }
    }
    printf("%d\n", count);
}
