package Students;

public class Student {
	private String name;
	private String age;
	public Student() {
		
	}
	public Student(String name) {
		this.name = name;
	}
	
	public  Student(String name, String age) {
		this.name = name;
		this.age = age;
	}
	
	public void setName(String name) {
		this.name = name;
	}

	public String getName() {
		return this.name;
	}
	
	public void setAge(String age) {
		this.age = age;
	}
	
	public String getAge() {
		return this.age;
	}
}
