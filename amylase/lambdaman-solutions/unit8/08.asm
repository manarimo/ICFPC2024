-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I4899

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
        ? ( B= vs @I8 )
          S
          B.
            BT @I8 BD (B* @I8 B% vs @I8) v# -- Decode the first entry
            (B$ vd (B/ vs @I8)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I64
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
@I340287538988205766685866615453454302986

-- Encoded string
@I353512305204406923477957737582529900350495009963140528458872842369232399287616984541855169148064912984574856677512041932427547922488221575737410208053418429171850866320869150072083571337628882297208504642343623359907961812723133421679512021338359173525932317206235507665025380855541196805235239257890239312346700432079008555921730843756382967519634400453964584861968772162765379240366349240312377790886241478688944945619266094778491369805184072180728186466464721556676712970592475627990735675820485617422874434960832800941004705344399184205180611521595016


