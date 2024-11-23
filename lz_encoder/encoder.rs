use std::cmp;

#[derive(Debug)]
struct LZ77Tuple {
    offset: usize,
    length: usize,
    char: char,
}

fn max_of_two(a: usize, b: usize) -> usize {
    cmp::max(a, b)
}

fn compress_lz77(history: &str, lookahead: &str) -> Vec<LZ77Tuple> {
    let mut compressed_data = Vec::new();
    let window_size = history.len();
    let mut i = 0;

    while i < lookahead.len() {
        let mut best_match_distance = 0;
        let mut best_match_length = 0;

        // Search for the longest match in the sliding window
        for j in max_of_two(0, history.len().saturating_sub(window_size))..history.len() {
            let mut length = 0;
            while i + length < lookahead.len()
                && j + length < history.len()
                && history[j + length..].chars().next().unwrap()
                    == lookahead[i + length..].chars().next().unwrap()
            {
                length += 1;
            }
            if length > best_match_length {
                best_match_distance = history.len() - j;
                best_match_length = length;
            }
        }

        if best_match_length > 0 && i + best_match_length < lookahead.len() {
            let next_char = lookahead.chars().nth(i + best_match_length).unwrap();
            compressed_data.push(LZ77Tuple {
                offset: best_match_distance,
                length: best_match_length,
                char: next_char,
            });
            i += best_match_length + 1;
        } else {
            compressed_data.push(LZ77Tuple {
                offset: 0,
                length: 0,
                char: lookahead.chars().nth(i).unwrap(),
            });
            i += 1;
        }
    }

    compressed_data
}

fn slice_and_compress(input_str: &str, n: usize) {
    let n = cmp::min(n, input_str.len());
    let new_text = &input_str[..n];
    println!("NewText: {}", new_text);

    let two_thirds_index = (2 * n) / 3;
    let history = &new_text[..two_thirds_index];
    let lookahead = &new_text[two_thirds_index..];

    println!("History: {}", history);
    println!("Lookahead: {}", lookahead);

    let compressed_data = compress_lz77(history, lookahead);

    println!("Compressed Data:");
    for tuple in &compressed_data {
        println!("({}, {}, '{}')", tuple.offset, tuple.length, tuple.char);
    }

    let memory_size_compressed: usize = compressed_data
        .iter()
        .map(|tuple| format!("{}{}{}", tuple.offset, tuple.length, tuple.char).len())
        .sum();
    let memory_size_original = new_text.len();

    println!("Memory Size of Compressed Data: {}", memory_size_compressed);
    println!("Memory Size of Original Data: {}", memory_size_original);

    let compression_ratio = memory_size_compressed as f64 / memory_size_original as f64;
    println!("Compression Ratio: {:.2}", compression_ratio);
}

fn main() {
    let input_str = "In radio c'è un pulcino In radio c'è un pulcino È il pulcino pio, è il pulcino pio E il pulcino pio, e il pulcino pio";
    let plaque = "2077518";

    let n: usize = plaque.chars().filter_map(|c| c.to_digit(10)).sum::<u32>() as usize;

    slice_and_compress(input_str, n);
}
