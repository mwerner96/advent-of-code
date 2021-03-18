fn part1(numbers: &Vec<u32>) -> u32 {
    for i1 in 0 .. numbers.len() {
        for i2 in i1 .. numbers.len() {
            if numbers[i1] + numbers[i2] == 2020 {
                return numbers[i1] * numbers[i2];
            }
        }
    }
    0
}

fn part2(numbers: &Vec<u32>) -> u32 {
    for i1 in 0 .. numbers.len() {
        for i2 in i1 .. numbers.len() {
            for i3 in i2 .. numbers.len() {
                if numbers[i1] + numbers[i2] + numbers[i3] == 2020 {
                    return numbers[i1] * numbers[i2] * numbers[i3];
                }
            }
        }
    }
    0
}

fn main() {
    let mut numbers: Vec<u32> = include_str!("./input")
        .lines()
        .map(|x| x.parse::<u32>().unwrap())
        .collect();
    numbers.sort_unstable();
    println!("{}", part1(&numbers));
    println!("{}", part2(&numbers));
}
