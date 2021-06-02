
import java.util.*;

public class Login {
	public static void main(String[] args) {
		User us = new User();
		Scanner sc = new Scanner(System.in);
		for (int i = 0; i < 3; i++) {
			System.out.println("input user:");
			String name = sc.nextLine();
			System.out.println("input password:");
			String passwrod = sc.nextLine();
			if (us.Login(name, passwrod)) {
				break;
			}
			else {
				System.out.println(2-i + " times left");
			}
		}
	}
}
