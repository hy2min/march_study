package java_study.com.algo.m2;

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
		
		StringTokenizer st=new StringTokenizer(br.readLine());
		String a = st.nextToken();
		String b = st.nextToken();
		String c = st.nextToken();

		for (int i=0;i<3;i++) {
			bw.write(a);
		}
		bw.write("\n");
		for (int i=0;i<3;i++) {
			bw.write(b);
		}
		bw.write("\n");
		for (int i=0;i<3;i++) {
			bw.write(c);
		}
		
		bw.close();
		br.close();
		
	}

}
