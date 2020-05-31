class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        if (len < 2){
            return s;
        }
        int maxlen = 1;
        int begin = 0;
        boolean[][] dp = new boolean[len][len];
        char[] charArray = s.toCharArray();
        for (int i = 0; i < len; i++){
            dp[i][i] = true;
        }
        for (int j = 1; j < len; j++){
            for (int i = 0; i < j; i++){
                if (charArray[i] != charArray[j]){
                    dp[i][j] = false;
                } else{
                    if (j - i < 3){
                        dp[i][j] = true;
                    } else {
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                // 只要 dp[i][j] == true 成立，就表示子串 s[i..j] 是回文
                if (dp[i][j] && j - i + 1 > maxlen){
                    maxlen = j - i + 1;
                    begin = i;
                }
            }
        }
        return s.substring(begin, begin + maxlen);

    }
}