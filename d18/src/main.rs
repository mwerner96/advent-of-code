enum Op {
    Add,
    Mul
}

fn eval1(exp: &[char], upper_idx: &mut usize) -> u64 {
    let mut val = 0;
    let mut idx = 0;
    let mut op = Op::Add;

    while idx < exp.len() {
        match exp[idx] {
            '(' => val = {
                let res = eval1(&exp[idx+1..], &mut idx);
                match &op {
                    Op::Add => val + res,
                    Op::Mul => val * res
                }
            },
            '0'..='9' => val = {
                let digit = u64::from(exp[idx].to_digit(10).unwrap());
                match &op {
                    Op::Add => val + digit,
                    Op::Mul => val * digit
                }
            },
            '+' => op = Op::Add,
            '*' => op = Op::Mul,
            ')' => {
                *upper_idx += idx + 1;
                break
            },
            _ => panic!()
        }
        idx += 1;
    }

    val
}

fn part1(expressions: &Vec<&str>) -> u64 {
    let mut sum = 0;
    for e in expressions {
        let ex: Vec<char> = e.chars().filter(|c| !c.is_whitespace()).collect();
        let mut idx = 0;
        sum += eval1(&ex[..], &mut idx);
    }
    sum
}

fn main() {
    let expressions: Vec<&str> = include_str!("../input")
        .lines()
        .collect();
    println!("{}", part1(&expressions));
}
