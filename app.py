from flask import Flask, render_template, request
import itertools
import math
import threading

app = Flask(__name__)
pagesize = 50


@app.route('/')
def main_page():
    values = [app.p.get_prime(i) for i in range(50)]
    return render_template(
        'index.html', primes=values, page_size=pagesize, start=pagesize
    )


@app.route('/primes')
def primes_only():
    page = request.args.get('page', default=0, type=int)
    values = [app.p.get_prime(i) for i in range(page, page + pagesize)]
    return render_template(
        'primes.html', primes=values, page_size=pagesize, start=page + pagesize
    )


class primes:
    def __init__(self):
        self.primes = []
        self.n = 0
        self.mu = threading.Lock()

    def get_prime(self, i):
        with self.mu:
            if i == 0:
                return 1
            elif i == 1:
                return 2
            else:
                idx = i - 2

                while idx >= self.n:
                    if self.n == 0:
                        start = 3
                    else:
                        start = self.primes[self.n - 1] + 2

                    for j in itertools.count(start, 2):
                        isprime = True
                        jsqrt = math.sqrt(j)
                        for pri in self.primes:
                            if j % pri == 0:
                                isprime = False
                                break
                            if pri > jsqrt:
                                break

                        if isprime:
                            self.primes.append(j)
                            self.n += 1
                            break

                return self.primes[idx]

app.p = primes()

if __name__ == '__main__':
    app.run()
