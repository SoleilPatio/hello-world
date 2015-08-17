package Jackson.Jackson;

public class MyValue {
	public String name;
	public int age;
	public Other other;
	
	public void action(){
		System.out.printf("[MyValue.action()]\n");
		
		System.out.printf("name = %s\n", name);
		System.out.printf("age = %d\n", age);
		System.out.printf("other.address = %s\n", other.address);
		
	}
}
