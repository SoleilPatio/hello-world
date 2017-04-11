package com.cloudslee.javatest;

public class TestClass {
	public int m_var1;
	public int m_var2;
	
	protected int m_var_protected;
	
	public TestClass() {
		System.out.println("I AM " + this.getClass().getName());
	}
	public void func1(){
		System.out.println("func1()");
	}
	
	public void func2(){
		System.out.println("func2()");
	}
	
	protected void func_protected(){
		System.out.println("func2()");
	}

}
