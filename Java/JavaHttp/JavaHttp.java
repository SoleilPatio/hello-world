import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

import java.nio.charset.*;
import org.apache.http.*;
import org.apache.http.util.*;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;
import org.apache.http.entity.*;

/*
import org.apache.http.Header;
import org.apache.http.HeaderElement;
import org.apache.http.HttpEntity;
import org.apache.http.util.EntityUtils;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.BasicResponseHandler;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.HttpResponse;
*/

public class JavaHttp
{
    public static void main( String[] args ) throws IOException
    {
        System.out.print("[INFO]: JavaHttp:Get :" + args[0] + "\n");

        String default_charset = "Big5";
        HttpClient client = new DefaultHttpClient();
        HttpGet request = new HttpGet( args[0] );
        HttpResponse response = client.execute(request);
        HttpEntity entity = response.getEntity();
        Header header = entity.getContentType();

        Charset charset = ContentType.getOrDefault( entity ).getCharset();

        if( charset == null )
        {
            System.out.println("[INFO]: charset is null");
        }
        else
        {
            System.out.println("[INFO]: charset :" + charset.displayName() );
            default_charset = charset.displayName();
        }


        
        if( header == null )
        {
            System.out.println("[INFO]: header is null" );
        }
        else
        {
            HeaderElement element[] = header.getElements();

            System.out.println("[INFO]: header name :" + header.getName() );
            System.out.println("[INFO]: header value :" + header.getValue() );
            System.out.println("[INFO]: element length :" + element.length );
            for( int i = 0; i < element.length; i++ )
            {
                System.out.println("[INDO]: element["+i+"]"+"="+element[i].getName()+":"+element[i].getValue() );
            }
        }



        String respContent = EntityUtils.toString( entity , default_charset ).trim();
        request.abort();
        client.getConnectionManager().shutdown();

        System.out.println( respContent );


        /*
        // Get the response
        BufferedReader rd = new BufferedReader
              (new InputStreamReader(response.getEntity().getContent()));
      
        String line = "";
        
        while ((line = rd.readLine()) != null) 
        {
            //System.out.println(line);
            System.out.println( new String( line.getBytes("big5"))  );

        }
        */
    }
}
