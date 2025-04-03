package java_study.com.algo.m9;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p4 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		
		String a = st.nextToken();
		String b = st.nextToken();
		
		String ret=getChar(a,b);
		bw.write(ret);
		
		br.close();
		bw.close();
		
	}
	
	public static String getChar(String str1,String str2) {
		
		if (str1.compareTo(str2)>0) {
			return str1;
		}else {
			return str2;
		}
		
	}
			
}
