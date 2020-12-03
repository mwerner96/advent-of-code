#include <stdint.h>
constexpr uint32_t input[] = {
    0b0000100100000001000000001000010,
    0b0011010101000000000000000000010,
    0b0000101011001000010000001000000,
    0b0000000001010000001100000100000,
    0b0000000000101110110001100000000,
    0b1000010100000001100000100100000,
    0b1000000000001010001001001101100,
    0b0000001100000000000001000001000,
    0b0011000000000011100101001100000,
    0b0000000000010000000010000001100,
    0b0011000000000001100000000000000,
    0b0010000001110100000101010000000,
    0b0010010010000000000101000010000,
    0b0100000110000000000000000000000,
    0b0001000110010001000000000100110,
    0b0100000010010010001000000101100,
    0b0011011000000010010000010010001,
    0b0000000000000010010010001000000,
    0b0001000100001100000100010001000,
    0b0000000000000000000000100010000,
    0b0000000100000010001001100010100,
    0b1100000010010000010000100000100,
    0b0000101011010100001000000000000,
    0b1000001100000000000001000000000,
    0b0000000000100000000000101000001,
    0b0001000110000101000000001001000,
    0b0000000000000000100101101100001,
    0b0000001000100011000110000100000,
    0b1100001001001000100100000000000,
    0b1000000000000000000100010100100,
    0b0000110000110100001001000000100,
    0b0000010000000000010000000001100,
    0b0010000000000000010000000001001,
    0b0000001100000000000000000000100,
    0b0010000011100011110001000101100,
    0b1001010000001000001000000010100,
    0b1101000000000111111000000001000,
    0b0010000111000101000000000000001,
    0b0000010000000000000010000000001,
    0b0000100000010010000000001000100,
    0b0000011100000101110000000111000,
    0b1010010000010000110001000000001,
    0b0011000010010000000001000101000,
    0b0010011000000000000010000101010,
    0b0011010010101000000000110000000,
    0b1010010000000001000000000000001,
    0b1001000000000111000000010100101,
    0b0000000000000100010000100000010,
    0b0000000000101000110111000001010,
    0b0010000010000000000000000000000,
    0b0000000100000011101000000010000,
    0b0000100001000000000100011101010,
    0b0100000000000001000000000000100,
    0b0000100100000000000001010000100,
    0b0000100000100010001101000000000,
    0b0010001000100000000000000000010,
    0b0000000010000100000100000000000,
    0b0000011000000010001010010010000,
    0b0001000000000000100101000000000,
    0b0000000000000000000000100000000,
    0b0000100000010000010100001000000,
    0b0000010010000000001000000000110,
    0b0000000000000001000001000011000,
    0b0001010100010010000000000010000,
    0b0100001110000001100010101010000,
    0b0000010001000011110000110000000,
    0b0010000001001000001101000100000,
    0b0001011001000010011000001000000,
    0b0010000001000100011000001000100,
    0b0000001000001000000001000000000,
    0b0010100001000000000000001100001,
    0b0010001000000110000000000001000,
    0b0110100000001000000010000001001,
    0b0001101100010000010000000100100,
    0b0000001100100001000000010000000,
    0b0000010010010100000100000100011,
    0b1101000101010000010001010101101,
    0b0000000000000000000111000100100,
    0b0100000110100000010000000010000,
    0b0110001101000000000010001000010,
    0b0000001000000000000001010000001,
    0b0001000000010010000000000010000,
    0b0111000100000000000011001000110,
    0b1100101000000000100000000000010,
    0b1000101000000101100000000000101,
    0b0101000100000000100000011000000,
    0b0000100010001000001000100001000,
    0b0001100000000000110000000001000,
    0b0000000001000100111000000000000,
    0b0010000000010000000000000001000,
    0b0000000000000100001010000000000,
    0b0000000010000001010000000100001,
    0b0000000000000000010000110101100,
    0b0010001100000000100000000000000,
    0b1001000000001000100001000000000,
    0b0000001010000010000010011101001,
    0b0000100000000000010001010100000,
    0b0000000000001000000000010001000,
    0b0000000000100001101000000000100,
    0b0000000000000010001000100100000,
    0b1000000100001001100001000000110,
    0b0001000010000000000000000010000,
    0b0101100000000000001000100001100,
    0b0000100100000000010010000100001,
    0b0010000011001000000101001000000,
    0b0010010000010000000010001001001,
    0b0000000001101011010000000100001,
    0b0010000000110110001000001000001,
    0b0000000000000110001000000000001,
    0b0010000001001000010001001011000,
    0b0000100000000100000010000000001,
    0b0000000100000000100101010011001,
    0b0010000001000000000001100010000,
    0b0000010010100010000000000000011,
    0b0100100000010000001000000001001,
    0b0001100000000000000010000100000,
    0b0000000100010000000110010000000,
    0b0000010000100010001001000001010,
    0b0001000000000100000100000000000,
    0b0001000001110000100001000100010,
    0b1001000001000000000100000000010,
    0b0000000000000000010100000100001,
    0b0000000000010000000000100100000,
    0b0000000010100001000100100000111,
    0b1000000000000000000000000000010,
    0b0011001001000110000000001000000,
    0b0000001100001010001000000000100,
    0b0000001001101000000100100000100,
    0b0001000000011000010100001000000,
    0b0000010000000010001000000000000,
    0b1000000010001000000000100000010,
    0b0000001000000100001001000000000,
    0b0010100000000100100000010000100,
    0b0100101000000000011000011101001,
    0b0001000010110010001000010000000,
    0b0010000010000001011100000001000,
    0b0000000000000000000000000000001,
    0b0000010010001000000000001000000,
    0b0110001000011000010101010000101,
    0b0100010000100010000000010000000,
    0b0000100000000000010001100100000,
    0b0000110010000100001000001000011,
    0b0000000000000100110101010000000,
    0b1000000010101000000010010010000,
    0b1001000000000001000000011100100,
    0b0100110100000100000000100000000,
    0b0010100000001000000000000100100,
    0b0000000000010010000000000001101,
    0b0000010000000100000100101101001,
    0b0000001000000110000011000000000,
    0b0011010010100100100000000000000,
    0b0000010000000000000110001010110,
    0b0100000011010000000000100000000,
    0b0010010000000001000001010100000,
    0b0010000010000000100000100100000,
    0b1010100000000101000100001001000,
    0b0101000000010000000000001000010,
    0b0000001000000000000000000100001,
    0b0100010001000001010000000000100,
    0b0100110000111100000000000101000,
    0b0011000001000101000010000100000,
    0b1000000000000000000000100001010,
    0b1110011101010000000000010000011,
    0b0000001000000100000000001000000,
    0b0001000000101100000100000011101,
    0b0000000000000100101000000000001,
    0b0010000000000000101001000001000,
    0b0001000000000000000100001100011,
    0b0000000010000000000000000010000,
    0b1001110000010000000110100000011,
    0b0000101000000000000001000000000,
    0b1000000000010000010011000100000,
    0b0000000000000000100010010000100,
    0b0010001000011000000000010100000,
    0b0000001000000001100000010010001,
    0b0001000010010000010000000100010,
    0b0100000100100010011100001000000,
    0b0000100000000010000101010000010,
    0b1010000100010000100000100110000,
    0b0000000100100100000000001000100,
    0b0010100100000110101000000000000,
    0b0010000100000100110010010100100,
    0b0010110100000000000100010010000,
    0b0000000001000000001000100000000,
    0b0010101000000011000000000101100,
    0b1010000000000101000100100000011,
    0b0100100000000000000000000101000,
    0b0110000001000000000000000010001,
    0b0011011111110000001000010000000,
    0b0000100011010000101000000000000,
    0b0110000100011000000010001001000,
    0b0000000000010001000100010010000,
    0b1000100000100000001000010000010,
    0b0000000000000100000000000000000,
    0b0000000010100000001000101010000,
    0b0000000000000010000000000001010,
    0b0000001000000110010000000100001,
    0b1100010000000000000000001000000,
    0b0000010000001110000010000000101,
    0b0000010100000000000010100000000,
    0b0010100100000000000010000101000,
    0b1101011101010100100000010000000,
    0b0001100000000100100000101010010,
    0b1100000010110000011110010000000,
    0b0000000000001000100100010010000,
    0b0001001000000000000000011010010,
    0b0100001010000000000011010100010,
    0b1111001000000000001000000011100,
    0b0000000100000000000000000100000,
    0b0000000100001000000011000010000,
    0b0010000000001000100001000000000,
    0b0000000000100100010100011001000,
    0b0000110000000000100000000011000,
    0b1000000000110010100100000001000,
    0b0100000000000100001000100010100,
    0b0000100100000100011000010100001,
    0b0100001000001000000100110110101,
    0b1000000100100000001100000000000,
    0b0001001000101000000000000000001,
    0b0000001000000011000011010000001,
    0b0000100001010100000100001000010,
    0b0010000000000101100011001000000,
    0b0001001000000001000010100100001,
    0b1100000001000000001000000000010,
    0b0100000000100000001000100110001,
    0b0010010011001000000000001000111,
    0b0010000001000000000010011000000,
    0b0100000100101000100010000000001,
    0b1010000001100000000000000000000,
    0b1000100000110000000000010000000,
    0b0000000010001000010000000110000,
    0b0001011000100001000010010010010,
    0b0001001000000110000100100110000,
    0b1000100000000001010000000000000,
    0b1100100000000110000010000000001,
    0b0000010000001010001110010000000,
    0b1001101001011100000000000110010,
    0b0000010000100000000001000000010,
    0b1100000000011010000000000000000,
    0b0000100000000010000000000001100,
    0b0000000100000000100000010010011,
    0b0100010001100100001001000000000,
    0b0000000000000100010100000000100,
    0b0000001001000100101110010000000,
    0b0000000011010010100100100000000,
    0b1011001001000000000010001100111,
    0b0110001000000000000101000110010,
    0b0000000000000000100001101000100,
    0b1000000000000000001000000000010,
    0b0001001001000000000000000000000,
    0b0010001101010000000000000000000,
    0b0000010001000000010000000000001,
    0b0010010000000001001101001010001,
    0b0000010100000101000000010000010,
    0b0000000000000000001001000010100,
    0b0010000011101100000001100001010,
    0b0010000001100000001000011010000,
    0b0000100000000000000000001001101,
    0b0000000100001011010000000100001,
    0b0010001000000100100011100001010,
    0b0010010100001000000000001000001,
    0b0000010010010000000100000000100,
    0b0000001011010000001000000000001,
    0b1000100001010011011001001100000,
    0b1000110000101000110000000010000,
    0b0011000000000000101010000000000,
    0b0000100000101001000000010010000,
    0b1001010000010010011000100110000,
    0b0001100000000100000000000100010,
    0b0111100000010011000000000101000,
    0b0000000100000000000000000000000,
    0b0000000000000000010000100100000,
    0b0000000001100000011100000000000,
    0b0110000001010100001010001001110,
    0b0000100000011011101010010000000,
    0b0000000000100000001100000011001,
    0b0000000000010000000100110000000,
    0b0000011100100000000000000110000,
    0b0000000011001010100000010000100,
    0b1000010000000000000000000000000,
    0b0000000000010000000000000001100,
    0b0000001000000000000000001000000,
    0b0000010001001100011000100010000,
    0b0000000000101000110111100000010,
    0b0010100000110000100000000000100,
    0b0000000000100001001000011000100,
    0b0100000001001100010001000001000,
    0b0001100001010000001100011000010,
    0b1000000010000000101101000101000,
    0b1000100000000000000000010000001,
    0b0010000000100000000000000010011,
    0b1000001000000000000000000100001,
    0b0110000010000010000001111000001,
    0b0010000000010001010000000010001,
    0b0011000001000010001000000000001,
    0b0010010000011001011000100000000,
    0b0000000000111001000011000001000,
    0b0001000100001011010001010000000,
    0b0011000000100000001000000011000,
    0b0000000000001000000000000100000,
    0b0110000100000000010000000000000,
    0b0000100001000010000000011000101,
    0b0000000110000000000000000000000,
    0b0000000000101000000000000000001,
    0b0000001101000100000000010000010,
    0b0010001000000100100000000000001,
    0b0000000000111010010100010010010,
    0b1001010010000110001000101000100,
    0b0100000000110001000000101100000,
    0b0001110100011000000000000001100,
    0b1010100010001001000010100100000,
    0b0101011001000010000001010000000,
    0b0001001010000110000000000010010,
    0b0000011001100000010100000000000,
    0b0000001000001000011110000100000,
    0b0101010001001001000000000001000,
    0b0000010000000000000000000000100,
    0b0000000001000000000101110110000,
    0b0000010000001100000000001000000,
    0b0010000000000011000000000001000,
    0b0000000000000010000000001000001,
    0b0010000100100010001101000000000,
    0b0101010000100000000001000000000,
};
