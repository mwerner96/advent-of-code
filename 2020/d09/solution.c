#include <stdbool.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <limits.h>

#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

#define LOOKBEHIND 25
int buf[1100];

int find_mismatch_build_buf(int * lineidx) {
    char *line;
    size_t len = 0;
    int sumbuf[LOOKBEHIND];
    int bufidx = 0, retval;
    FILE * fp = fopen("input", "r");
    if (fp == NULL) {
        printf("alles kaputt\n");
        exit(1);
    }
    for (*lineidx = 0; bufidx < LOOKBEHIND; (*lineidx)++, bufidx++) {
        getline(&line, &len, fp);
        buf[*lineidx] = sumbuf[bufidx] = strtol(line, NULL, 10);
    }
    while (getline(&line, &len, fp) != -1) {
        bool match = false;
        int current = strtol(line, NULL, 10);
        for (int i = 0; i < LOOKBEHIND; i++) {
            for (int j = i+1; j < LOOKBEHIND; j++) {
                if (sumbuf[i]+sumbuf[j] == current) {
                    match = true;
                    break;
                }
            }
            if (match)
                break;
        }
        if (!match)
            retval = current;
        bufidx = (bufidx+1) % LOOKBEHIND;
        buf[*lineidx] = sumbuf[bufidx] = current;
        (*lineidx)++;
    }
    fclose(fp);
    return retval;
}

int sum_lowhigh_in_range(int idx_low, int idx_high) {
    int lowest = INT_MAX, highest = 0;
    for (; idx_low <= idx_high; idx_low++) {
        lowest  = MIN(lowest,  buf[idx_low]);
        highest = MAX(highest, buf[idx_low]);
    }
    return lowest + highest;
}

int find_weakness(const int mismatch, const int lines) {
    int idx_low = 0, idx_high = 0, sum = 0;
    while (idx_high < lines) {
        sum += buf[idx_high++];
        while (sum > mismatch)
            sum -= buf[idx_low++];
        if (sum == mismatch)
            return sum_lowhigh_in_range(idx_low-1, idx_high-1);
    }
    return -1;
}

int main() {
    int inputlines, mismatch;
    printf("Part 1: %d\n", mismatch = find_mismatch_build_buf(&inputlines));
    printf("Part 2: %d\n", find_weakness(mismatch, inputlines));
}
