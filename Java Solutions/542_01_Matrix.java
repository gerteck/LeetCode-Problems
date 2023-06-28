class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;

        int [][] newMatrix = new int[m][n];

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    newMatrix[i][j] = 0;
                } else {
                    newMatrix[i][j] = n+m;
                }
            }
        }

        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++) {
                if (newMatrix[i][j] == 0) {
                    optimize_neighbours(i, j, newMatrix, m, n);
                }
            }
        }
        return newMatrix;
    }

    void optimize_neighbours(int i, int j, int[][] matrix, int m, int n) {
        int value = matrix[i][j];
        if (i > 0) {
            if (matrix[i-1][j] - 1 > value) {
                matrix[i-1][j] = value + 1;
                optimize_neighbours(i-1, j, matrix, m, n);
            }
        }
        if (i < m - 1 ) {
            if (matrix[i+1][j] - 1 > value) {
                matrix[i+1][j] = value + 1;
                optimize_neighbours(i+1, j, matrix, m, n);
            }
        }
        if (j > 0 ) {
            if (matrix[i][j-1] - 1 > value) {
                matrix[i][j-1] = value + 1;
                optimize_neighbours(i, j-1, matrix, m, n);
            }
        }
        if (j < n - 1 ) {
            if (matrix[i][j+1] - 1 > value) {
                matrix[i][j+1] = value + 1;
                optimize_neighbours(i, j+1, matrix, m, n);
            }
        }


    }

}