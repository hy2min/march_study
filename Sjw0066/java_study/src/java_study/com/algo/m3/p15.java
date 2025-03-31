package java_study.com.algo.m3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p15 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st= new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		
		for(int i=a;i>=0;i--) {
			if (i !=0){
				bw.write(i+"\n");				
			}else {
				bw.write(i+"\n¹ß»ç");
			}
				
		}
		
		
		bw.close();
		br.close();
		
	}

}
