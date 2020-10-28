package Students;
import java.util.*;
public class Student_main {
	
	public static void main(String[] args) {
		ArrayList<Student> studentsArray = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		for(int i = 0; i< 3; i ++) {
			System.out.println("input No." + (i+1) + " student name:");
			Student s = new Student();
			s.setName(sc.nextLine());
			System.out.println("input No." + (i+1) + " student age:");
			s.setAge(sc.nextLine());
			studentsArray.add(s);
		}
		for (int i = 0 ; i < studentsArray.size(); i ++) {
			System.out.println(studentsArray.get(i).getName() + "," + studentsArray.get(i).getAge());
		}
		

	}
}	
