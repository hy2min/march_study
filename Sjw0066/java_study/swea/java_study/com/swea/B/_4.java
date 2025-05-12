package java_study.com.swea.B;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

import com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader.Array;

public class _4 {
	static int N,M,L,idx,val;
	static ArrayList<Integer> arr;
	static StringTokenizer st ;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int tc =1; tc<T+1;tc++) {
			arr=new ArrayList<>();
			st=new StringTokenizer(br.readLine());
			N=Integer.parseInt(st.nextToken());
			M=Integer.parseInt(st.nextToken());
			L=Integer.parseInt(st.nextToken());
			st=new StringTokenizer(br.readLine());
			
			for (int i = 0;i<N;i++) {
				arr.add(Integer.parseInt(st.nextToken()));
			}
			
			for (int i = 0;i<M;i++) {
				st=new StringTokenizer(br.readLine());
				String first = st.nextToken();
				switch(first) {
				case "I":
					idx=Integer.parseInt(st.nextToken());
					val=Integer.parseInt(st.nextToken());
					arr.add(idx,val);
					continue;
				case "D":
					idx=Integer.parseInt(st.nextToken());
					arr.remove(idx);
					continue;
				case "C":
					idx=Integer.parseInt(st.nextToken());
					val=Integer.parseInt(st.nextToken());
					arr.set(idx,val);
					continue;
				}
			}
			if (arr.size()<L) {
				bw.write("#"+tc+" -1\n");
			}else {
				bw.write("#"+tc+" "+arr.get(L)+"\n");
			}
			
			
			
			
			
			
			
			
		}
		bw.flush();
		bw.close();
		br.close();
	}

}
