fn plus(a: usize, b: usize) -> usize {
    (a + b) % 256
}

struct Counter {
    depth: u8,
    MAX_LENGTH: u64,
    output: [u64; 256],
    acc: u32,
}

impl Counter {
    fn new(depth: u8) -> Counter {
        Counter {
            depth: depth,
            MAX_LENGTH: if depth == 1 { 253 } else { 251 },
            output: [0; 256],
            acc: 0,
        }
    }
    fn cases(&self, mut length: u64) -> u64 {
        assert!(length >= self.MAX_LENGTH);
        let mut acc = 1;
        while length > self.MAX_LENGTH {
            acc *= length;
            length -= 1;
        }
        acc
    }
    fn count(&mut self) {
        let depth = self.depth;
        self.sub_count(depth, [None; 256], 0, 0, [true; 256], 256);
    }
    fn sub_count(&mut self, depth: u8, S: [Option<usize>; 256], mut i: usize, mut j: usize, perm_list: [bool; 256], number: u64) {
        if depth == 0 {
            if S[plus(S[i].unwrap(), S[j].unwrap())].is_none() {
                for num in 0..256 { if perm_list[num] {
                    self.output[num] += self.cases(number - 1);  // 4
                }}
            } else {
                self.output[S[plus(S[i].unwrap(), S[j].unwrap())].unwrap()] += self.cases(number);  // 4
            }
            return;
        }

        if depth == 1 { 
            self.acc += 1;
            println!("{} / {}", self.acc, 256 * 256);
        }

        i = plus(i, 1);  // 1
        if S[i].is_none() {
            for x in 0..256 { if perm_list[x] {
                let mut perm_list1 = perm_list.clone();
                perm_list1[x] = false;
                let number1 = number - 1;
                let mut S1 = S.clone();
                S1[i] = Some(x);
                let j1 = plus(j, S1[i].unwrap());  // 2
                if S1[j1].is_none() {
                    for y in 0..256 { if perm_list1[y] {
                        let mut perm_list2 = perm_list1.clone();
                        perm_list2[y] = false;
                        let number2 = number1 - 1;
                        let mut S2 = S1.clone();
                        S2[j1] = Some(y);
                        S2.swap(i, j1);  // 3
                        self.sub_count(depth-1, S2, i, j1, perm_list2, number2);
                    }}
                } else {
                    S1.swap(i, j1);  // 3
                    self.sub_count(depth-1, S1, i, j1, perm_list1, number1);
                }
            }}
        } else {
            j = plus(j, S[i].unwrap());  // 2
            if S[j].is_none() {
                for y in 0..256 { if perm_list[y] {
                    let mut perm_list2 = perm_list.clone();
                    perm_list2[y] = false;
                    let number2 = number - 1;
                    let mut S2 = S.clone();
                    S2[j] = Some(y);
                    S2.swap(i, j);  // 3
                    self.sub_count(depth-1, S2, i, j, perm_list2, number2);
                }}
            } else {
                let mut S1 = S.clone();
                S1.swap(i, j);  // 3
                self.sub_count(depth-1, S1, i, j, perm_list, number);
            }
        }
    }
}

fn main() {
    let mut counter = Counter::new(2);
    counter.count();
    let mut acc: u64 = 0;
    for i in 0..256 {
        println!("{}: {}", i, counter.output[i]);
        acc += counter.output[i];
    }
    let expected: u64 = 256 * 255 * 254 * 253 * 252;
    println!("sum: {} (expected: {})", acc, expected);
}
