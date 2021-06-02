


import java.util.*;
public class funct_test {
	public static void main(String[] args) {
		System.out.println("pls input three num");
		Scanner sc = new Scanner(System.in);
		int num1 = sc.nextInt();
		int num2 = sc.nextInt();
		int num3 = sc.nextInt();
		int[] array = {num1, num2, num3};
		System.out.print("maxium is " + max(array));
	}
	public static int max(int[] array) {
		int max = 0;
		int len = array.length;
		for (int i = 0; i < len; i ++) {
			if (max < array[i] ) {
				max = array[i];
			}
		}
		return max;
	}
}
