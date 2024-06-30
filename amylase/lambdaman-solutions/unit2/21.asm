-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I42690

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
        ? ( B= vs @I16 )
          S
          B.
            BT @I2 BD (B* @I2 B% vs @I16) v# -- Decode the first entry
            (B$ vd (B/ vs @I16)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I32
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
@I31268425451213030026

-- Encoded string
@I142595086825784915728642726371371564701247276360529400545681330749246516302634566682394611581045128052348225044987409731902822274255449327780039904343554935630753109261369588744459156214038406177252384559201323017335183517931773819978045459786516034400624382397883989624524487456445820675167022091654399256994676702335611185229914127926570279592661134999421973784354683734255887302787894526273562656395273626399481703401312015798030060683811079478615706057421028182228649550638845907725936914479387420128722373499640154850128458569907865813339029885302548550338165573490981248168736014080926307728736253034139389051582950580393589935565441286794747983588019440867372827433549279675247753511772048223860941562381712157323891137912396868922648866050783735624051623280237938558942019735496598021490334896403633961221508398604881748514720327149009015232346808744324056825835397219693941330876057756842734561449916812751121649844006728095135681284226176759208656824981391468235100165852743919958329961494230986625086691110609795526617309472922969301889875750892620251581753820783025290094802169831256641086437789979171753836850509519544561330435388097522968728761660263427572866563817022720321028974626789647897160386212682507803907925570521314817552406973476604539354203831574838306908779679403496965833289639257642040280856833673600680352654537085924332289054570481682682137026997156556856668384666276961704803574806335237092631948063248600137015146411530616113072655197697798037257636536502299010220042366908524799502088132974243804058040278974059069275586571360751986766720459999179829787357965270719857901590753696587737165401831008876167448279375924445314622416168316692894887278059912840499674909801759134542516049886888088603061545014158686088085725743136038094927899804811282941079594049104310153263014886074402320720371865688198447497348323462239883742574416300750603099783742527354944987939365984045291263812541037718119487336158927588387555606771838397822222453908152428815498620596795954800713235859770130867555844589182317580421768810599711779719118091777708024192384961653469174417514181109169556485300626972795717479927113554336198477530818294307935287546954740612925363482931628002379408121285548052066517452626694697066888959769520187134911725169252560615970525513918441992357392061925537466951966967876494405918389824857648818918501312274654854841010697242914824802449777374780575000318784320287775374504633024956147839565605791740118116486875601256246042802703314937607551113476333996868966478327596261270742982478308249269797012609808330807105466511052117787488889174980573785757986989891510567702479877840661869741016886476108699775785776766064215300935641291515818923779897351461513937901487062687676119267612857139316189408177510842238124298459523438766658336815029361137997506292349140343754462587312653627510872959631304587358622262883842535101451057435432087777666975099787591402086534101297128061871660856084114874029289343053396587977270613806538572305812296732311312823313600322661001224871149401489924443616346272248952304687131047188133947353586538992984837806390152443816598301972958920413643460793454462730719029220488517548463067968327218275286643918880015558466053700017692956900680684007111238764501858524790880886379094806906282974512799326382010266613024544738179504162722444393527757997078288537933741497504067438693006884016610657361071398226550772349928425455680240528180306905843780971465996261124333010647020164765826906345284260200084708542345656148689943629103553929906312574878824473620852133786322893857340140074326534550248085175857524754601204492100600738313912924329031285284524504014703843037734774889495158763915401841796377287392503649876809479554832193272454344882706909670269916861424661782972109516697361394982592165879961990922240928076428380182312379581320000360530061985222958823972736212628173081465977920415984325289739732651229221871750712108838263558452148671139750252998589340080441820188301347507525391805701395749949070223703637694579185499810434109570235849153323414176966457457407471487453332973068048035421649415051923888802121925220276815154090525210973949800645102578195968857668075206482896073145780501085207854843095948116665479637304323544782034280155502224360205038969216711481929779828158088004037984440242185936319294855128673853556850028605940831579999413685400500304464724018029092579878910165862870025371264670435193463745648497720477898862454589526797020142579531924279835047107029952140709726087903216793630050724808726731136410205336479074548946932066770738674952445756473789748512813242078441959353290614530718602643980323256925962373772074875241278977717910662388244119981826504422893022694326235869183780344849624069339878217128071259675984657544766546482508353480350272787145225178291998963809845798091388438203812113692615005105153162313495926551982551270060315803142671688216034555664637882917904378822242844362344590275670518181491868295256657709760534111556460094073739382431922355335458722478169199822443698381837547492352205962748659587768522470310829721448630561606502827207454089266125316217108620147509853663546660402700680199658895726493931578051230295010550215110738297399726520074187262806019524150470481134880655117585165277429665221907867349764863757648715135736449282500408769459506877597194694212946849866979343143524959059418127579379860077605496832314787011720805911645601783332907370867665284079914078382183452641869482590568474163520110763746169021022553454959241135642202414670957378948621022063280602097444321688838232336332258372618990370309931609983798652832895010381474716827467966151879882804017507693706811917358934906145049963681766080202972562842074695118424858703832643406253322220855579359555159663556556727754216018365260656848694698122956159941299837513230474248409685173176940218176420721644448411899053921020994313502279350444733583420304862854159546565828508584253025169627340458169034657453765441580317812440073990208419828002273030400684293593173551297004897390569867631708978538109463102260675872128455837601381039763894485967652071889857651824307817478921447549539512710735750943389584240027882231433806044383528310825483579431298525386562235232789929331634702937079140687761326326652622779404428236194401527664015302245067933213506403228097927782320949771387669015292972422448082946174163784817969598251357967589466619677671384796574617756436117322210234901842634433865659092367515013526310878457788457008562905859113227731462329819775300693948892273428253124859008389093382331089848934226604897427771255720455943924439839197867947194376978914671485986854388017992154408418426004220649208155645835256359197256944971688280400302262069973611756850361137274453189352364696371243837962376315603124078416407475348844740326659900923348236072080325331467333407328390509023745614702653989462773137393985810223273725939562758997814088644682190388592253908190313182140546322326845157288420645352347904533558423587872295317112657626503154030807979612275712806363978410130382197033952176621268491352851412923580299636238777606179284932869785944803714029143092104525297200447876746081120001052906169026720601848546856586270030610917805610296868372287635812636390297482266154683648946667128594808245916888028692786162577797594525370529958394509562810345748306011264027010748539626104761624450635442164272019612185562440252479479194337591963571265357678402533211955936136830741711431056298939347637682754367023374738432421498378390757252867755238176927347952957518327896938177524903793721198943589984651565282099488222363775093806365925542853408516921433593671310112117293513804635944029111559127403193676284050507139027431676779453798713126403665959010146131083412489628605730368423447331846796425543475726802988593903435839084533146883539184754538960217478040438292785302680392790620788971063526312301376612273585873457603768153018657002496350536891115077238532354419197025005051408283022192511945921911198703346911615695417290099464975678687307612816855103076574728008445291021497749613375290946872461888594756474277330612024215490637767577245797364508267969927035936144270672495193010840072822491964914137235678660827620123120434918918367377026114967005423632376608286755130426205650448173645355253977334962592563084165799982019396819079477943525955762587222794092495449589454691345593821265876717144838247368824553317442804644924258206901053895522350213688507568316076480739116249168116406701054395506221263639377383339218827030825663863052648772338961795022306015454204688347389868515541312475873574215126257856170390849641292281228518192708450625660455390352659327695512279164576618720304049043476219332268891031998705510836694412459711223364541320972935542811912702146520364422186807824330308586434785388291373561971967306245622034301056959299948264297352065532369433184886090760732799583100326808060035788378946004475789756929818615351403566726848659102681330277306677204110580976891309973767581340650181742698593987758686359234636431959523548209261859908708603968361649079868450363343043331516247999078369814363629492545522004081489585789230752190360421483625821347748654941120832143560257441998597318234773088587544345769666491736076804543140082507035737095624292385713945844928835517935018555745269841179750777060063815740564150684562797004983108598459660014749772085897178815126179347056384127593298829556518538447750655873898144076772366660807244858616532511800292364336564630288240914978041774224624254071461876787239099736416953017923409452291074322564929868372588180138483679035257504551960845659192907886247564949572810330612475979154858849433696093268480850092698649808322852603554416031234432438464861840421357759656600658070497314647193078022328248803805877991188360756886040191871987882753381902012233569790098115352350444467482697683281400862629144924633746635264945399793955931173740189669102177162395126028834715284551828890335312522679984201033796865980060008520891558117218807241610175268940608870335283826463729466741410843112514861809932281230119710423257897123642980295004788031427687660838271645423240047715108041903095982395589250636452694294849001107415313222524956144961718309384855336838351137150273329746853446695649921240770398043183818896769171178451362100541559145793418694879720380996012664686512184631870379659429721559293870960789147869442941114268820248532832868901384483924702992195222850083724030383271625109063749860825055697654066932320897468204389978694582858326301365286739349671840860799669079768976822069391374696079573897803684529937267754583664135920380528361966732372668730145868918867750194351363818506011445129218099886111993750971004215667497806825506322534589808876360604976584994553818637134197736783338605116370330673299053681206579273969834840032401872349335943074678308422779664165278506789103192623532089624059312103325474478957314875245575069137662810179371241569826495198657578835515087186225182006800141893595695001339761952408390289135188571657606549892296792015012309771224764386949432774312704015067504776478123423237695781966381754272094489396674690219195151346339943360162874781647349012424240971124604795125208402924978351398840554008799286638312758494329594187493781046897194927152106725944632215989457841212606209249098942917064334924682944857661017521158527207426442216246120859372870210018214603003511886195824063598787191362077493415869011708816494604085516103730864131216771206974665561608626298490428478756510192572960197712485800366062105187837026763197826849472331414728124328930812249136444662279784187129185524433160964097687873466141512215844907059646939315563736675060063191695815474843406629363243477406301258572863409829798923535932893749738056112148453416461993074301574017736927498182799614829241080653575335286786415507820642950331016558708183456295073702305680003672658009528134830803650151300667340292683670099975990675583440992872159216422201744014598680483090406351273305344056229021470508701474949547636581942952803561425975682405079172882620856376255704271396993673544960400776390932380532046802041149832416131650363509820655176188400880358934842620554931657605801267033599771677463011373955552813615334260330895292949592055771403250144514012070690392670952702413183985255823855365919632185182924164380022063763233569863316331968647429133663503363420187239076547953974264881460339265182442484682863913274156885812756809866434888810849922390047902958641950519962624975055009450539327184145567988023361588623660911082625412962329934647757723392537125734104817014106151561326191158537019754568179714090440422955006281884427796580369231887716233525501393146537990736604362296093796910467857966592908504905877672058434800221458267857494730791941548942691055159143176682352389916837587762729299010193205014834017745009221664355120421297177037291705649157774264150610789442251430107081814504806965411931693761146330648578369297978615147922884180275100956136643187092004262271841939200091707731187142124698453491362167462126922447668094359521032766645787030736200036586161832532800954743201362192359848049485663744388439553163769995962052563861364660536385011332175325266156524576222100270490946505670653286511194278797833760980179899629458998406470378382388471296114851067513987319777868677076887087253519209955978330944197752991394257461714756685841983652188544523311039413789710427825621018151629367023761224921475579193734584659691430372067665878200193790365139899307816456415497835130191163557899430650956378142270557950816996442703125341668558864742733819643045915148359169621368670866604172801376822290322904628015515900380652317186235325385079113796794831465472320952249066140771975335393970336427091673607787909175873012145448018791958182805632904827484169053759532232517335653285106290461240600524926238699898529825996143750662769115975904230052133296136261417545602428875328197089492568224323977426462361239843699964999960138318582083076877052006442953911878811954795098541019616833496752680301509320282441747228453613686928785134661294474506504344769228265707085070665963302291007399953808550491030793694130131190757680371163999837383506055410611430158592041787224992229269397624717779087562715923819617187014022152272251890843120313802606915696976383417971112500684134421751303178312859001721310223674378203129323181483171140298191062214850044753014681173723041433948160313913523827999825317863255046850404384664000296014998681749521709890602758153258857055166814768241338968620927270977063187461665231071304643372244956560708847371189663715304502822839369833285561718143693530510997744239045584633874281578982584316229218245664140046406898710731263218150414526614815041364298974131844779692191178414424182900820680807647731980015814101410015675380020344677675127352042313976824493137321302503515210885048884685085535665739318938989791681931523361308698842647122923870084693064555682053702539950418364054044154819380617334538626536867006942947057474080182901700224142139441997480805425589133133272128079206158604534088470847196723468098124632149776467141535739088535571857542941500531667729333736024517190995701029170390035385661136269828179172400035274364290110030050050841884968917933756893620247823411209162692027876213099390965055080605824324128168762174470927502020770204216938571460881213030592791517991066915059780789958781280823052680411264504811142640180928228902584498257034219718735761023567225283936587194579644359839043971725484154890942695287710476935572369138379048988030721796700268151856130204205817063756778885325379115250679133733367477744510206047955151983141168266706684167968139919364958070662467535070613559983406628171938182348759313507398633742869677900693836412737366669468025088326060084247920190268188668026445715895880930168022468263028784784513753027475412461889410052450096809514787831118597640453570159095836201743512544228016274247734387653287321581267445876546061387167585525780121848200108575531104314310591686904129556058540393689146340576455629865584787850016588446485546632596591372648847861176339878207503127623335017274837775589929603170269277383728968625192656490511931024183449729343547179597446577349530212344205062407320844933998181757402859655094024421246616329772283424761939953329630512375121927516239967251941303455873280032597687214629273673080578213189006659911867899598281021754676241559290780037578773607759067821354648788060668696613276765876048242005264887878006101389571940909906036652581933415066548630850114106597329465057160430914809816487218935267912202715868455407445912567307858978439465582543788354030115970152847055493118477871419502253521104301419627905039056356942310637464060066306622232745700410004824682608273774690580134657326854103657675413346234074072287040845855304153390960891764329700186914811934211238738981851311223146845506241649018824223695734968640963606851386864576415499486559973541254523610640048511405262528651641299814555630040493991792565264207949610645034638632746563662582243591026457018813450703832841573088688649690007693463506392766916439856235347399613007988582189212612907310047480853087354527353624606665073486412304701392003311356180863137301986976039785664025300226798946172311789463845083917738246104878254525494946450631834636603863427382958546974438882988426960926791869823259855988926377231112897723797711746785302767972232960760094853835361275474691264369401638259723408429259749950079806155418308983568479562971724809026725455884704608037271881058738998629339384048169499207415947373672817034731836148610221143951555994456287371772044702968832213820906857178132458860614847962113132018826321922013455113299773008792780854076192502784780450275296008057413309832867559654131258760476084804633439342340900776850138158679587498505934567491091439712887925097364479829286231342711176486705036847774559331835382832621850062820558208870324819562925541358522023587044182395955642001516615049415299153174850746070921870395815096490182432886658760046862584668843684966860849033692762963609129556993803154464925483709202483568528947775744503207833419571628677262036784438715419345833731421147634125476540485428642140210028393619581762237020236324936512906689837800749034673701361424435171110163086360993335556338129621598949424334000036747821191237748916350957432088703079067700785310093020060463228417662101115697500681178631489543282743137846618089268365787778721533682538987336841244043431314588959338145439048685125884963236651877358248494774071014297459618223258704461534095549560485662847550408860307998176010223315661377745980519330633569996755523968404082945122707029832354996429162511794941487320225278853736819911708957073365479608701611532672800212591027743214126158465988465035887774559724268964568642603713243531140058927721025586791637813588893085456237011672213315203182133531121119879605695912801542838629278075272018301638069482073006308820942520833167124591347149696187657917773148443014234756900587023557761903807735280848355514946182167023713896878622724226423123500090716013111842418887536005495205412272315022661081561736691999622097267249033396901844825771695397303847969866972224058160933432448549877565628951912333924530155830898235593786246109389634766020809889670035061276267616037743022685215726683986198320856463666811462142603610868536794516365059883524240445651707858334756562366208291607098238350957030377151795029780608886296678966102091490321744430408661411577426170431708924922599641518570344622018704543687518648236028805571056761001204281824074385435741514306745059184308031129967519732532134072676560320685338345042778220583709229887925558073690275513463321801338386043664823718246189721829991326349593260262015383127495740562132626372965505150896005374490912844636517068696117534164173657369636762410462375206192323229547537987703846489985813725046672257134931160179714471792136894035110663465654688157660753917359889428812023660748279380868614614867872835588091210934292198272090279405962459365222325814717559628886294751786161008799712155754374373837286692143921522301884338596219541435364874941578793342171987699727676905667396803576044042765572839684671944837160547022974243014097119551013517128804888942731830085353603798064293968983005418019796704960442497606563158510661134631185870393813188249029658870184435468084885506400691906641543237473106295804111973470128947875595968819190124276723833485899937434306545549529733303362288432860793603719583844844037364529798723886943927595362991578028955829869160788834746974368602585078122327972006688376799099514569738215242975393411303162869624029378259896360312370098885739107071031078548153741230138673825830435556464333688118357046972507549105757130581136516097411285031618815496862304220947321273263786186130213208045003927591387772051861624573801325304014840476570078597839654070737906989188050135543759163610386742532573471902204105357449649153444229304081319741434622200780805749343194952661184510271095452932570368231965247396978358613155890320911991769046670596831055654064166881597530064258621579692588508537840225018479764427009690479955919761284313338818584816582115867316342386173869726276407281583998258865150653533267768540388644223626897311677440309393833231276363308677379455091060304752531275927724981285357618088142856331709408342946427826716180933310803336464474485051613017325189833035637265834259526693527101601008295571598856711279356198089488926417732929017881818663804734065039887254657308092918276824163212422501654137245655487721722124290595710373316031412488573092314597758601563968882940785846670043192537677576178180088755386955139690808787277132899275638170461072232709399477220202269650469914112113944929693110107590903336911128611699862977433707632381041630020346475462152305278118572261474195463542497814282038885445047141374106177083179506040192572537318315893952022432847534150517567659759773982374347247227509089910471431507883452053936956649552626171715886327457066650021883768233252352104526466146655877771452595220408985854799314580324675396975002654265596253004323519222762270668120315955437281732614112933082721063694965144284931115207290912906245412311132057652507618042884438662084297717726763454065326103362791704845259186938738657548759236750778283032964726001491932010866004803231330122375687254521049576874559234297867732596263844633531856929643158109483462442668698413907293412067171179892894403090288880838660163154903653055926524654917653879223768161863958538185618412172148521411243442449364234675545366269612428979707016505872900976436230618931453328062184060112213413879036355828123244713561861601945095287008735753371742990539256176347724761130021775737372020256254144992030186511147668821652241481734680037504397839411742674146597646625633750481030870987905500432216108139866956977892760628060899693643756229616887859242907849685206827419438408399592230925403100732081806275437538552537993374124148224696329087641552095154940194031298516760033205728267544931398562412788137707835841680013537358305644922672564297854494222517991132115956607014229502186130323216791853532167362837696242098426213537391716583459088090363128356665282453842229629435893573854809169321515941466220256438590311436749021430720770826556635182074926979150334879791366380842306353731411465709776974216037787970159524138020873498192538002990269800613481771044958110678299157461687842069553269693328821581627810370553072609208978099078646391689462826082940128320185798575304019994200203685615406619853596031723349411732165944094644964495376125220841740535004315974074740354505329044669417808536674864738826293703255152119967089724437949274351999164281055936289592743363070832065007131981694422415360017610512707946846638782473502953069728686357551143773454845608896614044163174058792165461022045069889754635300580963153689339414421666405874305955781479470810626971086322089551257220083653348652445881512819295912078018988976331555157809804211350065793385713515493309094005552162202557811132821013665501645794399035354655630343207836222241845367959986554593482367409238907315003384642019615625199989601802300477756803012592058040776201842573028068915766092781800345300282464896163025574581191563059549022676562216779851597594975436632494772531797081406978988547630936983173456678891384581864102434529500196859892665146386416717808714599925209494759167053680403114136741549386586389324291613485106954854190340680882318469798597240319598419390560549751872155041878440987448627800200773332970060613593726535038894215150167124145397286189146083423708314271732340922930133147092537898774704118459589518234516648928226136940321308696930390485633736573953252593761145871005217890751321854785111732861075573268221058719637080379887876209105141102920517398671317567078873069743303979775904243262240585123573212964955209702884933222147186482141037409989431144381778558563986208425843151214576637864902032370749894674883765867247943609456545456907069237864265969701242212485583483556115895572118821761379758959836674509393484956030710243322907550890524925191983776265997909558720633142297742934618994881824373958786837488325007188370935119180891982113403927323115377747385129555249951296223196379781662451577492570156978742961325142922953087425760306872789759624135001848087849945717602680195358608219971535299716162611930717128373379167179547312393396409844770101996614774999437104099077439043770821699433414825500771526838827358541855453276346901350584409323768721937084370961265398425031551903144788707483265088471933378014413148544386567268036419153465820906257586046131868110929901590101181109319424748452659433113735423888139901434808647812041061506807312957878486511700216680863324839205262515106632223941971679591583294908265180401600261916758320577933409002890367139054181925831497467234396910767011664005756472281023915106723279902271842518607400350842689093005137131735698473871621708906496


