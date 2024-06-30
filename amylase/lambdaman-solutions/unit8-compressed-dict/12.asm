-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I9630

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
        ? ( B= vs @I214 )
          S
          B.
            BT @I8 BD (B* @I8 B% vs @I214) v# -- Decode the first entry
            (B$ vd (B/ vs @I214)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I1712
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
@I106517038450315212126288297230945082707707778181188234826358871694242269281709483826614027040678065390740777324810841876058688741677545145626347998430590953901245359676964461839518103868643592955396661751481758275382279224803158093317388591508459667204108127459915844269304566179219636162608841615655136835292488955562327738799737773929341554640013886579407575700838682138331287089624541364333312776641617345021970586361423189188720141926733970513228308771418830632382601285801988114831995315366713696435664035331309148304776489829644243083223468688046878813736985164911862470383637437767712251106018260847540289542585973714050779758133376334939122276945455059492322667205413197912478579874435640992975644478394245406387077855628687734787659800854812841840623227476779639721627386366867390943319905469584671968458656188496832089544978924833642008342161210621398462339967822961534876280894557862716626722616695880811365984808829327108918358085105595414066613368070828997336103405899598212125073420140123441296991708154045609123250261

-- Encoded string
@I1411185907834232083067832522576329322544547451077740326805050615369488100111224129232625881178752804018273946196966292435222802292161102935156473781472414582131528820651496709459422842516399459725484704404824508265976106127320352113428796303315852632901415857828222249089504849803795977301441065346354141122294893480843438896717885757599227650117206844412987853635952534123428057769821254369361450705606822971838901888950548723769120976808508893544367939774654134086741708258406291599066134607084189611174730652904070651925469692327598531671958439932208528790607559721462846459636622210273197368036535622208949606368147624533152668270901305270845932056290671096830825296306930811956018320739147445612280130518404859075815564212591725844806363317866749700716951626696823375587357067402697203067674928297135017289844190544938892424895189920307097845777886455060146027148667141757235002117987308052878851365593303414801309459682119973109608034079732061270077064379800993958863575951864068991034951526294862421723915896226992066897871313306328663728219611794766093434599842616798343024919789157246690825057628237030935347920533185557088281955785558194266027450410454775076418241486285411266219335441450113661498500594881414297638136196012002924786902823144590690065751240865804771913292108790079013771687603649089771386061923516404177632285758778603629901779074609170949674246194179034614716412785012470534671659715140598904885500484539787711904974942566589203411251320833064310656841298156717051537211683386429937606792623150423617406817192126793529994114039141256470386066199564017809155211292150795510707040088065902327242257569643398707585055510681938974025543111000827173453300667172669941262008901889438038611114698341816805272671849604450547731062369876064170475823301249034146725932106173663209930950552897738688741522324942741768646362801963992008403722630519825983856957988341745205045098203102028515805197299176723725637627593468828509884680472368310562310887060192363222791010030221019711366051918583745948293732935831741036324343763559421528117675792228806723364218208025316980291138196561807381160752285846917341955782022931347564771877719279725578068382214705152690758130487193502533039025239928049265791970789149446074640269010102023974708328767101333695947286100381174737724973250407508325054899136613867978551359898269577027683732583710255344617826508216825415567682631531202817602143738726916445783052891808335404690169697626578355409598141802513653396176176799651564891412252203951311312721016178080354802436300255083637322783509398553239561312650001354688606208283217747500183824134616377438026387828347983879068155348366054407031626926682359503121870228641193772950016915636959236162661563925929841563796206336361081981582416871765515674099440962016495727129852313943909187427015606629049734

