package StudentManage;

public class StuClass {
	private String sid;
	private String name;
	private String age;
	private String addres;
	public StuClass() {}
	public StuClass(String sid, String name, String age, String address) {
		this.sid = sid;
		this.name = name;
		this.age = age;
		this.addres = address;
	}
	
	public void SetSid(String id) {
		this.sid = id;
	}
	public String GetSid() {
		return this.sid;
	}
	
	public void SetName(String name) {
		this.name = name;
	}
	public String GetName() {
		return this.name;
	}	
	
	public void SetAge(String age) {
		this.age = age;
	}
	public String GetAge() {
		return this.age;
	}
	
	public void SetAdd(String add) {
		this.addres = add;
	}
	public String GetAdd() {
		return this.addres;
	}
}
