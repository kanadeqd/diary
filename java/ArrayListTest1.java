import java.util.*; 

public class ArrayListTest1 {
	public static void main(String[] args) {
		ArrayList<String> array = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		System.out.println("three input");
		String s1 = sc.nextLine();
		String s2 = sc.nextLine();
		String s3 = sc.nextLine();
		
		array.add(s1);
		array.add(s2);
		array.add(s3);
		
		for (int i = 0 ; i < array.size(); i ++) {
			System.out.println(array.get(i));
		}
		
	}
}
