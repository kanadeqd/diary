import java.util.*;
public class mn {
	
	public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
    	int target = sc.nextInt();
        if (target < 2) {
             System.out.println("0");
        }
        if (target == 2) {
            System.out.println("1");
        }
        if (target == 3) {
            System.out.println("2");
        }
        int[] dp = new int[target + 1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 3;
        for (int i = 4; i <= target; i++) {
            int max = 0;
            for (int j = 1; j <= i / 2; j++) {
                int temp = dp[j] * dp[i - j];
                if (temp > max) {
                    max = temp;
                }
            }
            dp[i] = max;
        }
        System.out.println(dp[target]);
	}
	

  
}
