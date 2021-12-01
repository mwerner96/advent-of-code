#include <stdio.h>

#define WINDOW 3

int next_idx[] = {1, 2, 3, 0};

int sum(int *buf, int idx)
{
    int sum = buf[idx];
    sum += buf[next_idx[idx]];
    return sum + buf[next_idx[next_idx[idx]]];
}

int main()
{
    int windows[WINDOW + 1], idx = 0, increased = 0;
    scanf("%d\n", &windows[idx = next_idx[idx]]);
    scanf("%d\n", &windows[idx = next_idx[idx]]);
    scanf("%d\n", &windows[idx = next_idx[idx]]);
    while (scanf("%d\n", &windows[idx = next_idx[idx]]) != EOF)
    {
        increased += sum(windows, next_idx[idx]) < sum(windows, next_idx[next_idx[idx]]) ? 1 : 0;
    }
    printf("%d\n", increased);
}
