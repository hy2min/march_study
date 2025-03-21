package java_study.com.algo.m2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p11 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a=Integer.parseInt(br.readLine());
		if (a>0) {
			bw.write("###\n");
			bw.write("###\n");
			bw.write("###\n");
		}else {
			bw.write("$$$\n");
			bw.write("$$$\n");
		}
		
		bw.close();
		br.close();
		
	}

}
