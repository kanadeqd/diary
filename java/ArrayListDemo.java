
import java.util.*;

public class ArrayListDemo {
	public static void main(String[] args) {
		ArrayList<String> array = new ArrayList<>();
		
		array.add("hello");
		array.add("java");
		array.add(1,"world");
//		array.add(4,"123");  越界
	
//		array.remove(0);    根据索引删除
//		array.remove("world"); 根据内容删除
//		array.set(2, "python");
		System.out.println(array.get(0));
		System.out.println(array);
	}
}
