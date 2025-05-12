package java_study.com.swea;

import java.io.*;
import java.util.*;

public class swea5656 {
    static int N, W, H;
    static int[][] arr;
    static int[] dir_y = {-1, 0, 1, 0};
    static int[] dir_x = {0, 1, 0, -1};
    static int ans;

    // 중력 처리
    static int[][] block_down(int[][] blocks) {
        int[][] ret = new int[H][W];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < W; i++) {
            stack.clear();
            for (int j = 0; j < H; j++) {
                if (blocks[j][i] != 0) {
                    stack.push(blocks[j][i]);
                }
            }

            int idx_y = H - 1;
            while (!stack.isEmpty() && idx_y>=0) {
                ret[idx_y--][i] = stack.pop();
            }
        }

        return ret;
    }

    static int[][] boom(int y, int x, int[][] map) {
        int[][] next = new int[H][];
        for (int i = 0; i < H; i++) {
            next[i] = Arrays.copyOf(map[i], W);
        }

        Queue<int[]> q = new LinkedList<>();
        if (next[y][x] > 0) {
            q.add(new int[]{y, x, next[y][x]});
            next[y][x] = 0;
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int cy = cur[0];
            int cx = cur[1];
            int power = cur[2];

            for (int d = 0; d < 4; d++) {
                for (int p = 1; p < power; p++) {
                    int ny = cy + dir_y[d] * p;
                    int nx = cx + dir_x[d] * p;

                    if (ny < 0 || ny >= H || nx < 0 || nx >= W) continue;
                    if (next[ny][nx] == 0) continue;

                    if (next[ny][nx] > 1) {
                        q.add(new int[]{ny, nx, next[ny][nx]});
                    }
                    next[ny][nx] = 0;
                }
            }
        }

        return block_down(next);
    }

    // DFS로 가능한 경우 탐색
    static void dfs(int level, int[][] map) {
        if (level == N) {
            int cnt = 0;
            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    if (map[i][j] != 0) cnt++;
                }
            }
            ans = Math.min(ans, cnt);
            return;
        }

        boolean flag = true;
        for (int i = 0; i < W; i++) {
            for (int j = 0; j < H; j++) {
                if (map[j][i] != 0) {
                    int[][] temp = boom(j, i, map);
                    dfs(level + 1, temp);
                    flag = false;
                    break; // 다음 열로 넘어감
                }
            }
        }

        if (flag) {
            int cnt = 0;
            for (int i = 0; i < H; i++) {
                for (int j = 0; j < W; j++) {
                    if (map[i][j] != 0) cnt++;
                }
            }
            ans = Math.min(ans, cnt);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            H = Integer.parseInt(st.nextToken());
            arr = new int[H][W];
            ans = Integer.MAX_VALUE;

            for (int i = 0; i < H; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < W; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            dfs(0, arr);
            bw.write("#" + tc + " " + ans + "\n");
        }

        bw.close();
        br.close();
    }
}
