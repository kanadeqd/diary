package ClassTest;
/*
 * 
 * 	Test for class
 * 
 */
public class Game {
	
	String name;
	boolean published;
	
	public Game() {
		this.published = false;
	}
	
	public Game(String name) {
		this.name = name;
		this.published = false;
	}
	
	public void set_name(String name) {
		this.name = name;
	}
	
	public String get_name() {
		System.out.println(this.name);
		return this.name;
	}
	
	public void pass() {
		this.published = true;
	}
	
	public void show() {
		System.out.println(this.name + " is " + this.published);
	}
}
