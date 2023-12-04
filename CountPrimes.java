class CountPrimes {
        public int countPrimes(int n) {
            boolean[] isPrime= new boolean[n + 1];
            for (int i = 0; i < n+1; i++) {
                isPrime[i]=true;
            }
            int numOfPrimes = 0;
            int p = 2;
            while (p * p <= n) {
                if (isPrime[p]) {
                    for (int i = p * p; i <= n; i += p) {
                        isPrime[i] = false;
                    }
                }
                p++;
            }
    
            for (int num = 2; num < n; num++) {
                if (isPrime[num]) {
                    numOfPrimes++;
                }
            }
            return numOfPrimes;
    }
}