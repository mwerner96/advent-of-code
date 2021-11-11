#include <stdio.h>

#define UPDATE   \
    area += tmp; \
    smallest = tmp < smallest ? tmp : smallest;

int main()
{
    int w, l, h;
    int smallest;
    int area;
    long long int total = 0;
    int tmp;
    while (scanf("%dx%dx%d\n", &w, &l, &h) != EOF)
    {
        area = smallest = w * l;
        tmp = w * h;
        UPDATE
        tmp = l * h;
        UPDATE
        area <<= 1;
        area += smallest;
        total += area;
    }
    printf("%lld\n", total);
    return 0;
}
