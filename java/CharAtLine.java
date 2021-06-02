import java.util.*;

public class CharAtLine {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("input");
		String line = sc.nextLine();
		System.out.println("length is "+ line.length());
		int charNum = 0;
		int charBig = 0;
		int charSma = 0;
		for ( int i = 0; i < line.length(); i ++ ) {
//			System.out.println(line.charAt(i));
			char letter = line.charAt(i);		//char 可以进行对比
			if(letter >= 'a' && letter <= 'z') {
				charSma ++;
			}else if (letter >= 'A' && letter <= 'Z') {
				charBig ++;
			}else if(letter >= '0' && letter <= '9') {
				charNum ++;
			}
		}
		System.out.println("num: "+ charNum + " a: "+ charSma + " A: "+ charBig);
		
		
		
		
	}
}
