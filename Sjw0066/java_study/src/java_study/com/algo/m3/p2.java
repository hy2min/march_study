package java_study.com.algo.m3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p2 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int a,b;
		a=Integer.parseInt(st.nextToken());
		b=Integer.parseInt(st.nextToken());
		
		if (a==b) {
			bw.write("같은숫자");
			
		}else if (a>b) {
			bw.write("큰수는 "+a);
		}else {
			bw.write("큰수는 "+b);
		}
		
		bw.close();
		br.close();
		
		
		
		
	}

}
