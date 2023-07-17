COTD_FEW_SHOT = """\n\nHuman: I'm going to ask you a question. I want you to decompose it into a series of subquestions. Each subquestion should be self-contained with all the information necessary to solve it.

Make sure not to decompose more than necessary or have any trivial subquestions - you'll be evaluated on the simplicity, conciseness, and correctness of your decompositions as well as your final answer. You should wrap each subquestion in <sub_q></sub_q> tags. After each subquestion, you should answer the subquestion and put your subanswer in <sub_a></sub_a> tags. Once you have all the information you need to answer the question, output <FIN></FIN> tags.

Let's go through some examples together. Do you understand the instructions?

Assistant: Yes, I understand that I'm meant to decompose questions into subquestions and wrap each component in the appropriate tags. Once I have all the information I need, I'll output <FIN></FIN> tags.

Human: Question: What is the maiden name of the wife of the NBA player with the all-time scoring record?

Choices:
 (A) James
 (B) Abdul-Jabbar
 (C) Brinson
 (D) Alcindor

Assistant:
<sub_q>Who holds the NBA all-time scoring record?</sub_q>
<sub_a>LeBron James.</sub_a>
<sub_q>What is LeBron James' wife's first name?</sub_q>
<sub_a>Savannah.</sub_a>
<sub_q>What is Savannah James' maiden name?</sub_q>
<sub_a>Brinson.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (C) Brinson.

Human: Question: Was Michael Jackson born in the United States?

Choices:
 (A) Yes
 (B) No

Assistant:
<sub_q>Where was Michael Jackson born?</sub_q>
<sub_a>Gary, Indiana, United States.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (A) Yes.

Human: Question: What is the sum of the largest prime number between 1 and 10 and the largest odd number between 1 and 10?

Choices:
 (A) 10
 (B) 12
 (C) 14
 (D) 16
 (E) 18

Assistant:
<sub_q>What are the prime numbers between 1 and 10?</sub_q>
<sub_a>2, 3, 5, 7.</sub_a>
<sub_q>Which is the largest number in the list 2, 3, 5, 7?</sub_q>
<sub_a>7.</sub_a>
<sub_q>What are the odd numbers between 1 and 10?</sub_q>
<sub_a>1, 3, 5, 7, 9.</sub_a>
<sub_q>Which is the largest number in the list 1, 3, 5, 7, 9?</sub_q>
<sub_a>9.</sub_a>
<sub_q>What is 7 + 9?</sub_q>
<sub_a>16.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (D) 16.

Human: Question: Would the categorical imperative be likely to be covered in an introductory ethics class?

Choices:
 (A) Yes
 (B) No

Assistant:
<sub_q>What topics are covered in introductory ethics classes?</sub_q>
<sub_a>Major ethical theories and frameworks such as utilitarianism, deontology, virtue ethics. Key concepts such as moral relativism, moral absolutism. Important thinkers such as Aristotle, Kant, Mill.</sub_a>
<sub_q>Is the categorical imperative an important concept in utilitarianism?</sub_q>
<sub_a>No, the categorical imperative is a key part of Kant's deontological ethical theory.</sub_a>
<sub_q>Is the categorical imperative likely to be covered when discussing deontology in an intro ethics class?</sub_q>
<sub_a>Yes, the categorical imperative is central to Kant's deontology, so it would likely be covered.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (A) Yes.

Human: Question: A board 7ft. 9 inches long is divided into 3 equal parts. What is the length of each part?

Choices:
 (A) 31 inches
 (B) 32 inches
 (C) 33 inches
 (D) 34 inches
 (E) 35 inches

Assistant:
<sub_q>How many inches are in 7 feet 9 inches?</sub_q>
<sub_a>7 feet = 84 inches; 9 inches = 9 inches; 84 + 9 = 93 inches</sub_a>
<sub_q>The board is divided into 3 equal parts. What is 93 divided by 3?</sub_q>
<sub_a>93 / 3 = 31</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (A) 31 inches.

Human: Question: On October 1, 1980, a developer, owner of several hundred acres in a rural county, drafted a general development plan for the area. The duly recorded plan imposed elaborate limitations and restrictions upon the land in the plan, which was to be developed as a residential district. The restrictions were to extend to all persons acquiring any of the lots and to their heirs, assigns, and lessees. It was further provided that all subsequent owners would be charged with due notice of the restrictions. Among those restrictions in the general plan were the following:(22) A franchise right is created in a strip of land 10 feet in width along the rear of each lot for the use of public utility companies with right of ingress and egress. (23) No house or structure of any kind shall be built on the aforementioned strip of land running through the said blocks. In 2000, a retiree purchased one of the lots, built a house, and erected a fence in the rear of his property within the restricted area. In 2004, a teacher purchased a lot adjacent to the retiree's property and built a new house. Two years later, a librarian purchased the lot that adjoined the teacher's property. The three deeds to those properties each contained references to the deed book where the general plan was recorded. In 2008, the librarian began the construction of a seven-foot post-and-rail fence along the line dividing his lot with the teacher's, and along the center of the area subject to the franchise right. Although the teacher objected to its construction, the fence was completed. If the teacher seeks a mandatory injunction to compel removal of the librarian's fence, the court will most likely

Choices:
 (A) grant relief, because the fence was in violation of the easement restriction.
 (B) grant relief, because the encroachment of the fence violated the restriction in the original plan.
 (C) deny relief, because the teacher failed to enforce the restriction against the retiree.
 (D) deny relief, because the fence would not be construed as "a structure" within the terms of the restriction.

Assistant:
<sub_q>Will the court grant relief because the fence is in violation of the easement restriction?</sub_q>
<sub_a>No, the fences do not impede public utility access to the dedicated strip of land.</sub_a>
<sub_q>Will the court grant relief because the encroachment of the fence violated the restriction in the original plan?</sub_q>
<sub_a>Yes. There is a restriction against building structures on the 10-foot strip of land along the rear of each lot, and the librarian's fence encroaches upon this restricted area.</sub_a>
<sub_q>Will the court deny relief because the teacher failed to enforce the restriction against the retiree?</sub_q>
<sub_a>No, the teacher's failure to enforce the restriction in the past does not prevent enforcing it now against the librarian.</sub_a>
<sub_q>Will the court deny relief because the fence would not be construed as "a structure" within the terms of the restriction?</sub_q>
<sub_a>Maybe. It's unclear whether a fence would qualify as a "structure" for the purposes of this restriction. The court may find that the fence does not violate the restriction on this basis.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (B) grant relief, because the encroachment of the fence violated the restriction in the original plan.

Human: Question: On the list of a flower's goals would be to

Choices:
 (A) produce carbon dioxide
 (B) deroot and die
 (C) produce offspring
 (D) remain sterile

Assistant:
<sub_q>What are the main biological drives or goals of living organisms, including plants?</sub_q>
<sub_a>To survive, grow, and reproduce.</sub_a>
<sub_q>Does producing carbon dioxide help a flower survive, grow, or reproduce?</sub_q>
<sub_a>No, producing carbon dioxide is not one of a flower's biological goals.</sub_a>
<sub_q>Does derooting and dying help a flower survive, grow, or reproduce?</sub_q>
<sub_a>No, derooting and dying opposes a flower's biological drives.</sub_a>
<sub_q>Does producing offspring help a flower survive, grow, or reproduce?</sub_q>
<sub_a>Yes, producing offspring helps a flower reproduce, which is one of its key biological goals.</sub_a>
<sub_q>Does remaining sterile help a flower survive, grow, or reproduce?</sub_q>
<sub_a>No, remaining sterile prevents reproduction, which opposes a flower's biological goals.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (C) produce offspring.

Human: Question: In contrast to _______, _______ aim to reward favourable behaviour by companies. The success of such campaigns have been heightened through the use of ___________, which allow campaigns to facilitate the company in achieving _________ .

Choices:
 (A) Buycotts, Boycotts, Blockchain technology, Charitable Donations
 (B) Buycotts, Boycotts, Digital technology, Increased Sales
 (C) Boycotts, Buyalls, Blockchain technology, Charitable Donations
 (D) Boycotts, Buycotts, Digital technology, Increased Sales

Assistant:
<sub_q>What are campaigns that aim to punish unfavorable behavior by companies through refusing to buy their products?</sub_q>
<sub_a>Boycotts.</sub_a>
<sub_q>What are campaigns that aim to reward favorable behavior by companies through buying their products?</sub_q>
<sub_a>Buycotts.</sub_a>
<sub_q>What type of technology has allowed companies to easily facilitate and promote buycotts?</sub_q>
<sub_a>Digital technology like social media.</sub_a>
<sub_q>What is a key goal that companies aim to achieve through buycotts?</sub_q>
<sub_a>Increased sales.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (D) Boycotts, Buycotts, Digital technology, Increased Sales.

Human: Question: Was the band The Beatles formed after John F. Kennedy was assassinated?

Choices:
 (A) Yes
 (B) No

Assistant:
<sub_q>When was John F. Kennedy assassinated?</sub_q>
<sub_a>November 22, 1963.</sub_a>
<sub_q>When was the band The Beatles formed?</sub_q>
<sub_a>The Beatles were formed in 1960.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (B) No.

Human: Question: For which of these two scenarios does the main character (who uses I/me/my) do something clearly morally wrong, according to ordinary moral standards in the US as of 2020? Scenario 1 | During the house's demolition, I pushed him into a wall. Scenario 2 | When I choose a babysitter for my twin nieces, I don't care about her racial background.

Choices:
 (A) Wrong, Wrong
 (B) Wrong, Not wrong
 (C) Not wrong, Wrong
 (D) Not wrong, Not wrong

Assistant:
<sub_q>In Scenario 1, does pushing someone into a wall violate ordinary moral standards?</sub_q>
<sub_a>Yes, physically harming someone without cause is considered morally wrong.</sub_a>
<sub_q>In Scenario 2, does choosing a babysitter without regard for their racial background violate ordinary moral standards?</sub_q>
<sub_a>No, making hiring decisions without considering race does not violate widely held moral standards.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (B) Wrong, Not wrong.

Human: Question: Are both lizards and cats mammals?

Choices:
 (A) Yes
 (B) No

Assistant:
<sub_q>Are lizards mammals?</sub_q>
<sub_a>No, lizards are reptiles, not mammals.</sub_a>
<sub_q>Are cats mammals?</sub_q>
<sub_a>Yes, cats are mammals.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (B) No.

Human: Question: A state has recently enacted a statute prohibiting the disposal of any nuclear wastes within the state. This law does not contravene or conflict with any federal statutes. A man operates a company in the state that is engaged in the disposal of nuclear wastes. Subsequent to the passage of the state statute, the man, not yet aware of the new law, entered into contracts with many out-of-state firms to dispose of their nuclear wastes in the state. On account of this new law, however, the man will be unable to perform these contracts. Assume that the man has standing to challenge this state law. Which of the following presents his strongest constitutional grounds to challenge the state law prohibiting the disposal of nuclear wastes within the state?

Choices:
 (A) The equal protection clause of the Fourteenth Amendment.
 (B) The commerce clause.
 (C) The privileges and immunities clause of Article IV, Section 2.
 (D) The contract clause.

Assistant:
<sub_q>What is the equal protection clause of the Fourteenth Amendment?</sub_q>
<sub_a>Prohibits discrimination by the government.</sub_a>
<sub_q>Does the waste disposal law violate the equal protection clause?</sub_q>
<sub_a>Likely not, since the law does not specifically discriminate against any group of people.</sub_a>
<sub_q>What is the commerce clause?</sub_q>
<sub_a>Gives Congress the power to regulate interstate commerce.</sub_a>
<sub_q>Does the waste disposal law violate the commerce clause?</sub_q>
<sub_a>Yes, since it interferes with interstate contracts to dispose of waste in the state.</sub_a>
<sub_q>What is the priviliges and immunities clause?</sub_q>
<sub_a>Requires states to grant citizens from other states the same rights and privileges as its own citizens.</sub_a>
<sub_q>Does the waste disposal law violate the privileges and immunities clause?</sub_q>
<sub_a>No, since the law does not discriminate based on state citizenship.</sub_a>
<sub_q>What is the contract clause?</sub_q>
<sub_a>Prohibits states from passing laws impairing the obligation of contracts.</sub_a>
<sub_q>Does the waste disposal law violate the contract clause?</sub_q>
<sub_a>Possibly, if contracts were already in place before the new law was passed.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (B) The commerce clause.

Human: Question: This question refers to the following information. The excerpts below are from the Navigation Acts of 1651. [A]fter the first day of December, one thousand six hundred fifty and one, and from thence forwards, no goods or commodities whatsoever of the growth, production or manufacture of Asia, Africa or America, or of any part thereof; or of any islands belonging to them, or which are described or laid down in the usual maps or cards of those places, as well of the English plantations as others, shall be imported or brought into this Commonwealth of England, or into Ireland, or any other lands, islands, plantations, or territories to this Commonwealth belonging, or in their possession, in any other ship or ships, vessel or vessels whatsoever, but only in such as do truly and without fraud belong only to the people of this Commonwealth, or the plantations thereof, as the proprietors or right owners thereof; and whereof the master and mariners are also of the people of this Commonwealth, under the penalty of the forfeiture and loss of all the goods that shall be imported contrary to this act, , , , [N]o goods or commodities of the growth, production, or manufacture of Europe, or of any part thereof, shall after the first day of December, one thousand six hundred fifty and one, be imported or brought into this Commonwealth of England, or any other lands or territories to this Commonwealth belonging, or in their possession, in any ship or ships, vessel or vessels whatsoever, but in such as do truly and without fraud belong only to the people of this Commonwealth, and in no other, except only such foreign ships and vessels as do truly and properly belong to the people of that country or place, of which the said goods are the growth, production or manufacture. Which of the following best describes the outcome of the Navigation Acts of 1651?

Choices:
 (A) They served as a catalyst for the growth of English shipping and overseas trade, but did little to limit the prospects of the Dutch in the seventeenth century.
 (B) They brought about almost immediate hardships for the Dutch economy as their dominance of overseas trade quickly ended.
 (C) They were rescinded during the restoration of the Stuarts as they sought normal diplomatic relations with the Dutch so not as to need Parliament's financial support for war.
 (D) They led to nearly a century of recurrent war between England and the Netherlands, which would not end until after American independence.

Assistant:
<sub_q>What did the Navigation Acts aim to do?</sub_q>
<sub_a>Promote English shipping and trade by restricting foreign competition.</sub_a>
<sub_q>Did the Navigation Acts immediately cripple Dutch trade and shipping?</sub_q>
<sub_a>No, the Dutch remained dominant in trade for some time. The acts likely only had a gradual impact. </sub_a>
<sub_q>Were the Navigation Acts rescinded after the restoration of the Stuarts?</sub_q>
<sub_a>There is no evidence in the excerpt to suggest this. The acts seem to have remained in place.</sub_a>
<sub_q>Did the Navigation Acts lead to prolonged conflict between England and the Netherlands?</sub_q>
<sub_a>Possibly, as the acts were protectionist and aimed against Dutch trade dominance. This may have caused tensions with the Dutch.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (A) They served as a catalyst for the growth of English shipping and overseas trade, but did little to limit the prospects of the Dutch in the seventeenth century.

Human: Question: A son owed a creditor $5,000. The son's father contacted the creditor and told him that he wanted to pay the son's debt. The father signed a document that stated the father would pay the son's debt at a rate of $500 a month for 10 months. The creditor made no written or oral commitment to forbear to sue the son to collect the $5,000 debt, and the father made no oral or written request for any such forbearance. For the next five months, the father made and the creditor accepted the $500 monthly payments as agreed. During that period, the creditor, in fact, did forbear to take any legal action against the son. However, the father then informed the creditor that he would make no further payments on the debt. Which of the following is the most persuasive argument that the father is liable to the creditor under the terms of their agreement?

Choices:
 (A) The father's five payments to the creditor totaling $2,500 manifested a serious intent on the father's part to be contractually bound, and such manifestation is generally recognized as an effective substitute for consideration.
 (B) Because it was foreseeable that the father's promise would induce the creditor to forbear taking any action against the son, such forbearance was, as a matter of law, a bargained-for consideration for the father's promise.
 (C) The father's promise and the creditor's reliance thereon, if proved, gave rise to a valid claim by the creditor against the father based on the doctrine of promissory estoppel.
 (D) By assuming the antecedent debt obligation that the son owed to the creditor, the father became a surety whose promise to the creditor was enforceable, since it was in writing and supported by adequate consideration.

Assistant:
<sub_q>Was there consideration (something of value exchanged) for the father's promise to pay the debt?</sub_q>
<sub_a>Not explicitly. The creditor did not commit to forbearing collection from the son in exchange for the promise.</sub_a>
<sub_q>Can the father's partial performance (5 monthly payments) constitute consideration?</sub_q>
<sub_a>Possibly, but it is not entirely persuasive since the promise was for 10 payments, and the creditor did not request or rely on just 5 payments.</sub_a>
<sub_q>Can promissory estoppel (reasonable reliance) be argued as a basis for enforcing the father's promise?</sub_q>
<sub_a>Yes, the creditor relied on the father's promise by forbearing collection from the son, as could be reasonably expected. This provides the strongest argument for enforcing the promise. </sub_a>
<sub_q>Did the father become a surety whose written promise is enforceable?</sub_q>
<sub_a>No, there is no evidence the father agreed in writing to act as a surety, nor did the creditor release the son from liability in exchange for the father's promise.</sub_a>
<FIN></FIN>

Human: Based on the above, what's the correct answer to the question?

Assistant: The correct answer to the question is choice (C) The father's promise and the creditor's reliance thereon, if proved, gave rise to a valid claim by the creditor against the father based on the doctrine of promissory estoppel."""