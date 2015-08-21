package Jackson.Jackson;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;

import com.cloudslee.util.Debug;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;


public class MainJackson 
{
    public static void main( String[] args ) throws IOException
    {
        System.out.println( "Jackson Test" );
        
        MainJackson app = new MainJackson();
        
//        app.singleTest();
//        
//        app.arrayTest();
//        
//        app.listTest();
        
        app.mapTest();
        
    }
    
    void singleTest() throws IOException
	{
    	File f = new File("rsc/data_in.json");
		ObjectMapper mapper = new ObjectMapper(); // can reuse, share globally
		
		/*Read*/
		MyValue value1 = mapper.readValue(f, MyValue.class);
		value1.action();
		
		MyValue value2 = mapper.readValue(f, MyValue.class);
		value2.action();
		
		
		/*Write*/
		mapper.writeValue(new File("rsc/data_out.json"), value1);
		
	}
    
   
    
    void arrayTest() throws IOException
	{
		ObjectMapper mapper = new ObjectMapper(); // can reuse, share globally
		/*Read*/
		MyValue[] value_array = mapper.readValue(new File("rsc/data_in_array.json"), MyValue[].class);

		
		for (MyValue value: value_array ){
			value.action();
		}
		
		/*Write*/
		mapper.writeValue(new File("rsc/data_out_array.json"), value_array);
		
	}
    
    void listTest() throws IOException
	{
		ObjectMapper mapper = new ObjectMapper(); // can reuse, share globally
		/*Read*/
		List<MyValue> value_list = mapper.readValue(new File("rsc/data_in_array.json"), 
													new TypeReference<List<MyValue>>(){});

		for (MyValue value: value_list ){
			value.action();
		}
	
		/*Write*/
		mapper.writeValue(new File("rsc/data_out_list.json"), value_list);
		
	}
    
    void mapTest() throws IOException
	{
		ObjectMapper mapper = new ObjectMapper(); // can reuse, share globally
		/*Read*/
		Map<String, String> map = mapper.readValue(new File("rsc/data_in_map.json"), 
													new TypeReference<Map<String, String>>(){});

		Debug.printMap(map);
	
		/*Write*/
		mapper.writeValue(new File("rsc/data_out_map.json"), map);
		
	}
}
