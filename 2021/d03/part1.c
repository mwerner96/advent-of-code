#include <stdio.h>

#define LEN 12

int main()
{
    int count[LEN] = {0};
    char line[LEN + 1];
    int lines = 0, gamma = 0, epsilon = 0;
    while (scanf("%s\n", line) != EOF)
    {
        for (int i = 0; i < LEN; i++)
        {
            count[i] += line[i] == '1' ? 1 : 0;
        }
        lines++;
    }
    for (int i = 0; i < LEN; i++)
    {
        int shift = LEN - (1 + i);
        int most_common = count[i] * 2 > lines ? 1 : 0;
        int least_common = most_common ? 0 : 1;
        gamma |= most_common << shift;
        epsilon |= least_common << shift;
    }
    printf("%d\n", gamma * epsilon);
}
