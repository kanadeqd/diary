import java.util.*;
public class funct {
	public static void main(String[] args) {
		System.out.println("input");
		Scanner sc = new Scanner(System.in);
		int i = sc.nextInt() ;
		isEvenNum(i);
		System.out.println("input two int num");
		int a = sc.nextInt();
		int b = sc.nextInt();
		System.out.println(max(10,20));
		System.out.println(max(a,b));
		System.out.println("input two double num");
		double c = sc.nextDouble();
		double d = sc.nextDouble();
		System.out.println(max(c,d));
		sc.close();

	}
	public static void isEvenNum(int i) {
		if(i % 2 == 0) {
			System.out.println("true");
		}
		else {
			System.out.println("false");
		}
		
	}
	
	public static boolean max(int a, int b ) {
		if(a > b) {
			return true;
		}
		else{
			return false;
		}
	}
	
	public static int max( double a, double b) {
		if ( a> b) {
			return 1;
		}else {
			return 0;
		}
	}
}	
