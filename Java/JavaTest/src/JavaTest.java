import java.io.IOException;
import java.util.Calendar;


public class JavaTest {

	public JavaTest() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		System.out.printf("JavaTest\n");
		
		JavaTest javatest = new JavaTest();
		
		javatest.calendartest();
		
		/*******************************************/
		JacksonTest jacksonTest = new JacksonTest();
		
		jacksonTest.run();
		

	}
	
	public void calendartest()
	{
		/*
		 * NOTE:Month is 0 start!
		 */
		Calendar cal = Calendar.getInstance();
		int datecode = 20150804; 
		
				
		cal.getTime();
		
		
		
		System.out.printf("YEAR=%d\n",cal.get(Calendar.YEAR));
		System.out.printf("MONTH=%d\n",cal.get(Calendar.MONTH) + 1);
		System.out.printf("DAY_OF_MONTH=%d\n",cal.get(Calendar.DAY_OF_MONTH));
		System.out.printf("DAY_OF_WEEK=%d\n",cal.get(Calendar.DAY_OF_WEEK));
		System.out.printf("DAY_OF_YEAR=%d\n",cal.get(Calendar.DAY_OF_YEAR));
		
		cal.set( datecode/10000 , (datecode-datecode/10000*10000)/100 - 1, (datecode-datecode/100*100));
		
		System.out.printf("YEAR=%d\n",cal.get(Calendar.YEAR));
		System.out.printf("MONTH=%d\n",cal.get(Calendar.MONTH) + 1);
		System.out.printf("DAY_OF_MONTH=%d\n",cal.get(Calendar.DAY_OF_MONTH));
		System.out.printf("DAY_OF_WEEK=%d\n",cal.get(Calendar.DAY_OF_WEEK));
		System.out.printf("DAY_OF_YEAR=%d\n",cal.get(Calendar.DAY_OF_YEAR));
		
		
	}

}
