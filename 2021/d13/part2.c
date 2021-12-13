#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_X 2000
#define MAX_Y 2000

int main()
{
    bool paper[2000][2000] = {false};
    int pos_x, pos_y;
    while (scanf("%d,%d\n", &pos_x, &pos_y) == 2)
    {
        paper[pos_x][pos_y] = true;
    }
    char direction;
    int axis, cur_x = MAX_X, cur_y = MAX_Y;
    while (scanf("fold along %c=%d\n", &direction, &axis) != EOF)
    {
        switch (direction)
        {
        case 'x':
            for (int x = 0; x < axis; x++)
            {
                for (int y = 0; y < cur_y; y++)
                {
                    paper[x][y] |= paper[axis * 2 - x][y];
                    paper[axis * 2 - x][y] = false;
                }
            }
            cur_x = axis;
            break;
        case 'y':
            for (int x = 0; x < cur_x; x++)
            {
                for (int y = 0; y < axis; y++)
                {
                    paper[x][y] |= paper[x][axis * 2 - y];
                    paper[x][axis * 2 - y] = false;
                }
            }
            cur_y = axis;
            break;
        default:
            exit(1);
        }
    }
    for (int y = 0; y < cur_y; y++)
    {
        for (int x = 0; x < cur_x; x++)
            putchar(paper[x][y] ? '#' : ' ');
        putchar('\n');
    }
}
