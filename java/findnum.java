/*
 *  2020 10 22
 *  finish java quickly go big data
 * 
 */

import java.util.*;

public class findnum {
	public static void main(String[] args) {
		Random r = new Random();
		int num = r.nextInt(100);
		Scanner sc = new Scanner(System.in);
		System.out.println("pls input a num(0-99)");
		int gus = sc.nextInt();
		while(num != gus) {
			if (num > gus) {
				System.out.println("small");
				}
			else {
				System.out.println("large");
			}
			System.out.println("pls input a num(0-99)");
			gus = sc.nextInt();
		}
		System.out.println("right");
		sc.close();
		
	}
}
