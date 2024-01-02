public class Solution {
    public int solution(int n) {
        String tmp = Integer.toString(n);
        int answer = 0;
        for (int i = 0; i < tmp.length(); i++) {
            System.out.println((int) tmp.charAt(i));
            answer += Character.getNumericValue(tmp.charAt(i));
        }
        return answer;
    }
}