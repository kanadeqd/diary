package Students;

public class student_test {
	public static void main(String[] args) {
		Stu ming = new Stu();
		ming.name = "xiaoming";
		ming.setAge(30);
		
		System.out.println(ming.name + "," + ming.getAge());
		
		ming.doHomework();
		ming.study();
		
		Stu S2 = new Stu("xiaozhang");
		S2.show();
	}
}
