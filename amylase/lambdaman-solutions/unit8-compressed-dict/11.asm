-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I9622

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
@I72177737279645307294975761618036689805319710048094143299071825421548330015336214010960449899251723329641842697339317991968895768844201592659660452151780951187540806145403013931701290582303592230144479551949296614349787826591024190471362620456332547048104768207244287117417837874238105444393635695134449641631336397939461956398554053397596531848402512431645304790656452900497880154256316727118697689910586375623553303758106359546771476670405963526721106378876788370302174781700369299944291498643102321928794044124718137657881465813275434505026329176730916794866403683188484165624723049977034509781430085278732968119578301138164714770061925801122601472194528938595655515781351621012370110925629339717379186965190524173980187826600980046299944979113552516419614566145195826421868019274915318282972386202839056875926436994020586773153629148011896212168786779867741346905467201033827848103704084420094603298746969217961818059582033248500232039213342267056590623564429085040151013610423936057782741770226053539705962785195219343435435786

-- Encoded string
@I6588037640539320325036384363721415950297929539491197864908724874121945159774156576171547075058507629043934936339696627535685342966269762074496032048006890820495789965225113721235592712651493070681783200122673641234005643279937534873024240325096659632171688333133132086898302836682160302169527145592762638115167277499939885504018256831598752698408309094032267186859148754152222278751319665791287203102235490726793365422599591775036459427711895473303881803285434366331515321880869782307411491740836821954955889267944508617493610851583071321079610960756198621046140404643868178266713961604601756630931685599244725235815105024287890234960006171069257459007281248070865477026233118511372505141814878955658393032395593672818995757861348648479433120553699318914693432512701475132152218520460898284220028631220649256303172693221959286330484534648387842189750216454787757353567939863627978194531366973910097674575002362324739077215577252345894114730540636792830940954604520040762088318096507626457881137852966982070199573262743863269544137574055261613336115518877272785533310309128256494973740589716746453347855665444744703240476224275321147264298511514089516044725382110041017743393313951450263774396469600082527258642979986478834659435067574010006826313723162418639511563181952512491903363594868998783429089650605708822600222311298933037647934226588326551700324872948380369981238078666580501283139272615668409629583965460086694387368723984489106078017955971238760334419211298141795652085927459192399721585317515106069457394819974245685273703062089872927248843028094294875018236057812174529523332069290015446644709540797477361009863581151055043677580838959895037905972833954300261189943497120890656621538140749067904445863741361977904583439132446702871750182463710115925745608471667543277680030993767057261699838395449731180475213683450105211479384967614515277024844875077925462751323257233560861024902041311002804316031932527502065184184799964926210544072885992765679329300936468790061114064410157152126447963598061200784590657352290293434268345411379099006806069794849255606533701855043142913390514246651135161338986510930138131573701844925230116686478815958380710143872541095267571534257243366166088628917775982030478257249434509303898423869222271199857170084298644175420254737979186161061490326214763874072864861847919157400328246238156602201104563085405157606036856525540263684215353579840250087399737965217389772283627100428867793961500933763852148038028815800061677234468254503502456890979546190317589722737207848073819294482211157583681339856650999111782308660204397759566198248555574180663144252829851578757989253070939213734658778990738337604287172896413402868659817969941852878956102645442496395801833292268225756098586152811279567710601014832477715133936448142743058389841910545002132929997323115595558

