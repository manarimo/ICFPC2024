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
        ? ( B= vs @I9 )
          S
          B.
            BT @I4 BD (B* @I4 B% vs @I9) v# -- Decode the first entry
            (B$ vd (B/ vs @I9)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I36
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
@I5706674272959082441045

-- Encoded string
@I2394925481777574821617752271395922714742167709938977616697074234871786614780445978286642404535368442207466897916592341480720805098915595830111038191242519987750369321984371609893401886840548427322726448536665082805160568648019317076762045052873473891238176394692795789004234150906382890884360729392959007940921706429845942667804723168573551302798973861588581044622387254558906883529389402836176983359232875699305194890389128541236173315486685478684335523357253682364088662725493412185464234813402280691835444797311136229931243644661231477989339006447594458507855647316174260656659120892042664284083


