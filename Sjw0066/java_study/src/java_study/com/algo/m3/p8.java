package java_study.com.algo.m3;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p8 {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a= Integer.parseInt(br.readLine());
		for (int i = 0 ; i<a; i++) {
			bw.write("##\n");
		}
		bw.close();
		br.close();
		
	}

}
