from nltk.chat.util import Chat, reflections
import nltk

nltk.download('punkt')  # Ensure nltk data is downloaded

# Define pairs for chatbot responses
pairs = [
    (r"\bHi\b|\bHello\b", ["Hello, how can I assist you with legal matters today?"]),

    (r"\bHow are you\?", ["I'm good, thank you! How can I assist you?"]),

    (r"\bbye\b|\bquit\b", ["Thank you for using the legal chatbot. Goodbye!"]),

    #sections
    (r"\bSection 1\b", [
        "Section no: 1\n"
        "Definition: Section 1 of the Indian Penal Code (IPC) provides the short title and the extent of the Act. "
        "This section specifies that the IPC shall be known as the Indian Penal Code, and it applies throughout India, "
        "including territories under the jurisdiction of the Indian government. It also lays down that the IPC is intended "
        "to regulate criminal offenses in India. Additionally, the section clarifies that certain crimes committed by Indian citizens "
        "outside India may be governed by the provisions of the IPC as well.\n"
        "Punishment: No specific punishment mentioned in Section 1."
    ]),

    (r"\bSection 2\b", [
        "Section no: 2\n"
        "Definition: Section 2 of the Indian Penal Code explains the jurisdiction of the IPC. This section specifies that the "
        "provisions of the IPC apply to all offenses committed within India, regardless of the nationality of the offender. "
        "It extends the application of the IPC to every act committed within the country, whether by an Indian or a foreigner. "
        "The section thus forms the foundation for establishing the authority of Indian courts over crimes occurring within its territorial boundaries.\n"
        "Punishment: No specific punishment mentioned in Section 2."
    ]),

    (r"\bSection 3\b", [
        "Section no: 3\n"
        "Definition: Section 3 of the Consumer Protection Act, 1986 is aimed at the establishment of Consumer Protection Councils "
        "at the national, state, and district levels. These councils serve as a platform for promoting and protecting the rights "
        "of consumers, ensuring that their grievances are addressed, and that they are informed about their rights. The councils also "
        "help in promoting fair trade practices and educating consumers about their rights and responsibilities. They play a crucial role "
        "in the overall consumer protection ecosystem in India.\n"
        "Punishment: No specific punishment mentioned in Section 3."
    ]),

    (r"\bSection 4\b", [
        "Section no: 4\n"
        "Definition: Section 4 of the IPC extends its jurisdiction to cover offenses committed outside India by Indian citizens or individuals "
        "subject to the jurisdiction of the Indian government, such as officials working abroad or individuals on Indian ships or aircraft. "
        "This section aims to ensure that Indian citizens can be held accountable for crimes committed outside the country and that justice "
        "is served even beyond the borders of India. It emphasizes that the IPC applies to Indian nationals wherever they may be.\n"
        "Punishment: As per applicable laws for crimes committed outside India."
    ]),

    (r"\bSection 5\b", [
        "Section no: 5\n"
        "Definition: Section 5 of the IPC clarifies that the Indian Penal Code does not override special laws enacted for specific offenses. "
        "This means that if a special law provides for a different punishment or procedure for a certain crime, it takes precedence over the "
        "provisions of the IPC. This section ensures that the IPC works in conjunction with other laws, offering flexibility in the legal system.\n"
        "Punishment: Governed by the special laws applicable to the specific offense."
    ]),

    (r"\bSection 6\b", [
        "Section no: 6\n"
        "Definition: Section 6 of the IPC provides for the interpretation of terms used in the IPC. It allows the courts to apply general explanations, "
        "which help interpret specific words or phrases that may be ambiguous or open to multiple meanings. The section ensures that the IPC is applied "
        "fairly and consistently, providing clarity in legal proceedings.\n"
        "Punishment: No specific punishment mentioned in Section 6."
    ]),

    (r"\bSection 7\b", [
        "Section no: 7\n"
        "Definition: Section 7 of the IPC outlines the definition of 'person' under the code. It includes both individuals and legal entities such as corporations, "
        "associations, and institutions. This section ensures that all parties, regardless of whether they are individuals or organizations, can be held accountable "
        "under the IPC.\n"
        "Punishment: Applicable based on offenses committed by the 'person' as defined."
    ]),

    (r"\bSection 8\b", [
        "Section no: 8\n"
        "Definition: Section 8 of the IPC deals with gender-neutral language in the law. It clarifies that any reference to a male person "
        "in the IPC includes females as well, thus ensuring equality before the law for both genders. This provision allows the law to be "
        "applied fairly without gender bias.\n"
        "Punishment: No specific punishment mentioned in Section 8."
    ]),
    # Family Law
    (r"\bSection 9\b", [
        "Section no: 9\n"
        "Definition: Section 9 of the Hindu Marriage Act, 1955, addresses the concept of restitution of conjugal rights. This provision allows "
        "a spouse to file a petition in court if their partner has refused to live with them or fulfill their marital obligations. The court can "
        "issue an order directing the spouse to resume cohabitation or face consequences such as separation or divorce. This section highlights "
        "the importance of maintaining the integrity of marriage and ensuring both parties fulfill their duties towards each other.\n"
        "Punishment: Non-compliance with a court order can lead to legal consequences, including separation or divorce."
    ]),

    # Indian Contract Act
    (r"\bSection 10\b", [
        "Section no: 10\n"
        "Definition: Section 10 of the Indian Contract Act, 1872, outlines the essential conditions required for a contract to be legally valid and "
        "enforceable. These conditions include free consent, lawful consideration, capacity of the parties involved, and the agreement being for a lawful "
        "object. This section emphasizes that for a contract to be valid, both parties must voluntarily and knowingly enter into the agreement, without any "
        "form of coercion, fraud, or misrepresentation. Contracts based on these principles are legally binding, providing the foundation for commercial "
        "and personal agreements in India.\n"
        "Punishment: Invalid or unlawful contracts may be deemed void and unenforceable by law."
    ]),

    (r"\bSection 11\b", [
        "Section no: 11\n"
        "Definition: Section 11 of the IPC defines the term 'person' broadly to include any individual or entity capable of holding rights and duties. "
        "This provision ensures that the IPC applies to a wide range of parties, including individuals, companies, organizations, and even the government. "
        "This broad definition helps in extending the provisions of the IPC to a variety of legal contexts.\n"
        "Punishment: Not applicable directly, as this section focuses on definitions."
    ]),

    (r"\bSection 12\b|\bDomestic Violence Act\b", [
        "Section no: 12\n"
        "Definition: Section 12 of the Domestic Violence Act, 2005, allows an individual (usually a woman) who is a victim of domestic violence to approach "
        "the court for relief. The victim can file a complaint with the magistrate and seek various protective measures, including protection orders, residence "
        "orders, and monetary relief. This section empowers victims to break free from abusive relationships and seek justice through the legal system. The "
        "Domestic Violence Act aims to provide protection and justice to individuals facing domestic abuse, highlighting the importance of safeguarding personal "
        "well-being in intimate relationships.\n"
        "Punishment: Violators of protective orders can face fines or imprisonment under the Domestic Violence Act."
    ]),

    (r"\bSection 13\b", [
        "Section no: 13\n"
        "Definition: Section 13 of the Hindu Marriage Act, 1955, lays down the provisions for divorce. It lists the grounds on which either spouse can file for "
        "divorce, such as adultery, cruelty, desertion, conversion to another religion, mental illness, and renunciation of the world. This section aims to provide "
        "relief to individuals trapped in irretrievably broken marriages.\n"
        "Punishment: Not directly applicable; this section focuses on legal procedures for divorce."
    ]),

    (r"\bArticle 14\b", [
        "Article no: 14\n"
        "Definition: Article 14 of the Indian Constitution guarantees equality before the law and equal protection of the laws. It prohibits discrimination on the basis "
        "of religion, race, caste, sex, or place of birth. This article ensures that every person is treated equally under the law, promoting fairness and justice within "
        "the legal system. Courts often use this article to strike down discriminatory laws or practices, and it plays a crucial role in advancing social equality and "
        "protecting individual rights.\n"
        "Punishment: Not applicable; this is a constitutional provision ensuring rights."
    ]),

    (r"\bSection 15\b", [
        "Section no: 15\n"
        "Definition: Section 15 of the IPC defines the offense of harboring offenders. This includes knowingly providing shelter or assistance to someone wanted by the "
        "police for committing a crime. The section emphasizes the importance of aiding law enforcement in bringing criminals to justice and preventing individuals from "
        "escaping legal consequences.\n"
        "Punishment: Imprisonment or fines, depending on the severity of the offense and the context of harboring."
    ]),

    (r"\bSection 16\b", [
        "Section no: 16\n"
        "Definition: Section 16 of the IPC defines the punishment for acts of sedition. It applies to individuals or groups who incite violence or create hostility "
        "against the state through words, signs, or visible representations. This section aims to maintain public order and protect the sovereignty of the nation.\n"
        "Punishment: Imprisonment up to life, with or without a fine, depending on the gravity of the offense."
    ]),

    (r"\bSection 17\b", [
        "Section no: 17\n"
        "Definition: Section 17 of the Indian Penal Code (IPC) defines 'fraudulent' as a deliberate misrepresentation or concealment of facts with the intent to deceive or defraud another party. "
        "This section specifically addresses actions involving false statements made to induce someone to act in a way that causes harm or injury to them. Fraudulent acts are punishable under the IPC as they harm public trust.\n"
        "Punishment: Imprisonment for a term that may extend to 7 years, and may also include a fine, depending on the severity of the fraudulent act."
    ]),

    (r"\bSection 18\b", [
        "Section no: 18\n"
        "Definition: Section 18 of the Indian Contract Act, 1872, defines the concept of 'coercion.' It stipulates that any contract entered into under coercion, "
        "which involves compelling a person to act against their will through threats or force, can be considered voidable. The section ensures that contracts signed "
        "under duress are not legally binding, offering protection to individuals who may have been forced or intimidated into an agreement. This provision ensures that "
        "parties cannot be held accountable for agreements made under conditions that undermine free will.\n"
        "Punishment: Not applicable; this section invalidates coercive contracts."
    ]),

    (r"\bArticle 19\b", [
        "Article no: 19\n"
        "Definition: Article 19 of the Indian Constitution guarantees certain freedoms, including the freedom of speech and expression, the freedom to assemble peacefully, "
        "the freedom to move freely within India, and the freedom to reside and settle in any part of India. However, these freedoms are subject to reasonable restrictions "
        "based on national security, public order, and other interests. This article serves as a cornerstone for individual freedoms, ensuring that citizens can express "
        "themselves and associate freely, while also balancing these rights with the need to maintain public peace and security.\n"
        "Implications: While ensuring freedoms, it also outlines restrictions to safeguard public interest and national security."
    ]),

    (r"\bSection 20\b", [
        "Section no: 20\n"
        "Definition: Section 20 of the Indian Penal Code (IPC) deals with the offense of 'criminal intimidation.' This involves threatening someone with harm to their person, reputation, or property, intending to cause fear or compel the person to act against their will. "
        "The section ensures that people are protected from undue threats and intimidation in their personal and professional lives.\n"
        "Punishment: Imprisonment for a term that may extend to 2 years, or a fine, or both, depending on the severity of the intimidation."
    ]),

    (r"\bSection 21\b", [
        "Section no: 21\n"
        "Definition: Section 21 of the Indian Penal Code defines the term 'public servant.' It refers to anyone employed in the service of the government or any person holding a public office, whose duties include the administration of laws or public resources. "
        "This section is important for identifying those who are bound by the law to act in the public interest and maintain justice.\n"
        "Punishment: The section does not prescribe punishment, but is crucial for classifying individuals as public servants under various legal provisions."
    ]),

    (r"\bSection 22\b", [
        "Section no: 22\n"
        "Definition: Section 22 of the Indian Penal Code defines 'vessel' to include any kind of ship, boat, or other floating structures that are capable of being used for transportation on water. "
        "This definition is essential in legal cases involving maritime offenses, ensuring that all types of watercraft are covered under the law.\n"
        "Punishment: There is no direct punishment under this section, as it primarily provides a definition for legal purposes in the context of maritime laws."
    ]),

    (r"\bSection 23\b", [
        "Section no: 23\n"
        "Definition: Section 23 of the Indian Penal Code defines 'dishonestly' as an intention or act that is designed to deprive someone of their property or rights unlawfully. "
        "The section specifically highlights the intention to cause wrongful gain or loss and is essential for identifying fraudulent or dishonest actions under the law.\n"
        "Punishment: Punishments vary depending on the offense in which dishonesty is involved. It can lead to imprisonment or fines as per the specific crime being committed."
    ]),

    (r"\bSection 24\b", [
        "Section no: 24\n"
        "Definition: Section 24 of the Indian Penal Code (IPC) defines 'intentional acts.' This section lays down that if an individual commits an act with the intention to cause harm or with knowledge that the act is likely to cause harm, such an act is punishable under the IPC.\n"
        "Punishment: The punishment varies depending on the specific crime committed. The severity of the punishment depends on the nature of the harm caused by the act."
    ]),

    (r"\bSection 25\b", [
        "Section no: 25\n"
        "Definition: Section 25 of the Indian Penal Code defines 'voluntary acts.' It stipulates that an individual will not be held liable for an act committed in good faith, without knowledge or intention to cause harm. In cases where the act was committed under duress or compulsion, it may not be considered as an offense.\n"
        "Punishment: This section generally exempts certain actions from being penalized, provided they meet the criteria of good faith and absence of intent to harm."
    ]),

    (r"\bSection 26\b", [
        "Section no: 26\n"
        "Definition: Section 26 of the Indian Penal Code defines 'legal liability for a minor.' It provides that a child below 7 years of age is not considered criminally responsible for their actions. The law recognizes the lack of understanding of consequences by minors at that age.\n"
        "Punishment: No punishment is imposed on children under 7 years of age, as they are considered incapable of forming criminal intent. However, children between 7 and 12 may be held criminally liable if it is proven that they had the understanding of the consequences of their actions."
    ]),

    (r"\bSection 27\b", [
        "Section no: 27\n"
        "Definition: Section 27 of the Indian Penal Code (IPC) deals with 'murder committed by a person under the age of 18.' It explains that if a person below the age of 18 intentionally causes the death of another person, they can be charged with murder, though the punishment might differ compared to an adult.\n"
        "Punishment: The punishment for this offense may be imprisonment or other punishments depending on the specifics of the case, but the court will consider the age of the individual when determining the sentence."
    ]),

    (r"\bSection 28\b", [
        "Section no: 28\n"
        "Definition: Section 28 of the Indian Penal Code defines the term 'offense committed by a person of unsound mind.' This section provides that an individual who commits an offense due to a mental condition that impairs their ability to understand the nature of their actions may not be held criminally responsible.\n"
        "Punishment: No punishment is imposed on a person who is deemed to be of unsound mind at the time of committing the offense. However, the court may order medical treatment or hospitalization in such cases."
    ]),

    (r"\bSection 29\b", [
        "Section no: 29\n"
        "Definition: Section 29 of the Indian Penal Code deals with 'illegal possession of property.' This section lays down that any individual found in illegal possession of stolen or unlawfully obtained property may be subject to penalties.\n"
        "Punishment: The punishment for this offense can vary based on the circumstances, but it typically includes imprisonment or fines, depending on the seriousness of the crime and the value of the property involved."
    ]),

    (r"\bSection 30\b", [
        "Section no: 30\n"
        "Definition: Section 30 of the Indian Penal Code outlines the definition of 'criminal conspiracy.' It states that when two or more people come together with the intention to commit a crime, they are considered to be involved in a criminal conspiracy.\n"
        "Punishment: The punishment for criminal conspiracy varies depending on the crime being conspired, but it generally includes imprisonment and possible fines, with the severity depending on the crime involved."
    ]),

    (r"\bSection 31\b", [
        "Section no: 31\n"
        "Definition: Section 31 of the Indian Penal Code deals with the punishment for attempting to commit an offense. It provides that anyone who attempts to commit a crime and fails to do so will be punished as if they had committed the offense itself. This provision is important because it ensures that individuals who attempt to commit crimes are not exempt from punishment simply due to failure.\n"
        "Punishment: The punishment for attempting to commit an offense is the same as the punishment for the offense itself."
    ]),

    (r"\bSection 32\b", [
        "Section no: 32\n"
        "Definition: Section 32 of the Indian Penal Code addresses the punishment for acts that cause injury or harm to a person in a particular way. It deals with instances where a person is intentionally or knowingly injured by a method that results in a specific consequence or effect. This section aims to cover acts that are directly related to harm done through specific actions or devices.\n"
        "Punishment: The punishment depends on the severity of the harm caused, and can range from fines to imprisonment."
    ]),

    (r"\bSection 33\b", [
        "Section no: 33\n"
        "Definition: Section 33 of the Indian Penal Code deals with the punishment for the unlawful possession or use of dangerous weapons or materials. It covers cases where individuals are caught in the act of carrying or using dangerous tools, weapons, or substances with the intent to harm others. The section highlights the importance of maintaining public safety by controlling the possession and use of dangerous materials.\n"
        "Punishment: The punishment for violating this section can include imprisonment or fines, depending on the severity of the crime."
    ]),

    (r"\bSection 34\b", [
        "Section no: 34\n"
        "Definition: Section 34 of the Indian Penal Code addresses the principle of joint liability. It states that when a criminal act is done by several persons acting together with a common intention, each of them is equally liable for the offense. This section is important as it ensures that individuals who act in concert with others to commit a crime are held equally responsible, regardless of the specific role each person played.\n"
        "Punishment: The punishment for joint liability is the same as that for the offense committed, and it is applicable to all individuals involved."
    ]),

    (r"\bSection 35\b", [
        "Section no: 35\n"
        "Definition: Section 35 of the Indian Penal Code addresses joint responsibility when multiple people act with a common intention. In cases where several individuals work together to commit a crime, each person involved is equally liable, regardless of their specific role in the offense. This provision aims to ensure that no one can escape liability by claiming that they did not directly participate in the criminal act, emphasizing collective responsibility.\n"
        "Punishment: The punishment for this offense varies depending on the specific crime committed, but all parties involved will face similar consequences, with each being liable to the same extent as the primary offender."
    ]),

    (r"\bSection 36\b", [
        "Section no: 36\n"
        "Definition: Section 36 of the Indian Penal Code holds individuals accountable for aiding or abetting a crime, with punishments similar to those imposed on the primary offender. If someone assists, encourages, or facilitates the commission of a crime, they can be charged and punished as if they committed the crime themselves. This section plays a crucial role in punishing accomplices and enforcers of criminal activities, ensuring that the legal system holds everyone who contributes to a crime accountable.\n"
        "Punishment: The punishment for aiding or abetting a crime is generally similar to the punishment for the main offense, depending on the nature and severity of the crime involved."
    ]),

    (r"\bSection 37\b", [
        "Section no: 37\n"
        "Definition: Section 37 of the Indian Penal Code deals with the punishment for conspiracy. It specifies that anyone who conspires to commit a criminal offense is liable to be punished as if they had committed the offense themselves. The section is designed to ensure that individuals who plan crimes together are held accountable for their actions, even if the crime itself is not successfully completed.\n"
        "Punishment: The punishment for conspiracy can be the same as for the offense committed, depending on the nature of the crime."
    ]),

    (r"\bSection 38\b", [
        "Section no: 38\n"
        "Definition: Section 38 of the Indian Penal Code addresses the liability of individuals who, by their presence, encourage or facilitate the commission of a crime. It defines the role of a person who is present at the scene of a crime and assists, even indirectly, in its commission.\n"
        "Punishment: The punishment for being an accomplice or abettor to the crime can be similar to the punishment for the principal offender."
    ]),

    (r"\bSection 39\b", [
        "Section no: 39\n"
        "Definition: Section 39 of the Indian Penal Code defines the offense of 'public mischief'. It includes acts that cause harm or injury to public security, such as false information, unlawful assemblies, or threats that disturb public peace. The section is aimed at maintaining law and order in public spaces by criminalizing actions that pose a danger to society.\n"
        "Punishment: The punishment for public mischief can include imprisonment, fines, or both, depending on the severity of the offense."
    ]),

    (r"\bSection 40\b", [
        "Section no: 40\n"
        "Definition: Section 40 of the Indian Penal Code defines the term 'offense'. It provides a broad definition that encompasses any act that is prohibited by law and for which a punishment is prescribed. This section helps clarify what constitutes a crime under the IPC and is important for the legal system to determine the actions that can be penalized.\n"
        "Punishment: This section does not prescribe a specific punishment but defines the scope of what is considered an offense under the law."
    ]),

    (r"\bSection 41\b", [
         "Section no: 41\n"
        "Definition: Section 41 of the Indian Penal Code deals with the term 'commits' when referring to the commission of an offense. It emphasizes that when a person 'commits' an offense, it refers to an action that leads to the violation of the law.\n"
        "Punishment: This section does not prescribe a specific punishment but defines the concept of 'committing' an offense as a legal term used in criminal law."
    ]),

    (r"\bSection 42\b", [
        "Section no: 42\n"
        "Definition: Section 42 of the Indian Penal Code defines 'being a member of an unlawful assembly.' An unlawful assembly is one that gathers with the intent to commit an illegal act. This section helps in categorizing people involved in unlawful gatherings and distinguishes them from those who are not part of criminal activities.\n"
        "Punishment: If an individual is found guilty of being part of an unlawful assembly, they may be punished under related sections, depending on the crime committed by the assembly as a whole."
    ]),

    (r"\bSection 43\b", [
        "Section no: 43\n"
        "Definition: Section 43 of the Indian Penal Code defines the term 'illegal' in the context of actions that are prohibited by law. It specifies that an act is 'illegal' if it is done with the intention of violating legal rules or obstructing legal proceedings.\n"
        "Punishment: This section does not prescribe specific punishment but categorizes actions as illegal, subjecting them to the punishments outlined for related offenses under the law."
    ]),

    (r"\bSection 44\b", [
        "Section no: 44\n"
        "Definition: Section 44 of the Indian Penal Code defines the term 'injury' as any harm caused to an individual's body, mind, reputation, or property. This section is used in determining the severity of crimes like assault, defamation, and property damage. It helps courts evaluate the consequences of criminal actions and the extent to which victims have been affected. The section is essential for determining the compensation or punishment for criminal acts involving harm.\n"
        "Punishment: The section is used to assess punishment based on the nature and severity of the injury caused."
    ]),

    (r"\bSection 44\b", [
        "Section no: 44\n"
        "Definition: Section 44 of the Indian Penal Code defines the term 'injury' as any harm caused to an individual's body, mind, reputation, or property. This section is used to determine the impact of crimes such as assault, defamation, and property damage.\n"
        "Punishment: This section does not prescribe specific punishment but aids courts in evaluating the severity of harm caused and deciding appropriate penalties."
    ]),

    (r"\bSection 45\b", [
        "Section no: 45\n"
        "Definition: Section 45 of the Indian Penal Code defines the term 'life' as the life of a human being unless the contrary appears from the context. This term is used in provisions where the law refers to the sanctity and duration of human life.\n"
        "Punishment: This section does not prescribe specific punishment but provides clarity for interpreting laws concerning human life."
    ]),

    (r"\bSection 46\b", [
        "Section no: 46\n"
        "Definition: Section 46 of the Indian Penal Code defines the term 'death' as the death of a human being unless the context indicates otherwise. This definition is vital for legal proceedings concerning cases involving death.\n"
        "Punishment: This section does not prescribe specific punishment but ensures a consistent understanding of the term in legal contexts."
    ]),

    (r"\bSection 47\b", [
        "Section no: 47\n"
        "Definition: Section 47 of the Indian Penal Code defines the term 'animal' as any living creature other than a human being. This section is important for laws related to animal rights, protection, and offenses involving animals.\n"
        "Punishment: This section does not prescribe specific punishment but establishes the legal definition of 'animal' for relevant provisions."
    ]),

    (r"\bSection 48\b", [
        "Section no: 48\n"
        "Definition: Section 48 of the Indian Penal Code defines the term 'vessel' as anything made for the conveyance of goods or passengers by water. This definition is used in legal contexts involving maritime laws and offenses.\n"
        "Punishment: This section does not prescribe specific punishment but ensures clarity in cases related to maritime activities."
    ]),

    (r"\bSection 49\b", [
        "Section no: 49\n"
        "Definition: Section 49 of the Indian Penal Code explains the use of the singular and plural forms in the code. It specifies that words in the singular include the plural and vice versa unless explicitly stated otherwise.\n"
        "Punishment: This section does not prescribe specific punishment but aids in the interpretation of legal provisions."
    ]),

    (r"\bSection 50\b", [
        "Section no: 50\n"
        "Definition: Section 50 of the Indian Penal Code defines the term 'section' as a portion of the IPC, providing a systematic way of referring to specific provisions or clauses.\n"
        "Punishment: This section does not prescribe specific punishment but ensures uniformity in referencing legal provisions within the IPC."
    ]),


    (r"\bSection 51\b", [
        "Section no: 51\n"
        "Definition: Section 51 of the Indian Penal Code defines the term 'Oath' as including any form of affirmation or declaration required or authorized by law to be made before a public servant or other authorized person.\n"
        "Punishment: This section does not prescribe specific punishment but provides clarity for interpreting legal requirements concerning oaths."
    ]),

    (r"\bSection 52\b", [
        "Section no: 52\n"
        "Definition: Section 52 of the Indian Penal Code defines the term 'Good faith' as something done with due care and attention, ensuring that an action is carried out with honest intent and a reasonable standard of care.\n"
        "Punishment: This section does not prescribe specific punishment but is used to determine whether an act qualifies as being performed in good faith."
    ]),

    (r"\bSection 53\b", [
        "Section no: 53\n"
        "Definition: Section 53 of the Indian Penal Code provides a list of punishments that may be imposed for criminal offenses. These include death, life imprisonment, imprisonment (rigorous or simple), forfeiture of property, and fine.\n"
        "Punishment: This section outlines the types of punishments applicable under the IPC."
    ]),

    (r"\bSection 54\b", [
        "Section no: 54\n"
        "Definition: Section 54 of the Indian Penal Code provides the President of India and the State Governors the power to commute a sentence of death to life imprisonment or another form of lesser punishment.\n"
        "Punishment: This section does not prescribe specific punishments but allows for their commutation under constitutional powers."
    ]),

    (r"\bSection 55\b", [
        "Section no: 55\n"
        "Definition: Section 55 of the Indian Penal Code allows for the commutation of a sentence of life imprisonment to a term not exceeding 14 years by the government.\n"
        "Punishment: This section facilitates the reduction of life imprisonment sentences as a matter of policy or clemency."
    ]),

    (r"\bSection 56\b", [
        "Section no: 56\n"
        "Definition: Section 56 of the Indian Penal Code was repealed by the Criminal Law (Removal of Racial Discriminations) Act, 1949. Previously, it addressed sentences involving transportation beyond the seas, which is now obsolete.\n"
        "Punishment: Not applicable as the section has been repealed."
    ]),

    (r"\bSection 57\b", [
        "Section no: 57\n"
        "Definition: Section 57 of the Indian Penal Code provides that for calculating fractions of terms of punishment, life imprisonment is equivalent to 20 years. This is used for legal purposes such as determining eligibility for parole or other considerations.\n"
        "Punishment: This section does not prescribe specific punishments but aids in the calculation of punishment durations."
    ]),

    (r"\bSection 58\b", [
        "Section no: 58\n"
        "Definition: Section 58 of the Indian Penal Code is related to abetment of suicide. It provides that any individual who helps or encourages another person to commit suicide, especially a married woman, may be charged with a crime. This law highlights the serious implications of emotional and psychological abuse within marriage, offering protection against coercion and manipulation that may lead to suicidal tendencies.\n"
        "Punishment: Punishment for abetment of suicide can include imprisonment, depending on the circumstances and the severity of the offense."
    ]),

    # Information Technology Act (India)
    (r"\bSection 65\b", [
        "Section no: 65\n"
        "Definition: Section 65 of the Indian Penal Code deals with the punishment for offenses related to the destruction of evidence or obstruction of justice. It is a crime to falsify or destroy documents or evidence with the intent to deceive or hinder legal proceedings. Individuals found guilty under this section can face imprisonment or fines. The section ensures that individuals who engage in tampering with evidence are held accountable, thereby protecting the integrity of legal investigations.\n"
        "Punishment: Imprisonment and/or fines depending on the severity of the offense."
    ]),

    (r"\bSection 66\b", [
        "Section no: 66\n"
        "Definition: Section 66 of the Information Technology Act, 2000, addresses the offense of hacking. It specifically deals with unauthorized access to computer systems or networks, and illegal tampering with data or information. Anyone convicted of hacking under Section 66 can face up to three years of imprisonment and/or a fine up to 5 lakh INR. This section aims to safeguard digital assets and online security by deterring cybercrime and ensuring that anyone found guilty of hacking faces stringent penalties.\n"
        "Punishment: Up to three years of imprisonment and/or a fine of up to 5 lakh INR."
    ]),

    (r"\bSection 66A\b", [
        "Section no: 66A\n"
        "Definition: Section 66A of the Information Technology Act was struck down in 2015 by the Supreme Court, as it was found to be unconstitutional due to its broad and vague language, which led to the infringement of freedom of speech. Previously, Section 66A penalized individuals who sent offensive or harmful messages through electronic communication. Those found guilty could have been sentenced to up to three years in prison and fined. The section was criticized for being misused to stifle free expression, and its repeal was seen as a victory for freedom of speech.\n"
        "Punishment: Previously, up to three years of imprisonment and a fine; however, the section was repealed in 2015."
    ]),

    (r"\bSection 67\b", [
        "Section no: 67\n"
        "Definition: Section 67 of the Information Technology Act, 2000, pertains to the punishment for publishing or transmitting obscene material in electronic form. Anyone found guilty under this section may face imprisonment for up to five years and a fine of up to 10 lakh INR. This section is intended to protect users from being exposed to harmful and explicit content online, ensuring that digital platforms remain safe and responsible environments.\n"
        "Punishment: Imprisonment for up to five years and a fine of up to 10 lakh INR."
    ]),


    (r"\b(commit suicide|Section 309)\b", [
        "Section no: 309\n"
        "Definition: Section 309 of the Indian Penal Code criminalizes attempting suicide. It provides that anyone attempting suicide can be punished with imprisonment for a term which may extend to one year, or with a fine, or both. However, the Mental Healthcare Act of 2017 decriminalized suicide attempts for individuals with mental health conditions, focusing on treatment rather than punishment.\n"
        "Punishment: The punishment for attempting suicide under Section 309 may extend to one year of imprisonment, a fine, or both. However, under the Mental Healthcare Act of 2017, individuals with mental health conditions are not subject to criminal punishment."
    ]),

    (r"\bSection 302\b|\bPunishment for murder\b", [
        "Section 302 of the IPC deals with the punishment for murder. The section mandates that anyone convicted of murder may face either the death penalty or life imprisonment. In addition, the court may also impose a fine. The section provides specific guidelines for the courts when determining the punishment for murder, taking into account the severity of the offense, the intention behind it, and any mitigating factors such as provocation or mental state. Murder is considered one of the most serious offenses under Indian law, and this section ensures stringent penalties for those found guilty."]),

    (r"\bSection 307\b", [
        "Section 307 of the IPC addresses the offense of attempting to commit murder. The section stipulates that a person who attempts to commit murder can face a punishment ranging from 10 years to life imprisonment. The penalty may also include a fine, depending on the circumstances of the case. The section also clarifies that if the attempt to commit murder leads to injury, the severity of the punishment may increase. The law takes into account the seriousness of the intent and the potential harm caused by the act of attempting murder."]),

    (r"\bSection 375\b", [
        "Section 375 of the IPC defines the offense of rape and outlines the conditions under which an individual can be convicted of this crime. The section specifies that a man is guilty of rape if he has sexual intercourse with a woman without her consent, or with her consent obtained through coercion or manipulation. The section also details the legal framework for establishing consent and outlines the punishments for the offense, which range from 7 years to life imprisonment, and may also include fines. This provision aims to protect women’s bodily autonomy and dignity, ensuring that anyone committing sexual assault faces severe legal consequences."]),

    (r"\bSection 498A\b", [
        "Section 498A of the IPC addresses cruelty by a husband or his relatives towards a wife. This section protects women from various forms of mental and physical abuse, including harassment, dowry demands, and domestic violence. It states that if a husband or his relatives subject a woman to cruelty, they can be punished with imprisonment for up to three years and may also be required to pay a fine. The provision is aimed at curbing domestic violence and providing women with a legal recourse against abusive partners or in-laws."]),

    (r"\bSection 420\b", [
        "Section 420 of the IPC deals with cheating and dishonestly inducing the delivery of property. It covers various fraudulent activities where an individual deceives another party into parting with property or money. The law is meant to protect individuals and organizations from financial deceit. Conviction under this section can lead to imprisonment for up to seven years, along with fines. The severity of the punishment reflects the serious nature of financial fraud and dishonesty in transactions."]),



    # Negotiable Instruments Act
    (r"\bSection 138\b", [
        "Section 138 of the Negotiable Instruments Act, 1881, deals with the dishonor of cheques due to insufficient funds. If a person issues a cheque that is returned by the bank due to insufficient funds, they can be penalized under this section. The penalties may include imprisonment for up to two years or a fine that may amount to twice the value of the dishonored cheque. The section serves to promote trust in financial transactions and encourages individuals to maintain adequate funds in their accounts when issuing cheques."]),


    # International laws
    (r"\bGDPR\b", [
        "The General Data Protection Regulation (GDPR) is a comprehensive data privacy law enacted by the European Union in 2018 to protect individuals' personal data and privacy. It regulates how companies collect, store, and process personal information of EU citizens, giving them greater control over their data. Key features of GDPR include the right to access personal data, the right to erasure ('right to be forgotten'), and strict penalties for non-compliance, with fines reaching up to 4% of a company's global annual turnover or €20 million, whichever is higher. GDPR is a major global milestone in data privacy regulation, influencing laws worldwide."]),

    (r"\bSarbanes-Oxley\b", [
        "The Sarbanes-Oxley Act of 2002 (SOX) is a U.S. federal law that was enacted to protect investors from corporate fraud. It mandates strict reforms to improve financial disclosures, corporate governance, and auditing practices. SOX requires companies to establish internal controls to detect and prevent fraud, and it holds CEOs and CFOs personally responsible for the accuracy of financial statements. The Act also established the Public Company Accounting Oversight Board (PCAOB) to oversee the auditing profession and ensure compliance with the new standards. SOX is considered one of the most significant reforms in corporate accounting and transparency."]),

    # Environmental Protection Act
    (r"\bEnvironmental Protection Act\b", [
        "The Environmental Protection Act of 1986 is a comprehensive law designed to provide a framework for the protection and improvement of India's environment. The Act empowers the government to take action on pollution control, waste management, and environmental impact assessment. It also provides for penalties, including imprisonment or fines, for individuals or organizations that fail to comply with environmental standards. This law plays a vital role in ensuring that industrial development and urbanization do not come at the expense of the environment."]),

    # Employment Rights Act (UK)
    (r"\bEmployment Rights Act\b", [
        "The Employment Rights Act 1996 (UK) provides essential protections to employees, including the right to a written contract, protection from unfair dismissal, and entitlement to various statutory rights such as maternity leave and holiday pay. It also covers issues related to redundancy, wages, and discrimination. The Act is designed to ensure that employees are treated fairly and can work in an environment free from exploitation, with legal mechanisms available to resolve disputes and enforce their rights."]),



    # General legal questions
    (r"\bWhat is law\b\?", [
        "Law is a system of rules created and enforced by institutions such as governments, courts, and regulatory bodies. It is a framework designed to regulate behavior, maintain order, protect individual rights, and promote justice in society. Laws can be criminal, civil, or administrative and are applicable within specific jurisdictions or territories. Law ensures that individuals and organizations follow prescribed norms and standards, providing mechanisms for resolving disputes and upholding fairness."]),

    (r"\bWhat is a legal contract\b", [
        "A legal contract is a formal and binding agreement between two or more parties that outlines mutual obligations, rights, and responsibilities. For a contract to be legally enforceable, it must meet several key criteria, such as offer, acceptance, consideration (something of value exchanged), and mutual intent to enter into the agreement. A contract can be written, verbal, or implied, but for serious or complex agreements, a written contract is often preferred to prevent future disputes. Legal contracts are governed by statutory laws and case precedents, ensuring fairness and clarity in commercial and personal dealings."]),

    (r"\bHow can I file a lawsuit\b", [
        "To file a lawsuit, the first step is to consult with a lawyer to evaluate your case and understand your legal rights. Once your lawyer determines the validity of your claim, they will help you prepare a formal complaint or petition, which will be filed in the appropriate court. The complaint should include specific details about the nature of the dispute, the parties involved, and the remedy you seek. After filing, the court will notify the opposing party, and legal proceedings will begin. Depending on the case, it may involve several stages, including discovery, hearings, and trials."]),

    (r"\bWhat are the grounds for divorce\b", ["Common grounds for divorce include irreconcilable differences, adultery, abandonment, or abuse. In addition, some jurisdictions may recognize mental cruelty, desertion, or habitual drunkenness as valid grounds. In most cases, the person seeking the divorce must demonstrate that the marriage has broken down irretrievably. Each jurisdiction may have specific requirements, and the process may differ for fault-based and no-fault divorce systems."]),

    (r"\bHow can I get child custody\b", ["Child custody decisions are made by family court, prioritizing the best interests of the child. Factors considered include the child's age, emotional needs, the ability of each parent to provide care, and sometimes the child's own preferences. Courts may grant joint or sole custody depending on the circumstances. It is important to present a compelling case to the court, showing that you are the better caregiver and that the arrangement will serve the child's well-being."]),

    (r"\bWhat should I do if I'm arrested\b", ["Exercise your right to remain silent and request an attorney to represent you. Do not answer questions without legal counsel present, as anything you say can be used against you in court. You also have the right to be informed of the charges against you and to a fair trial. If you're being detained, ask if you are under arrest and for the reasons behind it. It is also important to avoid resisting arrest, as this can lead to additional charges."]),

    (r"\bWhat is the difference between a felony and a misdemeanor\b", ["Felonies are more serious crimes with heavier penalties, such as long-term imprisonment, large fines, or even the death penalty in extreme cases. Examples include murder, rape, and major fraud. Misdemeanors are lesser offenses that usually result in shorter jail sentences, smaller fines, or community service. Examples include petty theft, vandalism, and minor assaults. The classification varies by jurisdiction, but felonies carry greater legal consequences."]),

    (r"\bWhat are my rights as an employee\b", ["Employee rights typically include fair wages, safe working conditions, protection from discrimination, the right to organize or join a union, and the right to privacy. Employees are also entitled to protections against wrongful termination and retaliation for whistleblowing. In some regions, specific labor laws govern issues like working hours, overtime pay, and benefits. These rights are enshrined in labor laws and statutes and can be enforced through legal action if violated."]),

    (r"\bHow do I file a patent\b", ["To file a patent, submit a detailed application to the patent office in your jurisdiction. The application must include a clear description of the invention, how it works, and any diagrams if applicable. A patent search is often done to ensure your invention is novel and non-obvious. After submission, the patent office examines the application, and if it meets all criteria, the patent is granted. It is recommended to consult a patent attorney for assistance to navigate the technical and legal requirements."]),


]



# Create the chatbot object
chatbot = Chat(pairs, reflections)
