package java_study.com.algo.m2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p10 {

	public static void main(String[] args)throws IOException{
		BufferedWriter bw= new BufferedWriter(new OutputStreamWriter(System.out));
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		int a= Integer.parseInt(br.readLine());
		if (a>3) {
			a++;
			bw.write(a+"");
		}else {
			a--;
			bw.write(a+"");
		}
		
		bw.close();
		br.close();
	
		
	}

}
