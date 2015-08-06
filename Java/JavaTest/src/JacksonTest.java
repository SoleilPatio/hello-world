import java.io.File;
import java.io.IOException;

import com.fasterxml.jackson.databind.ObjectMapper;



public class JacksonTest {

	
	public void run() throws IOException
	{
		ObjectMapper mapper = new ObjectMapper(); // can reuse, share globally
		
		/*Read*/
		MyValue value = mapper.readValue(new File("rsc/data_in.json"), MyValue.class);
		
		System.out.printf("name=%s\n", value.name);
		System.out.printf("age=%d\n", value.age );
		
		/*Write*/
		mapper.writeValue(new File("rsc/data_out.json"), value);
		
	}

}
