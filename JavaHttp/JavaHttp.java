import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.HttpResponse;

public class JavaHttp
{
    public static void main( String[] args ) throws IOException
    {
        System.out.print("JavaHttp:Get :" + args[0] + "\n");

        HttpClient client = new DefaultHttpClient();
        HttpGet request = new HttpGet( args[0] );
        HttpResponse response = client.execute(request);

        // Get the response
        BufferedReader rd = new BufferedReader
              (new InputStreamReader(response.getEntity().getContent()));
      
        String line = "";
        
        while ((line = rd.readLine()) != null) 
        {
            System.out.println(line);
        }
    }
}
