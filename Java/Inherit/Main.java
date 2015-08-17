public class Main 
{
	public static void main(String[] args) 
	{
		Main pMain = new Main();
		
		pMain.test1();
		pMain.test2();
		pMain.test3();
	}

	public void test1() 
	{
		System.out.printf("[INFO]Hello!\n");
		
		System.out.printf("[INFO]A pA = new A();\n");
		A pA = new A();
		
		
		System.out.printf("[INFO]B pB = new B();\n");
		B pB = new B();
		
		System.out.printf("[INFO]解說:extends 的constructor 會繼承呼叫\n\n");
		
		System.out.printf("[INFO]pA.action();\n");
		pA.action();
		System.out.printf("[INFO]pB.action();\n");
		pB.action();
		
		System.out.printf("[INFO]pA1.action();\n");
		A pA1 = pB;
		pA1.action();
		System.out.printf("[INFO]解說:java的都是default 多型,因為都是指標參考\n\n");
		
		System.out.printf("[INFO]pC.action();\n");
		C pC = new C();
		pC.action();
		pC.interface_action();
		System.out.printf("[INFO]解說:沒override就用上一層\n\n");
		
	}
	
	public void test2()
	{
		/**
		 * Downcast test
		 */
		
		A pA = new B();
		B pB = (B)pA;
	}
	
	public void test3()
	{
		A pA = new D();
		
		pA.doSomething((String)"HAHA");
	}
	
	
	
	

}
