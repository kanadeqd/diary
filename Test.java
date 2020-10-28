

import java.util.*;

public class Test {
	public static void main(String[] args) {
//		fit();
//		seven();
//		rabbit();
//		chicken();
//		get_sum();
		int[] a1 = {11,22,33,44,55};
		int[] a2 = {11,22,33,44,55};
//		System.out.println(check_same(a1, a2));
//		find_num();
//		System.out.println( arr_change(a1)[4]);
		System.out.println(mark());
 	}
	
	public static void fit() {

		Scanner sc = new Scanner(System.in);
		System.out.println("input a day number"); 
		int day = sc.nextInt();
		switch(day) {
		case 1 :
			System.out.println("run");
			break;
		case 2:
			System.out.println("swim");
			break;
		case 3:
			System.out.println("walk");
			break;
		default:
			System.out.println("eat");			
			break;
		}
		
	}	
	public static void seven() {
		for (int i = 1; i <= 100 ; i ++) {
			if (i% 7 == 0) {
				System.out.println(i);
			}else if(i % 10 == 7){
				System.out.println(i);
			}else if(i / 10 % 10 == 7) {
				System.out.println(i);
			}
		}
	}
	public static void rabbit() {
		int[] rab = new int [20];
		rab[0] = 1;
		rab[1] = 1;
		for (int i = 2; i< 20 ;i ++) {
			rab[i] = rab[i-1] + rab[i-2];
		}
		System.out.println(rab[19]);
	}
	public static void chicken() {
		for (int i = 1; i < 20; i ++) {
			for ( int j = 1; j < 34; j ++) {
				int k = 100 -i - j;
				if(k% 3 == 0 && 5 * i + 3 * j + k/3 == 100){
					System.out.println(i + "--"+ j + "--" + k);
					
				}
			}
		}
	}
	public static void get_sum() {
		int[] arr = {68, 27 , 95, 88 ,171,996,51,210};
		int sum = 0;
		for (int i = 0; i < arr.length; i ++) {
			if (arr[i] %2 == 0 && arr[i] % 10 != 7 && arr[i]/10 %10 != 7 ) {
				sum += arr[i];
			}
		}
		System.out.println(sum);

	}
	public static boolean check_same(int[] arr1, int[] arr2) {
		if (arr1.length != arr2.length) {
			return false;
		}
		for( int i = 0; i < arr1.length ; i ++) {
			if (arr1[i] != arr2[i]) {
				return false;
			}
		}
		return true;
	}
	public static int find_num() {
		int[] arr = {19,28,37,46,50};
		System.out.println("input");
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for(int i = 0; i < arr.length; i ++) {
			if ( n == arr[i]) {
				System.out.println("index is " + i);
				return i;
			}
		}
		return 0;
	}
	public static int[] arr_change(int[] arr1) {
		int length = arr1.length;
		int[] res = new int[length];
		for(int i = 0; i < length;i ++) {
			res[i] = arr1[length - i - 1];
		}
		return res;
	}
	public static int mark() {
		int max = 0;
		int min = 101;
		int sum = 0;
		int i;
		Scanner sc = new Scanner(System.in);
		for ( int k = 0; k < 6; k++) {
			System.out.println("input mark");
			i = sc.nextInt();
			sum += i;
			if (max < i) {
				max = i;
			}
			if (min > i) {
				min = i;
			}
		}
		return (sum - max - min )/4;
	}
}
