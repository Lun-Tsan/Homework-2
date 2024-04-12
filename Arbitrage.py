liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}
def swap_tokens(liquidity, amount, token_in, token_out):
    if (token_in, token_out) in liquidity:
        reserve_in, reserve_out = liquidity[(token_in, token_out)]
    else:
        reserve_out, reserve_in = liquidity[(token_out, token_in)]

    k = reserve_in * reserve_out
    new_reserve_in = reserve_in + amount
    new_reserve_out = k / new_reserve_in
    amount_out = reserve_out - new_reserve_out

    if (token_in, token_out) in liquidity:
        liquidity[(token_in, token_out)] = [new_reserve_in, new_reserve_out]
    else:
        liquidity[(token_out, token_in)] = [new_reserve_out, new_reserve_in]
    return amount_out

def find_target_sequence(liquidity, initial_amount, current_token, target_amount, target_token, sequence, depth, max_depth):
    if depth > max_depth:
        return None, []

    possible_swaps = [key for key in liquidity.keys() if current_token in key]
    results = []
    for swap in possible_swaps:
        token_out = swap[0] if swap[1] == current_token else swap[1]
        new_liquidity = liquidity.copy()
        swapped_amount = swap_tokens(new_liquidity, initial_amount, current_token, token_out)
        if token_out == target_token and round(swapped_amount) == target_amount:
            return swapped_amount, sequence + [(current_token, token_out)]
        elif token_out != target_token:
            result_amount, result_sequence = find_target_sequence(new_liquidity, swapped_amount, token_out, target_amount, target_token, sequence + [(current_token, token_out)], depth + 1, max_depth)
            if result_amount is not None:
                results.append((result_amount, result_sequence))
    
    if results:
        results.sort(key=lambda x: abs(target_amount - x[0]))
        return results[0]
    return None, []

max_search_depth = 7
initial_token = 'tokenB'
result_amount, result_sequence = find_target_sequence(liquidity, 5, initial_token, 21, initial_token, [], 0, max_search_depth)
print("path:  tokenB",end='')
for i in result_sequence:
    print('->'+i[1],end='')
print(", tokenB balance=",result_amount,'.')
