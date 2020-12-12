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

struct Coordinate {
    int x, y;

    Coordinate(int x, int y) : x(x), y(y) {}
};

struct Ship {
    Coordinate ship;
    Coordinate waypoint;
    std::vector<Instruction> instructions;

    Ship (std::string route) : ship(0, 0), waypoint(10, 1)
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
        ship.x += waypoint.x * i.amount;
        ship.y += waypoint.y * i.amount;
    }

    inline void rotate(Instruction &i)
    {
        // we can assume, that we rotate only in steps of 90degrees and never by 0 (or 360)
        int amount = i.direction == 'R' ? i.amount : -i.amount;
        if (amount < 0)
            amount += 360;
        int tmp;
        switch (amount) {
        case 90:
            tmp = waypoint.x;
            waypoint.x = waypoint.y;
            waypoint.y = -tmp;
            break;
        case 180:
            waypoint.x = -waypoint.x;
            waypoint.y = -waypoint.y;
            break;
        case 270:
            tmp = waypoint.x;
            waypoint.x = -waypoint.y;
            waypoint.y = tmp;
            break;
        default:
            throw std::invalid_argument("Invalid argument.");
        }
    }

    inline void move(Instruction &i)
    {
        switch (i.direction) {
        case 'N':
            waypoint.y += i.amount;
            break;
        case 'E':
            waypoint.x += i.amount;
            break;
        case 'S':
            waypoint.y -= i.amount;
            break;
        case 'W':
            waypoint.x -= i.amount;
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
    std::cout << abs(s.ship.x) + abs(s.ship.y) << std::endl;
}
