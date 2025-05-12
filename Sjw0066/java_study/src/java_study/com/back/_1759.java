package java_study.com.back;

import java.io.*;
import java.util.*;

public class _1759 {
    static int L, C;
    static String[] arr;
    static List<String> result = new ArrayList<>();
    static Set<String> vowelSet = new HashSet<>(Arrays.asList("a", "e", "i", "o", "u"));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        arr = br.readLine().split(" ");
        Arrays.sort(arr);  // 사전 순 정렬

        dfs(0, 0, 0, "");

        for (String s : result) {
            bw.write(s + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int start, int len, int vowelCount, String path) {
        if (len == L) {
            int consonantCount = L - vowelCount;
            if (vowelCount >= 1 && consonantCount >= 2) {
                result.add(path);
            }
            return;
        }

        for (int i = start; i < C; i++) {
            String ch = arr[i];
            boolean isVowel = vowelSet.contains(ch);
            dfs(i + 1, len + 1, vowelCount + (isVowel ? 1 : 0), path + ch);
        }
    }
}
