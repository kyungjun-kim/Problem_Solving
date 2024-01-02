import java.util.Arrays;
class Solution {
    public double solution(int[] arr) {
        double answer = (double) Arrays.stream(arr).sum() / arr.length;
        return answer;
    }
}