package java_study.com.algo.m4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p6 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st= new StringTokenizer(br.readLine());
		
		int[] arr = {3,4,1,6,7,5};
		
		
		
		int ans=arr[Integer.parseInt(st.nextToken())]+arr[Integer.parseInt(st.nextToken())];
		bw.write(ans+"");
		
		bw.close();
		br.close();
		
	}

}
