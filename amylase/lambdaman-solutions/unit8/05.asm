-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I142

-- Pass the encoded string
B$

-- Bind the expanded dictionary
B$
L#
  -- Make the recursive function of Decode
  B$
    Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx -- Fix

      -- Decode :: Self -> String -> String
      -- Decodes the first entry in the source then recursively process the rest.
      Ld Ls
        ? ( B= vs @I18 )
          S
          B.
            BT @I8 BD (B* @I8 B% vs @I18) v# -- Decode the first entry
            (B$ vd (B/ vs @I18)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I144
-- Apply the compressed dictionary to obtain the dict
B$

-- Make the recursive Expand function
B$
-- Fix
Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx

-- Expand :: Self -> Int -> String
Le Lp
  ? (B= vp @I0)
    S
    B.
      BT @I1 BD (B% vp @I4) @SLRDU
      B$ ve (B/ vp @I4)
@I513593309718655041318030102072599915047554010523718584856243393131881985990964802957321

-- Encoded string
@I747445606689889243214802


