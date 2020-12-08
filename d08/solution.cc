#include <iostream>
#include <fstream>
#include <string>
#include <vector>

static constexpr int LINE_LEN = 32;

struct Operation {
    char op;
    int val;
    Operation(const char * line)
    {
        op = line[0];
        std::string s(line+4);
        val = std::stoi(s);
    }
    int exec(int &pc, int &acc)
    {
        switch (op) {
        case 'n':
            break;
        case 'a':
            acc += val;
            break;
        case 'j':
            pc += val - 1;
            break;
        case 'e':
            return acc;
        default:
            exit(1);
        }
        op = 'e';
        pc++;
        return 0;
    }
};

struct Program {
    std::vector<Operation> ops;
    int pc, acc;
    Program() : pc(0), acc(0)
    {
        std::ifstream is("input");
        if (!is.is_open())
            exit(1);
        char line[LINE_LEN];
        while (is.getline(line, LINE_LEN)) {
            ops.emplace_back(line);
        }
        is.close();
    }
    int run(bool &exited_normally)
    {
        int res;
        exited_normally = false;
        while (!(res = ops[pc].exec(pc, acc))) {
            if (pc >= ops.size()) {
                exited_normally = true;
                return acc;
            }
        }
        return res;
    }
    void flip_instruction(int idx)
    {
        int i = 0;
        for (auto &op : ops) {
            if (op.op == 'n' || op.op == 'j') {
                if (i == idx) {
                    op.op = op.op == 'n' ? 'j' : 'n';
                    return;
                }
                i++;
            }
        }
    }
};

int main() {
    Program p;
    bool exitstatus;
    std::cout << "Part 1: " << p.run(exitstatus) << std::endl;
    int flipidx = 0;
    while (!exitstatus) {
        Program p;
        p.flip_instruction(flipidx++);
        int res = p.run(exitstatus);
        if (exitstatus) {
            std::cout << "Part 2: " << res << std::endl;
            break;
        }
    }
}
