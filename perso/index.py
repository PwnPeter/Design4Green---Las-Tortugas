#!/usr/bin/python3
# -*- coding: utf-8 -*

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()


q1 = {
	"id" : 1,
	"question" : "1. In which sector of activity is your company active? (linked with your APE code)",
	"type" : 1,
	"answer" : ["Industry",
				"Business",
				"Information and communication",
				"Other services activity",
				"All other activities (financial, agricultural activities ...)",
				"Construction",
				"Public sector",
				"Specialized",
				"Scientific and Technical or Administrative and Support Services Activities",
				"Real estate"
				]
	}

q2 = {
	"id" : 2,
	"question" : "2. What is the number of employees in your company on 18/12/31?",
	"type" : 1,
	"answer" : [
				"0",
				"1 to 2",
				"3 to 9",
				"10 to 49",
				"50 to 249",
				"250 to 4999",
				"More than 5000"
				]
	}

q3 = {
	"id" : 3,
	"question" : "3. What is the turnover of your company in the last fiscal year? (or annual budget for Public sector)",
	"type" : 1,
	"answer" : [
				"0 to 100K€",
				"100 to 500 K€",
				"500 to 2 M€",
				"2 to 10 M€",
				"10 to 50 M€",
				"More than 50 M€"
				]
	}

q4 = {
	"id" : 4,
	"question" : "4. Do you develop digital services for internal or external use (sales to customers)?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No"
				]
	}

q5 = {
	"id" : 5,
	"question" : "5. What is the number of users of your digital services?",
	"type" : 2,
	"answer" : "text"
	}

q6 = {
	"id" : 6,
	"type" : 5,
	"question" : "6. Do you apply the rules and best practices for digital accessibility?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q7 = {
	"id" : 7,
	"type" : 5,
	"question" : "7. Have you optimized the states and printouts in your application tools (reduced number of pages when printing, ink consumption ...)?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q8 = {
	"id" : 8,
	"type" : 5,
	"question" : "8. Do you integrate the principles of the ecodesign of digital services?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q9 = {
	"id" : 9,
	"type" : 5,
	"question" : "9. Do you use a modular application architecture?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q10 = {
	"id" : 10,
	"type" : 5,
	"question" : "10. Do you use a modular application architecture?",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q11 = {
	"id" : 11,
	"question" : "11. What is the overall storage volume of your corporate data (centralized on external hard drives, centralized server, NAS, SAN ...) in Terabytes (TB) useful?",
	"type" : 3,
	"textfield" : [2],
	"answer" : [
				"I don't know",
				"I do not want to answer",
				"TB"
				]
	}

q12 = {
	"id" : 12,
	"question" : "12. Do you have a server or do you only work with one or more workstations?",
	"type" : 1,
	"answer" : [
				"We work with workstation (s), without centralized physical server",
				"We have (at least) a centralized physical server"
				]
	}

q13 = {
	"id" : 13,
	"question" : "13. Do you have a dedicated room, simple room or cupboard with bay dedicated to your IT infrastructure?",
	"type" : 1,
	"answer" : [
				"A closet or a room without any specific system",
				"A dedicated room"
				]
	}

q14 = {
	"id" : 14,
	"question" : "14. Is your computer room in house or at a host?",
	"type" : 1,
	"answer" : [
				"Internal",
				"Host Member of the European Code of Conduct for Datacenters",
				"Non-adhering Host of the European Code of Conduct for Data Centers"
				]
	}

q15 = {
	"id" : 15,
	"question" : "15. What is the total area of your computer rooms (excluding technical infrastructure *)? (in m2)",
	"type" : 3,
	"textfield" : [0],
	"answer" : [
				"m²"
				"I don't know",
				"I do not want to answer"
				]
	}

q16 = {
	"id" : 16,
	"question" : "16. Do you know the PUE of your Data Center? (PUE : Power Usage Effectiveness)",
	"type" : 1,
	"answer" : [
				"Less than 1,6",
				"Between 1,6 and 2,1",
				"More than 2,1",
				"I don't know"
				]
	}

q17 = {
	"id" : 17,
	"question" : "17. What is the rate of charge or energy use of your computer rooms? (Rate = Electrical power absorbed by your IT equipment, divided by room capacity in kW, then multiplied by 100 (used energy / available energy))",
	"type" : 1,
	"answer" : [
				"100% - 90%",
				"90% - 60%",
				"Less than 60%",
				"I don't know"
				]
	}

q18 = {
	"id" : 18,
	"type" : 5,
	"question" : "18. Have you led or are you planning actions to optimize your infrastructure? Especially :",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q19 = {
	"id" : 19,
	"type" : 5,
	"question" : "The purchase of non-IT equipment from IT rooms (air conditioning, air treatment, inverters, etc.) according to energy efficiency criteria",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q20 = {
	"id" : 20,
	"type" : 5,
	"question" : """Implementing the good practices of the "European Code of Conduct for DataCenter?" """,
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q21 = {
	"id" : 21,
	"type" : 5,
	"question" : "Data center PUE tracking",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q22 = {
	"id" : 22,
	"type" : 5,
	"question" : "Regular monitoring of environmental indicators of computer rooms",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q23 = {
	"id" : 23,
	"type" : 5,
	"question" : "Environmental impact analysis of the datacenter in life cycle approach",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q24 = {
	"id" : 24,
	"type" : 5,
	"question" : "Optimizing the architecture and layout of rooms",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q25 = {
	"id" : 25,
	"type" : 5,
	"question" : "The urbanization of halls in hot / cold aisles",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q26 = {
	"id" : 26,
	"type" : 5,
	"question" : "Containment of air flows (corridors)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q27 = {
	"id" : 27,
	"type" : 5,
	"question" : "The use of natural cooling sources (freecooling)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q28 = {
	"id" : 28,
	"type" : 5,
	"question" : "Implementation of a heat recovery system for computer rooms (heating)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q29 = {
	"id" : 29,
	"type" : 5,
	"question" : "The set temperature in the cold corridor remains higher than 24 °",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q30 = {
	"id" : 30,
	"type" : 5,
	"question" : "The choice of a modular datacenter architecture",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}


q31 = {
	"id" : 31,
	"type" : 5,
	"questions" : "Have you led or are you planning actions to optimize your infrastructure? Especially :",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q32 = {
	"id" : 32,
	"type" : 5,
	"question" : "Suspending network equipment",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q33 = {
	"id" : 33,
	"type" : 5,
	"question" : "Pooling physical equipment",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q34 = {
	"id" : 34,
	"type" : 5,
	"question" : "Uninstalling unnecessary infrastructure",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q35 = {
	"id" : 35,
	"type" : 5,
	"question" : "Traceability of material elements (CMDB)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q36 = {
	"id" : 36,
	"type" : 5,
	"question" : "The correct sizing of the servers in relation to their use",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q37 = {
	"id" : 37,
	"type" : 5,
	"question" : "Give priority to ASHRAE 2 compatible equipment",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q38 = {
	"id" : 38,
	"type" : 5,
	"question" : "A procedure for provisioning and de-provisioning data-processing equipment in datacenters",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q39 = {
	"id" : 39,
	"question" : "Do you know the number of physical servers and virtual servers in your company?",
	"type" : 1,
	"answer" : [
				"No",
				"I do not want to answer",
				"Yes"
				]
	}

q40 = {
	"id" : 40,
	"question": "How many physical servers do you have?",
	"type": 2,
	"answer": "text"
	}

q41 = {
	"id" : 41,
	"question": "How many virtual servers do you have?",
	"type": 2,
	"answer": "text"
	}

q42 = {
	"id" : 42,
	"question": "How many virtual servers do you have?",
	"type" : 3,
	"textfield" : [0, 1],
	"answer": [
			"In %",
			"In quantity",
			"I do not want to answer",
			"I don't know"
			]
	}

q43 = {
	"id" : 43,
	"question": "What will be the evolution of your number of virtual servers for 2019? (in% or quantity)",
	"type" : 3,
	"textfield" : [0, 1],
	"answer": [
			"In %",
			"In quantity",
			"I do not want to answer"
			"I don't know"
			]
	}

q44 = {
	"id" : 44,
	"question" : "Has your company appointed a Green IT Manager / Digital Manager?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q45 = {
	"id" : 45,
	"question" : "Do you have a responsible digital strategy broken down into an action plan?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q46 = {
	"id" : 46,
	"question" : "Is Green IT a topic integrated into your CSR strategy?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q47 = {
	"id" : 47,
	"question" : "Do you regularly evaluate the environmental impacts of your information system?",
	"type" : 1,
	"answer" : [
				"Yes partially, including only equipment present in the company",
				"Yes totally, including our internal equipment and services hosted by third parties",
				"No",
				"I do not know"
				]
	}

q48 = {
	"id" : 48,
	"question" : "Do you have a team of competent referees on the topics of Green IT?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q49 = {
	"id" : 49,
	"question" : "Have you integrated Green IT into your business strategy",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q50 = {
	"id" : 50,
	"type" : 5,
	"question" : "Do you have those equipments in your compagny: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q51 = {
	"id" : 51,
	"type" : 5,
	"question" : "Fixed stations, workstations",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q52 = {
	"id" : 52,
	"type" : 5,
	"question" : "Laptops, digital tablets",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q53 = {
	"id" : 53,
	"type" : 5,
	"question" : "Small printers (<15kg, potentially used by a household)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q54 = {
	"id" : 54,
	"type" : 5,
	"question" : "Flat screen monitors",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q55 = {
	"id" : 55,
	"type" : 5,
	"question" : "Other flat screens (TV, projection screen, digital board ...)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q56 = {
	"id" : 56,
	"type" : 5,
	"question" : "CRT monitors (monitors or other)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q57 = {
	"id" : 57,
	"type" : 5,
	"question" : "Video projectors",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q58 = {
	"id" : 58,
	"type" : 5,
	"question" : "Mobile phones",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q59 = {
	"id" : 59,
	"type" : 5,
	"question" : "Fixed telephones (standalone not connected to such a standard)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q60 = {
	"id" : 60,
	"type" : 5,
	"question" : "Digital cameras",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q61 = {
	"id" : 61,
	"type" : 5,
	"question" : "Hard Disk Devices, Storage, Backup",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q62 = {
	"id" : 62,
	"question" : "Do you have other devices in your company? (Keyboards, mouse, graphic tablets, scanners, microphones, speakers, office equipment ...)",
	"type" : 1,
	"answer" : [
				"Yes",
				"No"
				]
	}

q63 = {
	"id" : 63,
	"type" : 5,
	"question" : "Regarding other devices, do you have in your company: (Used: equipment used in the business activity ; Not used functional: equipment in working order but no more used by the company (stored) ; Neither used nor functional: out of service equipment (HS) waiting for end of life treatment)",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q64 = {
	"id" : 64,
	"type" : 5,
	"question" : "Keyboards",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q65 = {
	"id" : 65,
	"type" : 5,
	"question" : "Mouse",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q66 = {
	"id" : 66,
	"type" : 5,
	"question" : "Graphic Tablets",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q67 = {
	"id" : 67,
	"type" : 5,
	"question" : "Scanners",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q68 = {
	"id" : 68,
	"type" : 5,
	"question" : "Speakers",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}

q69 = {
	"id" : 69,
	"type" : 5,
	"question" : "Office Automation",
	"column" : [
				"Used",
				"Not used functional",
				"Neither used nor functional"
				]
	}


q70 = {
	"id" : 70,
	"question" : "Do you know the consumption of your workstation in kWh per year?",
	"type" : 3,
	"textfield" : [0],
	"answer" : [
				"Yes (please specify how much in kWh / year)",
				"No"
				]

	}

q71 = {
	"id" : 71,
	"question" : "Do you track the energy consumption of your compagny activities?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q72 = {
	"id" : 72,
	"question" : "Do you know the share of IT and IT equipment in your company's total energy consumption?",
	"type" : 3,
	"textfield" : [0],
	"answer" : [
				"Yes (please specify how much in %)",
				"No"
				]
	}

q73 = {
	"id" : 73,
	"question" : "Have you set up a power management system? (automatic shutdown / shutdown of workstations)",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q74 = {
	"id" : 74,
	"question" : "Do you use copiers from a repackaging industry (second-hand / second-hand)?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q75 = {
	"id" : 75,
	"question" : "Do you consolidate individual printers to shared printers?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q76 = {
	"id" : 76,
	"question" : "Have you set up an identification system on printers (to trigger printing)?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q77 = {
	"id" : 77,
	"question" : "What is the average life of your professional copier / MFP *? * MFP Multi Fonction Printer",
	"type" : 3,
	"textfield" : [2],
	"answer" : [
				"I do not know",
				"Do not want to answer",
				"x years (please specify)"
				]
	}

q78 = {
	"id" : 78,
	"type" : 5,
	"question" : "Are your printers set by default in eco mode? Especially :",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q79 = {
	"id" : 79,
	"type" : 5,
	"question" : "Energy saving (Automatic standby)",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q80 = {
	"id" : 80,
	"type" : 5,
	"question" : "Black and white by default",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q81 = {
	"id" : 81,
	"type" : 5,
	"question" :"Default duplex",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q82 = {
	"id" : 82,
	"type" : 5,
	"question" : "Default draft mode",
	"column" : [
				"Yes",
				"No",
				"I don't know"
				]
	}

q83 = {
	"id" : 83,
	"question" : "What is the number of pages printed / day / employee? (A4 equivalent)",
	"type" : 1,
	"answer" : [
				"Less than 10",
				"From 10 to 20",
				"From 20 to 30",
				"More than 30",
				"I don't know"
				]
	}

q84 = {
	"id" : 84,
	"question" : "Can you specify the number of cartridges / toners:",
	"type" : 8,
	"answer" : [
				"Cartridges used a year",
				"Cartridges stored in the average business",
				"Toners used a year",
				"Toners stored in the average business"
				]
	}

q85 = {
	"id" : 85,
	"question" : "Do you organize the separate collection of waste cartridges / toners?",
	"type" : 1,
	"answer" : [
				"Yes, to a repackaging industry",
				"Yes, towards a recycling channel (destruction)",
				"No no separate collection device is planned"
				]
	}

q86 = {
	"id" : 86,
	"question" : "Do you prefer the use of recycled paper?",
	"type" : 4,
	"answer" : [
				"Yes, our paper is made from virgin paste",
				"Yes, mixed paper",
				"Yes, 100\% recycled",
				"Yes, European Label",
				"I'm not paying attention"
				]
	}

q87 = {
	"id" : 87,
	"question" : "Do you choose certified paper?",
	"type" : 7,
	"textfield" : [4],
	"answer" : [
				"Yes, FSC",
				"Yes, PEFC",
				"Yes, Blue Angel",
				"Yes, European Label",
				"Yes, other",
				"I'm not paying attention"
				]
	}

q88 = {
	"id" : 88,
	"question" : "Do you organize the separate collection of waste paper for recycling?",
	"type" : 1,
	"answer" : [
				"Yes",
				"No",
				"I don't know"
				]
}
def header():
    html = """<!DOCTYPE html>
            <html lang="fr">

            <head>
            <title>An HTML standard template</title>
            <meta charset="utf-8" />
            <link rel="icon" type="image/png" href="/img/favicon.png"/>
            <meta name="description" content="" />
            </head>

            <body>"""

    return html

def footer():
    html = """<input type="submit" name="next" value="Next"/></div></form></body><footer></footer></html>"""
    return html

def intro():
    html = """<div class="container justify">
        <h2>Welcome to the survey design4green!</h2>
        <form action="" method="post">
        <p>
            With the support of ADEME, the Ministry of Ecology, Energy and the Sea and the
            Ministry of Economy and Finance, the association AGIT (Alliance for Green IT) and
            the eco-organizations of the recycling network of Waste Electrical and Electronic
            Equipment (WEEE) organize a survey to assess the deposits of computer and office
            equipment present in companies and more generally on the maturity of companies in
            France in the use of eco-responsible digital services.
        </p>
        <p>
            The duration of the questionnaire is estimated at 15 minutes if you are able to
            answer questions directly.
        </p>
        <p>
            You can return at any time on the questionnaire, answer in several times, your
            previous answers are recorded. In case of modification, only the last answer will
            be taken into account.
        </p>
        <p>
            You can submit this questionnaire to several people in your organization. All you
            have to do is simply share the link to the questionnaire.
        </p>
        <p>
            Thank you for participating in this survey. Your answer is invaluable to us to
            constitute the most representative sample of the companies in France.
        </p>
        <button name="0. Intro" class="button">Start</button>
    </div>"""

    return html

def type_x(dictionnaire_q):
    if dictionnaire_q["type"] == 1:
        question = dictionnaire_q["question"]
        liste_answer = dictionnaire_q["answer"]
        id_q = dictionnaire_q["id"]

        html = """<p><form action="" method="post">"""
        html += """<h2>"""+question+"""</h2>"""
        for reponse in liste_answer:
            html += """<input type="radio" name='"""+question+"""' value='"""+str(id_q)+""":"""+str(liste_answer.index(reponse))+"""' id="lala" required <label for="">"""+reponse+"""</label></p>"""

    elif dictionnaire_q["type"] == 2:
        question = dictionnaire_q["question"]

        html = """<p><form action="" method="post">"""
        html += """<h2>"""+question+"""</h2>"""
        html += """<input type="text" name='"""+question+"""' placeholder="Answer..." required/><p>"""

    elif dictionnaire_q["type"] == 3:
        # print("cc valou")
        id_obt = ""
        question = dictionnaire_q["question"]
        liste_answer = dictionnaire_q["answer"]
        textfield = dictionnaire_q["textfield"]
        id_q = dictionnaire_q["id"]

        for machin in textfield:
            id_obt += str("'"+str(machin)+"',")

        html = """<p><form action="" method="post">"""
        html += """<h2>"""+dictionnaire_q["question"]+"""</h2>"""
        for reponse in liste_answer:
            html += """<p><input onclick="resetTxtField(["""+id_obt+"""])" type="radio" name='"""+question+"""'
                        value='"""+str(id_q)+""":"""+str(liste_answer.index(reponse))+"""'
                        id='"""+str(liste_answer.index(reponse))+"""'/>
                        <label for='"""+str(liste_answer.index(reponse))+"""'>"""+reponse+"""</label>"""
        # html += """<input onclick="setFocus('"""+liste_answer.index(reponse)+"""')" id='"""+liste_answer.index(reponse)+""":textfill' type="text" name="other" """

            for pos in textfield:
                if pos == liste_answer.index(reponse):
                    html += """<input onclick="setFocus('"""+str(liste_answer.index(reponse))+"""')" id='"""+str(id_q)+""":"""+str(liste_answer.index(reponse))+"""' type="text" name="other"/>"""
        html = html.replace("',])", "'])")
        html += """</p>"""

    elif dictionnaire_q["type"] == 4:
        question = dictionnaire_q["question"]
        liste_answer = dictionnaire_q["answer"]
        id_q = dictionnaire_q["id"]

        html = """<p><form action="" method="post">"""
        html += """<h2>"""+question+"""</h2>"""

        for reponse in liste_answer:
            html += """<input type="checkbox" name='"""+question+"""'
                    value='"""+str(id_q)+""":"""+str(liste_answer.index(reponse))+"""'
                    id='"""+str(liste_answer.index(reponse))+"""'/>
                    <label for='"""+str(liste_answer.index(reponse))+"""'>"""+reponse+"""</label>"""
        html += """</p>"""

    elif dictionnaire_q["type"] == 5:
        question = dictionnaire_q["question"]
        liste_column = dictionnaire_q["column"]
        id_q = dictionnaire_q["id"]
        html = """<p><form action="" method="post">"""
        html += """
        <div id="type5" class="container">
            <table style="width:100%">
                 <tr>
                   <td><h2>"""+question+"""</h2></td>"""

        for colonne in liste_column:
            html += """
                       <td>
                           <input type="radio"
                              name='"""+question+"""'
                              value='"""+str(id_q)+""":"""+str(liste_column.index(colonne))+"""'
                              id='"""+str(id_q)+""":"""+str(liste_column.index(colonne))+"""'/>
                           <label for='"""+str(id_q)+""":"""+str(liste_column.index(colonne))+"""'>"""+colonne+"""</label>
                       </td>"""

        html += """</tr>
        </table>
        </div>"""
        html += """</p>"""


#    elif dictionnaire_q["type"] == 6:
#        print(cc)

    elif dictionnaire_q["type"] == 7:
        # print("cc valou")
        id_obt = ""
        question = dictionnaire_q["question"]
        liste_answer = dictionnaire_q["answer"]
        textfield = dictionnaire_q["textfield"]
        id_q = dictionnaire_q["id"]

        for machin in textfield:
            id_obt += str("'"+str(machin)+"',")

        html = """<p><form action="" method="post">"""
        html += """<h2>"""+question+"""</h2>"""
        for reponse in liste_answer:
            html += """<p><input onclick="resetTxtField(["""+id_obt+"""])" type="checkbox" name='"""+question+"""'
                        value='"""+str(id_q)+""":"""+str(liste_answer.index(reponse))+"""'
                        id='"""+str(liste_answer.index(reponse))+"""'/>
                        <label for='"""+str(liste_answer.index(reponse))+"""'>"""+reponse+"""</label>"""
        # html += """<input onclick="setFocus('"""+liste_answer.index(reponse)+"""')" id='"""+liste_answer.index(reponse)+""":textfill' type="text" name="other" """

            for pos in textfield:
                if pos == liste_answer.index(reponse):
                    html += """<input onclick="setFocus('"""+str(liste_answer.index(reponse))+"""')" id='"""+str(id_q)+""":"""+str(liste_answer.index(reponse))+"""' type="text" name="other"/>"""
        html = html.replace("',])", "'])")
        html += """</p>"""


    elif dictionnaire_q["type"] == 8:
        question = dictionnaire_q["question"]
        liste_answer = dictionnaire_q["answer"]

        html = """<div id="type8" class="container">
        <p><form action="" method="post">
        <h2>"""+question+"""</h2>
        """
        for reponse in liste_answer:
            html += """<p><label for='"""+str(liste_answer.index(reponse))+"""'>"""+reponse+"""</label><input type="text"
                       name='"""+question+ """'
                       id='"""+str(liste_answer.index(reponse))+"""'
                       placeholder='"""+reponse+"""'required/>
                       </p>"""

            html += """</div>"""

    return html

liste_q = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60, q61, q62, q63, q64, q65, q66, q67, q68, q69, q70, q71, q72, q73, q74, q75, q76, q77, q78, q79, q80, q81, q82, q83, q84, q85, q86, q87, q88]

if form:
    list_tempo = []
    for i in form:
        list_tempo.append(i.split('.'))

    if list_tempo.count(['next']) != 0:
        list_tempo.remove(['next'])

    id_req = int(list_tempo[0][0])

    html = header()+type_x(liste_q[id_req])+footer()
else:

#    html = header()+intro()
    html = header()+type_x(liste_q[0])+footer()

print(html)
