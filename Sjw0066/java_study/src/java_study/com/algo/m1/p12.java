package java_study.com.algo.m1;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class p12 {
	
	public static void main(String[] args){
		int a,ans;
		ans=1;
		a=8;
		
		for (int i=0;i<5;i++) {
			ans=ans*a;
		}
			
		System.out.println(ans);
	}
	
}
