#include <iostream>
#include <fstream>

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
                count += __builtin_popcount(map_group);
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
    count += __builtin_popcount(map_group);

    std::cout << count << std::endl;

    is.close();
}
