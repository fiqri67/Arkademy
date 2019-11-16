/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package regex;
 
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
 
public class Nomor2 {
	private static final String PATTERN = "^[A-Z]{7}$";
        private static final String PATTERN_Pass ="/^r'(0-9){3}'[*]r'(a-zA-Z){3}'$/";
	public static void main(String args[]){ 
		List<String> username= new ArrayList<String>();	       
		username.add("JAIPAHUU"); 
		username.add("SAMBADA"); 
		username.add("jai12345");
		username.add("jai_singh");
 
		Pattern pattern = Pattern.compile(PATTERN);
		for (String value : username){
		  Matcher matcher = pattern.matcher(value);
		  if(matcher.matches()){
			  System.out.println("Username "+ value +" is True");
		  }else{
			  System.out.println("Username "+ value +" is False");
		  }		  
		}
                System.out.println("===============");
                List<String> password = new ArrayList<String>();	
		password.add("jaisingh1A@"); 
		password.add("222*ddd"); 
		password.add("jaiA@");
		password.add("jai*");
 
		Pattern pattern_pass = Pattern.compile(PATTERN_Pass);
		for (String value : password){
		  Matcher matcher = pattern.matcher(value);
		  if(matcher.matches()){
			  System.out.println("Password "+ value +" is True");
		  }else{
			  System.out.println("Password "+ value +" is False");
		  }		  
		}
	}
}
