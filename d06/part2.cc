#include <iostream>
#include <fstream>

// from: https://jjj.de/fxt/fxtbook.pdf
// Arndt, Joerg: Matters Computational
static inline uint32_t count_bits(uint32_t a) {
    const uint32_t mask = 011111111111UL;
    a = (a - ((a&~mask)>>1)) - ((a>>2)&mask);
    a += a>>3;
    a = (a & 070707) + ((a>>18) & 070707);
    a *= 010101;
    return ((a>>12) & 0x3f);
}

int main() {
    std::ifstream is("input");

    if (!is.is_open())
        exit(1);

    char c;
    uint32_t map_group = 0xFFFFFFFF;
    uint32_t map_individual = 0;
    uint32_t count = 0;
    bool new_record = false;
    while (is.get(c)) {
        if (c == '\n') {
            if (new_record) {
                count += count_bits(map_group);
                map_group = 0xFFFFFFFF;
            }
            else {
                map_group &= map_individual;
                map_individual = 0;
            }
            new_record = true;
            continue;
        }
        new_record = false;
        map_individual |= 1 << (c - 'a');
    }

    // add last entry, since we don't have the double '\n' there
    count += count_bits(map_group);

    std::cout << count << std::endl;

    is.close();
}
