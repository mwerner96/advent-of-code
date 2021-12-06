#include <stdio.h>
#include <assert.h>

#define MAX_COORD 1000
#define INPUT_LINES 500

#define min(a, b) (((a) < (b)) ? (a) : (b))
#define max(a, b) (((a) > (b)) ? (a) : (b))

typedef struct vector
{
    int x1, y1;
    int x2, y2;
} vector_t;

int main()
{
    int grid[MAX_COORD][MAX_COORD] = {0};
    vector_t pipes[INPUT_LINES] = {0};
    vector_t *cur = pipes;
    int amount = 0;
    while (scanf("%d,%d -> %d,%d\n", &cur->x1, &cur->y1, &cur->x2, &cur->y2) != EOF)
    {
        assert(cur->x1 < MAX_COORD);
        assert(cur->y1 < MAX_COORD);
        assert(cur->x2 < MAX_COORD);
        assert(cur->y2 < MAX_COORD);
        assert(amount < INPUT_LINES);
        cur++;
        amount++;
    }

    int overlap = 0;
    cur = pipes;
    for (int i; i < amount; i++)
    {
        if (cur->x1 == cur->x2)
        {
            for (int y = min(cur->y1, cur->y2); y <= max(cur->y1, cur->y2); y++)
            {
                grid[cur->x1][y]++;
                overlap += grid[cur->x1][y] == 2 ? 1 : 0;
            }
        }
        else if (cur->y1 == cur->y2)
        {
            for (int x = min(cur->x1, cur->x2); x <= max(cur->x1, cur->x2); x++)
            {
                grid[x][cur->y1]++;
                overlap += grid[x][cur->y1] == 2 ? 1 : 0;
            }
        }
        cur++;
    }
    printf("%d\n", overlap);
}
