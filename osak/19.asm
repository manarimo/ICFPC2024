B. @Ssolve@_lambdaman19@_

-- Bind Direction function
B$
Ld

-- Main
B$
Lf -- Bind Fractal
  B. B. B.
    B$ vf @I0
    B$ vf @I1
    B$ vf @I2
    B$ vf @I3

-- Recursive Fractal
B$
Lf
  B$ B$ vf vf @I64
-- Fractal :: Self -> Int -> Int -> String
-- l: length, o: offset
Lf Ll Lo
  ? (B= vl @I0)
  S
  B$ B$ L$ Lr
    B. B. B. B.
      B$ vr (B$ vd vo) -- Go to next depth
      B$ v$ vo -- Front
      B$ v$ (B+ vo @I1) -- Left
      B$ v$ (B+ vo @I3) -- Right
      B$ vr (B$ vd (B+ vo @I2)) -- Go back
  B$ B$ vf vf (B/ vl @I2)
  -- Recursive Repeat
  B$
  Lf
    B$ B$ vf vf vl
  -- Repeat :: Self -> Int -> String -> String
  Lr Ln Ls
    ? (B= vn @I1)
      vs
      B. vs B$ B$ B$ vr vr (B- vn @I1) vs

-- Direction :: Int -> String
Ld
  BT @I1 BD (B% vd @I4) @SULDR


