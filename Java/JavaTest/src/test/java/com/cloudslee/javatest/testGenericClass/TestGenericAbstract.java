package com.cloudslee.javatest.testGenericClass;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;

public abstract class TestGenericAbstract<T>  {
	public TestGenericAbstract() {
		System.out.println("TestGenericAbstract: constor!");

		Type superClass = getClass().getGenericSuperclass();
		if (superClass instanceof Class<?>) { // sanity check, should never
												// happen
			throw new IllegalArgumentException(
					"Internal error: TypeReference constructed without actual type information");
		}
		/*
		 * 22-Dec-2008, tatu: Not sure if this case is safe -- I suspect it is
		 * possible to make it fail? But let's deal with specific case when we
		 * know an actual use case, and thereby suitable workarounds for valid
		 * case(s) and/or error to throw on invalid one(s).
		 */
		Type _type = ((ParameterizedType) superClass).getActualTypeArguments()[0];

		System.out.println("TestGenericAbstract: type = " + _type.toString());
	}
}
