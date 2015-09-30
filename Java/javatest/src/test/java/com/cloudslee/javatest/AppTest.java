package com.cloudslee.javatest;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

import com.cloudslee.rutile.db_fields.StockRecord;
import com.cloudslee.rutile.db_fields.Stockinfo;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest
		extends TestCase {
	/**
	 * Create the test case
	 *
	 * @param testName
	 *            name of the test case
	 */
	public AppTest(String testName) {
		super(testName);
	}

	/**
	 * @return the suite of tests being tested
	 */
	public static Test suite() {
		return new TestSuite(AppTest.class);
	}

	/**
	 * Rigourous Test :-)
	 * 
	 * @throws IllegalAccessException
	 * @throws IllegalArgumentException
	 */
	public void testClassClass() throws IllegalArgumentException, IllegalAccessException {
		TestClass tc = new TestClass();
		Class<?> clazz = tc.getClass();
		tc.m_var1 = 123;
		tc.m_var2 = 456;

		System.out.println(tc.getClass());
		System.out.println(clazz.getName());

		System.out.println("Methods------");
		for (Method element : clazz.getMethods()) {
			System.out.println(element.getName());
		}

		System.out.println("Fields------");
		for (Field element : clazz.getFields()) {
			System.out.println(element.getName());
			System.out.println(element.getType().toString());
			System.out.println(element.getInt(tc));
		}
	}

	public void testClassPOJO() throws IllegalArgumentException, IllegalAccessException {
		StockRecord<Stockinfo> tc = new StockRecord<Stockinfo>(Stockinfo.class);
		// TestClass tc = new TestClass();
		Class<StockRecord<Stockinfo>> clazz = (Class<StockRecord<Stockinfo>>) tc.getClass();
		tc.code = "2454";
		tc.body().name = "聯發科";

		System.out.println(tc.getClass());
		System.out.println(clazz.getName());

		System.out.println("Methods------");
		for (Method element : clazz.getMethods()) {
			System.out.println(element.getName());
		}

		System.out.println("Fields------");
		for (Field element : clazz.getFields()) {
			System.out.println("------");
			System.out.println("field name :" + element.getName());
			System.out.println("field type :" + element.getType().getName());
			System.out.println("field value :" + element.get(tc));
			if( element.getType().getName().equals("java.lang.Object") ){
				System.out.println("\tthis is embedded object");
				
				//Class<?> clazz_l2 = element.getClass();
				Class<?> clazz_l2 = Stockinfo.class;
				
				System.out.println("\tClass name : " + clazz_l2.getName());
				for (Field element_l2 : clazz_l2.getFields()) {
					System.out.println("------");
					System.out.println("\tfield name :" + element_l2.getName());
					System.out.println("\tfield type :" + element_l2.getType().getName());
					System.out.println("\tfield value :" + element_l2.get(tc.body()));
				}
				
			}
		}
	}
}
