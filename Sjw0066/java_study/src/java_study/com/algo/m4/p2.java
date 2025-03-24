package java_study.com.algo.m4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p2 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int idx=Integer.parseInt(br.readLine());
		
		int[] arr= {4,1,3,6,9};
		
		bw.write(idx+"번index의값은"+arr[idx]+"입니다");
		
		
		bw.close();
		br.close();
		
	}

}
