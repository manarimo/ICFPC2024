-- base64 format: [encoded: ICFP string] [prefix: ICFP integer]
-- encoded string is decoded to LRDU string and then first prefix characters are taken

-- Finally take prefix
BT

-- String length
@I3578

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
        ? ( B= vs @I337 )
          S
          B.
            BT @I8 BD (B* @I8 B% vs @I337) v# -- Decode the first entry
            (B$ vd (B/ vs @I337)) -- Process the rest

-- Expand the compressed dictionary
-- The compressed data must contain a non-zero sentinel in the end.
BT @I2696
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
@I1429102329893608026549821896460776358103327276797210136318030170828560568481867889194033939016028907682609380599276499976230949101300683356520323619589774599945087953726267394483252180290231577665700039085424360852297134936214938349817626437521994735896745061079612969278617479966373087762109839619461129153363490721316126485138453776233724668063478544078295367739834326506755077636800545645561204428087087314570430639080451293471597109697648837935510012659941275117930657285871850169709305360193548281612920493010161805362780503795970248058015857057778746690194313554454843620030190056372315201855661930038028252476958937866784663705492158135668901827952445263568079017768071189836937428688235480862848367107382840919544564751163951115964147294465462732391659400817192400173206840128295352550446099124843248370169954555765140010187366022069851899693914039319208341390789444685252385012832274772319265395446807640766438468052207920695331763965656443327882257216309328111290613760759673101596232774705219869542753715381854755558042594431047853707270340897743599573710425067525846982759101406684860153638893771733799056205347307245178933210712517637511154931708491051019999179482719514883919991172372616541104413066719960972643668310907833479013365616283418715000842239225314762433106215791214558283578217915697234504029967015608000187918093289346466479121572477182956356218154787143475255268888802507678997169665662501689497950241614376260406627860824274255527334101073934292421074908296977774682185535613785323676943925805043037734396699094763080179359650382374864296458670151789755813199808875136981381734150208999983327914

-- Encoded string
@I8053667900899621464448365520224980129757033593450572779996016616625779911896809298843631534200706668531448653478300118199742149881781095779963903982933856817715661656427954929287930057251765556112249861036218470389065029871363352029561910848293223276057800786640622013017880313742333873434440001577208348853073778740374148027681461089086094126100928334853780752889083854135440447251256905687611587717823900010172935787816062936164544182955644446376801489184039141328918359478661160796742505796919682839266503210124672770410687196281268946988094451949388224108797216444862753353895782147108360056390943675539129710326840848441314478835207900265426660846546872660561432776219258846347436813921046765351744270468277051648728986133594519791602778833820878881769817638476800352461889340855752787417949508869106481375750266135765741844291648710691870251473229198749013580588471495597481152545833759778678032883618479294172424795861826383033761188785237754424073537394480219843406172967274956054231781410915041262074336871817163005713039111276356493678002954047731045595439843425290730431154965393531970582723546653854661720281389381410685155

