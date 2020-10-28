/*
 * 10/20 continue and break
 * 
 * 
 */
public class con_bre {
	public static void main(String[] agrs) {
		for (int i = 1; i <= 5; i++) {
			if ( i % 2 == 0) {
				continue;
			}
			System.out.println(i);
		}
		for (int i = 1; i <= 5 ;i++) {
			if( i % 2 == 0) {
				break;
			}
			System.out.println(i);
		}
		
	}
}
