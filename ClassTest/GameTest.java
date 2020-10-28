package ClassTest;

public class GameTest {
	public static void main(String[] args) {
		Game g1 = new Game();
		Game g2 = new Game("arknights");
		g2.show();
		g1.show();
		System.out.println("---------");
		g1.set_name("fgo");
		g1.get_name();
		g1.show();
		System.out.println("---------");
		g2.pass();
		g1.show();
		g2.show();
	}
}
