/*
 *  private need set and get function.  -> 封装
 * 	
 * 		
 */

package Students;

public class Stu {
	String name;
	private int age;

	public void setAge(int a) {
		if (a < 0) {
			System.out.println("incorrect age");
		} else {
			this.age = a;
		}
	}
	
	public Stu() {
		
	}
	
	public Stu(String name) {
		this.name = name;
	}
	
	// 没有 void  可以重构
	
	
	public int getAge() {
		return age;
	}

	public void study() {
		System.out.println("studying");
	}

	public void doHomework() {
		System.out.println("doing homework");
	}

	public void show() {
		System.out.println(name + "," + age);
	}

	public void set_name(String name) {
		this.name = name;
	}
}
