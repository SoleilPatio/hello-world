
public class D extends A {
	
	@Override //Annotation is important for override
	public void doSomething(String str) //Correct version
	//public void doSomething(Object str) //False version : make doSomething as Overloading instead of overriding 
	{
		System.out.println("D:"+str);
	}

}
