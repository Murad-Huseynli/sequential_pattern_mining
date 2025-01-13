# Sequential Pattern Mining Algorithms Performance Analysis

## About The Project

This research project focuses on evaluating and comparing the time complexity of four widely used sequential pattern mining algorithms: Brute Force, SPADE, PrefixSpan, and SPAM. The study systematically analyzes how these algorithms perform under various conditions by manipulating dataset hyperparameters. The goal is to provide researchers and practitioners with insights for selecting the most effective sequential pattern mining algorithm for their specific needs.

### Key Findings

* Algorithms show polynomial dependency on the number of transactions
* Exponential dependency on sequence length
* Exponential decay relationship with the number of distinct items
* PrefixSpan demonstrated the most stable and effective performance across all test cases

### Built With

* Python
* Custom implementations of SPADE, SPAM, and PrefixSpan algorithms
* Machine learning algorithms for polynomial and exponential fitting
* Referenced SPMF Java Framework

## Getting Started

### Prerequisites

* Python environment
* Required Python libraries for data processing and analysis

### Dataset Structure

The project uses randomly generated datasets with the following parameters:
* num_sequences: Number of customers/sequences
* max_sequence_length: Total number of items per customer
* num_items: Number of different items

Example dataset format:
```
[{1, 2, 4}, {2, 3, 4}, {2, 3, 4}],
[{2, 7, 8}, {1, 2, 3}, {4, 5}, {2}],
[{1, 2}, {2, 3, 4}, {1, 3, 5, 7}]
```

## Usage

The project includes implementations of three main algorithms:

1. SPADE (Sequential PAttern Discovery using Equivalence classes)
2. SPAM (Sequential PAttern Mining)
3. PrefixSpan (Prefix-projected Sequential pattern mining)

Each algorithm can be tested with different dataset parameters to evaluate performance under various conditions leveraging the driver file.

## Experimental Results

### Case 1: Varying Number of Transactions
* Fixed parameters:
  * max_sequence_length = 20
  * num_items = 5
* Results: SPADE and PrefixSpan outperform SPAM

### Case 2: Varying Sequence Length
* Fixed parameters:
  * num_sequences = 100
  * num_items = 20
* Results: SPAM and PrefixSpan outperform SPADE

### Case 3: Varying Number of Items
* Fixed parameters:
  * num_sequences = 100
  * max_sequence_length = 20
* Results: SPAM and PrefixSpan demonstrate similar performance, both outperforming SPADE

## Roadmap

- [x] Implementation of core algorithms
- [x] Performance evaluation under various conditions
- [x] Comparative analysis
- [ ] Optimization of existing implementations
- [ ] Port implementation to C++ for better performance
- [ ] Add more sequential pattern mining algorithms
- [ ] Create a comprehensive library with stable algorithms

## Contributing

Project Contributors:
* Murad Huseynli (14297)
* Emil Inochkin (16285)
* Amir Adamov (5055)

## License

Research project conducted at ADA University, School of Information Technologies and Engineering.

## Contact

School of Information Technologies and Engineering  
ADA University  
Data Mining (CSCI4700)  
Spring 2023

## Acknowledgments

* SPMF Java Framework for reference implementation
* Dr. Mohammed J. Zaki for SPADE algorithm
* Dr. Jian Pei for PrefixSpan algorithm
* Ayres et al. for SPAM algorithm

## References

1. Pei, J., et al. (2001). Mining Sequential Patterns by Pattern-Growth: The PrefixSpan Approach
2. Slimani, T., & Lazzez, A. (2013). Sequential Mining: Patterns and Algorithms Analysis
3. Zaki, M. J. (2001). SPADE: An Efficient Algorithm for Mining Frequent Sequences
4. Mohammed, Z., & Meira, W. (2020). Data Mining and Machine Learning Fundamental Concepts and Algorithms
5. Ayres, J., et al. (2002). Sequential PAttern Mining using a Bitmap Representation