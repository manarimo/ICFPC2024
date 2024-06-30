-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I2499

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
        ? ( B= vs @I13 )
          S
          B.
            BT @I8 BD (B* @I8 B% vs @I13) v# -- Decode the first entry
            (B$ vd (B/ vs @I13)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I104
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
@I411710918728067422842719883721778020133517624930056204741858645

-- Encoded string
@I61547159256822497938158215306928113098207694046280779104503256620681714061606889509385993242880506849091673387571872554164564840458984214325787468956594157836065216894284108734600016013999216346838604353782779148278303035057619901535247599530002330865790550039763212697382292226819371827565488529536511745841587940258156061331833820925739540246176479


