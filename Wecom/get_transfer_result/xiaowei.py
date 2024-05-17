#!/usr/bin/env python3
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import re


"001583":"15806233720",
"010551":"15806233720",
"002663":"15806233720",
"004328":"15806233720",
"011021":"15806233720",
"001626":"15806233720",
"004398":"15806233720",
"004024":"15806233720",
"010673":"15806233720",
"010015":"15806233720",
"004327":"15806233720",
"002347":"15806233720",
"003165":"15806233720",
"004071":"15806233720",
"009907":"15806233720",
"010977":"15806233720",
"002530":"15806233720",
"004399":"15806233720",
"003986":"15806233720",
"008985":"15806233720",
"002349":"15806233720",
"003164":"15806233720",
"008437":"15806233720",
"010953":"15806233720",
"003560":"15806233720",
"010548":"15806233720",
"010952":"15806233720",
"010014":"15806233720",
"002532":"15806233720",
"001624":"15806233720",
"010132":"15806233720",
"010678":"15806233720",
"004366":"15806233720",
"003531":"15806233720",
"003910":"15806233720",
"009115":"15806233720",
"010549":"15806233720",
"003105":"15806233720",
"003984":"15806233720",
"002529":"15806233720",
"003104":"15806233720",
"004358":"15806233720",
"004441":"15806233720",
"004324":"15806233720",
"008626":"15806233720",
"009502":"15806233720",
"009501":"15806233720",
"771016":"15806233720",
"771015":"15806233720",
"001132":"15806233720",
"008653":"19351885966",
"002201":"19351885966",
"002840":"19351885966",
"002192":"19351885966",
"010098":"19351885966",
"002504":"19351885966",
"002841":"19351885966",
"010561":"19351885966",
"010562":"19351885966",
"004413":"19351885966",
"010870":"19351885966",
"002507":"19351885966",
"009093":"19351885966",
"009190":"19351885966",
"010651":"19351885966",
"009522":"19351885966",
"010649":"19351885966",
"010781":"19351885966",
"002838":"19351885966",
"004339":"19351885966",
"009757":"19351885966",
"008651":"19351885966",
"001575":"19351885966",
"009548":"19351885966",
"010097":"19351885966",
"002194":"19351885966",
"002505":"19351885966",
"009507":"19351885966",
"002502":"19351885966",
"002200":"19351885966",
"002195":"19351885966",
"002503":"19351885966",
"010117":"19351885966",
"010373":"19351885966",
"002506":"19351885966",
"001580":"19351885966",
"002501":"19351885966",
"010101":"19351885966",
"009506":"19351885966",
"001573":"19351885966",
"009758":"19351885966",
"002198":"19351885966",
"008872":"19351885966",
"002833":"19351885966",
"002508":"19351885966",
"004585":"19351885966",
"010996":"19351885966",
"003411":"19351885966",
"010567":"19351885966",
"001265":"17798662581",
"008357":"17798662581",
"009201":"17798662581",
"002190":"17798662581",
"002191":"17798662581",
"002835":"17798662581",
"004583":"17798662581",
"004584":"17798662581",
"002832":"17798662581",
"008790":"17798662581",
"010860":"17798662581",
"004059":"17798662581",
"011022":"17798662581",
"002964":"17798662581",
"008608":"17798662581",
"009510":"17798662581",
"009937":"17798662581",
"009944":"17798662581",
"010856":"17798662581",
"010858":"17798662581",
"004580":"17798662581",
"002199":"17798662581",
"010568":"17798662581",
"009756":"17798662581",
"010652":"17798662581",
"010850":"17798662581",
"010653":"17798662581",
"010976":"17798662581",
"004036":"17798662581",
"001570":"17798662581",
"009753":"17798662581",
"002196":"17798662581",
"009198":"17798662581",
"010563":"17798662581",
"010849":"17798662581",
"010975":"17798662581",
"001684":"17798662581",
"001579":"17798662581",
"010565":"17798662581",
"002837":"17798662581",
"010832":"17798662581",
"009200":"17798662581",
"010095":"17798662581",
"010783":"17798662581",
"008654":"17798662581",
"010569":"17798662581",
"004419":"17798662581",
"010564":"17798662581",
"009938":"17798662581",
"001745":"17798662581",
"010780":"17798662581",
"011190":"17798662581",
"009508":"17798662581",
"008607":"17798662581",
"002839":"17798662581",
"010782":"17798662581",
"009373":"17798662581",
"003412":"17798662581",
"004194":"17798662581",
"002116":"14751198479",
"009633":"14751198479",
"003609":"14751198479",
"003996":"14751198479",
"004007":"14751198479",
"002864":"14751198479",
"004588":"14751198479",
"010984":"14751198479",
"004420":"14751198479",
"010626":"14751198479",
"003917":"14751198479",
"004341":"14751198479",
"003916":"14751198479",
"002422":"14751198479",
"003982":"14751198479",
"004338":"14751198479",
"010684":"14751198479",
"002862":"14751198479",
"004590":"14751198479",
"004323":"14751198479",
"004258":"14751198479",
"002865":"14751198479",
"003342":"14751198479",
"010682":"14751198479",
"004326":"14751198479",
"002747":"14751198479",
"004404":"14751198479",
"004703":"14751198479",
"010885":"14751198479",
"011060":"14751198479",
"002303":"14751198479",
"010624":"14751198479",
"003620":"14751198479",
"004390":"14751198479",
"003606":"14751198479",
"004282":"14751198479",
"003971":"14751198479",
"003344":"14751198479",
"003366":"14751198479",
"003983":"14751198479",
"004141":"14751198479",
"010772":"14751198479",
"010675":"14751198479",
"003564":"14751198479",
"010600":"14751198479",
"004521":"14751198479",
"002745":"14751198479",
"008781":"18015120486",
"009919":"18015120486",
"010230":"18015120486",
"009382":"18015120486",
"008968":"18015120486",
"009388":"18015120486",
"008983":"18015120486",
"011015":"18015120486",
"003142":"18015120486",
"004651":"18015120486",
"002947":"18015120486",
"008980":"18015120486",
"004517":"18015120486",
"010110":"18015120486",
"009385":"18015120486",
"001850":"18015120486",
"010112":"18015120486",
"001845":"18015120486",
"008613":"18015120486",
"009390":"18015120486",
"001847":"18015120486",
"004040":"18015120486",
"004373":"18015120486",
"002539":"17798660253",
"010127":"17798660253",
"004023":"17798660253",
"004011":"17798660253",
"004041":"17798660253",
"004103":"17798660253",
"003731":"17798660253",
"004382":"17798660253",
"004422":"17798660253",
"001871":"17798660253",
"009624":"17798660253",
"010586":"17798660253",
"003573":"17798660253",
"003575":"17798660253",
"003631":"17798660253",
"010166":"15806233050",
"002162":"15806233050",
"010584":"15806233050",
"010755":"15806233050",
"002534":"15806233050",
"004334":"15806233050",
"004578":"15806233050",
"010598":"15806233050",
"002157":"15806233050",
"003903":"15806233050",
"003622":"15806233050",
"003621":"15806233050",
"004335":"15806233050",
"010725":"15806233050",
"003333":"15806233050",
"010751":"15806233050",
"010709":"15806233050",
"004010":"15806233050",
"004107":"15806233050",
"002476":"15806233213",
"002989":"15806233213",
"003973":"15806233213",
"003995":"15806233213",
"004274":"15806233213",
"002152":"15806233213",
"004315":"15806233213",
"004593":"15806233213",
"004254":"15806233213",
"010158":"15806233213",
"002481":"15806233213",
"003532":"15806233213",
"010831":"15806233213",
"004098":"15806233213",
"004637":"15806233213",
"004253":"15806233213",
"002480":"15806233213",
"001606":"15806233213",
"003601":"15806233213",
"004360":"15806233213",
"004283":"15806233213",
"004507":"15806233213",
"001682":"15806233213",
"003600":"15806233213",
"004106":"15806233213",
"004281":"15806233213",
"001592":"15806233213",
"003365":"15806233213",
"010752":"15806233213",
"003998":"15806233213",
"004701":"15806233213",
"001687":"15806233213",
"002614":"15806233213",
"010505":"15806233213",
"003938":"15806233213",
"004102":"15806233213",
"004508":"15806233213",
"004573":"15806233213",
"010294":"15806233213",
"001986":"15806233213",
"010838":"15806233213",
"003962":"15806233213",
"002603":"15806233213",
"004073":"15806233213",
"010839":"15806233213",
"010744":"15806233213",
"001690":"15806233213",
"002994":"15806233213",
"010594":"15806233213",
"004250":"15806233213",
"010018":"15806233213",
"001266":"15806232833",
"009082":"15806232833",
"004275":"15806232833",
"003735":"15806232833",
"003426":"15806232833",
"004661":"15806232833",
"010340":"15806232833",
"002997":"15806232833",
"002527":"15806232833",
"002526":"15806232833",
"004717":"15806232833",
"002991":"15806232833",
"003967":"15806232833",
"010745":"15806232833",
"004038":"15806232833",
"003636":"15806232833",
"003805":"15806232833",
"002986":"15806232833",
"002150":"15806232833",
"003008":"15806232833",
"001605":"15806232833",
"004577":"15806232833",
"002370":"15806232833",
"010823":"15806232833",
"010674":"15806232833",
"010525":"15806232833",
"009292":"15806233253",
"009279":"15806233253",
"008776":"15806233253",
"002125":"15806233253",
"004069":"15806233253",
"004163":"15806233253",
"011172":"15806233253",
"002154":"15806233253",
"010992":"15806233253",
"003920":"15806233253",
"004132":"15806233253",
"004594":"15806233253",
"004715":"15806233253",
"009076":"17706233956",
"001075":"17706233956",
"003724":"17706233956",
"002391":"17706233956",
"004596":"17706233956",
"004644":"17706233956",
"004506":"17706233956",
"004587":"17706233956",
"009333":"18262118135",
"001688":"18262118135",
"009095":"18262118135",
"009278":"18262118135",
"003205":"18262118135",
"010543":"18262118135",
"004499":"18262118135",
"010873":"18262118135",
"004095":"18262118135",
"004322":"18262118135",
"002790":"18262118135",
"002788":"18262118135",
"004003":"18262118135",
"004199":"18262118135",
"003970":"18262118135",
"001713":"18262118135",
"002792":"18262118135",
"003504":"18262118135",
"010874":"18262118135",
"003803":"18262118135",
"010687":"18262118135",
"004504":"18262118135",
"004435":"18262118135",
"010092":"18262118135",
"003212":"18262118135",
"002276":"18262118135",
"001980":"18262118135",
"001620":"18262118135",
"002791":"18262118135",
"003251":"18262118135",
"010702":"18262118135",
"004344":"18262118135",
"004592":"18262118135",
"009068":"17706238475",
"008991":"17706238475",
"001671":"17706238475",
"002843":"17706238475",
"003643":"17706238475",
"010560":"17706238475",
"010846":"17706238475",
"004317":"17706238475",
"004652":"17706238475",
"003975":"17706238475",
"002023":"17706238475",
"001955":"17706238475",
"003277":"17706238475",
"002006":"17706238475",
"002486":"17706238475",
"004100":"17706238475",
"001616":"17706238475",
"003450":"17706238475",
"010877":"17706238475",
"003481":"17706238475",
"003927":"17706238475",
"003452":"17706238475",
"001680":"17706238475",
"010871":"17706238475",
"003720":"17706238475",
"010872":"17706238475",
"003592":"17706238475",
"004050":"17706238475",
"001598":"17706238475",
"002155":"17706238475",
"003935":"17706238475",
"004367":"17706238475",
"004267":"17706238475",
"010847":"17706238475",
"002847":"17706238475",
"004716":"17706238475",
"001597":"17706238475",
"001665":"17706238475",
"002848":"17706238475",
"003298":"17706238475",
"003641":"17706238475",
"010876":"17706238475",
"010083":"17706238475",
"001594":"17706238475",
"004131":"17706238475",
"003969":"17706238475",
"004052":"17706238475",
"010892":"17706238475",
"003988":"17706238475",
"002844":"17706238475",
"010607":"17706238475",
"004733":"17706238475",
"009465":"15806232719",
"010275":"15806232719",
"009734":"15806232719",
"003506":"15806232719",
"009731":"15806232719",
"003887":"15806232719",
"009142":"15806232719",
"009741":"15806232719",
"004639":"15806232719",
"003921":"15806232719",
"009733":"15806232719",
"003497":"15806232719",
"004688":"15806232719",
"003900":"15806232719",
"004072":"15806232719",
"010664":"15806232719",
"004681":"15806232719",
"010647":"15806232719",
"003922":"15806232719",
"004415":"15806232719",
"009723":"15806232719",
"004650":"15806232719",
"010840":"15806232719",
"009728":"15806232719",
"004575":"15806232719",
"003895":"15806232719",
"010272":"15806232719",
"003913":"15806232719",
"003902":"15806232719",
"010266":"15806232719",
"004179":"15806232719",
"009993":"15806232719",
"001263":"15806232719",
"001104":"15806232719",
"008770":"18012227699",
"009399":"18012227699",
"002854":"18012227699",
"003075":"18012227699",
"010740":"18012227699",
"003987":"18012227699",
"004150":"18012227699",
"003889":"18012227699",
"003730":"18012227699",
"004241":"18012227699",
"002856":"18012227699",
"002852":"18012227699",
"004242":"18012227699",
"004096":"18012227699",
"004407":"18012227699",
"003888":"18012227699",
"002886":"18012227699",
"003077":"18012227699",
"004271":"18012227699",
"003909":"18012227699",
"004142":"18012227699",
"004259":"18012227699",
"009126":"15806233102",
"010051":"15806233102",
"010231":"15806233102",
"009533":"15806233102",
"010894":"15806233102",
"010053":"15806233102",
"003615":"15806233102",
"003990":"15806233102",
"009761":"15806233102",
"010347":"15806233102",
"010059":"15806233102",
"008620":"15806233102",
"009765":"15806233102",
"010608":"15806233102",
"009531":"15806233102",
"003980":"15806233102",
"009128":"15806233102",
"010058":"15806233102",
"003944":"15806233102",
"010346":"15806233102",
"002381":"15806233102",
"002615":"15806233102",
"004133":"15806233102",
"010409":"15806233102",
"009766":"15806233102",
"009791":"15806233102",
"771161":"15806233102",
"002383":"18662324395",
"010379":"18662324395",
"003381":"18662324395",
"010784":"18662324395",
"004502":"18662324395",
"004503":"18662324395",
"004265":"18662324395",
"003977":"18662324395",
"003382":"18662324395",
"004236":"18662324395",
"009554":"15806232783",
"009549":"15806232783",
"010418":"15806232783",
"009550":"15806232783",
"003424":"15806232783",
"010388":"15806232783",
"010392":"15806232783",
"009799":"15806232783",
"003182":"15806232783",
"003891":"15806232783",
"010416":"15806232783",
"003898":"15806232783",
"009107":"15806232783",
"009808":"15806232783",
"010377":"15806232783",
"003941":"15806232783",
"009552":"15806232783",
"009809":"15806232783",
"004372":"15806232783",
"004501":"15806232783",
"003380":"15806232783",
"003350":"15806232783",
"010376":"15806232783",
"010069":"15806232783",
"002362":"15806232783",
"009807":"15806232783",
"010385":"15806232783",
"009813":"15806232783",
"009470":"15806232869",
"010370":"15806232869",
"010068":"15806232869",
"010362":"15806232869",
"003432":"15806232869",
"003940":"15806232869",
"002558":"15806232869",
"003125":"15806232869",
"002365":"15806232869",
"003113":"15806232869",
"002674":"15806232869",
"009998":"15806232869",
"002857":"15806232869",
"003354":"15806232869",
"004207":"15806232869",
"003966":"15806232869",
"004359":"15806232869",
"009743":"18651363809",
"009999":"18651363809",
"008650":"18651363809",
"002817":"18651363809",
"003881":"18651363809",
"010553":"18651363809",
"004640":"18651363809",
"010698":"18651363809",
"002812":"18651363809",
"003577":"18651363809",
"002816":"18651363809",
"010699":"18651363809",
"003943":"18651363809",
"004343":"18651363809",
"003626":"18651363809",
"002818":"18651363809",
"002901":"18651363809",
"004352":"18651363809",
"002813":"18651363809",
"002811":"18651363809",
"002851":"18651363809",
"010556":"18651363809",
"010700":"18651363809",
"010897":"18651363809",
"003978":"18651363809",
"004444":"18651363809",
"010557":"18651363809",
"009049":"17798660283",
"009312":"17798660283",
"002103":"17798660283",
"003524":"17798660283",
"003705":"17798660283",
"010028":"17798660283",
"002104":"17798660283",
"004391":"17798660283",
"002498":"17798660283",
"010969":"17798660283",
"001246":"17798660283",
"009659":"17798660283",
"009671":"17798660283",
"009788":"17798660283",
"003007":"17798660283",
"009673":"17798660283",
"004224":"17798660283",
"011133":"17798660283",
"011020":"17798660283",
"010947":"17798660283",
"003525":"17798660283",
"003939":"17798660283",
"004417":"17798660283",
"010247":"17798660283",
"010296":"17798660283",
"003015":"17798660283",
"001940":"17798660283",
"004257":"17798660283",
"004248":"17798660283",
"004074":"17798660283",
"004405":"17798660283",
"004520":"17798660283",
"010260":"17798660283",
"010297":"17798660283",
"009221":"17798660283",
"003968":"17798660283",
"010250":"17798660283",
"010257":"17798660283",
"003003":"17798660283",
"001943":"17798660283",
"010256":"17798660283",
"003523":"17798660283",
"004418":"17798660283",
"004643":"17798660283",
"010261":"17798660283",
"004203":"17798660283",
"002495":"17798660283",
"001611":"17798660283",
"010295":"17798660283",
"004228":"17798660283",
"010869":"17798660283",
"010669":"17798660283",
"004342":"17798660283",
"010950":"17798660283",
"001074":"17798660283",
"001942":"17798660283",
"004727":"17798660283",
"009830":"18051539136",
"004154":"18051539136",
"004262":"18051539136",
"004255":"18051539136",
"004368":"18051539136",
"004427":"18051539136",
"004433":"18051539136",
"004138":"18051539136",
"004369":"18051539136",
"004682":"18051539136",
"004687":"18051539136",
"004707":"18051539136",
"010128":"17706238426",
"003284":"17706238426",
"003428":"17706238426",
"010728":"17706238426",
"010732":"17706238426",
"003740":"17706238426",
"004617":"17706238426",
"004708":"17706238426",
"010623":"17706238426",
"003175":"17706238426",
"003616":"17706238426",
"004000":"17706238426",
"004139":"17706238426",
"004336":"17706238426",
"009299":"15806232707",
"002735":"15806232707",
"010991":"15806232707",
"010997":"15806232707",
"004062":"15806232707",
"010761":"15806232707",
"003348":"15806232707",
"004054":"15806232707",
"004025":"15806232707",
"002733":"15806232707",
"002980":"15806232707",
"004039":"15806232707",
"004019":"15806232707",
"010535":"15806232707",
"002734":"15806232707",
"010696":"15806232707",
"004363":"15806232707",
"009230":"15806233616",
"001954":"15806233616",
"009294":"15806233616",
"002141":"15806233616",
"003001":"15806233616",
"004599":"15806233616",
"009866":"15806233616",
"004005":"15806233616",
"010116":"15806233616",
"010993":"15806233616",
"011169":"15806233616",
"002616":"15806233616",
"009248":"15806233616",
"004710":"15806233616",
"010074":"15806233616",
"001844":"15806233616",
"003647":"15806233616",
"003919":"15806233616",
"002464":"15806233616",
"010672":"15806233616",
"010663":"15806233616",
"004505":"15806233616",
"004009":"15806233616",
"004206":"15806233616",
"010024":"15806233616",
"010671":"15806233616",
"003526":"15806233616",
"010842":"15806233616",
"004104":"15806233616",
"001953":"15806233616",
"008764":"17798660206",
"009229":"17798660206",
"001950":"17798660206",
"010826":"17798660206",
"003930":"17798660206",
"002485":"17798660206",
"003161":"17798660206",
"004205":"17798660206",
"003603":"17798660206",
"009859":"17798660206",
"003958":"17798660206",
"001951":"17798660206",
"003604":"17798660206",
"002624":"17798660206",
"011005":"17798660206",
"010621":"17798660206",
"004576":"17798660206",
"003737":"17798660206",
"011039":"17798660206",
"003602":"17798660206",
"001996":"17798660206",
"009858":"17798660206",
"004572":"17798660206",
"001993":"17798660206",
"003726":"17798660206",
"010625":"17798660206",
"010994":"17798660206",
"003392":"17798660206",
"009171":"15151699607",
"002096":"15151699607",
"010659":"15151699607",
"010875":"15151699607",
"010968":"15151699607",
"003914":"15151699607",
"004318":"15151699607",
"002953":"15151699607",
"003911":"15151699607",
"010812":"15151699607",
"010985":"15151699607",
"010973":"15151699607",
"002519":"15151699607",
"003329":"15151699607",
"010806":"15151699607",
"004237":"15151699607",
"004437":"15151699607",
"004395":"15151699607",
"010552":"15151699607",
"003489":"15151699607",
"010989":"15151699607",
"004696":"15151699607",
"002955":"15151699607",
"003327":"15151699607",
"010958":"15151699607",
"004316":"15151699607",
"003256":"15151699607",
"003936":"15151699607",
"010443":"15806231855",
"009909":"15806231855",
"002516":"15806231855",
"002514":"15806231855",
"010879":"15806231855",
"004068":"15806231855",
"011004":"15806231855",
"004402":"15806231855",
"011000":"15806231855",
"004346":"15806231855",
"004264":"15806231855",
"002056":"15806231855",
"003495":"15806231855",
"010868":"15806231855",
"010747":"15806231855",
"002873":"15806231855",
"004362":"15806231855",
"004037":"15806231855",
"010668":"15806231855",
"004347":"15806231855",
"002342":"15806231855",
"010679":"15806231855",
"003558":"15806231855",
"004361":"15806231855",
"002043":"15806231855",
"003961":"15806231855",
"004202":"15806231855",
"001926":"15806231855",
"010680":"15806231855",
"001813":"15806231855",
"010666":"15806231855",
"004445":"15806231855",
"010748":"15806231855",
"004060":"15806231855",
"003928":"15806231855",
"003154":"15806231855",
"003180":"15806231855",
"004429":"15806231855",
"010667":"15806231855",
"004201":"15806231855",
"010134":"15806231879",
"009073":"15806231879",
"010223":"15806231879",
"003198":"15806231879",
"010138":"15806231879",
"010890":"15806231879",
"003151":"15806231879",
"010628":"15806231879",
"003947":"15806231879",
"003912":"15806231879",
"010899":"15806231879",
"004589":"15806231879",
"010239":"15806231879",
"003965":"15806231879",
"004089":"15806231879",
"004511":"15806231879",
"010342":"15806231879",
"010855":"15806231879",
"010844":"15806231879",
"010878":"15806231879",
"010854":"15806231879",
"001655":"15806231879",
"003158":"15806231879",
"003985":"15806231879",
"004647":"15806231879",
"003945":"15806231879",
"003157":"15806231879",
"010865":"15806231879",
"003993":"15806231879",
"004035":"15806231879",
"011042":"15806231879",
"004591":"15806231879",
"010435":"15806231879",
"010866":"15806231879",
"004231":"15806231879",
"004672":"15806231879",
"002424":"15806231879",
"004319":"15806231879",
"008820":"15806231879",
"008556":"15806231879",
"002208":"15806231879",
"002623":"15806231879",
"001590":"17706239406",
"002515":"17706239406",
"010814":"17706239406",
"001859":"17706239406",
"004135":"17706239406",
"004513":"17706239406",
"010864":"17706239406",
"003915":"17706239406",
"004252":"17706239406",
"004396":"17706239406",
"003443":"17706239406",
"003795":"17706239406",
"003942":"17706239406",
"004663":"17706239406",
"003960":"17706239406",
"010843":"17706239406",
"002546":"17706239406",
"002654":"17706239406",
"003517":"17706239406",
"004312":"17706239406",
"004385":"17706239406",
"004595":"17706239406",
"010816":"17706239406",
"004099":"17706239406",
"001919":"17706239406",
"010815":"17706239406",
"003964":"17706239406",
"004646":"17706239406",
"003156":"17706239406",
"001927":"17706239406",
"004731":"17706239406",
"008602":"19906234681",
"001916":"19906234681",
"004108":"19906234681",
"001912":"19906234681",
"002542":"19906234681",
"010988":"19906234681",
"003124":"19906234681",
"004648":"19906234681",
"001910":"19906234681",
"001913":"19906234681",
"010043":"19906234681",
"003185":"19906234681",
"004193":"19906234681",
"003187":"19906234681",
"001908":"19906234681",
"010613":"19906234681",
"004635":"19906234681",
"003117":"19906234681",
"001907":"19906234681",
"010614":"19906234681",
"003123":"19906234681",
"004134":"19906234681",
"003794":"19906234681",
"004182":"19906234681",
"004353":"19906234681",
"004723":"19906234681",
"001269":"18262101019",
"009571":"18262101019",
"002177":"18262101019",
"004667":"18262101019",
"004515":"18262101019",
"009563":"18262101019",
"009880":"18262101019",
"004204":"18262101019",
"004412":"18262101019",
"004425":"18262101019",
"004263":"18262101019",
"004679":"18262101019",
"009588":"18262101019",
"010579":"18262101019",
"004075":"18262101019",
"004239":"18262101019",
"004256":"18262101019",
"004080":"18262101019",
"004408":"18262101019",
"004397":"18262101019",
"004414":"18262101019",
"004678":"18262101019",
"008493":"18051539069",
"009608":"18051539069",
"010161":"18051539069",
"008850":"18051539069",
"010157":"18051539069",
"010156":"18051539069",
"004325":"18051539069",
"002556":"18051539069",
"003623":"18051539069",
"004709":"18051539069",
"009607":"18051539069",
"002168":"18051539069",
"004329":"18051539069",
"004645":"18051539069",
"009604":"18051539069",
"002555":"18051539069",
"010749":"18051539069",
"008644":"18051539069",
"010150":"18051539069",
"003931":"18051539069",
"002554":"18051539069",
"004600":"18051539069",
"002165":"18051539069",
"004514":"18051539069",
"010147":"18051539069",
"002163":"18051539069",
"010580":"18051539069",
"003885":"18051539069",
"002164":"18051539069",
"010582":"18051539069",
"004638":"18051539069",
"008645":"18051539069",
"009301":"15806232705",
"009298":"15806232705",
"010035":"15806232705",
"003901":"15806232705",
"003431":"15806232705",
"004370":"15806232705",
"002181":"15806232705",
"002905":"15806232705",
"003570":"15806232705",
"002949":"15806232705",
"009610":"15806232705",
"010046":"15806232705",
"004232":"15806232705",
"009887":"15806232705",
"004416":"15806232705",
"010042":"15806232705",
"002183":"15806232705",
"009881":"15806232705",
"009611":"15806232705",
"003569":"15806232705",
"004013":"15806232705",
"004381":"15806232705",
"009882":"15806232705",
"002185":"15806232705",
"009879":"15806232705",
"009613":"15806232705",
"010893":"15806232705",
"002869":"15806232705",
"004371":"15806232705",
"009596":"18706239226",
"008600":"18706239226",
"008578":"18706239226",
"010315":"18706239226",
"002170":"18706239226",
"009574":"18706239226",
"009889":"18706239226",
"003755":"18706239226",
"010962":"18706239226",
"004140":"18706239226",
"003756":"18706239226",
"008861":"18706239226",
"010326":"18706239226",
"010961":"18706239226",
"004409":"18706239226",
"008854":"18706239226",
"003754":"18706239226",
"003118":"18706239226",
"009578":"18706239226",
"004410":"18706239226",
"004266":"18706239226",
"004434":"18706239226",
"010998":"18706239226",
"004403":"18706239226",
"004700":"18706239226",
"010303":"18706239226",
"003757":"18706239226",
"009890":"18706239226",
"004240":"18706239226",
"004260":"18706239226",
"004668":"18706239226",
"004705":"18706239226",
"009520":"18706239226",
"002172":"18706239226",
"002541":"18706239226",
"010972":"18706239226",
"003119":"18706239226",
"004516":"18706239226",
"010960":"18706239226",
"004152":"18706239226",
"004714":"18706239226",