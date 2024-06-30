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
        ? ( B= vs @I4 )
          S
          B.
            BT @I2 BD (B* @I2 B% vs @I4) v# -- Decode the first entry
            (B$ vd (B/ vs @I4)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I8
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
@I89866

-- Encoded string
@I482837342679615559330962548018306115920981657920137591546989561284157908180583635134356467386031876285169991650112151188651693467619814437373891593127383469386962259587356042714897360705049881357679930072148163362661908826002171935421350910297269309756227147117673743031850940414960545062803005856945503029236610241859323368752604531705339019937946175986205762827669659550213466175227831867987644171972154018195252456617448235604958940438468528703325210698711756989749174312358211909536927212177170798308485921515226940273548382785870777140834539623175742044754318488930721159090130929395035940992849392754633547299431551794114642561157613511284715136383926965742618611004561703590195697730897574466899591505410192560537567325810780049123480045301875277908375135564184362031810629172898561827803740575075303910272668706440679856777388370065675341323086966427523737917226654161656293025277490750033521902009673795459207464536681224950256951515629407874913013363232665669653492086523833060439362210594712224614786157403493584377074107402779142991014374820717342226240103813575165621760902824315530210464182236333625894232101844521277916409749497375179872835807570754650533965559002364200544924043191655091047170961358300538387521463179779169404927688402681701100047033033980437091978046569605376145210376590643148236273554781889524226843898292975321496891251386665058974977443152758953513107015924501883513035527038218146988462392553157674946800836140683369741104540611385757604

