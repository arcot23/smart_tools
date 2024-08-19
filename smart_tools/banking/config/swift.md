https://www2.swift.com/knowledgecentre/publications/usgi_20230720/2.0?topic=con_31492.htm
https://www2.swift.com/knowledgecentre/publications/usgi_20230720/2.0?topic=con_34195.htm

Types of characters Allowed

```
n	[0-9]	numeric digits (0 through 9) only
a	[A-Z]	alphabetic letters (A through Z), upper case only
c	[A-Z0-9]	alphabetic letters (upper case) and digits only
h	[ABCDEF0-9]	hexadecimal letters A through F (upper case) and digits only
x	[0-9A-Za-z\/-?:().,'+ ]	any character of the X permitted set (General FIN application set) upper and lower case allowed (SWIFT Character Set (X Character Set))
y	[A-Z0-9.,\-()\/='+:?!"%&*<>; ]	any character of the EDIFACT level A character set as defined in ISO 9735 upper case only (EDIFACT Level A Character Set (Y Character Set))
z	[a-zA-Z0-9.,\-()\/='+:?!"%&*<>;{@#_\r\n ]	any character as defined by the Information Service (Information Service Character Set (Z Character Set))
d	[0-9.]	decimals
e	[ ]	blank space
```

- Option A: Identifier Code

    ```
    [/1a][/34x]	(Party Identifier)	^(\/([A-Z]))?(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))?$
    4!a2!a2!c[3!c]	(Identifier Code)	^(([A-Z]{4})([A-Z]{2})([A-Z0-9]{2})([A-Z0-9]{3})?)$
    ```

- Option B: Branch of Sender/Receiver

    ```
    [/1a][/34x]	(Party Identifier)	^(\/([A-Z]))?(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))?$
    [35x]	(Location)	^([0-9A-Za-z\/-?:().,'+ ]{1,35})?$
    ```

- Option C: Account Number/Party Identifier

    ```
    /34x	(Account)	^(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))$
    ```

- Option D: Name and Address

    ```
    [/1a][/34x]	(Party Identifier)	^(\/([A-Z]))?(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))?$
    4*35x	(Name and Address)	^([0-9A-Za-z\/-?:().,'+ ]{1,35}){1,4}$
    ```

- Option F: Party Identifier/Name and Address

    ```
    [35x]	(Party Identifier)	^([0-9A-Za-z\/-?:().,'+ ]{1,35})?$
    4*35x	(Name and Address)	^([0-9A-Za-z\/-?:().,'+ ]{1,35}){1,4}$
    ```

    - TYPE 1

        ```
        Line 1 (subfield Party Identifier)	/34x	(Account)	^(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))$
        Line 2-5 (subfield Name and Address)	1!n/33x	(Number)(Details)	^(([0-9])\/([0-9A-Za-z\/-?:().,'+ ]{1,33}))$
        ```

    - TYPE 2

        ```
        Line 1 (subfield Party Identifier)	4!a/2!a/27x	(Code)(Country Code)(Identifier)	^([A-Z]{4})\/([A-Z]{2})\/([0-9A-Za-z\/-?:().,'+ ]{1,27})$
        Line 2-5 (subfield Name and Address)	1!n/33x	(Number)(Details)	^(([0-9])\/([0-9A-Za-z\/-?:().,'+ ]{1,33}))$
        ```

    - TYPE 3

        ```
        Line 1 (subfield Party Identifier)	[/34x]	(Account)	^(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))?$
        Line 2-5 (subfield Name and Address)	1!n/33x	(Number)(Details)	^(([0-9])\/([0-9A-Za-z\/-?:().,'+ ]{1,33}))$
        ```

- Option G: Identifier Code

    ```
    /34x	(Account)	^(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))$
    4!a2!a2!c[3!c]	(Identifier Code)	^(([A-Z]{4})([A-Z]{2})([A-Z0-9]{2})([A-Z0-9]{3})?)$
    ```

- Option H: Name and Address

    ```
    /34x	(Account)	^(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))$
    4*35x	(Name and Address)	^([0-9A-Za-z\/-?:().,'+ ]{1,35}){1,4}$
    ```

- Option J: Party Identification with no Party Identifier

    ```
    5*40x	(Narrative)	^([0-9A-Za-z\/-?:().,'+ ]{1,40}){1,5}$
    ```

- Option K: Name and Address

    ```
    [/34x]	(Account)	^(\/([0-9A-Za-z\/-?:().,'+ ]{1,34}))?$
    4*35x	(Name and Address)	^([0-9A-Za-z\/-?:().,'+ ]{1,35}){1,4}$
    ```

- Option L: Party Identification

    ```
    35x	(Narrative)	^([0-9A-Za-z\/-?:().,'+ ]{1,35})$
    ```
