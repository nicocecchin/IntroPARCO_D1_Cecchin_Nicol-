#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <immintrin.h> 

// Function to initialize a random n x n matrix
std::vector<std::vector<float>> initializeMatrix(int n) {
    std::vector<std::vector<float>> matrix(n, std::vector<float>(n));
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> dist(0.0, 100.0);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = dist(gen);
        }
    }
    return matrix;
}

bool checkSym(const std::vector<std::vector<float>> &matrix) {
    int n = matrix.size();
    int blockSize = 90;
    bool isSymmetric = true; 

    for (int bi = 0; bi < n; bi += blockSize) {
        for (int bj = bi + 1; bj < n; bj += blockSize) {
            for (int i = bi; i < std::min(bi + blockSize, n); ++i) {
                for (int j = std::max(bj, i + 1); j < std::min(bj + blockSize, n); ++j) {
                    if (matrix[i][j] != matrix[j][i]) {
                        isSymmetric = false;
                    }
                }
            }
        }
    }
    return isSymmetric;
}

std::vector<std::vector<float>> matTransposeCombined(const std::vector<std::vector<float>> &matrix) {
    int n = matrix.size();
    std::vector<std::vector<float>> transpose(n, std::vector<float>(n));

    int blockSize = 90;
    
    for (int i = 0; i < n; i += blockSize) {
        for (int j = 0; j < n; j += blockSize) {
            for (int ii = i; ii < std::min(i + blockSize, n); ii += 8) {
                for (int jj = j; jj < std::min(j + blockSize, n); ++jj) {
                    if (ii + 8 <= n) { 
                        __m256 row = _mm256_loadu_ps(&matrix[ii][jj]);  
                        _mm256_storeu_ps(&transpose[jj][ii], row);     
                    } else {
                        for (int k = ii; k < n; ++k) {
                            transpose[jj][k] = matrix[k][jj];
                        }
                    }
                }
            }
        }
    }
    return transpose;
}



int main(int argc, char *argv[]){
    
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <matrix_size>" << std::endl;
        return 1;
    }

    int n = std::stoi(argv[1]);

    // Initialize the matrix
    auto matrix = initializeMatrix(n);

    // Measure symmetry check time
    auto start = std::chrono::high_resolution_clock::now();
    bool isSymmetric = checkSym(matrix);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> checkSymDur = end - start; 
    std::cout << checkSymDur.count() << ", ";

    // Measure transpose time-----------------------------------------------------------
    start = std::chrono::high_resolution_clock::now();
    auto transpose = matTransposeCombined(matrix);
    end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> matTransposeDur = end - start; 
    std::cout << matTransposeDur.count();
              
    return 0;
}