package java_study.com.tower.dfs;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;


public class p2 {
	static ArrayList<ArrayList<Integer>> tree = new ArrayList<>();
	static boolean[] visited;
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	static void preorder(int now) throws IOException{
		visited[now]=true;
		List<Integer> sortedList = new ArrayList<>(tree.get(now));
		Collections.sort(sortedList, Collections.reverseOrder());
		bw.write(now+" ");
		for (int next:sortedList) {
			
			if (visited[next]!=true) {
				
				preorder(next);
			}
		}
		
		
	}
	
	static void postorder(int now) throws IOException {
		visited[now]=true;
		
		List<Integer> sortedList = new ArrayList<>(tree.get(now));
		Collections.sort(sortedList, Collections.reverseOrder());
		
		for (int next:sortedList) {
			if (visited[next]!=true) {
				postorder(next);
				
			}
			
		}
		bw.write(now+" ");
		
		
	}
	
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st= new StringTokenizer(br.readLine());
		int N=Integer.parseInt(st.nextToken());
		int K=Integer.parseInt(st.nextToken());
		int S=Integer.parseInt(br.readLine());
		
		for (int i = 0; i <= N; i++) {
			tree.add(new ArrayList<>());
		}
		
		for (int i=0;i<K;i++) {
			StringTokenizer stt=new StringTokenizer(br.readLine());
			int a=Integer.parseInt(stt.nextToken());
			int b=Integer.parseInt(stt.nextToken());
			tree.get(a).add(b);
		}
		
		visited=new boolean[N+1];
		preorder(S);
		bw.write("\n");
		visited=new boolean[N+1];
		postorder(S);
		
		
		br.close();
		bw.close();
		
		
	}

}
