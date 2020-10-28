
public class funct2 {
	public static void main(String[] args) {
		int num = 0;
		int[] num_l = {0};
		change(num);
		change(num_l);
		System.out.print(num + "  ");
		System.out.println(num_l[0]);
	} 
	public static void change(int num ) {
		num = 200;
	}
	public static void change(int[] num) {
		num[0] = 200;
	}
}
