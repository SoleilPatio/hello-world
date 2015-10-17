package com.cloudslee.javatest;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

import com.cloudslee.javatest.testGenericClass.TestDerivativeFromAbstract;
import com.cloudslee.javatest.testGenericClass.TestDerivativeFromClass;
import com.cloudslee.javatest.testGenericClass.TestGenericAbstract;
import com.cloudslee.javatest.testGenericClass.TestGenericClass;
import com.cloudslee.javatest.testJacksonMapper.QuotRecord;
import com.cloudslee.javatest.testJacksonMapper.BaseRecord;
import com.fasterxml.jackson.databind.ObjectMapper;

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
	public void testJacksonMapper() throws IOException {

		// StockRecord<?> quotation_entry = new SrQuotation();
		QuotRecord quotation_entry = new QuotRecord();
		

		((BaseRecord)quotation_entry).name = "聯發科";
//		quotation_entry.market = "TWSE";
//		quotation_entry.code = "2454";
//		quotation_entry.datecode = new Datecode().setToday().toInt();
//		quotation_entry.body.volume = 10;
//		quotation_entry.body.deal = 99;

		System.out.println(quotation_entry);

		/*
		 * To File
		 */
		ObjectMapper mapper = new ObjectMapper(); // can reuse, share globally

		mapper.writeValue(new File("temp_data_out.json.tmp"), quotation_entry);

		/*
		 * To String
		 */
		System.out.println("1:Json:" + mapper.writeValueAsString(quotation_entry));

		/*
		 * To String2
		 */
//		System.out.println("2:Json:" + quotation_entry.toJson());

		/*
		 * To BSON
		 */
//		System.out.println("3:Bson:" + quotation_entry.toBson());

		/*
		 * From JSON
		 */
//		StockRecord<?> clone = (StockRecord<?>) quotation_entry.fromJson(quotation_entry.toJson());
		// SrQuotation clone = (SrQuotation)
		// quotation_entry.fromJson(quotation_entry.toJson());
		// StockRecord<Quotation> clone =
		// mapper.readValue(quotation_entry.toJson(), new
		// TypeReference<StockRecord<Quotation>>(){});
//		System.out.println("4:Body Jason:" + clone.body.toString());
//		System.out.println("4:Jason:" + clone.toJson());
//
//		quotation_entry = (SrQuotation) quotation_entry.fromJson(quotation_entry.toJson());
//		System.out.println("5:Bson:" + quotation_entry.toJson());

	}

	@SuppressWarnings("unused")
	public void testGenericClass() {
		/*
		 * 這方法只能抓SuperClass的GenericType,所以GenericType物件必須被繼承後才能用
		 */
		System.out.println("OK: new a Interface ( a anonymous derivatived object)");
		TestGenericAbstract<Integer> objTGA = new TestGenericAbstract<Integer>() {
		};

		System.out.println("OK: new a anonymous derivateved object");
		TestGenericClass<Integer> objTGCC = new TestGenericClass<Integer>() {
		};

		System.out.println("Failed: new a Object");
		TestGenericClass<Integer> objTGCO = new TestGenericClass<Integer>();

		System.out.println("OK: new a Derivatived Object");
		TestDerivativeFromClass objTDFC = new TestDerivativeFromClass();

		System.out.println("OK: new a Derivatived Abstract Object ==> suggest this usage");
		TestDerivativeFromAbstract objTDFA = new TestDerivativeFromAbstract();

	}

	public void testClassReflect() throws IllegalArgumentException, IllegalAccessException {
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
}
