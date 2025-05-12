package java_study.com.algo.m1;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class p7 {
	
	public static void main(String[] args){
		int t = 5;
		System.out.print("t에서 1씩 증가=");
		for(int i=0;i<3;i++) {
			System.out.print(i+t+" ");
		}
		System.out.println();
		System.out.print("t에서 2씩 감소=");
		for (int j =0; j>-5; j-=2 ) {
			System.out.print(j+t+" ");
		}
	}
	
}
