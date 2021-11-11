#include <iostream>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>

static constexpr int LINE_LEN = 10;

struct Instruction {
    char direction;
    int amount;

    Instruction (std::string instruction)
    {
        direction = instruction[0];
        amount = std::stoi(instruction.substr(1, std::string::npos));
    }
};

struct Ship {
    int x, y, angle;
    std::vector<Instruction> instructions;

    Ship (std::string route) : x(0), y(0), angle(0)
    {
        std::ifstream is(route);
        if (!is.is_open())
            throw std::invalid_argument(route);
        char line[LINE_LEN];
        while (is.getline(line, LINE_LEN))
            instructions.emplace_back(line);
        is.close();
    }

    inline void forward(Instruction &i)
    {
        // trigonometric functions caused rounding errors
        x += angle == 0 ? i.amount : 0;
        y += angle == 90 ? i.amount : 0;
        x -= angle == 180 ? i.amount : 0;
        y -= angle == 270 ? i.amount : 0;
    }

    inline void rotate(Instruction &i)
    {
        angle += i.direction == 'L' ? i.amount : -i.amount;
        while (angle >= 360)
            angle -= 360;
        while (angle < 0)
            angle += 360;
    }

    inline void move(Instruction &i)
    {
        switch (i.direction) {
        case 'N':
            y += i.amount;
            break;
        case 'E':
            x += i.amount;
            break;
        case 'S':
            y -= i.amount;
            break;
        case 'W':
            x -= i.amount;
            break;
        }
    }

    void navigate()
    {
        for (auto &inst : instructions) {
            switch (inst.direction) {
            case 'F':
                forward(inst);
                break;
            case 'R':
            case 'L':
                rotate(inst);
                break;
            case 'N':
            case 'E':
            case 'S':
            case 'W':
                move(inst);
                break;
            default:
                throw std::invalid_argument("Invalid argument.");
            }
        }
    }
};

int main()
{
    Ship s("input");
    s.navigate();
    std::cout << abs(s.x) + abs(s.y) << std::endl;
}
