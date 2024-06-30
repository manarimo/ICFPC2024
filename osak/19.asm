B. @Ssolve@_lambdaman19@_

-- Bind Direction and Repeat functions
B$ B$
Ld Lr

-- Main
B$
Lf -- Bind Fractal
  B. B. B.
    B$ B$ vf @I128 @I0
    B$ B$ vf @I128 @I1
    B$ B$ vf @I128 @I2
    B$ B$ vf @I128 @I3

-- Recursive Fractal
B$
Lf
  B$ vf vf
-- Fractal :: Self -> Int -> Int -> String
-- l: length, o: offset
Lf Ll Lo
  ? (B= vl @I0)
  S
  B$ L$
  B. B. B. B.
    B$ B$ vr vl (B$ vd vo) -- Go to next depth
    B$ v$ vo -- Front
    B$ v$ (B+ vo @I1) -- Left
    B$ v$ (B+ vo @I3) -- Right
    B$ B$ vr vl (B$ vd (B+ vo @I2)) -- Go back
  B$ B$ vf vf (B/ vl @I2)

-- Direction :: Int -> String
Ld
  BT @I1 BD (B% vd @I4) @SULDR

-- Recursive Repeat
B$
Lf
  B$ vf vf
-- Repeat :: Self -> Int -> String -> String
Lr Ln Ls
  ? (B= vn @I1)
    vs
    B. vs B$ B$ B$ vr vr (B- vn @I1) vs
