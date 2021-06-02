
public class Str {
	public static void main(String[] args) {
		char[] chs = {
				'a', 'b', 'c'
		};							// 地址为000  chs
		String s1 = new String(chs); // 地址为 001 - ref of chs
		String s2 = new String(chs); // 地址为 002 - different ref of chs
		
		String s3 = "abc";			// 地址为003 abc
		String s4 = "abc";			// 地址为003 abc
		
		System.out.println(s1 == s2);
		System.out.println(s1 == s3);
		System.out.println(s3 == s4);	// 比较地址
		System.out.println("---------");
		System.out.println(s1.equals(s2));
		System.out.println(s1.equals(s3));
		System.out.println(s3.equals(s4));	// 比较值
	
		String s = "hello"; // 地址为001
		s += "world"; // world 地址为002  hello wrold 为003
		
		StringBuilder sb = new StringBuilder();   //动态string
		StringBuilder sb2 = sb.append("123");
		
		System.out.println(sb == sb2); // 内存一样
		
		StringBuilder sb3 = new StringBuilder("123");
		sb3.reverse();
		
		System.out.println(sb3);
		
		sb3.toString(); // sb to s
		
		StringBuilder sb4 = new StringBuilder(sb3);  // s to sb
		
		byte a = 1;
		byte b = 127;
		b+= a;
		System.out.println(b);
		
	}
}
