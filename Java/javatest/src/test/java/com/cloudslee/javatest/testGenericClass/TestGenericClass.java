package com.cloudslee.javatest.testGenericClass;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;

public class TestGenericClass<T> {
	public TestGenericClass() {
		System.out.println("TestGenericClass: constor!");

		Type superClass = getClass().getGenericSuperclass();
		if (superClass instanceof Class<?>) { // sanity check, should never
												// happen

			/*
			 throw new IllegalArgumentException(
			 "Internal error: TypeReference constructed without actual type
			 information");
			 */
			
			System.out.println("Internal error: TypeReference constructed without actual type information");
			
			return;
		}
		/*
		 * 22-Dec-2008, tatu: Not sure if this case is safe -- I suspect it is
		 * possible to make it fail? But let's deal with specific case when we
		 * know an actual use case, and thereby suitable workarounds for valid
		 * case(s) and/or error to throw on invalid one(s).
		 */
		Type _type = ((ParameterizedType) superClass).getActualTypeArguments()[0];

		System.out.println("TestGenericClass: type = " + _type.toString());
	}
}
