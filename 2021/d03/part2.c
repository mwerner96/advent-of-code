#include <stdio.h>
#include <stdlib.h>

#define LEN 12
#define LINES 1000

typedef struct line
{
    char line[LEN + 1];
    struct line *link_1, *link_2;
} line_t;

line_t lines_buf[LINES];

void init_lines_buf();
int find_oxygen();
int find_scrubber();

int main()
{
    init_lines_buf();

    int oxygen = find_oxygen();
    int scrubber = find_scrubber();

    printf("%d\n", oxygen * scrubber);
}

void init_lines_buf()
{
    int lines = 0;
    line_t *cur_line = lines_buf;
    while (scanf("%s\n", cur_line->line) != EOF)
    {
        lines++;
        cur_line->link_1 = lines_buf + lines;
        cur_line->link_2 = lines_buf + lines;
        cur_line++;
        if (lines > LINES)
            exit(1);
    }
    cur_line--;
    cur_line->link_1 = NULL;
    cur_line->link_2 = NULL;
}

int find_oxygen()
{
    line_t *first, *cur;
    int idx = 0, count = 0, lines = 0;
    first = cur = lines_buf;
    while (cur)
    {
        count += cur->line[idx] == '1' ? 1 : 0;
        cur = cur->link_1;
        lines++;
    }
    while (first->link_1)
    {
        line_t *prev = NULL;
        cur = first;
        char most_common = count * 2 > lines ? '1' : '0';
        most_common = 2 * count == lines ? '1' : most_common;
        count = lines = 0;
        while (cur)
        {
            if (cur->line[idx] == most_common)
            {
                count += cur->line[idx + 1] == '1' ? 1 : 0;
                lines++;
                prev = cur;
            }
            else
            {
                // remove cur
                if (cur == first)
                    first = cur->link_1;
                else
                    prev->link_1 = cur->link_1;
            }
            cur = cur->link_1;
        }
        idx++;
    }
    // first is result
    int oxygen = 0;
    for (int i = 0; i < LEN; i++)
    {
        int shift = LEN - (1 + i);
        oxygen |= (first->line[i] == '1' ? 1 : 0) << shift;
    }
    return oxygen;
}

int find_scrubber()
{
    line_t *first, *cur;
    int idx = 0, count = 0, lines = 0;
    first = cur = lines_buf;
    while (cur)
    {
        count += cur->line[idx] == '1' ? 1 : 0;
        cur = cur->link_2;
        lines++;
    }
    while (first->link_2)
    {
        line_t *prev = NULL;
        cur = first;
        char least_common = count * 2 < lines ? '1' : '0';
        least_common = 2 * count == lines ? '0' : least_common;
        count = lines = 0;
        while (cur)
        {
            if (cur->line[idx] == least_common)
            {
                count += cur->line[idx + 1] == '1' ? 1 : 0;
                lines++;
                prev = cur;
            }
            else
            {
                // remove cur
                if (cur == first)
                    first = cur->link_2;
                else
                    prev->link_2 = cur->link_2;
            }
            cur = cur->link_2;
        }
        idx++;
    }
    // first is result
    int scrubber = 0;
    for (int i = 0; i < LEN; i++)
    {
        int shift = LEN - (1 + i);
        scrubber |= (first->line[i] == '1' ? 1 : 0) << shift;
    }
    return scrubber;
}
