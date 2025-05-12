package java_study.com.algo.m2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p9 {

	public static void main(String[] args) throws IOException{
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int a= Integer.parseInt(br.readLine());
		
		bw.write(a+" 입력함\n");
		a++;
		bw.write("a++을 수행하면 ");
		bw.write(a+"");
		bw.write("이 됩니다");
	
		br.close();
		bw.close();
		
		
	}

}
