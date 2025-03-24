package java_study.com.algo.m4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p4 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int a= Integer.parseInt(br.readLine());
		
		int[] arr = new int[5];
		
		for (int i = 0 ; i<5 ; i++) {
			arr[i] = a+5;
		}
		
		for (int j =0 ; j<5 ;j++) {
			bw.write(arr[j]+" ");
		}
		
		
		bw.close();
		br.close();
		
	}

}
