# yape-nft

![alt text](https://github.com/0xSumna/yape-nft/blob/main/Test/23.png?raw=true)
![alt text](https://github.com/0xSumna/yape-nft/blob/main/Test/42.png?raw=true)
![alt text](https://github.com/0xSumna/yape-nft/blob/main/Test/69.png?raw=true)
![alt text](https://github.com/0xSumna/yape-nft/blob/main/Test/83.png?raw=true)

This is our plugin that will generate art for NFTs
It will likely have chainlink VRF to choose which patterns are going to be distributed. 

Gameplan is to consume chainlink VRF
That data gets sent to a server that then gives the file to IPFS, then pinned to Arweave.
We will hash the IPFS link so that it can only be gathered with keccak256 to ensure data privacy.
