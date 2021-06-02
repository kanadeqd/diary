package StudentManage;

import java.util.*;
public class StuMain {
	public static void main(String[] args) {
		ArrayList<StuClass> students = new ArrayList<>();
		Scanner sc = new Scanner(System.in);
		int num = 0;
		while(num != 5) {
			System.out.println("-----欢迎来到学生管理系统--------");
			System.out.println("1 添加学生");
			System.out.println("2 删除学生");
			System.out.println("3 修改学生");
			System.out.println("4 查看所有学生");
			System.out.println("5 退出");
			System.out.println("请输入你的选择：");
			
			num = sc.nextInt();
			if (num == 1) {
				addStu(students);
			}
			if (num == 2) {
				delteStu(students);
			}
			if(num == 3) {
				changeStu(students);
			}
			if(num == 4) {
				showStu(students);
			}
			if(num == 4) {
				System.out.println("感谢使用");
			}
		}
		sc.close();
	}
	
	public static void addStu(ArrayList<StuClass> students) {
		StuClass s = new StuClass();
		Scanner sc_add = new Scanner(System.in);
		System.out.println("请输入学生学号：");
		String id = sc_add.nextLine();
		for (int i = 0; i<students.size(); i++) {
			if(students.get(i).GetSid().equals(id)) {
				System.out.println("该学生已存在，请重试");
				return;
			}
		}
		s.SetSid(id);
		System.out.println("请输入学生姓名：");
		s.SetName(sc_add.nextLine());
		System.out.println("请输入学生年龄：");
		s.SetAge(sc_add.nextLine());
		System.out.println("请输入学生居住地：");
		s.SetAdd(sc_add.nextLine());
		students.add(s);
		System.out.println("添加学生成功");
	}
	
	public static void showStu(ArrayList<StuClass> students) {
		if (students.size() == 0) {
			System.out.println("请先添加学生");
			return;
		}
		System.out.println("学号\t姓名\t年龄\t居住地" );
		for (int i =0 ; i < students.size(); i++) {
			System.out.println(students.get(i).GetSid()+"\t" + students.get(i).GetName() + "\t" + 
					students.get(i).GetAge() + "\t" + students.get(i).GetAdd());
		}
	}

	public static void changeStu(ArrayList<StuClass> students) {
		if (students.size() == 0) {
			System.out.println("请先添加学生");
			return;
		}
		StuClass s = new StuClass();
		Scanner sc_change = new Scanner(System.in);
		System.out.println("请输入你要修改学生的学生学号：");
		String target = sc_change.nextLine();
		for (int i = 0 ; i < students.size(); i++) {
			if (students.get(i).GetSid().equals(target)) {
				s.SetSid(target);
				System.out.println("请输入学生新姓名：");
				s.SetName(sc_change.nextLine());
				System.out.println("请输入学生新年龄：");
				s.SetAge(sc_change.nextLine());
				System.out.println("请输入学生新居住地：");
				s.SetAdd(sc_change.nextLine());
				students.set(i, s);
				System.out.println("修改学生成功");
				return;
			}
		}
		System.out.println("你要修改学生的学生学号错误");
	}
	
	public static void delteStu(ArrayList<StuClass> students) {
		if (students.size() == 0) {
			System.out.println("请先添加学生");
			return;
		}
		StuClass s = new StuClass();
		Scanner sc_del = new Scanner(System.in);
		System.out.println("请输入你要删除学生的学生学号：");
		String target = sc_del.nextLine();
		for (int i = 0 ; i < students.size(); i++) {
			if (students.get(i).GetSid().equals(target)) {
				students.remove(i);
				System.out.println("删除学生成功");
				return;
			}
		}
		System.out.println("你要删除学生的学生学号错误");
	}
}
