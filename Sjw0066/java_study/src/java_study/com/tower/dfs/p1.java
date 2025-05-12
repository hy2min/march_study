package java_study.com.tower.dfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class p1 {
		static int computer;
		static int n;
		static int cnt=-1;
		static ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
		static boolean[] visited;
		
		static void dfs(int now) {
			
			for (int next:arr.get(now)) {
				if (visited[next]!=true) {
					visited[next] = true;
					cnt++;
					dfs(next);
				}
			} 
			
		}
		
		
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));		
		computer=Integer.parseInt(br.readLine());
		n=Integer.parseInt(br.readLine());
		visited=new boolean[computer+1];
		for (int i=0;i<computer+1;i++) {
			arr.add(new ArrayList<>());
		}
		
		
		for (int i=0;i<n;i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a=Integer.parseInt(st.nextToken());
			int b=Integer.parseInt(st.nextToken());
			arr.get(a).add(b);
			arr.get(b).add(a);
		}
		
		dfs(1);
		
		bw.write(cnt+"");
		
		br.close();
		bw.close();
	}

}
