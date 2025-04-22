package java_study.com.back;

import java.io.*;

public class _16637 {
    static int N;
    static int ans = Integer.MIN_VALUE;
    static String[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = br.readLine().split("");

        dfs(0, Integer.parseInt(arr[0]));
        System.out.println(ans);
    }

    static void dfs(int idx, int result) {
        if (idx >= N - 1) {
            ans = Math.max(ans, result);
            return;
        }

        //현재에 괄호 갈기기
        int noBracket = cal(result, arr[idx + 1], Integer.parseInt(arr[idx + 2]));
        dfs(idx + 2, noBracket);

        //다음연사 괄호일시
        if (idx + 4 <= N - 1) {
            int bracket = cal(Integer.parseInt(arr[idx + 2]), arr[idx + 3], Integer.parseInt(arr[idx + 4]));
            int total = cal(result, arr[idx + 1], bracket);
            dfs(idx + 4, total);
        }
    }

    static int cal(int a, String op, int b) {
        switch (op) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
        }
        return 0;
    }
}
