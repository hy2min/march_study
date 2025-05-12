package java_study.com.algo.m4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class p8 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int idx=Integer.parseInt(br.readLine());
		int[] arr= {3,9,27,81,243};
		
		bw.write(arr[idx]-100+"");
		
		bw.close();
		br.close();
		
	}

}
