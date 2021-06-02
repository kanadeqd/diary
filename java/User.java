
public class User {
	private String user = "admin";
	private String pw = "admin";
	public Boolean Login(String user, String pw) {
			if (this.user.equals(user) && this.pw.equals(pw)) {
				System.out.println("sucessful");
				return true;
			}else {
				System.out.println("unsucessful");
				return false;
			}
	}
}
