-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I8190

-- Pass the encoded string
B$

-- Make the recursive function of Decode
B$
  Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx -- Fix
  -- Decode :: Self -> String -> String
  -- Decodes the first entry in the source then recursively process the rest.
  Ld Ls
    ? ( B= vs @I9 )
      S
      B.
        BT @I8 BD (B* @I8 B% vs @I9) @SRRDDLLDDDDRRUURRDDRRUUUULLUURRRRRRDDLLLLUULLDDDDUULLDDLLLLUURRUULLUURRLL -- Decode the first entry
        (B$ vd (B/ vs @I9)) -- Process the rest

-- Encoded string
@I1382360580628847604886846823939923629056320631093536497460519762584013080236986181196235110607608801811552758318501605462150923422800219172641841154571030017730898606672494757489250242644219818731438071610457559312747045024856681838936362980750657776263604692233573532579419697963733461559171882601655794152621143049097827961046135480222457684489939927101307195020937538517872662960527262314873588671180418131529595274825297009046042146136198806561745324286114186868814937195676706158921333466920862172402427630093118093657840208240992137636479967692893537706854343955787173149099300087286785897804781105731454491676428908921798167833536531634317650921698094920172679028614773955257302442128504582801048618715939945493284338183196440859574976214033257566762298541291998631538231318838227517547699677616942957731757373808672819195473322413024267599284179057649154315802288776318693297337050180579138398356726515082787650730506645394616051324676225562591840475566825864931972012157

