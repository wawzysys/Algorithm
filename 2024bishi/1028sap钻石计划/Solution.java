import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> dic = new HashMap<>();
        int i = -1, res = 0, len = s.length();
        for(int j = 0; j < len; j++) {
            if (dic.containsKey(s.charAt(j)))
                i = Math.max(i, dic.get(s.charAt(j))); 
            dic.put(s.charAt(j), j); 
            res = Math.max(res, j - i); 
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "abcabcbb";
        System.out.println( solution.lengthOfLongestSubstring(s1));
    }
}