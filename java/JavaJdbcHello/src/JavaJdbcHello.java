/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//package hello;

import java.sql.*;

/**
 *
 * @author Clouds
 */
public class JavaJdbcHello 
{
    Connection connection;
    
    public JavaJdbcHello()
    {
        try 
        {
            Class.forName("com.mysql.jdbc.Driver").newInstance();
            System.out.println("Good to go");
        } 
        catch (Exception e) 
        {
            System.out.println("JDBC Driver error");
            System.out.println( e.toString() );
        }
    }
    
    public void connectToDB() 
    {
        try 
        {
            connection = DriverManager.getConnection(
                        "jdbc:mysql://Mnemosyne/hello_db?user=faceless");
            
            System.out.println("Connect to Database!");
        }
        catch(SQLException e) 
        {
            displaySQLErrors(e);
        }
    }
    
    
    public void executeSQL() 
    {
        try 
        {
            Statement statement = connection.createStatement();
            ResultSet rs = statement.executeQuery(
                                "SELECT * FROM acc");
            while (rs.next()) 
            {
                System.out.println(rs.getString(1));
            }
            rs.close();
            statement.close();
            connection.close();
        }
        catch(SQLException e) 
        {
            displaySQLErrors(e);
        }
    }
    
    private void displaySQLErrors(SQLException e) 
    {
        System.out.println("SQLException: " + e.getMessage());
        System.out.println("SQLState: " + e.getSQLState());
        System.out.println("VendorError: " + e.getErrorCode());
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) 
    {
        JavaJdbcHello JdbcHello;
        
        // TODO code application logic here
        System.out.println("Hello!JDBC Connector/J!");
        
        JdbcHello = new JavaJdbcHello();
        
        JdbcHello.connectToDB();
        JdbcHello.executeSQL();
        
        
    }
    
}
