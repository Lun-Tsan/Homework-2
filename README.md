# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).   
Swapped tokenB to tokenE: 0.5 tokenE received   
Swapped tokenE to tokenA: 1.90909090909091 tokenA received   
Swapped tokenA to tokenD: 1.016129032258065 tokenD received   
Swapped tokenD to tokenC: 2.342007434944236 tokenC received   
Swapped tokenC to tokenE: 1.5180722891566258 tokenE received   
Swapped tokenE to tokenD: 3.434802362562472 tokenD received   
Swapped tokenD to tokenC: 5.774733109403087 tokenC received   
Swapped tokenC to tokenB: 21.268139969829456 tokenB received   
Final amount of Token B: 21.268139969829456   

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

當AMM中的預期交易價格跟實際交易價格差很大的時候，就可以稱為slippage，主要的原因是liquidity不足，所以Uniswap V2用constant product formula(x*y=K)來處理這個問題。  
假設有100個A幣和100個B幣，如果要一次買10個A，那此時B的價格會變為100/90=111.1，跟原本的差距很大。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

為了避免有些幣的價值太低，甚至為0，因為用constant product formula的時候，如果有一個為0，那乘積就會是0，故有最小值來避免這種狀況，確保供應量不會從0開始。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

為了要維持穩定，避免有人想要隨意操控價格，所以用x*y=K，來讓滑點產生的難度增加。也藉由價格的穩定來保障liquidity provider的權益不會受損，能公平的交易。

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?
如果有人要換幣，但是有另一個人想要攻擊從中獲利，舉例來說:有人想買A幣，且攻擊者得知訊息後抬高了A幣的價錢，讓那個人多花錢之後，再賣出去賺價差。  
這會讓swap時候的滑點增大，增加金錢上的損失。

