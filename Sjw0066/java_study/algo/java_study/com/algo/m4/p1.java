package java_study.com.algo.m4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class p1 {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr=new int[5];
		for (int i=0 ;i<5;i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int idx=0;idx<5;idx++) {
			bw.write(arr[idx]+" ");
			
		}
		bw.close();
		br.close();
		
	}

}
