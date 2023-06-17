class Solution {
    public int maxProfit(int[] prices) {

        int length = prices.length;
        if (length == 0) return 0;

        int pastMin = prices[0];
        int maxProfit = 0;
        int profit;

        for (int i = 0; i < length; i++) {
            profit = prices[i] - pastMin;
            if (profit > maxProfit) maxProfit = profit;

            if (prices[i] < pastMin) pastMin = prices[i];
        }

        return maxProfit;

    }
}