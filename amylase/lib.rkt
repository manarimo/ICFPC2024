(define order "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`|~ \n")
(define itos (lambda (i) 
    (if (= i 0)
        ""
        (string-append 
            (itos (quotient i 94)) 
            (substring order (remainder i 94) (+ 1 (remainder i 94)))
        )
    )
))
(define stoi (lambda (s) 
    (if (> (string-length s) 0)
        (+ 
            (* 94 (stoi (substring s 0 (- (string-length s) 1))))
            (car (car (regexp-match-positions (substring s (- (string-length s) 1)) order)))
        )
        0
    )
))
