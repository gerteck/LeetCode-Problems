class Solution {
    int m = 0;
    int n = 0;
    int srcColor = 0;
    int color = 0;

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
         this.color = color;
         srcColor = image[sr][sc];
         m = image.length;
         n = image[0].length;
        Boolean[][] processed = new Boolean[m][n];

        //DFS and BFS both works
        image[sr][sc] = color;
        process(sr, sc, image, processed);
        return image;
    }

     boolean checkEntry(int r, int c, int[][] image, Boolean[][] processed) {
        if (r < 0 || r > m - 1 || c < 0 || c > n - 1) {
            return false;
        }
        if (processed[r][c] != null) {
            return false;
        }
        if (image[r][c] != srcColor) {
            return false;
        }
        return true;
    }

     void process(int r, int c, int[][] image, Boolean[][] processed) {
        if(checkEntry(r-1, c, image, processed)) {
            image[r-1][c] = color;
            processed[r-1][c] = true;
            process(r-1, c, image, processed);
        }
        if(checkEntry(r+1, c, image, processed)) {
            image[r+1][c] = color;
            processed[r+1][c] = true;
            process(r+1, c, image, processed);
        }
        if(checkEntry(r, c+1, image, processed)) {
            image[r][c+1] = color;
            processed[r][c+1] = true;
            process(r, c+1, image, processed);
        }
        if(checkEntry(r, c-1, image, processed)) {
            image[r][c-1] = color;
            processed[r][c-1] = true;
            process(r, c-1, image, processed);
        }
    }
}