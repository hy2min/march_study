package java_study.com.tower.dfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

import com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader.Array;


public class p3 {
	static int[] arr = new int[1001];
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static void preorder(int now) {
		
	}
	
	static void inorder(int now) {
		
	}
	
	static void postorder(int now) {
		
	}
	
	
	public static void main(String[] args) throws IOException{
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
			int N = Integer.parseInt(br.readLine());
			
			for (int i=0; i<N;i++) {
				StringTokenizer st=new StringTokenizer(br.readLine());
				int a= Integer.parseInt(st.nextToken());
				int b= Integer.parseInt(st.nextToken());
				int c= Integer.parseInt(st.nextToken());
				if (i == 0 ) {
					arr[1]=a;
				}
				int idx=Arrays.asList(arr).indexOf(a);
				if (b != -1) {
					arr[idx*2]=b;
				}
				if (c != -1) {
					arr[idx*2+1]=c;
				}//end if	
			}//end for
			
			preorder();
			inorder();
			postorder();
			
			br.close();
			bw.close();
	}//end main
}// end class
