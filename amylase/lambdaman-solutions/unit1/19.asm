-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I16345

-- Pass the encoded string
B$

-- Make the recursive function of Decode
B$
  Lf B$ Lx B$ vf B$ vx vx Lx B$ vf B$ vx vx -- Fix
  -- Decode :: Self -> String -> String
  -- Decodes the first entry in the source then recursively process the rest.
  Ld Ls
    ? ( B= vs @I4 )
      S
      B.
        BT @I1 BD (B* @I1 B% vs @I4) @SRLDU -- Decode the first entry
        (B$ vd (B/ vs @I4)) -- Process the rest

-- Encoded string
@I22341768722715741855999961646231935592182931858015598568012010583698251085921236329348592238646714837079855330796617533684898098268020905502632553894734911813738027778575315437546620658299261000293405820414679243687903585597641186362716645198347946136971478105331350998731188098557655182006654450667374523769080483697592491564703045565643391822366336351771520334394602009364579188816994589139119524048245916020479611551031920498742981539543276919168209860293373321757642950453949730234522786799079487740365000169960820296813451714841975172671964071383617170310290251689877876222275533521604787382032763091763134470540978095118779677550232710596482956801576325596765290434107981068580581368562789784926364840922745102456994249188524568036813852449611058497541543646444029528363993825117167849700974213573454942991966497422350764280048983886513209949988493762444008371920817898703290056114059484973182194910808134854507711122049274433393004840640538373616455025384702859441177818588329594452480656671068010481871788011768042861570453146122896837914768650292430741365388716598177925916928124815325647210497011222094310641682394725340143875147778373838827085513318905618079979620210322054201142413672049292407797398861430624794238732501705782077317072230812001461735119932455252555007517119815612382524788140981043856879097412599064309264160447118056249172469091877577209924645666503260513788180539497681922639105847891907385672371558334514177683538075010297556216813975274067702301475817019508224289331200229791684121174526455954540161091619328580115340063424574110690149432068178812709439310957960333658864305132285422367608821630340783630147030859415230510678864541956394218204615039049840188649648997765346434791445498990340606425458693752662683373176581927069328025918061129838225589011257315974386800754303249091756758829396335650399772728907166854148556562961809702870580486641652620203180589658603511992481990621949341315933585489134076655535561343351979109241920844317827819239395673060411303595260080164864551078312747900718980312157965401323338532927601841986070283556000130635539287965643181268852855366648463403130852739169351095157576697144828186401269298316875842684539214109361907575935924926851604826013848545104523185240275851532160068606324476409010700699499953088968982865216177911398566036126593122593207253123759294117832171640923781365717366030083573991149416277290773537079495455118584984553703038281490860529898926792495076338830911245699902138992859298412062077755047743238418332820707988560996067702221101329447084916846211860824751713126614709972787318272416225576160798445342165179374493876150089852208714346770159641058928566929033095992743008553211087776211597516038642854389825931274449709707549774042742102169772425715576672414064525924676012093687690732314372286265662147268884900413114399691018512074643272659793297104169991895392261372666818477161562419943421000896556442963476137094722875190890263607212712877940896050615398424949068853106585426863403794301911538761271229832548332984677904589412198624679740288988203256012380094902166088463384207651072361634790631878839340363264736078917060348866490560194569799226408590564555716696547430415016453373484887088899165293674806941274148530993831943306663314005868795973855010822911685283840931166509584741467130485610058254470511514982926404323937450838756345527786986943823906814127038449874522761958972944129851562383016534457938377130140018492082202367537975680820942544534480848298736320090245419361046029643208470415154223179172756469488456831263771564067554935151387100480136566276867545421527060324714413569422923318933779718713561106582903809353801458376492976130100585049861096106571659476921861723870658331353401742744086503434563819386892895696093120575250883757535855104744804811064723476366632856889032863200264516230430590955305062851228210017646128779666715940598879502866787802054168681842918534147300311642647373537666380723503323880391452708308096907807550421316474521139952356648238478612788708695811125418355120564917486831795423568081916044357738734016026483745319671925012067513484334936402852424862719608011194505970180314437331013048010639588306326520052090488750437058381661190162953068853554606920828128979707416004303408146942530899316770717462902388392871892556273768747328465600442922823233006332923483778861005768923449684241694998091039088361534200895858911658960669786819563795176596262126576381253103741324029690053455708947127402239249009885750209061419365531805733575956601678209642242811838000852271200460610461338115399836409114060881297552191887406292286628994354797404901997393782021117940415932618790592441509828815098208160931105161124426844202766224899382744999651270979252826676677885741199291924915680179040823862433608733541165006248244302778013525696583276187837329844322234013332507422145788926768043528075846368219208904649302151916835800397850445433835034608971723993461239239738217273062919526531170850211956684110574047380169259060363354280315887864739313316507736581813753536544108658334553156303799773768168065931119145085543095894805823328998154915055533053954807377600556932716483132344473848152943765656679930404232930796298161554228898950775096440396401230266335674538704376916019500478520601385843143476924357110001414757087511588376985656851512739307496049847398468431898407089907334933960148563173714296857705088523269841369806699874197980986766588784481245098156486677526172072516224144799754489474374406979316557210571698236131518027828113850973560559319974559187506121969070227198204387887257020204059424885232620683075172101815205789683158860735383977136773051747714478958878886876523160885040136824052453165560777318858553044807696319406217603274401743611739880903071511597708462682674093886074048917029543487912433445482553330461941151671771956339671880171615724581281862006606494141825234961626682114347587375096440432556692143010991521380485340677782845139403217029563672870603972224086380542384625457765305436693933214546115738374036260801475925506217610382238634057288538112378366539245345248537428954043783902836019022163753930108577972565311044174664752059529382641993337850972419631601849885757566461552860672300224562094359969824455810057183232930735406603385480317120708360936261524351462300881641271584207467020406281190324010198668407116053988414160833355056676655382332584248180224916435433738614456794865407513760317913964544904050178855385154397745641575507709812405050537180984848628966365496772006504041034838483056567871319588986515209805621883596905728144824078339182398605319945965736994397574339516279030386435185964216045291612713573068798799689689037268450444146161319947580686881230128117430092802457558521072748132004926936953710674634789738949115536416993666209695887323775958793581271907462056872685792746250406666375215062509602029735854504008170154380315476362334993389587693971940055257667808446093194189536240676241296106717902910236794294343522918700872367460832211467468747736912914521503432128268402568068202458270274535072322952050902670820768181405573067038321909029811382207056986246204191056471084160301795118094790378177342645776567186609850961106560059130708239784451265883433361358080385733689178245278435945365245888696057240466650092031091212466225017142345209571596130789720056733113492580317807415449355018729910374830274202589688701215635591444053771194895325654559591920732691986559917335615259727942390816641779421121513946763623964605248814623069120846834823458584039021918726198766688901556195789724631275528851356493126690037476819707594984091458501629307004394975077658520945113554770763970771665233644916965446021702112253605869140701836210900929568832971467896684505939328650190942955965473535934074898380621150534587542439187217436716830310385910720284121907294806620122803150806244550489334407680587338783368548877406409273523786017657679730871041080603570784597349913244025400180190186547184444000129233668901022676541817968170034591599288610785504006311011730492992126444939476840606798834358787978344623704540225956356956088161214593145005012767166150214923217421686306835829825895398912436856015351867367580157079885898777142388506091033924113847113772118611237519693841096393295472704172107017581298011834224779136733201327516379555879736888612027253173602546834316676741521616670292117833769841066682665634663452081840317346871750858542800110354686289653347173196061906273792773042817806641979552433833112656962304478022086791385717777140783950824551022147406427126363661073082137049034009776499264318299267370156915359405725916627329302162190917290104760238984077406784748463693663971980058956000450794525911766237669739144033819083938502703123913612298011739313171930630645834097106193293564418204952705566573883101492686229601101186074685204770375314753090744808869522024319319327314104143064373076949268620974085558549099034214352637137910009830545628147497413278555062516228144068011214733340848227496649130978645313606696649158991792306737182702794140714981152670511370358980896392072155808677731919183542161316330541615588445033361842331404670065671380784947394868446849221037739708709040350554818820208425815157605179301018650207718974386874769071468208836053891601841882599867716091837888220326807349843590114068658186706855130440176588456583563023979178688206906818948936245662276857028658617084364395607378976017424659073011402878694868106755259618423764910176028900832928471955635227900244544513093825756868661213197455845685631879718234041050886089568016975460584222962406394366470504203186055290457354954454509776305150847765803840639150794948348141887593534389023761487172390622711623309256802469520723570893718027790964631190995877539373061979856844953312846952089750939974854392330060222062187222061987071473063763314097641126399889484184083199095145868973718204125127008370234452079947897426679060491537067129438208

