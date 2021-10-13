# yape-nft

![alt text](https://github.com/yapeswap/yape-art-generator/blob/main/Assets/ReadMePreviews/0.png)
![alt text](https://github.com/yapeswap/yape-art-generator/blob/main/Assets/ReadMePreviews/1.png)
![alt text](https://github.com/yapeswap/yape-art-generator/blob/main/Assets/ReadMePreviews/2.png)
![alt text](https://github.com/yapeswap/yape-art-generator/blob/main/Assets/ReadMePreviews/3.png)

This is our plugin that will generate art for NFTs
It will likely have chainlink VRF to choose which patterns are going to be distributed. 

Gameplan is to consume chainlink VRF
That data gets sent to a server that then gives the file to IPFS, then pinned to Arweave.
We will hash the IPFS link so that it can only be gathered with keccak256 to ensure data privacy.
