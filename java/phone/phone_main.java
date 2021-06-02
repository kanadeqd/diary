package phone;

public class phone_main {
	public static void main(String[] args) {
		phone_class p = new phone_class();
		String b = p.brand;
		p.call();
		p.brand = "Mi";
		System.out.println(p.brand);
	}
}
